## 题目

| 题 | 满分 | 内容 |
| --- | --- | --- |
| 高阶题 · rust v3.3 | 100 | 一个rust后端加sqlite加静态前端(rust为绝对主要) |

## 榜单

| 模型 | 积分 | 成本(折算API价格) | 订阅折算 | 输出token | 缓存 | 接入方式 | 备注 |
|---|---|---|---|---|---|---|---|
| deepseek-flash-1017(max) | 61.34 | 3.28-6.56元 | 无 | 214k | 92.2%(23.151m) | 官方api | 无 |
| kimi-k3.1-pro(high) | 60.26 | 34.34元 | 2.74元 | 81k | 98.5%(19.301m) | kimi订阅 | 无 |
| ernie-light-dt-1.0(max) | 59.83 | 46.64元 | 14元 | 242k | 99.3%(46.514m) | 千帆tokenplan | 无 |
| qwen4-1102(xhigh) | 59.72 | 43.5元 | 6.96元 | 138k | 71%(8.571m) | - | 无 |
| qwen-latest-series-invite-2609(xhigh) | 58.85 | -元 | - | 266k | 97%(21.792m) | 官方api | 无 |
| ernie-5.5-flash-preview(high) | 58.14 | 5.9元 | 1.77元 | 146k | 98.3%(45.293m) | 官方api | 无 |
| mimo-v2.6-pro(thinking) | 57.82 | 1.8元 | 1.458元 | 155k | 97.7%(9.146m) | 官方api | 无 |
| qwen4-max-preview(xhigh) | 57.82 | -元 | 1125credits | 163k | 89.8%(17.308m) | qwen tokenplan | 无 |
| claude-haiku-5.5(xhigh) | 57.72 | 约10元 | - | 892k | 87.4%(10.214m) | zenmux api | claudecode预设 |
| deepseek-v4.1-flash(max) | 54.23 | 1.67-3.34元 | 无 | 283k | 97.7%(20.114m) | 官方api | 无 |
| qwen3.8-flash(max) | 52.52 | 4.98元 | 1.243元 | 261k | 98%(36.75m) | 官方api | 无 |
| ernie-5.5-flash-preview(low) | 50.14 | 1.21元 | 0.363元 | 61k | 96.5%(7.035m) | 官方api | 无 |
| minimax-m3.1-flash(max) | 47.95 | 7.82元 | - | 432k | 99.8%(58.965m) | zenmux api | 无 |
| gpt-5.6-luna(max) | 47.34 | 4.19元 | - | 140k | 98.6%(19.426m) | zenmux api | 无 |
| step-5-preview(high) | 36.98 | 24.6元 | 0.61元 | 258k | 99.7%(55.503m) | step订阅 | 无 |
| glm5.3(max) | - | -元 | -元 | -k | -%(-m) | 官方api | zcode预设 |
| glm-5.3-flash(max) | - | -元 | -元 | -k | -%(-m) | 官方api | zcode预设 |
| hy4-preview(high) | - | -元 | - | -k | -%(-m) | - | - |
| kimi-k2.8-preview(max) | - | -元 | - | -k | -%(-m) | kimi订阅 | kimicode预设 |
| kimi-k3(max) | - | -元 | - | -k | -%(-m) | kimi订阅 | kimicode预设 |

## 说明

* 满分 100；`积分` 为该子项一次完整交付的得分
* `成本(折算API价格)`：按模型官方/中转 API 价格折算的一次评测费用，`-` 为未统计
* `订阅折算`：按订阅套餐折算的单次成本（单位见单元格，如 `元`、`credits`）
* `输出token`：输出 token 总量（由缓存命中 token 反算，四舍五入到 5k，标注 `(估算)`）
* `缓存`：prompt cache 命中率与命中 token 量
* `接入方式` / `备注`：调用渠道与所用预设
* 缺测显示 `-` 或 `未测试`；表格默认按积分降序，点表头可切换升降序，缺测始终排在最后
