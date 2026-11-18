# code_bench · 大模型开发能力评测

个人维护的大模型**开发场景**评测榜单，托管于 GitHub Pages：

- **在线榜单**：<https://snnh.github.io/code_bench/>

## 评测说明

1. 个人性质评测，题库规模有限，不使用任何互联网公开题目。
2. 题目会持续更新，不同版本号的成绩存在差异，请以最新数据为准。
3. 评测仅供参考，实际选型请结合自身业务场景，切勿盲信任何榜单。

---

## 评测体系

### 1. code_bench v1.5

**当前测试项**

- `full_v3`：高阶题，满分 100（3 大 + 1 小模块，开发一个 coding agent）
- `rust v3.2`：高阶题，满分 100（Rust 后端 + SQLite + 静态前端，Rust 为绝对主体）
- `cowork`：高阶题，满分 100（新增协作办公场景评测）
- 基础题 `core` / `server` / `web v2`（满分各 30）成绩仍保留在明细页与历史快照中，不再计入实时月榜

**月榜机制**

- 按月展示「模型 × 子项」成绩矩阵（不设总分列），默认显示最新月份。
- `2026-11` 为实时滚动月榜，涵盖 `full_v3`、`rust v3.2`、`cowork`；成绩随子项明细自动刷新。
- `2026-10` 起月榜只统计高阶子项，早期基础题不再计入。
- `2026-10`、`2026-09` 为历史月榜快照；已退出现行排行的历史模型统一归档至 `2026-09` 快照，不再单独成表。
- 快照数据取自当月最后一次提交的子项成绩，之后补测的成绩不回溯。

**计分、排序与可视化**

- **总榜排序**：默认遵循「排行」表给定顺序；未上榜模型按各子项折算百分制后的加权均分降序排列（高阶题权重 2，其余 1）。
- **子项明细**：默认展示百分制折算分，可在页面切换回原始分。
- **表格排序**：点击表头切换升降序，第三次点击恢复默认顺序；空值与 `-` / `未测试` 始终排在最后。
- **象限图**：支持「积分 × 成本 / Token 效率」双轴分析，分界取当前数据集中位数（成本为区间如 `3.24-6.48元` 时取下界，Token 的 `k` / `m` 后缀按实际数量级还原）。
- **成本口径**：`成本(折算API价格)` 为按模型官方 / 中转 API 价格折算的一次评测费用，`订阅折算` 为按订阅套餐折算的单次成本。

**历史与归档**：已下线的基础题（`core` / `server` / `web v2`）与早期旧版题库（`rust v1`、`rust v2.1`、`full_v2`、旧版 `web`）统一移入归档页或历史快照留存。

### 2. 开发场景 OCR Benchmark v5

面向代码、配置文件、终端输出、错误日志与 IDE 截图的专项 OCR 评测。固定测试集共 304 题（内容版本 5.2），采用「P01–P09 主类别 × 难度」双轴诊断；v5.2 结果不与 v4 及更早内容版本直接混排。

---

## 站点架构与自动同步

本项目采用 **Markdown 驱动**，仓库内的 `.md` 文件是唯一数据源。修改 `code/**` 或 `ocr/**` 下的文件并推送至 `main` 分支后，GitHub Actions（`.github/workflows/sync-md.yml`）会自动运行 `scripts/sync_md.py`，编译生成 `docs/` 目录下的静态页面与数据文件。

### 数据源与产物映射

| 数据源 (Markdown) | 生成页面 (`docs/`) | 生成数据 (`docs/data/`) | 用途说明 |
| --- | --- | --- | --- |
| `code/code_bench.md` | `bench.html` | `code_bench/v1.5-rank.csv`<br>`notes.json` | 总说明、默认排行，以及首页底部的「分析 / 声明 / 致谢」 |
| `code/<子项>.md`（如 `full-v3`、`rust-v3-2`、`cowork`） | `full-v3.html`、`cowork.html` 等 | `code_bench/v1.5-*.csv` | 各子项题目说明与榜单明细 |
| `code/monthly/<YYYY-MM>.md` | `monthly-2026-10.html` 等 | `code_bench/v1.5-monthly-*.csv` | 历史月榜快照（含已退榜历史模型） |
| `code/code_bench_archive.md` | `archive.html` | `code_bench/archive-*.csv` | 旧版本题目与历史成绩归档 |
| `ocr/ocr_benchmark_v5.md` | `ocr_bench.html` | `ocr_bench/*.csv` | OCR v5 评测说明与榜单数据 |

> **前端渲染逻辑**：首页仪表盘（`index.html`）由 `docs/assets/app.js` 读取 `docs/data/datasets.json` 驱动。实时月榜由前端跨子项 CSV 按模型名实时聚合（JOIN），历史月榜则直接读取对应的快照 CSV。

---

## 本地开发与扩展

### 本地预览

```bash
# 根据 Markdown 重新生成 HTML、CSV 与 notes.json
python3 scripts/sync_md.py

# 仅校验格式与表头，不写入文件（CI 校验用；退出码恒为 0，需看输出里有没有「需要更新」）
python3 scripts/sync_md.py --check

# 启动本地服务预览站点
cd docs && python3 -m http.server
```

### 新增一个 Benchmark

1. **配置构建规则**：在 `scripts/sync_md.py` 的 `SYNC_CONFIG` 中参照现有条目新增配置，声明 `doc_page`（说明页路径）、`page`（标题 / 导航等元信息）、`csvs`（Markdown 小节与输出 CSV 的映射）及 `expected_headers`（表头校验）。
2. **注册前端展示**：在 `docs/data/datasets.json` 中登记对应数据集（指定 `category`、`reportDate`、`tableIndex`、`title`、`csv` 等；矩阵视图需带 `type: "matrix"`，code 子项需声明 `tier: "basic" | "advanced"` 与 `fullScore`），否则前端不会加载该数据。
3. **同步首页说明（可选）**：如需将 Markdown 中的特定小节渲染至首页底部，在 `scripts/sync_md.py` 的 `notes.sections` 中登记小节名称即可。

---

## 赞助

如果这个项目对你有帮助，欢迎通过赞助支持持续开发与题库维护：

<img src="https://raw.githubusercontent.com/snnh/openwebcode/refs/heads/main/assets/donate-wechat.png" alt="微信赞赏码" width="240">

---

## 致谢

1. 感谢 [llm2014](https://github.com/llm2014/llm_benchmark) 的网站模板，欢迎大家前往他的 benchmark，他才是真大佬。
2. 感谢 shyliuli 和 Karpy II。
