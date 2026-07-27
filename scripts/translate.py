#!/usr/bin/env python3
"""Generate bilingual posts from _raw/ using Gemini API."""

import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from dotenv import load_dotenv
from google import genai

ROOT = Path(__file__).parent.parent
RAW_DIR = ROOT / "_raw"
POSTS_DIR = ROOT / "_posts"

load_dotenv(ROOT.parent / ".env")

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
MODEL = "gemini-3.1-pro-preview"

SYSTEM_PROMPT = """You are a professional translator. Translate the given blog post content.
Preserve all markdown formatting, code blocks, links, and images exactly.
Keep the same structure and tone. Do not add or remove content.
Only translate the text, not code or URLs."""

EN_PROMPT = """Translate this blog post to fluent English.
If it contains mixed Chinese/English, translate Chinese parts to English.
Return ONLY the translated content, no explanations."""

ZH_PROMPT = """Translate this blog post to fluent Chinese.
If it contains mixed Chinese/English, translate English parts to Chinese.
Return ONLY the translated content, no explanations."""


@dataclass
class Task:
    raw_path: Path
    out_name: str
    target_lang: str
    src_lang: str
    front_matter: dict
    body: str
    needs_translate: bool


def detect_lang(text: str) -> str:
    """Detect if text is primarily Chinese or English."""
    text_only = re.sub(r"[^\w\u4e00-\u9fff]", "", text)
    if not text_only:
        return "en"
    chinese_chars = len(re.findall(r"[\u4e00-\u9fff]", text_only))
    return "zh" if chinese_chars / len(text_only) > 0.3 else "en"


def parse_post(content: str) -> tuple[dict, str]:
    """Parse front matter and body from post content."""
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", content, re.DOTALL)
    if not match:
        return {}, content
    fm_lines = match.group(1).strip().split("\n")
    front_matter = {}
    for line in fm_lines:
        if ":" in line:
            key, val = line.split(":", 1)
            front_matter[key.strip()] = val.strip().strip('"\'')
    return front_matter, match.group(2)


def build_front_matter(fm: dict, lang: str, pair_slug: str) -> str:
    """Build front matter string for generated post."""
    lines = ["---", "layout: post", f'title: "{fm.get("title", "")}"']
    if "excerpt" in fm:
        lines.append(f'excerpt: "{fm["excerpt"]}"')
    if "date" in fm:
        lines.append(f"date: {fm['date']}")
    lines.append(f"lang: {lang}")
    lines.append(f"pair: {pair_slug}")
    if fm.get("published") == "false":
        lines.append("published: false")
    lines.append("---\n")
    return "\n".join(lines)


def get_slug(filename: str) -> str:
    """Extract slug from filename like 2025-02-01-my-post.en.md -> my-post."""
    match = re.match(r"\d{4}-\d{2}-\d{2}-(.+)\.(en|zh)\.md$", filename)
    if match:
        return match.group(1)
    match = re.match(r"\d{4}-\d{2}-\d{2}-(.+)\.md$", filename)
    return match.group(1) if match else filename.replace(".md", "")


def translate_text(text: str, target_lang: str) -> str:
    """Translate text to target language."""
    if not text.strip():
        return text
    prompt = EN_PROMPT if target_lang == "en" else ZH_PROMPT
    response = client.models.generate_content(
        model=MODEL,
        contents=f"{SYSTEM_PROMPT}\n\n{prompt}\n\n---\n\n{text}",
        config={"temperature": 0.3},
    )
    return response.text.strip()


def process_task(task: Task) -> tuple[str, str | None]:
    """Process a single task. Returns (out_name, error_message or None)."""
    slug = get_slug(task.raw_path.name)
    pair_slug = f"{slug}.{'zh' if task.target_lang == 'en' else 'en'}"
    fm = task.front_matter.copy()

    if task.needs_translate:
        fm["title"] = translate_text(fm.get("title", ""), task.target_lang)
        if "excerpt" in fm:
            fm["excerpt"] = translate_text(fm["excerpt"], task.target_lang)
        body = translate_text(task.body, task.target_lang)
    else:
        body = task.body

    final = build_front_matter(fm, task.target_lang, pair_slug) + body
    (POSTS_DIR / task.out_name).write_text(final, encoding="utf-8")
    return task.out_name, None


def scan_status() -> tuple[list[dict], list[Task]]:
    """Scan all raw posts and return (status_list, tasks_to_process)."""
    status: list[dict] = []
    tasks: list[Task] = []

    for raw_path in sorted(RAW_DIR.glob("*.md")):
        content = raw_path.read_text(encoding="utf-8")
        front_matter, body = parse_post(content)
        if not body.strip():
            continue

        slug = get_slug(raw_path.name)
        date_prefix = raw_path.name[:10]
        src_lang = detect_lang(body)

        en_name = f"{date_prefix}-{slug}.en.md"
        zh_name = f"{date_prefix}-{slug}.zh.md"
        en_exists = (POSTS_DIR / en_name).exists()
        zh_exists = (POSTS_DIR / zh_name).exists()

        status.append({"raw": raw_path.name, "en": en_exists, "zh": zh_exists})

        for lang, out_name, exists in [("en", en_name, en_exists), ("zh", zh_name, zh_exists)]:
            if not exists:
                tasks.append(Task(
                    raw_path=raw_path,
                    out_name=out_name,
                    target_lang=lang,
                    src_lang=src_lang,
                    front_matter=front_matter,
                    body=body,
                    needs_translate=src_lang != lang,
                ))
    return status, tasks


def main():
    if not os.environ.get("GEMINI_API_KEY"):
        print("❌ GEMINI_API_KEY not found")
        sys.exit(1)

    POSTS_DIR.mkdir(exist_ok=True)
    status, tasks = scan_status()

    if not status:
        print("No raw posts found")
        return

    print("Raw posts status:")
    for s in status:
        en = "✅" if s["en"] else "⬜"
        zh = "✅" if s["zh"] else "⬜"
        print(f"  {s['raw']:40} EN {en}  ZH {zh}")

    if not tasks:
        print("\nAll posts are up to date")
        return

    print(f"\nTo process ({len(tasks)}):")
    for t in tasks:
        action = "translate" if t.needs_translate else "copy"
        print(f"  → {t.out_name} ({action})")

    input("\nPress Enter to start...")

    failed: list[tuple[str, str]] = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(process_task, t): t for t in tasks}
        for future in as_completed(futures):
            task = futures[future]
            try:
                out_name, err = future.result()
                if err:
                    failed.append((out_name, err))
                    print(f"❌ {out_name}: {err}")
                else:
                    action = "translated" if task.needs_translate else "copied"
                    print(f"✅ {out_name} ({action})")
            except Exception as e:
                failed.append((task.out_name, str(e)))
                print(f"❌ {task.out_name}: {e}")

    print(f"\nDone: {len(tasks) - len(failed)}/{len(tasks)}")
    if failed:
        print(f"\nFailed ({len(failed)}):")
        for name, err in failed:
            print(f"  {name}: {err}")


if __name__ == "__main__":
    main()
