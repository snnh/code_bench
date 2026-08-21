# 开发场景 OCR Benchmark v5

更新时间：2026-07-15

开发场景 OCR 不只关心字符编辑距离。代码、配置、终端、错误日志和 IDE 截图更重视符号、缩进、阅读顺序、结构格式、噪声控制，以及输出能否直接复制、搜索和理解。

Benchmark 名称保持 v5，当前内容版本为 5.2。固定测试集包含 304 题，使用 P01-P09 主类别与 `simple` / `medium` / `hard` 难度双轴诊断。v5.2 结果不能与 v4 或更早内容版本直接混排。

## 数据集

当前活动数据集为 `code_ocr_eval_benchmark_v5_content_5_2_photo30_20260710`，入口为仓库根目录：

```text
test.jsonl
test.json
测试集/
```

难度分布：

| 难度 | 数量 |
| --- | ---: |
| simple | 63 |
| medium | 156 |
| hard | 85 |

类别分布：

| 主类别 | 数量 |
| --- | ---: |
| P01 代码编辑器主体 | 75 |
| P02 终端与命令行 | 35 |
| P03 报错诊断与日志 | 36 |
| P04 配置与工程声明 | 31 |
| P05 版本控制与代码审阅 | 20 |
| P06 文档与网页代码块 | 33 |
| P07 API 参考与表格化结构 | 24 |
| P08 交互式开发工具视图 | 20 |
| P09 多区域混合开发屏 | 30 |

## 流程

```text
固定 304 题 v5.2 测试集 + 模型 OCR 预测文本
        |
dev_ocr_judge_v5_compat 六维 LLM 裁判
        |
样本分 -> P01-P09 类别加权
        |
基础稳定性、难度风险与可靠性扣分
        |
Benchmark v5 最终积分 + 类别/难度诊断
```

## Benchmark v5 结果

最终排序使用 `final_score_v5`。全局均值和 NED 仅作诊断，不直接参与最终积分。LLM 裁判带来的总分展示误差按 `±0.5` 计，小于 0.5 分的差距不视为显著差异。不同提示词策略不得混排。

### 短提示榜 `<image>OCR:`

| 方案 | 记录 | 最终积分 | 原始积分 | 类别加权 | 全局均值 | 最弱类别 | 最弱难度 | 严格可用率 | 完成率 | 安全分 | 平均 NED | 报告 | 备注 |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| PaddleOCR-VL-1.6 本地微调版 | 304/304 | 58.4427 ±0.5 | 60.3374 | 72.8633 | 73.3494 | P09 | hard | 38.1579% | 99.0132% | 90.7895% | 0.1744 | [report](reports/ppocr-vl16-6-for-code+local-finetune+image_ocr.md) | 本地 vLLM；正式参数 `max_tokens=4096`、`repetition_penalty=1.08`、`temperature=0` |
| StepFun step-3.7-flash(high) | 304/304 | 57.3628 ±0.5 | 62.3365 | 75.7061 | 75.5229 | P09 | hard | 50.3289% | 97.6974% | 79.2763% | 0.2481 | [report](reports/step-3.7-flash+high+image_ocr.md) | StepFun 官网 API；`reasoning_effort=high` |
| Qwen3.7 Plus (thinking) | 303/304 | 42.3615 ±0.5 | 55.8352 | 74.8958 | 74.9389 | P03 | hard | 28.9474% | 99.6711% | 64.1447% | 0.4205 | [report](reports/qwen3.7-plus+thinking+image_ocr.md) | 阿里百炼 API；API 默认 thinking；主批次 `max_tokens=4096`、`temperature=0`；1 条默认参数补跑成功，另 1 条持续 504 |
| DeepSeek V4 Flash Vision-Exp (thinking) | 304/304 | 42.2189 ±0.5 | 52.89 | 71.5374 | 71.7351 | P03 | hard | 32.5658% | 95.0658% | 71.7105% | 0.2502 | [report](reports/deepseek-v4-flash-vision-exp+think+image_ocr.md) | 官方；`temperature=0`、`max_tokens` 不限；裁判为 deepseek-v4-flash 开思考 |
| PaddleOCR-VL-1.6 官网 API | 303/304 | 40.1408 ±0.5 | 44.0553 | 63.8491 | 62.3878 | P01 | hard | 25.6579% | 98.0263% | 80.2632% | 0.2660 | [report](reports/PaddleOCR-VL-1.6+official+image_ocr.md) | 官网异步 API；沿用旧版 1 条缺失记录 |
| HyOCR 1.5 本地 vLLM | 304/304 | 29.0668 ±0.5 | 39.5339 | 59.8956 | 60.6122 | P09 | hard | 28.9474% | 98.6842% | 57.8947% | 0.3813 | [report](reports/hyocr1.5+local-vllm+image_ocr.md) | `temperature=0.0`；`top_p=1.0`；`top_k=-1`；`repetition_penalty=1.08` |
| Gemini 3.5 Flash (medium) | 304/304 | 0.0000 ±0.5 | 6.7391 | 40.3386 | 39.1830 | P01 | medium | 1.3158% | 94.7368% | 12.8289% | 0.6807 | [report](reports/gemini-3.5-flash+medium+image_ocr.md) | 中转站 OpenAI-compatible API；短提示 |
| Kimi K2.6 (thinking) | 304/304 | 0.0000 ±0.5 | 6.4828 | 38.7807 | 38.9743 | P03 | medium | 1.9737% | 94.7368% | 11.5132% | 0.7793 | [report](reports/kimi-k2.6+thinking+image_ocr.md) | 阿里百炼 API；API 默认 thinking；`max_tokens=4096`、`temperature=0` |

