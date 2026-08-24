# code_bench · 大模型开发能力评测

个人维护的大模型**开发场景**评测榜单，托管于 GitHub Pages：

- 榜单查询：<https://snnh.github.io/code_bench/>

## 简介

1. 本评测是个人性质，题库规模不大，不使用任何互联网公开题目。
2. 题目会更新，不同版本号成绩会有所差距，请以最新为准。
3. 每个人应依据自身需求考察大模型，不可盲信任何评测。

## 评测项目

### code_bench v1.2

复刻 openwebcode（C11 执行器、Node 服务层、React 前端）的编程题评测，含基础题（core / server / web / 拼接）与高阶题（full）。

- 说明页：`docs/bench.html`
- 榜单数据：`docs/data/code_bench/*.csv`

### 开发场景 OCR Benchmark v5

针对代码、配置、终端、错误日志与 IDE 截图的 OCR 评测，P01–P09 主类别 × 难度双轴诊断，固定测试集 304 题。

- 说明页：`docs/ocr_bench.html`
- 榜单数据：`docs/data/ocr_bench/*.csv`

## 站点结构

GitHub Pages 站点由 `docs/` 提供：

| 页面 | 内容 |
| --- | --- |
| `index.html` | 榜单仪表盘（交互筛选、排序、搜索、趋势图） |
| `bench.html` | code_bench v1.2 题目说明 |
| `ocr_bench.html` | 开发场景 OCR Benchmark v5 题目说明 |

榜单数据以 CSV 存于 `docs/data/<bench>/`，由 `docs/assets/app.js` + `docs/data/datasets.json` 驱动。

## 站点自动同步

`docs/` 下的说明页与榜单 CSV **由 Markdown 自动生成**，Markdown 是唯一数据源：

| 数据源 | 生成的说明页 | 生成的榜单 CSV |
| --- | --- | --- |
| `code/code_bench.md` | `docs/bench.html` | `docs/data/code_bench/*.csv` |
| `ocr/ocr_benchmark_v5.md` | `docs/ocr_bench.html` | `docs/data/ocr_bench/*.csv` |

修改上述 Markdown 并推送到 `main` 后，GitHub Actions（`.github/workflows/sync-md.yml`）自动运行 `scripts/sync_md.py`，重新生成 HTML 与 CSV 并提交。工作流监听 `code/**` 与 `ocr/**` 路径。

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

## 致谢

1. 感谢 [llm2014](https://github.com/llm2014/llm_benchmark) 的网站模板，欢迎大家前往他的 benchmark，他才是真大佬。
2. 感谢 shyliuli 提供的 glm5.3 server 项目评测环境。
