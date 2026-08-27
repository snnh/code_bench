# code_bench v1.3

## 题目结构

| 题目              | 满分      | 内容                                             |
| --------------- | ------- | ---------------------------------------------- |
| 基础题 · core      | 30      | 复刻 C11 执行器 `owc-exec`（stdio JSON-RPC 2.0）      |
| 基础题 · server    | 30      | 复刻 Node 20+ 服务层（HTTP/WS API + agent 循环）        |
| 基础题 · web       | 30      | 复刻 React 19 + Vite 前端                          |
| 基础题 · 拼接(题目编写中) | 10      | 三个子项拼成端到端系统，**不限制拼接方法**（A/B/C 档系数 1.0/0.8/0.5） |
| **基础题总分**       | **100** | 3×30 + 10 − 中断扣分                               |
| 高阶题 · full      | 50      | 三层完整复刻（独立一张卷）                                  |
| 高阶题 · rust v2   | 50      | 一个网络服务开发，包含规则引擎 + 报文编解码 + 稀疏配置 + CLI四部分        |
| **高阶题总分**       | **100** | 归一化后等权重相加                                      |

---

## 环境

debian13 x86-64 上使用 [openwebcode](https://github.com/snnh/openwebcode)

* 注：*部分模型会开启环境模拟扩展以发挥最高水平*

---

## 排行

| 模型                              |
| --------------------------------- |
| kimi-k3(high)                     |
| glm5.3(max)                       |
| qwen3.8-flash(max)                |
| glm-5.3-flash(max)                |
| deepseek-v4-pro0813(max)          |
| deepseek-v4-flash-vision-exp(max) |
| glm-ox-alpha(max)                 |
| deepseek-v4-flash0731(max)        |
| gemini-3.7-flash(high)            |
| ...                               |

### 基础题

**基础题总分**

| 模型 | 积分 | 成本(折算API价格) | 订阅折算 | token(不算缓存) | 接入渠道 | 备注 |
|---|---|---|---|---|---|---|
| kimi-k3(high) | 81.2  | 77.66元        | 约6元         | 628k        | 官方 | 采用kimicode预设 |
| glm5.3(max) | 79    | 约150元         | 约12元        | 约1200-1300k | 官方 | 采用zcode预设    |
| deepseek-v4-pro0813(max) | 78/79   | 18.13-36.26元  | 无           | 738k        | 官方api | 采用dsh极简模式预设  |
| deepseek-v4-flash0731(max) | 74.1  | 28.08-56.16元  | 无           | 13981k      | 官方api | 无 |
| deepseek-v4-flash-vision-exp(max) | 52.4 | 15.95-31.9+元 | 无 | 6692+k | 官方api | 无 |
| glm-ox-alpha(max) | 51.4+  | 0元            | 无           | 1013k | openrouter | 无 |
| gemini-3.7-flash(high) | 47.6+ | 18.3+元        | 9.15元(限时半价) | 1630+k | openrouter | 无 |
| … | 未测试   | 元             | 元           | k           | 官方         | 无            |

* token消耗未统计缓存，缓存消耗具体看细则缓存部分
* kimi订阅倍率约0.07-0.08(199档实测)
* glm5.3订阅倍率约0.08(官方api文档说明)
* glm5.3flash订阅倍率约0.26(官方api文档说明)
* qwen订阅倍率约0.3(官方api文档说明)

**core**

| 模型 | 积分 | 成本(折算API价格) | token(不算缓存) | 缓存 |
|---|---|---|---|---|
| kimi-k3(high)              | 26.2 | 54.89元 | 394k        | 98.7%(16.485m) |
| deepseek-v4-pro0813(max)   | 26   | 9.33-18.66元 | 315k        | 99.8%(37.834m) |
| glm5.3(max)                | 25.6 | 82.19元      | 455k        | 99.3%(37.21m)  |
| deepseek-v4-flash-vision-exp(max) | 25.2 | 3.53-7.06元 | 352k | 99.7%(46.685m) |
| deepseek-v4-flash0731(max) | 24.6 | 5.05-10.1元  | 782k        | 99.2%(57.256m) |
| glm-ox-alpha(max) | 24.2 | 0元 | 628k | 99.2%(55.048m) |
| gemini-3.7-flash(high)     | 23.7 | ~12.15元     | 1069k       | 91%(9.57m)     |

**server**

| 模型 | 积分 | 成本(折算API价格) | token(不算缓存) | 缓存 |
|---|---|---|---|---|
| kimi-k3(high)              | 27.2      | 14.63元      | 138k        | 97.8%(4.085m)  |
| glm5.3(max)                | 25.1      | 约30-40元     | ?k          | ?%(?m)         |
| deepseek-v4-pro0813(max)   | 25.8      | 4.75-9.5元   | 221k        | 99.5%(17.062m) |
| deepseek-v4-flash0731(max) | 22.7/24.7 | 20.9-41.8元  | 12563k      | 72%(30.052m)   |
| gemini-3.7-flash(high)     | 测试中      | 元           | k           | %(m)           |
| … | 未测试 | 元 | k | %(m) |

**web**

| 模型 | 积分 | 成本(折算API价格) | token(不算缓存) | 缓存 |
|---|---|---|---|---|
| glm5.3(max) | 28.3 | 33.26元       | 400k        | 98.1%(13.577m) |
| kimi-k3(high) | 27.8 | 8.14元        | 96k         | 96.4%(1.46m)   |
| glm-ox-alpha(max) | 27.2 | 0元           | 385k        | 96.7%(9.209m)  |
| deepseek-v4-pro0813(max) | 27.2 | 4.05-8.1元    | 202k        | 99.5%(12.519m) |
| deepseek-v4-flash-vision-exp(max) | 27.2 | 12.42-24.84元 | 6340k       | 88%(43.989m)   |
| deepseek-v4-flash0731(max) | 26.8 | 2.13-4.26元   | 636k        | 97%(16.102m)   |
| gemini-3.7-flash(high) | 23.9 | ~6.15元       | 561k        | 90.7%(5.155m)  |
| … | 未测试 | 元 | k | %(m) |


### 高阶题

**高阶题总分**

| 模型 | 积分 | 成本(折算API价格) | token(不算缓存) | 缓存 | 接入方式 | 备注 |
|---|---|---|---|---|---|---|
| deepseek-v4-flash-vision-exp(max) | 30.03 | 1.76-3.52元 | 290k | 99.2%(16.964m) | 官方api | 无 |
| kimi-k3(high) | 未测试 | ?元 | ? | ?% | kimi订阅 | kimicode预设 |
| deepseek-v4-flash0731(max) | 未测试 | ?元 | ? | ?% | 官方api | 无 |
| deepseek-v4-pro0813(max) | 未测试 | ?元 | ? | ?% | 官方api | dsh-minimal预设 |

**full**

| 模型 | 积分 | 成本(折算API价格) | token(不算缓存) | 缓存 | 接入方式 | 备注 |
|---|---|---|---|---|---|---|
| kimi-k3(high) | 未测试 | ?元 | ? | ?% | kimi订阅 | kimicode预设 |
| deepseek-v4-flash0731(max) | 未测试 | ?元 | ? | ?% | 官方api | 无 |
| deepseek-v4-pro0813(max) | 未测试 | ?元 | ? | ?% | 官方api | dsh-minimal预设 |

**rust v2**

| 模型 | 积分 | 成本(折算API价格) | 订阅折算 | token(不算缓存) | 缓存 | 接入方式 | 备注 |
|---|---|---|---|---|---|---|---|
| qwen3.8-flash(max) | 42.34 | 1.21元 | 0.363元 | 321k | 97%(6.324m) | 官方api | 无 |
| deepseek-v4-pro0813(max) | 31.27 | 4.54-9.08元 | 无 | 261k | 99.3%(11.981m) | 官方api | dsh-minimal预设 |
| deepseek-v4-flash-vision-exp(max) | 30.03 | 1.76-3.52元 | 无 | 290k | 99.2%(16.964m) | 官方api | 无 |
| glm-5.3-flash(max) | 28.66 | 1.99元 | 0.517元 | 557k | 98%(12.657m) | 官方api | 无 |
| kimi-k3(high) | 未测试 | ?元 | 0.08x | ? | ?% | kimi订阅 | kimicode预设 |
| deepseek-v4-flash0731(max) | 未测试 | ?元 | 无 | ? | ?% | 官方api | 无 |


---

## 分析

1. K3的high思考强度偏向于节省token精简架构，无论是c项目还是前端项目，都比其他的更简洁，c因为有编译器兜底，所以bug更少，web需要人工review，模型为了省token，导致部分bug没找出来
2. 单纯从颜值上来讲，我更喜欢k3的风格，美观程度为主观评判，未参与积分
3.  实际体验来讲，glm5.3好于v4-pro0813，v4稳定性难评
4. gemini-3.7-flash(high)web错误：f2-stop-visible / f3-tool-block / f3-tool-done「找不到 composer」实为找不到 send + f3-reload-auto/persist
5. ...

---

## 声明

1. 本bench由 github 用户 [snnh](https://github.com/snnh) 版权所有。
2. bench内容将在彻底完善之后开源
3. 1.2版本优化了rust项目的题目和评分标准
4. 1.3版本进一步优化rust项目评分标准，同时修复v4p得分异常问题

---

## 致谢

1. 感谢shyliuli提供的glm5.3 server项目评测环境
