# code_bench v1.3

## 题目结构

| 题目              | 满分      | 内容                                             |
| --------------- | ------- | ---------------------------------------------- |
| 基础题 · core      | 30      | 复刻 C11 执行器 `owc-exec`（stdio JSON-RPC 2.0）      |
| 基础题 · server    | 30      | 复刻 Node 20+ 服务层（HTTP/WS API + agent 循环）        |
| 基础题 · web  v2  | 30      | 复刻 React 19 + Vite 前端  基于owc1.9.9版本提交          |
| 基础题 · 拼接(题目编写中) | 10      | 三个子项拼成端到端系统，**不限制拼接方法**（A/B/C 档系数 1.0/0.8/0.5） |
| 基础题·python      | 30 | 用python开发一个文件分享程序                               |
| 高阶题 · full_v2      | 100   |   3大+1小模块，开发一个coding agent    |
| 高阶题 · rust v2.1   | 50      | 一个网络服务开发，包含规则引擎 + 报文编解码 + 稀疏配置 + CLI四部分        |

---

## 环境

debian13 x86-64 上使用 [openwebcode](https://github.com/snnh/openwebcode)

* 注：*部分模型会开启环境模拟扩展以发挥最高水平*

---

## 排行

| 模型                              |
| --------------------------------- |
| deepseek-v4.1-flash(max) |
| kimi-k3(max)                     |
| kimi-k3(high)                     |
| hy4-preview(high) |
| deepseek-v4.1-flash-expires-on-0910(max) |
| glm5.3(max)                       |
| qwen3.8-flash(max)                |
| deepseek-v4-pro0813(max)          |
| deepseek-v4-flash0902(max) |
| glm-5.3-flash(max)                |
| deepseek-v4-flash-vision-exp(max) |
| glm-ox-alpha(max)                 |
| deepseek-v4-flash0731(max)        |
| gemini-3.7-flash(high)            |
| ...                               |

### 基础题

* token消耗未统计缓存，缓存消耗具体看细则缓存部分
* kimi订阅倍率约0.07-0.08(199档实测)
* glm5.3订阅倍率约0.08(官方api文档说明)
* glm5.3flash订阅倍率约0.26(官方api文档说明)
* qwen订阅倍率约0.3(官方api文档说明)

**core**

| 模型 | 积分 | 成本(折算API价格) | token(不算缓存) | 缓存 |
|---|---|---|---|---|
| kimi-k3(high)              | 26.2 | 54.89元 | 394k        | 98.7%(16.485m) |
| deepseek-v4.1-flash-expires-on-0910(max) | 26 | 3.24-6.48元 | 525k | 99.1%(36.854m) |
| deepseek-v4-pro0813(max)   | 26   | 9.33-18.66元 | 315k        | 99.8%(37.834m) |
| deepseek-v4-flash0902(max) | 25.8 | 6.43-12.86元  | 528k        | 99.8%(90.021m) |
| glm5.3(max)                | 25.6 | 82.19元      | 455k        | 99.3%(37.21m)  |
| glm-5.3-flash(max)                | 24.9 |  3.83元      | 499k        | 99.1%(29.582m)  |
| deepseek-v4-flash-vision-exp(max) | 25.2 | 3.53-7.06元 | 352k | 99.7%(46.685m) |
| deepseek-v4-flash0731(max) | 24.6 | 5.05-10.1元  | 782k        | 99.2%(57.256m) |
| glm-ox-alpha(max) | 24.2 | 0元 | 628k | 99.2%(55.048m) |
| gemini-3.7-flash(high)     | 23.7 | ~12.15元     | 1069k       | 91%(9.57m)     |

**server**

| 模型 | 积分 | 成本(折算API价格) | token(不算缓存) | 缓存 |
|---|---|---|---|---|
| kimi-k3(high)              | 27.2      | 14.63元      | 138k        | 97.8%(4.085m)  |
| deepseek-v4.1-flash-expires-on-0910(max) | 25.8(稳定性不好) | 2.31-4.62元 | 499k | 97.7%(20.219m) |
| glm5.3(max)                | 25.1      | 约30-40元     | ?k          | ?%(?m)         |
| deepseek-v4-pro0813(max)   | 25.8      | 4.75-9.5元   | 221k        | 99.5%(17.062m) |
| glm-5.3-flash(max)         | 23.8 |  5.44元      | 573k        | 99.1%(43.651m)  |
| deepseek-v4-flash0731(max) | 22.7/24.7 | 20.9-41.8元  | 12563k      | 72%(30.052m)   |
| gemini-3.7-flash(high)     | - | 元           | k           | %(m)           |
| … | 未测试 | 元 | k | %(m) |

**web v2**

| 模型 | 积分 | 成本(折算API价格) | token(不算缓存) | 缓存 | 接入方式 | 备注 |
|---|---|---|---|---|---|---|
| kimi-k3(high) | - | -元        | -k         | -%(-m)   | kimi订阅 | 无 |
| glm-5.3-flash(max) | 24 | 1.94元(限时5折) | 307k | 98.8%(14.674m) | 官方api | 无 |
| deepseek-v4.1-flash-expires-on-0910(max) | 24 | 4.22-8.44元 | 339k | 99.8%(60.087m) | 官方api | 无 |
| qwen3.8-flash(max) | 23.6 | 4.25元 | 735k | 98.5%(31.408m) | 官方api | 无 |
| glm5.3(max) | 23.4 | 32.14元       | 310k        | 98.7%(13.454m) | 官方订阅 | zcode预设 |
| hy4-preview(high) | 23.4 | 12.28元 | 636k | 97.8%(21.541m) | 官方API | 无 |
| deepseek-v4-flash-vision-exp(max) | 13.3 | 1.99元 | 503k  | 97.9%(15.849m)   | 官方api | 无 |
| deepseek-v4-pro0813(max) | - | -元    | -k        | -%(-m) | 官方api | 无 |
| … | 未测试 | 元 | k | %(m) | 官方 | 无 |


### 高阶题

**full_v2**

| 模型 | 积分 | 成本(折算API价格) | token(不算缓存) | 缓存 | 接入方式 | 备注 |
|---|---|---|---|---|---|---|
| deepseek-v4.1-flash(max) | 73.54 | 1.765-3.53元 | 354k | 99.7%(27.732m) | 官方api | 无 |
| deepseek-v4.1-flash-expires-on-0910(max) | 65.8 | 2.37-4.74元 | 311k | 99.7%(23.698m) | 官方api | 无 |
| glm5.3(max) | 61.5 | 98.28元 | 766k | 98.7%(44.189m) | glm订阅 | zcode |

**rust v2.1**

| 模型 | 积分 | 成本(折算API价格) | 订阅折算 | token(不算缓存) | 缓存 | 接入方式 | 备注 |
|---|---|---|---|---|---|---|---|
| hy4-preview(high) | 43.62 | 6.77元 | - | 412k | 97.5%(12.4m) | codebuddy | codebuddy cli(hy4-preview-x) |
| deepseek-v4.1-flash(max) | 41.57 | 1.03-2.06元 | 无 | 249k | 99.4%(13.376m) | 官方api | 无 |
| qwen3.8-flash(max) | 41.26(疑似优势区间) | 1.21元 | 0.363元 | 321k | 97%(6.324m) | 官方api | 无 |
| deepseek-v4.1-flash-expires-on-0910(max) | 40.46 | 2.09-4.18元 | 无 | 240k | 99.7%(24.017m) | 官方api | 无 |
| glm5.3(max) | 40.43 | 26.18元 | 2.09元 | 407k | 97.4%(10.063m) | 官方api | zcode预设 |
| kimi-k3(max) | 38.74 | 23.08元 | 2.07 | 264k | 97%(4.21m) | kimi订阅 | kimicode预设 |
| kimi-k3(high) | 36.36 | 13.05元 | 1.04 | 168k | 95%(1.953m) | kimi订阅 | kimicode预设 |
| deepseek-v4-pro0813(max) | 30.87 | 4.54-9.08元 | 无 | 261k | 99.3%(11.981m) | 官方api | dsh-minimal预设 |
| deepseek-v4-flash0902(max) | 30.87 | 2.41-4.82元 | 无 | 337k | 99.5%(23.753m) | 官方api | 无 |
| deepseek-v4-flash-vision-exp(max) | 29.63 | 1.76-3.52元 | 无 | 290k | 99.2%(16.964m) | 官方api | 无 |
| glm-5.3-flash(max) | 28.46 | 1.99元 | 0.517元 | 557k | 98%(12.657m) | 官方api | 无 |
| deepseek-v4-flash0731(max) | 未测试 | ?元 | 无 | ? | ?% | 官方api | 无 |


---

## 分析

1. K3的high思考强度偏向于节省token精简架构，无论是c项目还是前端项目，都比其他的更简洁，c因为有编译器兜底，所以bug更少，web需要人工review，模型为了省token，导致部分bug没找出来
2. 单纯从颜值上来讲，我更喜欢k3的风格，美观程度为主观评判，未参与积分
3.  实际体验来讲，glm5.3好于v4-pro0813，v4稳定性难评
4. v4.1f-0910稳定性不如glm5.3好于v4p，但速度极快
5. ...

---

## 声明

0. full_v2项目主要反映模型从0到1的理解用户需求，规划和开发能力
1. 本bench由 github 用户 [snnh](https://github.com/snnh) 版权所有。
2. 接受模型送测(只是为了多体验更多模型)
3. 欢迎赞助token

---

## 致谢

1. 感谢shyliuli和Karpy II提供的glm5.3评测环境
