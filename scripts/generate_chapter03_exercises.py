#!/usr/bin/env python3
"""从 knowledge-base/question_bank/ch03_exercises.md 生成 exercises/chapter03/ 代码与索引。"""

from __future__ import annotations

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SOURCE = REPO / "knowledge-base" / "question_bank" / "ch03_exercises.md"
OUT_DIR = REPO / "exercises" / "chapter03"

JSON_PATTERN = re.compile(
    r"<!-- AUTO-DATA-BEGIN -->\s*```json\s*(.*?)\s*```\s*<!-- AUTO-DATA-END -->",
    re.S,
)


def load_data() -> dict:
    text = SOURCE.read_text(encoding="utf-8")
    m = JSON_PATTERN.search(text)
    if not m:
        raise ValueError("未找到 AUTO-DATA JSON 区块，请检查 ch03_exercises.md 格式")
    return json.loads(m.group(1))


def generate_c_file_content(question: dict) -> str:
    qid = question["id"]
    kp = question["knowledge_point"]
    title = question["title"]
    template_file = question.get("template_file")
    if not template_file:
        raise ValueError(f"{qid} 缺少 template_file 字段")
    body = (REPO / template_file).read_text(encoding="utf-8")

    header = f'''/*
 * 题号：{qid}
 * 题目：{title}
 * 考点：对应《C程序设计（第五版）》第三章中的 {kp}。
 * 解题思路：
 * 1) 先将输入数据读取到变量中，明确每个变量在内存中的值。
 * 2) 按表达式求值顺序逐步计算中间结果，避免一次性“心算跳步”。
 * 3) 将最终结果按题目要求格式化输出，并处理非法输入场景。
 */

'''
    return header + body


def render_readme(data: dict) -> str:
    chapter = data["chapter"]
    title = data["chapter_title"]
    lines: list[str] = [
        f"# Chapter {chapter} 作业与练习索引（{title}）",
        "",
        "本目录由脚本 `scripts/generate_chapter03_exercises.py` 自动生成。",
        "",
        "## 一、阅读程序写结果（标准答案解析）",
        "",
    ]

    for item in data["reading_questions"]:
        lines += [
            f"### {item['id']}",
            f"- 题目：{item['prompt']}",
            f"- 标准答案：{item['answer']}",
            f"- 解析：{item['analysis']}",
            "",
        ]

    lines += ["## 二、编程题索引", ""]
    for item in data["programming_questions"]:
        lines += [
            f"### {item['id']} {item['title']}",
            f"- 题目：{item['prompt']}",
            f"- 输入：{item['input_spec']}",
            f"- 输出：{item['output_spec']}",
            f"- 样例输入：`{item['sample_input']}`",
            f"- 样例输出：`{item['sample_output']}`",
            f"- 代码文件：`./{item['filename']}`",
            "",
        ]

    lines += [
        "## 三、使用方式",
        "",
        "```bash",
        "python scripts/generate_chapter03_exercises.py",
        "```",
        "",
    ]
    return "\n".join(lines)


def generate() -> None:
    data = load_data()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for question in data["programming_questions"]:
        content = generate_c_file_content(question)
        (OUT_DIR / question["filename"]).write_text(content, encoding="utf-8")

    readme = render_readme(data)
    (OUT_DIR / "README.md").write_text(readme, encoding="utf-8")


if __name__ == "__main__":
    generate()
