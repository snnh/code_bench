#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
code_bench 站点同步脚本：以仓库内 Markdown 为唯一数据源，自动生成：
  1. docs/<page>.html        —— 题目说明页（整页由 md 渲染）
  2. docs/data/<bench>/      —— 榜单 CSV（供仪表盘查询）

用法：
  python3 scripts/sync_md.py [--check]

--check 只校验不写文件（CI 中可用）。
新增 bench（如 OCR）：在 SYNC_CONFIG 中按 ocr/ocr_benchmark_v5.md 的格式
添加条目即可，推送后 GitHub Actions 自动运行本脚本。
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- 配置

# md 文件 → 生成目标
# "csvs" 键为 (h3 小节名, h4 加粗标签)，None 表示该小节下直接跟的表格
SYNC_CONFIG = {
    "code/code_bench.md": {
        "doc_page": "docs/bench.html",
        "page": {
            "title": "code_bench v1.3｜题目说明",
            "h1": "code_bench v1.3",
            "subtitle": "大模型复刻 openwebcode 项目评测榜单 · 题目说明",
            "description": "code_bench v1.3 题目结构、评测环境、基础题与高阶题排行、分析、声明与致谢。",
            "nav": [
                {"href": "./", "label": "榜单"},
                {"href": "bench.html", "label": "说明", "active": True},
                {"href": "ocr_bench.html", "label": "OCR 说明"},
                {"href": "archive.html", "label": "归档"},
            ],
            "tip": "本页为 code_bench v1.3 完整题目与说明；榜单数据可在"
                   "<a href=\"./\">榜单查询</a> 中交互查看（筛选、排序、搜索）。",
        },
        "csvs": {
            ("排行", None): "docs/data/code_bench/v1.3-rank.csv",
            ("基础题", "core"): "docs/data/code_bench/v1.3-core.csv",
            ("基础题", "server"): "docs/data/code_bench/v1.3-server.csv",
            ("基础题", "web v2"): "docs/data/code_bench/v1.3-web.csv",
            ("高阶题", "高阶题总分"): "docs/data/code_bench/v1.3-advanced-total.csv",
            ("高阶题", "full"): "docs/data/code_bench/v1.3-full.csv",
            ("高阶题", "rust v2"): "docs/data/code_bench/v1.3-rust.csv",
        },
        "expected_headers": {
            "docs/data/code_bench/v1.3-rank.csv": [
                "模型",
            ],
            "docs/data/code_bench/v1.3-core.csv": [
                "模型", "积分", "成本(折算API价格)", "token(不算缓存)", "缓存",
            ],
            "docs/data/code_bench/v1.3-server.csv": [
                "模型", "积分", "成本(折算API价格)", "token(不算缓存)", "缓存",
            ],
            "docs/data/code_bench/v1.3-web.csv": [
                "模型", "积分", "成本(折算API价格)", "token(不算缓存)", "缓存", "接入方式", "备注",
            ],
            "docs/data/code_bench/v1.3-full.csv": [
                "模型", "积分", "成本(折算API价格)", "token(不算缓存)", "缓存", "接入方式", "备注",
            ],
            "docs/data/code_bench/v1.3-rust.csv": [
                "模型", "积分", "成本(折算API价格)", "订阅折算", "token(不算缓存)", "缓存", "接入方式", "备注",
            ],
            "docs/data/code_bench/v1.3-advanced-total.csv": [
                "模型", "积分", "成本(折算API价格)", "token(不算缓存)", "缓存", "接入方式", "备注",
            ],
        },
    },
    "code/code_bench_archive.md": {
        "doc_page": "docs/archive.html",
        "page": {
            "title": "code_bench 归档｜rust 题目",
            "h1": "code_bench 归档",
            "subtitle": "已归档题目与榜单",
            "description": "code_bench 已归档的 rust 高阶题题目说明与榜单。",
            "nav": [
                {"href": "./", "label": "榜单"},
                {"href": "bench.html", "label": "说明"},
                {"href": "ocr_bench.html", "label": "OCR 说明"},
                {"href": "archive.html", "label": "归档", "active": True},
            ],
            "tip": "本页为 code_bench 已归档的 rust 题目与榜单；榜单数据可在"
                   "<a href=\"./\">榜单查询</a> 中交互查看。",
        },
        "csvs": {
            ("高阶题 · rust（已归档）", "rust 榜单"): "docs/data/code_bench/archive-rust.csv",
            ("基础题 · web（已归档）", "web 榜单"): "docs/data/code_bench/archive-web.csv",
        },
        "expected_headers": {
            "docs/data/code_bench/archive-rust.csv": [
                "模型", "积分", "成本", "token", "缓存", "接入方式", "备注",
            ],
            "docs/data/code_bench/archive-web.csv": [
                "模型", "积分", "成本", "token", "缓存",
            ],
        },
    },
    "ocr/ocr_benchmark_v5.md": {
        "doc_page": "docs/ocr_bench.html",
        "page": {
            "title": "开发场景 OCR Benchmark v5｜题目说明",
            "h1": "开发场景 OCR Benchmark v5",
            "subtitle": "开发场景 OCR 评测 · 题目说明",
            "description": "开发场景 OCR Benchmark v5 数据集、榜单、LLM 六维评分与积分规则。",
            "nav": [
                {"href": "./", "label": "榜单"},
                {"href": "bench.html", "label": "说明"},
                {"href": "ocr_bench.html", "label": "OCR 说明", "active": True},
                {"href": "archive.html", "label": "归档"},
            ],
            "tip": "本页为开发场景 OCR Benchmark v5 完整说明；榜单数据可在"
                   "<a href=\"./\">榜单查询</a> 中交互查看（筛选、排序、搜索）。",
        },
        "csvs": {
            ("短提示榜 <image>OCR:", None): "docs/data/ocr_bench/v5-short.csv",
            ("官方推荐提示词榜", None): "docs/data/ocr_bench/v5-official.csv",
            ("类别诊断（短提示）", None): "docs/data/ocr_bench/v5-category.csv",
            ("难度诊断（短提示）", None): "docs/data/ocr_bench/v5-difficulty.csv",
        },
        "expected_headers": {
            "docs/data/ocr_bench/v5-short.csv": [
                "方案", "记录", "最终积分", "原始积分", "类别加权", "全局均值",
                "最弱类别", "最弱难度", "严格可用率", "完成率", "安全分",
                "平均 NED", "报告", "备注",
            ],
            "docs/data/ocr_bench/v5-official.csv": [
                "方案", "记录", "最终积分", "原始积分", "类别加权", "全局均值",
                "最弱类别", "最弱难度", "严格可用率", "完成率", "安全分",
                "平均 NED", "报告", "备注",
            ],
            "docs/data/ocr_bench/v5-category.csv": ["类别", "最佳方案", "类别分"],
            "docs/data/ocr_bench/v5-difficulty.csv": ["难度", "最佳方案", "难度分", "severe"],
        },
    },
}