短提示榜结论：

- PaddleOCR-VL-1.6 本地微调版以正式参数成绩 `58.4427` 暂列第一，领先 StepFun step-3.7-flash(high) `1.0799` 分。
- Step 的类别加权分与严格可用率更高，但 severe 比例更高；本地微调版的安全分为 `90.7895%`，完成率为 `99.0132%`。
- 本地微调版 `rp=1.08` 比 `rp=1.10` 诊断分高 `0.3581`：simple 直接可用率提高并减少基础题扣分，但 P09、hard 和类别加权分略降。
- Qwen3.7 Plus 的类别加权分达到 `74.8958`，但 186 次解释性输出和 170 次额外包装把可靠性扣分推到 `13.4737`；另有 1 条复杂画面持续 504。
- DeepSeek V4 Flash Vision-Exp 的 NED（`0.2502`）与类别加权分（`71.5374`）接近第一梯队，但 simple 直接可用率仅 `33.3333%`、P03 与 P09 的 severe 偏高，可靠性扣分为 `10.6711`。注意该行裁判为 deepseek-v4-flash 开思考模式。
- PaddleOCR-VL-1.6 官网 API 完成率较高，但 simple 直接可用率和 P01 代码场景得分偏低。
- HyOCR 1.5 在文档、配置等单区域内容上有一批高质量结果，但 severe 达到 `42.1053%`；多区域画面中的解释、幻觉和代码改写使最终积分降至 `29.0668`。
- Gemini 在短提示下频繁产生解释、补全和改写，可靠性扣分达到上限，最终积分为 `0`。
- Kimi K2.6 几乎把整套测试当成代码讲解任务，293 题出现解释性文字、205 题出现幻觉，最终积分为 `0`。

### 官方推荐提示词榜

本组使用模型卡官方推荐提示词，不与 `<image>OCR:` 短提示榜直接排序。OvisOCR2 的提示词要求提取全部可读内容、按 Markdown 输出，并把表格转换为 HTML；这一目标与开发截图的主区域忠实转写存在口径差异。

| 方案 | 记录 | 最终积分 | 原始积分 | 类别加权 | 全局均值 | 最弱类别 | 最弱难度 | 严格可用率 | 完成率 | 安全分 | 平均 NED | 报告 | 备注 |
| --- | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| OvisOCR2 本地 vLLM | 304/304 | 49.1981 ±0.5 | 53.3494 | 68.4454 | 67.9593 | P09 | hard | 29.2763% | 96.0526% | 79.6053% | 0.2414 | [report](reports/ovisocr2+local-vllm+official-prompt.md) | 官方模型卡提示词；`temperature=0.0`；本地 vLLM `0.21.0` |

本组结论：

- OvisOCR2 在 P06 文档代码块、P02 终端和 P04 配置上表现较好，类别分分别为 `78.4000`、`77.8444`、`74.4524`。
- 官方“全部可读内容”提示使行号、标签页和其他 UI 更容易进入输出，`extra_ui_text` 达 172 次；P01 和 P09 分别只有 `56.7428`、`56.2631`。
- P07 表格类受官方 HTML 转换要求与忠实转写真值的双重影响，类别分为 `64.3873`，severe 为 `37.5000%`。
- 15 题输出长度超过真值 3 倍，重复输出出现 12 次；最终可靠性扣分为 `4.1513`。

