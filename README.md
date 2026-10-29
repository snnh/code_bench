# code_bench · 大模型开发能力评测

个人维护的大模型**开发场景**评测榜单，托管于 GitHub Pages：

- 榜单查询：<https://snnh.github.io/code_bench/>

## 简介

1. 本评测是个人性质，题库规模不大，不使用任何互联网公开题目。
2. 题目会更新，不同版本号成绩会有所差距，请以最新为准。
3. 每个人应依据自身需求考察大模型，不可盲信任何评测。

---

## 评测项目

### code_bench v1.5

复刻 openwebcode（C11 执行器、Node 服务层、React 前端）的编程题评测：

- **月榜**：按月划分的模型 × 子项矩阵（无总分列）——`2026-10` 起只保留 v3.x（full_v3 / rust v3.1），`2026-09` 为旧结构快照；默认显示最新月份
- **基础题**：core / server / web v2（旧版 web 已归档）
- **高阶题**：full_v3 / rust v3.1（满分 100，成绩陆续补测）
- **历史模型**：已退出现行排行的模型统一归档到 `2026-09` 月榜快照（不再单独成数据集）
- **归档**：rust（v1）、rust v2.1、full_v2 与旧版 web
- **明细页**：`core.html` / `server.html` / `web-v2.html` / `full-v3.html` / `rust-v3-1.html`（数据源为 `code/core.md` 等独立文件）
- **月榜快照页**：`monthly-2026-09.html`（数据源 `code/monthly/2026-09.md`）

- 说明页：`docs/bench.html`
- 归档页：`docs/archive.html`
- 榜单数据：`docs/data/code_bench/*.csv`
- 排行：`docs/data/code_bench/v1.5-rank.csv`（总榜默认排序依据）

### 开发场景 OCR Benchmark v5

针对代码、配置、终端、错误日志与 IDE 截图的 OCR 评测，P01–P09 主类别 × 难度双轴诊断，固定测试集 304 题。

- 说明页：`docs/ocr_bench.html`
- 榜单数据：`docs/data/ocr_bench/*.csv`

---

## 站点结构

GitHub Pages 站点由 `docs/` 提供：

| 页面 | 内容 |
| --- | --- |
| `index.html` | 榜单仪表盘（总榜矩阵、象限图、交互筛选、排序、搜索、趋势图，底部为 md 自动生成的说明与分析） |
| `bench.html` | code_bench v1.5 总说明（题目结构 / 实时排行 / 说明 / 分析） |
| `core.html`、`server.html`、`web-v2.html`、`full-v3.html`、`rust-v3-1.html` | 各子项题目与榜单明细 |
| `monthly-2026-09.html` | 2026-09 月榜快照（含历史模型） |
| `archive.html` | code_bench 归档（rust v1 / rust v2.1、full_v2 与旧版 web 题目、榜单） |
| `ocr_bench.html` | 开发场景 OCR Benchmark v5 题目说明 |

榜单数据以 CSV 存于 `docs/data/<bench>/`，由 `docs/assets/app.js` + `docs/data/datasets.json` 驱动。code 类别提供**月榜矩阵**：`datasets.json` 中 `type:"matrix"` 的条目（`code_total`）按月划分。实时月榜（如 `2026-10`）由 `app.js` 跨 `code_detail` 各子项 CSV 按「模型」列 JOIN 成模型 × 子项矩阵（无总分列），可用 `matrixColumns` 限定列、`matrixOnlyScored` 只保留有成绩的模型、`matrixExcludeModels` 排除已归档模型；历史月（如 `2026-09`）用 `matrixSource:"snapshot"` 直接读快照 CSV（`columns` 声明每列满分与 tier）。默认按排行行序排序（未上榜模型按加权平均分降序：各子项折算百分制后高阶项权重 2、基础项权重 1），`tier:"advanced"` 的子项列名加“(高阶)”后缀。

---

## 站点自动同步

`docs/` 下的说明页、榜单 CSV 与站点底部说明 **由 Markdown 自动生成**，Markdown 是唯一数据源：

| 数据源 | 生成的说明页 | 生成的榜单 CSV | 生成的底部说明 |
| --- | --- | --- | --- |
| `code/code_bench.md` | `docs/bench.html` | `v1.5-rank.csv` | `docs/data/notes.json`（「分析 / 声明 / 致谢」小节） |
| `code/core.md` 等 5 个子项文件 | `docs/core.html` 等 | `v1.5-core.csv` 等 | — |
| `code/monthly/2026-09.md` | `docs/monthly-2026-09.html` | `v1.5-monthly-2026-09.csv` | — |
| `code/code_bench_archive.md` | `docs/archive.html` | `docs/data/code_bench/archive-rust.csv`、`archive-rust-v2.1.csv`、`archive-full-v2.csv`、`archive-web.csv` | — |
| `ocr/ocr_benchmark_v5.md` | `docs/ocr_bench.html` | `docs/data/ocr_bench/*.csv` | — |

修改上述 Markdown 并推送到 `main` 后，GitHub Actions（`.github/workflows/sync-md.yml`）自动运行 `scripts/sync_md.py`，重新生成 HTML、CSV 与 `notes.json` 并提交。工作流监听 `code/**` 与 `ocr/**` 路径。

榜单页（`index.html`）底部的「说明与分析」板块由 `docs/data/notes.json` 驱动（`app.js` 的 `loadSiteNotes` / `renderSiteNotes`）：内容取自 md 里的小节，改 md 即自动更新；要新增小节只需在 `scripts/sync_md.py` 的 `notes.sections` 中登记小节名。

code 子项榜单默认以**百分制**显示积分（按子项满分折算，可在“分数显示”切回原始分），并带**象限图**（积分 × 成本 / Token 效率），指标下拉按当前 CSV 实际列动态生成，分界取当前数据集的中位数；成本为区间（如 `3.24-6.48元`）时取下界，token 的 `k`/`m` 后缀按真实数量级还原。

### 本地预览

```bash
python3 scripts/sync_md.py          # 生成 / 更新 HTML 与 CSV
python3 scripts/sync_md.py --check  # 只校验不写文件（CI 用）

cd docs && python3 -m http.server   # 本地预览站点
```

### 新增一个 benchmark

在 `scripts/sync_md.py` 的 `SYNC_CONFIG` 中按现有条目格式新增配置即可：

- `doc_page`：说明页路径
- `page`：标题 / 副标题 / 导航 / 提示语
- `csvs`：md 小节 → CSV 路径的映射
- `expected_headers`：各 CSV 期望表头（用于校验）

另外需在 `docs/data/datasets.json` 登记表格（`category` / `title` / `csv` 等；矩阵项带 `type:"matrix"`，code 子项另带 `tier: basic|advanced`），否则前端不会显示该 CSV。

---

## 致谢

1. 感谢 [llm2014](https://github.com/llm2014/llm_benchmark) 的网站模板，欢迎大家前往他的 benchmark，他才是真大佬。
2. 感谢 shyliuli 和 Karpy II
