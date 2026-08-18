# code_bench v1.1

[榜单查询](https://snnh.github.io/code_bench/)

## 简介
1. 本评测是个人性质
2. 本评测的题库规模不大，不使用任何互联网公开题目。题目会有更新，不同版本号成绩会有所差距，请以最新为准。每个人应该根据自己所需，对大模型进行考察。不可盲信任何评测。

## 题目结构

| 题 | 满分 | 内容 |
| --- | --- | --- |
| 基础题 · core | 30 | 复刻 C11 执行器 `owc-exec`（stdio JSON-RPC 2.0） |
| 基础题 · server | 30 | 复刻 Node 20+ 服务层（HTTP/WS API + agent 循环） |
| 基础题 · web | 30 | 复刻 React 19 + Vite 前端 |
| 基础题 · 拼接(题目编写中) | 10 | 三个子项拼成端到端系统，**不限制拼接方法**（A/B/C 档系数 1.0/0.8/0.5） |
| **基础题总分** | **100** | 3×30 + 10 − 中断扣分 |
| 高阶题 · full | 100 | 三层完整复刻（独立一张卷） |

## 环境

debian13 x86-64 上使用 [openwebcode](https://github.com/snnh/openwebcode)

* 注：*部分模型会开启环境模拟扩展以发挥最高水平*

## 致谢

1. 感谢[llm2014](https://github.com/llm2014/llm_benchmark)的网站模板，欢迎大家前往他的benchmark，他才是真大佬。
2. 感谢shyliuli提供的glm5.3 server项目评测环境