### 类别诊断（短提示）

| 类别 | 最佳方案 | 类别分 |
| --- | --- | ---: |
| P01 代码编辑器主体 | Qwen3.7 Plus (thinking) | 73.0144 |
| P02 终端与命令行 | StepFun step-3.7-flash(high) | 84.3840 |
| P03 报错诊断与日志 | StepFun step-3.7-flash(high) | 75.3920 |
| P04 配置与工程声明 | Qwen3.7 Plus (thinking) | 84.7752 |
| P05 版本控制与代码审阅 | StepFun step-3.7-flash(high) | 74.8332 |
| P06 文档与网页代码块 | StepFun step-3.7-flash(high) | 90.0255 |
| P07 API 参考与表格化结构 | StepFun step-3.7-flash(high) | 81.0332 |
| P08 交互式开发工具视图 | Qwen3.7 Plus (thinking) | 85.7786 |
| P09 多区域混合开发屏 | Qwen3.7 Plus (thinking) | 70.5303 |

### 难度诊断（短提示）

| 难度 | 最佳方案 | 难度分 | severe |
| --- | --- | ---: | ---: |
| simple | StepFun step-3.7-flash(high) | 80.3142 | 14.2857% |
| medium | StepFun step-3.7-flash(high) | 77.3041 | 21.1538% |
| hard | Qwen3.7 Plus (thinking) | 71.6304 | 36.4706% |

## LLM 六维评分

裁判模型为 `tencent/hy3:free`，prompt 版本为 `dev_ocr_judge_v5_compat_hy3_reasoning_none`。裁判只比较人工真值与模型输出，不把 NED 传入 prompt。`DeepSeek V4 Flash Vision-Exp (thinking)` 一行为口径例外：该行使用 `deepseek-v4-flash` 裁判（开思考、max_tokens 不限、同一 prompt 版本），严格度高于 hy3 裁判，其积分仅作参考，不参与横向排序比较。

| 维度 | 满分 | 含义 |
| --- | ---: | --- |
| `content_coverage_0_10` | 10 | 主要内容覆盖 |
| `symbol_accuracy_0_10` | 10 | 字符、代码符号、大小写、数字、路径和标点准确性 |
| `indentation_alignment_0_10` | 10 | 缩进、嵌套层级、表格或列表对齐 |
| `structure_format_0_10` | 10 | 换行、代码块、列表、表格和区域结构 |
| `reading_region_order_0_10` | 10 | 阅读顺序、区域顺序和多文本块顺序 |
| `noise_and_usability_0_10` | 10 | 重复、幻觉、无关文本、解释性文字和实际可用性 |

## 积分规则

样本分：

```text
sample_score = 100 * (
  0.18 * content_coverage^1.35
+ 0.24 * symbol_accuracy^1.35
+ 0.16 * indentation_alignment^1.35
+ 0.16 * structure_format^1.35
+ 0.10 * reading_region_order^1.35
+ 0.16 * noise_and_usability^1.35
)
```

P01-P09 类别权重依次为 `15% / 8% / 15% / 12% / 10% / 8% / 12% / 8% / 12%`。每个类别先求样本分均值，再进行类别加权。

最终公式：

```text
raw_score_v5 =
  category_weighted_score_v5
- simple_penalty_v5
- medium_risk_penalty_v5
- hard_risk_penalty_v5

final_score_v5 = clamp(raw_score_v5 - reliability_penalty_v5, 0, 100)
```

simple 基础题只扣分不加分；medium 和 hard 按 severe 比例扣分。可靠性扣分综合 severe、缺失、代码改写及幻觉/解释比例，上限为 15 分。完整公式见 `文档/评测/benchmark_guide_v5.md`。

## Severe Badcase

以下情况计入 severe：

```text
missing_record
or noise_and_usability_0_10 <= 1
or content_coverage_0_10 <= 2
or symbol_accuracy_0_10 <= 2
or structure_format_0_10 <= 2
or error_tags contains code_added_removed_or_rewritten
or error_tags contains hallucinated_text
or error_tags contains empty_or_too_short
or error_tags contains refusal_or_unrecognized
or error_tags contains repeated_output
or output_length > 3 * label_length and noise_and_usability_0_10 <= 4
```

任一主类别或难度切片的 severe 比例超过 35% 时，应在对应模型报告中标记该切片不稳定。标签由 StepFun `step-3.7-flash` 每请求 5 张图片生成，仅用于视觉切片，不参与积分。