# 占位行（"… | 未测试 ..."）不写入 CSV
PLACEHOLDER_FIRST_CELLS = {"…", "..."}

# ---------------------------------------------------------------- 页面模板

def render_page(content, meta):
    nav_items = "".join(
        '<a%s href="%s">%s</a>'
        % (' class="current" aria-current="page"' if item.get("active") else "",
           item["href"], item["label"])
        for item in meta["nav"]
    )
    canonical = "https://snnh.github.io/code_bench/%s" % os.path.basename(meta["doc_page"])
    return """<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>%(title)s</title>
    <meta name="description" content="%(description)s" />
    <meta name="robots" content="index, follow" />
    <link rel="canonical" href="%(canonical)s" />
    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="code_bench" />
    <meta property="og:locale" content="zh_CN" />
    <meta property="og:url" content="%(canonical)s" />
    <meta property="og:title" content="%(title)s" />
    <meta property="og:description" content="%(description)s" />
    <link rel="icon" type="image/png" sizes="64x64" href="assets/favicon.png" />
    <link rel="stylesheet" href="assets/styles.css" />
  </head>
  <body>
    <script>
      (function () {
        var key = "llm-dashboard-theme";
        var mode = "system";
        try {
          mode = window.localStorage.getItem(key) || "system";
        } catch (e) {}
        if (mode === "light") document.documentElement.setAttribute("data-theme", "light");
        else if (mode === "dark") document.documentElement.setAttribute("data-theme", "dark");
      })();
    </script>
    <header class="page-header">
      <div class="header-actions">
        <a class="header-action-button" href="./">榜单</a>
      </div>
      <a
        class="github-corner"
        href="https://github.com/snnh/code_bench/"
        target="_blank"
        rel="noopener noreferrer"
        aria-label="View source on GitHub"
      >
        <svg viewBox="0 0 250 250" aria-hidden="true">
          <path class="github-corner-bg" d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z" />
          <path
            class="octo-arm"
            d="M128.3,109 C113.8,99.7 119,89.6 119,89.6 C122,82.7 120.5,78.6 120.5,78.6 C119.2,72 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2"
          />
          <path
            class="octo-body"
            d="M115,115 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88 127.5,74.4 143.8,58 C148.5,53.4 154,51.2 159.7,51 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96 205.4,96.6 C205.1,102.4 203,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z"
          />
        </svg>
      </a>
      <h1>%(h1)s</h1>
      <p class="subtitle">%(subtitle)s</p>
    </header>

    <main>
      <nav class="doc-nav" aria-label="页面导航">
        %(nav)s
      </nav>

      <article class="doc-article">
        <p class="doc-tip">%(tip)s</p>

%(content)s
      </article>
    </main>

    <footer class="page-footer">
      <small>Vibe Coding by Codex -&gt; Kimi K3</small>
    </footer>
  </body>
</html>
""" % {
        "title": meta["title"],
        "description": meta["description"],
        "canonical": canonical,
        "h1": meta["h1"],
        "subtitle": meta["subtitle"],
        "nav": nav_items,
        "tip": meta["tip"],
        "content": content,
    }


