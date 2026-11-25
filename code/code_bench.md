# code_bench v1.5

## 题目结构

| 题目              | 满分      | 内容                                             |
| --------------- | ------- | ---------------------------------------------- |
| 基础题 · core      | 30      | 复刻 C11 执行器 `owc-exec`（stdio JSON-RPC 2.0）      |
| 基础题 · server    | 30      | 复刻 Node 20+ 服务层（HTTP/WS API + agent 循环）        |
| 基础题 · web  v2  | 30      | 复刻 React 19 + Vite 前端  基于owc1.9.9版本提交          |
| 基础题 · 拼接(题目编写中) | 10      | 三个子项拼成端到端系统，**不限制拼接方法**（A/B/C 档系数 1.0/0.8/0.5） |
| 基础题·python      | 30 | 用python开发一个文件分享程序                               |
| 高阶题 · full_v3 | 100 | 3大+1小模块，开发一个coding agent |
| 高阶题 · rust v3.3 | 100  | 一个rust后端加sqlite加静态前端(rust为绝对主要)    |
| 高阶题 · cowork | 100 | 辅助教师办公 |

* 子项明细：[core](core.html) · [server](server.html) · [web v2](web-v2.html) · [full_v3](full-v3.html) · [rust v3.3](rust-v3-3.html) · [cowork](cowork.html)
* 历史月榜：[2026-10](monthly-2026-10.html) · [2026-09](monthly-2026-09.html)
* 已归档：高阶题 · full_v2（见[归档页](archive.html)）

---

## 环境

debian13 x86-64 上使用 [openwebcode](https://github.com/snnh/openwebcode)

* 注：*部分模型会开启环境模拟扩展以发挥最高水平*

---

## 排行

| 模型 |
| --- |
| deepseek-flash-1017(max) |
| hy4(high) |
| kimi-k3.1-pro(high) |
| qwen4-1102(xhigh) |
| qwen-latest-series-invite-2609(xhigh) |
| ernie-light-dt-1.0(max) |
| ernie-5.5-flash-preview(high) |
| claude-haiku-5.5(xhigh) |
| mimo-v2.6-pro(thinking) |
| qwen4-max-preview(xhigh) |
| deepseek-v4.1-flash(max) |
| minimax-m3.1-flash(max) |
| gpt-5.6-luna(max) |
| step-5-preview(high) |
| ... |

实时总榜见[榜单查询](./)。

---

## 说明

* token消耗未统计缓存，缓存消耗具体看细则缓存部分
* kimi订阅倍率约0.07-0.08(199档实测)
* glm5.3订阅倍率约0.08(官方api文档说明)
* glm5.3flash订阅倍率约0.26(官方api文档说明)
* qwen订阅倍率约0.16(官方api文档说明)
* step订阅倍率约0.025(官方api文档说明)
* mimo订阅倍率约0.81
* hy4按照0.25x倍率进行推算
* 千帆tokenplan倍率约0.3x
* 榜单默认按积分降序，缺测（`-` / `未测试`）始终排在最后；点表头可切换升降序，第三次点击恢复默认顺序
* 各子项满分不同（core / server / web v2 各 30，full_v3 / rust v3.3 / cowork 各 100），总榜按各子项满分折算百分制后再横向比较
* 模型具体水平请按各子项分别判断，总榜顺序只代表作者大致印象

---

## 分析

1. 部分模型的具体分析详见微信公众号 热爱ai的省略号
2. haiku5.5的实际体验很差劲
3. ernie-5.5-flash-preview在不同思考强度下，前端区别极大，简单问题几乎无差别

---

## 声明

0. full项目主要反映模型从0到1的理解用户需求，规划和开发能力
1. 本bench由 github 用户 [snnh](https://github.com/snnh) 版权所有。
2. 接受模型送测(只是为了多体验更多模型)
3. 欢迎赞助token

---

## 致谢

1. 感谢shyliuli和Karpy II提供的glm5.3评测环境
