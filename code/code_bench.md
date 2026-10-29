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
| 高阶题 · rust v3.1 | 100  | 一个rust后端加sqlite加静态前端(rust为绝对主要)    |

* 子项明细：[core](core.html) · [server](server.html) · [web v2](web-v2.html) · [full_v3](full-v3.html) · [rust v3.1](rust-v3-1.html)
* 历史月榜：[2026-09](monthly-2026-09.html)
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
| kimi-k3.1-pro(high) |
| qwen-latest-series-invite-2609(max) |
| kimi-k3(max) |
| mimo-v2.6-pro(thinking) |
| deepseek-v4.1-flash(max) |
| claude-haiku-5.5(xhigh) |
| kimi-k2.8-preview(max)    |
| hy4-preview(high) |
| glm5.3(max) |
| minimax-m3.1-flash(max) |
| gpt-5.6-luna(max) |
| glm-5.3-flash(max) |
| step-5-preview(high) |
| gemini-3.7-flash(high) |
| ... |

实时总榜见[榜单查询](./)。

---

## 说明

* token消耗未统计缓存，缓存消耗具体看细则缓存部分
* kimi订阅倍率约0.07-0.08(199档实测)
* glm5.3订阅倍率约0.08(官方api文档说明)
* glm5.3flash订阅倍率约0.26(官方api文档说明)
* qwen订阅倍率约0.2495(官方api文档说明)
* step订阅倍率约0.025(官方api文档说明)
* mimo订阅倍率约0.81

---

## 分析

1. K3在C部分相当高效，但在full_v2项目C之外的部分表现不佳，（high思考强度偏向于节省token精简架构，无论是c项目还是前端项目，都比其他的更简洁，c因为有编译器兜底，所以bug更少，web需要人工review，模型为了省token，导致部分bug没找出来）
2. 单纯从颜值上来讲，我更喜欢k3的风格，美观程度为主观评判，未参与积分
3.  实际体验来讲，glm5.3好于v4-pro0813，v4稳定性难评
4. v4.1f-0910稳定性不如glm5.3好于v4p，但速度极快
5. step5preview有些复古
6. kimi-k2.8-preview细节不行，虽然不影响得分，但影响后续开发速度和体验
7. ...

---

## 声明

0. full_v2项目主要反映模型从0到1的理解用户需求，规划和开发能力
1. 本bench由 github 用户 [snnh](https://github.com/snnh) 版权所有。
2. 接受模型送测(只是为了多体验更多模型)
3. 欢迎赞助token

---

## 致谢

1. 感谢shyliuli和Karpy II提供的glm5.3评测环境