# ---------------------------------------------------------------- md 渲染

SEPARATOR_RE = re.compile(r":?-{2,}:?")


def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline(text):
    """行内样式：code / 链接 / 加粗 / 斜体（先转义，再用占位符保护 code 与链接）。"""
    text = escape_html(text)
    stash = []

    def keep(html_fragment):
        stash.append(html_fragment)
        return "\x00%d\x00" % (len(stash) - 1)

    text = re.sub(r"`([^`]+)`", lambda m: keep("<code>%s</code>" % m.group(1)), text)
    text = re.sub(
        r"\[([^\]]+)\]\(([^)\s]+)\)",
        lambda m: keep('<a href="%s">%s</a>' % (escape_html(m.group(2)), m.group(1))),
        text,
    )
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    for index, fragment in enumerate(stash):
        text = text.replace("\x00%d\x00" % index, fragment)
    return text


def heading_text(line):
    """标题行去除行内 code 反引号，便于作为小节名参与映射。"""
    return re.sub(r"`([^`]+)`", r"\1", line).strip()


def parse_table(lines, index):
    """解析以 | 开头结尾的表格块，返回 (rows, 下一行下标)。跳过分隔行。"""
    rows = []
    while index < len(lines):
        line = lines[index].strip()
        if not (line.startswith("|") and line.endswith("|")):
            break
        cells = [c.strip() for c in line.strip("|").split("|")]
        if all(SEPARATOR_RE.fullmatch(c) for c in cells):
            index += 1
            continue
        rows.append(cells)
        index += 1
    return rows, index


def render_table(rows):
    if not rows:
        return ""
    out = ['<table class="doc-table">', "<thead><tr>"]
    for cell in rows[0]:
        out.append("<th>%s</th>" % inline(cell))
    out.append("</tr></thead><tbody>")
    for row in rows[1:]:
        out.append("<tr>")
        for cell in row:
            out.append("<td>%s</td>" % inline(cell))
        out.append("</tr>")
    out.append("</tbody></table>")
    # 宽表包一层横向滚动容器，避免撑破文章栏宽
    return '<div class="doc-table-wrap">' + "".join(out) + "</div>"


def render_lists(lines, index):
    """收集连续的列表项（有序/无序），返回 (html, 下一行下标)。"""
    items = []
    ordered = None
    while index < len(lines):
        line = lines[index].strip()
        if not line:
            break
        match = re.match(r"^(\d+)\.\s+(.*)$", line)
        if match:
            if ordered is False:
                break
            ordered = True
            items.append(inline(match.group(2)))
        elif line.startswith("* ") or line.startswith("- "):
            if ordered is True:
                break
            ordered = False
            items.append(inline(line[2:].strip()))
        else:
            break
        index += 1
    if not items:
        return "", index
    tag = "ol" if ordered else "ul"
    cls = "doc-list" if ordered else "doc-note"
    html = '<%s class="%s">' % (tag, cls)
    for item in items:
        html += "<li>%s</li>" % item
    html += "</%s>" % tag
    return html, index


def md_to_blocks(text):
    """把 md 解析为块序列 [(type, payload)]。type: h1/h2/h3/h4/table/list/p/code/blockquote"""
    lines = text.splitlines()
    blocks = []
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        if not line:
            index += 1
            continue
        if line.startswith("```"):
            # 围栏代码块
            code_lines = []
            index += 1
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code_lines.append(lines[index])
                index += 1
            index += 1  # 跳过闭合围栏
            blocks.append(
                ("html", "<pre><code>%s</code></pre>" % escape_html("\n".join(code_lines)))
            )
        elif line.startswith("#### "):
            blocks.append(("h4", heading_text(line[5:])))
            index += 1
        elif line.startswith("### "):
            blocks.append(("h3", heading_text(line[4:])))
            index += 1
        elif line.startswith("## "):
            blocks.append(("h2", heading_text(line[3:])))
            index += 1
        elif line.startswith("# "):
            blocks.append(("h1", heading_text(line[2:])))
            index += 1
        elif re.fullmatch(r"-{3,}", line) or re.fullmatch(r"\*{3,}", line):
            blocks.append(("hr", None))
            index += 1
        elif line.startswith("|") and line.endswith("|"):
            rows, index = parse_table(lines, index)
            blocks.append(("table", rows))
        elif re.fullmatch(r"\*\*.+\*\*", line):
            blocks.append(("h4", line.strip("*")))
            index += 1
        elif line.startswith("* ") or line.startswith("- ") or re.match(r"^\d+\.\s", line):
            html, index = render_lists(lines, index)
            if html:
                blocks.append(("html", html))
        elif line.startswith(">"):
            parts = []
            while index < len(lines) and lines[index].strip().startswith(">"):
                parts.append(inline(lines[index].strip()[1:].strip()))
                index += 1
            blocks.append(("html", "<blockquote><p>%s</p></blockquote>" % "<br>".join(parts)))
        else:
            paragraph = [line]
            index += 1
            while index < len(lines) and lines[index].strip():
                next_line = lines[index].strip()
                if next_line.startswith(("|", "#", ">", "* ", "- ", "```")) or re.match(
                    r"^\d+\.\s", next_line
                ):
                    break
                paragraph.append(next_line)
                index += 1
            blocks.append(("p", inline(" ".join(paragraph))))
    return blocks


def blocks_to_html(blocks):
    out = []
    for kind, payload in blocks:
        if kind == "h1":
            # 页面刊头（<header><h1>）已承载主标题；正文里的 # 标题渲染为引言，避免重复 h1
            out.append('<div class="doc-lead">%s</div>' % inline(payload))
        elif kind == "h2":
            out.append("<h2>%s</h2>" % inline(payload))
        elif kind == "h3":
            out.append("<h3>%s</h3>" % inline(payload))
        elif kind == "h4":
            out.append("<h4>%s</h4>" % inline(payload))
        elif kind == "table":
            out.append(render_table(payload))
        elif kind == "hr":
            out.append('<hr class="doc-hr" />')
        elif kind == "p":
            out.append("<p>%s</p>" % payload)
        elif kind == "html":
            out.append(payload)
    return "\n        ".join(out)


# ---------------------------------------------------------------- CSV 生成

def to_csv(rows):
    def quote(cell):
        return '"%s"' % str(cell).replace('"', '""')

    lines = [",".join(quote(cell) for cell in row) for row in rows]
    return "\n".join(lines) + "\n"


def extract_csvs(blocks, csv_config, expected_headers):
    """按 (h3 小节, h4 标签) 映射抽取表格 → {csv路径: 内容}。"""
    outputs = {}
    used_targets = set()
    section = None
    label = None
    for kind, payload in blocks:
        if kind in ("h1", "h2", "h3"):
            section = payload
            label = None
        elif kind == "h4":
            label = payload
        elif kind == "table":
            if section is None:
                continue
            key = (section, label) if label else (section, None)
            if key not in csv_config:
                continue
            target = csv_config[key]
            if target in used_targets:
                print("  ! 跳过重复表：%s（%s）" % (key, target))
                continue
            rows = [row for row in payload if row and row[0] not in PLACEHOLDER_FIRST_CELLS]
            expected = expected_headers[target]
            if rows and rows[0] != expected:
                raise SystemExit(
                    "表头不匹配：%s\n  期望: %s\n  实际: %s" % (target, expected, rows[0])
                )
            outputs[target] = to_csv(rows)
            used_targets.add(target)
            print("  - %s <- %s（%d 行）" % (os.path.relpath(target, ROOT), key, len(rows) - 1))
    return outputs


# ---------------------------------------------------------------- 主流程

def sync_one(md_path, config, check_only=False):
    abs_md = os.path.join(ROOT, md_path)
    with open(abs_md, encoding="utf-8") as fh:
        text = fh.read()
    blocks = md_to_blocks(text)

    print("[%s]" % md_path)

    # 1) 文档页
    content = blocks_to_html(blocks)
    meta = dict(config["page"])
    meta["doc_page"] = config["doc_page"]
    page_html = render_page(content, meta)
    write_if_changed(os.path.join(ROOT, config["doc_page"]), page_html, check_only)

    # 2) 榜单 CSV
    csvs = extract_csvs(blocks, config["csvs"], config["expected_headers"])
    for rel, content in sorted(csvs.items()):
        write_if_changed(os.path.join(ROOT, rel), content, check_only)


def write_if_changed(path, content, check_only):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as fh:
            if fh.read() == content:
                print("  = 无变化：%s" % os.path.relpath(path, ROOT))
                return
    if check_only:
        print("  ! 需要更新：%s" % os.path.relpath(path, ROOT))
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(content)
    print("  ✓ 已更新：%s" % os.path.relpath(path, ROOT))


def main():
    check_only = "--check" in sys.argv
    for md_path, config in SYNC_CONFIG.items():
        if not os.path.exists(os.path.join(ROOT, md_path)):
            print("[%s] 跳过：文件不存在（等待添加）" % md_path)
            continue
        sync_one(md_path, config, check_only)


if __name__ == "__main__":
    main()
