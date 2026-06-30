# LLM + 时序预测 + 金融 —— 核心推荐阅读列表

> 基于研究方向：推荐系统子模块（Transformer / GNN / 对比学习 / 损失函数）迁移到金融时序预测，LLM/Agent 增强
>
> 整理时间：2026-06-24

---

## 📖 三篇期刊论文

### 1. Relational Stock Selection via Probabilistic State Space Learning

- **期刊**: IEEE TKDE, Vol. 37, Issue 2, pp. 865–880, February 2025 | CCF-A
- **DOI**: [10.1109/TKDE.2024.3509267](https://doi.org/10.1109/TKDE.2024.3509267)
- **作者**: Qiang Gao, Zhengxiang Liu, Li Huang, Kunpeng Zhang, Jun Wang, Guisong Liu
- **机构**: 西南财经大学、马里兰大学

**为什么读**：TKDE 上最接近「推荐系统视角做选股」的论文。本质是 pairwise ranking——建模股票对的相对期望收益来做排序推荐。GNN + 成对排序 + 概率状态空间建模。

**与你的研究方向的关系**：你实验室的 BPR loss 和自适应负采样策略可以直接替换文中的排序损失函数——文中用的是 pairwise margin loss，BPR 的贝叶斯框架理论上更优。这是最直接的迁移点。

---

### 2. An Evidence-Based Paradigm for Financial GNNs: The Case for Principled Simplicity in Volatility Spillover Modeling

- **期刊**: IEEE TKDE, Vol. 38, Issue 2, pp. 783–793, February 2026 | CCF-A
- **DOI**: [10.1109/TKDE.2025.3638410](https://doi.org/10.1109/TKDE.2025.3638410) 附近
- **作者**: Shengting Shen, Jason Gemsun Young, Jyh-Shing Roger Jang
- **机构**: 台湾大学、工业技术研究院（台湾）

**为什么读**：通过严格消融实验（DOW30 & SPY TOP40，2019–2025 30分钟数据）直接证明三件事：

| 发现 | 数据 | 含义 |
|------|------|------|
| 稀疏图优于稠密图 | K-NN 400 边 > 全连接 1560 边，QLIKE 提升 5.1%，计算节省 74% | 图结构比图复杂度重要 |
| GNN 大幅优于非图基线 | GNN vs LSTM/HAR：准确率提升 52–55% | 图建模是必要组件 |
| 简单架构就够了 | 12ms 推理，13MB 内存 | 不需要复杂设计 |

**与你的研究方向的关系**：这三个结论恰好支持把 LightGCN 的简化传播层搬到金融场景——去掉特征变换和非线性激活，只保留邻居聚合。作者证明了「少即是多」在金融 GNN 中也成立，但没有引用 LightGCN——你的机会就是明确建立这个连接，并给出 LightGCN 在金融图上的系统 benchmark。

---

### 3. Financial News Sentiment Meets Market Data: A Large Language Model-Based Approach to Stock Price Prediction

- **期刊**: Information Sciences, Vol. 754, 2026 | CCF-B，中科院一区
- **DOI**: [10.1016/j.ins.2026.123711](https://doi.org/10.1016/j.ins.2026.123711)
- **核心内容**: 零样本 LLM（Llama、Vicuna、Mistral）提取情感 → LSTM/GAN/Transformer 预测；8652 条新闻 × 47 只股票

**为什么读**：代表了当前期刊上「LLM + 金融」的**标准模板**：

```
新闻文本 → LLM 情感提取（零样本）→ 情感分数 → 独立时序模型（LSTM/Transformer）→ 预测
```

LLM 在整个流水线里只是一个 fancy 的特征提取器，和时序模型是松耦合的——LLM 不知道时序模型的预测目标是什么，时序模型也不知道 LLM 提取的信息是否和自己的预测方向一致。

**与你的研究方向的关系**：你的 SASRec + LLM 融合方案可以做**紧耦合**——让 LLM 生成的语义表示直接参与自注意力计算，而不是作为独立特征输入。你的 story：为什么在期刊标准模板之上，紧耦合能带来额外收益（信息流动更充分、端到端优化）。

---

## 🎯 四篇会议论文

### 4. TS-Agent: Structured Agentic Workflows for Financial Time-Series Modeling with LLMs and Reflective Feedback

- **会议**: NeurIPS 2025 | CCF-A
- **作者**: Ang, Bao, Jiang, Tao, Tung, Szpruch, Ni
- **机构**: NUS、UCL、University of Edinburgh

**核心内容**：Planner Agent + 知识库（案例库 / 金融 TS 代码库 / 精炼知识库）→ 三阶段迭代：模型选择 → 代码精炼 → 微调。超越 AutoGluon、H2O 等 AutoML 基线。

**与你的研究方向的关系**：TS-Agent 的 Planner 是在**已有的**模型库里选模型。你可以扩展为：Planner 不止选模型，还能**动态选择推荐系统中的子模块**——哪种 self-attention（SASRec 因果 vs BERT4Rec 双向）、哪种 GNN 聚合（LightGCN vs GAT）、哪种损失函数（BPR vs CE）——来组装金融时序模型。推荐系统的技术资产变成 Agent 的「工具箱」。

---

### 5. TimeRAG: Retrieval-Augmented Generation for Continuous Time Series Forecasting

- **会议**: ICLR 2025 | CCF-A
- **链接**: OpenReview

**核心内容**：首个把 RAG 引入连续时序预测的工作。LLM 反馈作为训练信号 → 训练检索器 → 检索相似历史时序片段 → 增强预测。在 ACL18、BIGDATA22、CIKM18、Stock23 四个金融数据集上验证。

**与你的研究方向的关系**：TimeRAG 的检索器是通用设计。你可以把检索改为**用推荐模型的序列表示来做相似性检索**——用 SASRec/BERT4Rec 的序列 encoder 输出做 query，从历史 market regime 库中检索相似的 regime 片段。推荐社区在序列相似性学习上有大量积累，可以直接注入。

---

### 6. FactorGCL: A Hypergraph-Based Factor Model with Temporal Residual Contrastive Learning for Stock Returns Prediction

- **会议**: AAAI 2025 | CCF-A
- **DOI**: [10.1609/aaai.v39i1.31993](https://doi.org/10.1609/aaai.v39i1.31993)
- **作者**: Yitong Duan, Weiran Wang, Jian Li
- **机构**: 清华大学

**核心内容**：超图结构捕获股票-因子的高阶关系 → 级联残差超图架构分解收益（先验 beta → 隐藏 beta → 个股 alpha）→ **时序残差对比学习（TRCL）**：同一股票不同时间段的 alpha 残差做正样本对，InfoNCE 损失。中国 A 股 5028 只股票 2014–2023，多周期 IC/ICIR 超越 SOTA。

**与你的研究方向的关系**：推荐系统里的 SimGCL / SGL / CL4SRec 等一系列图/序列对比增强方法可以直接扩展 FactorGCL。FactorGCL 只用了一种对比学习（时序残差），你可以引入多视角图增强（边扰动 + 节点 dropout + 子图采样），让模型在多种扰动视角下学到更鲁棒的股票表示。这篇论文证明了**金融社区接受对比学习思路**，但还没用到推荐社区最新的图增强技巧。

---

### 7. Kronos: A Foundation Model for the Language of Financial Markets

- **会议**: AAAI 2026 | CCF-A
- **arXiv**: [2508.02739](https://arxiv.org/abs/2508.02739)
- **代码**: [github.com/shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos)
- **模型**: HuggingFace — Kronos-mini (4.1M) / small (24.7M) / base (102.3M) / large (499.2M)
- **作者**: Yu Shi, Zongliang Fu, Shuo Chen, Bohan Zhao, Wei Xu, Changshui Zhang, Jian Li
- **机构**: 清华大学 IIIS、自动化系

**核心内容**：第一个开源金融 K 线基础模型：

```
OHLCV 数据 → BSQ Tokenizer（二元球面量化，离散化为层级 token）
           → 自回归 Decoder-only Transformer 预训练
           → 45 个交易所、120 亿条 K 线、7 种时间粒度
```

零样本 RankIC 提升 93%，波动率 MAE 降低 9%，生成保真度提升 22%。

**与你的研究方向的关系**：Kronos 证明了「把金融数据当语言处理」这条路是通的。**SASRec 天然就是做这件事的架构**——item token → causal self-attention → next token prediction。Kronos 用的是通用 Decoder-only Transformer，你可以论证 SASRec 的因果自注意力 + item embedding 模式比通用的 next-token prediction 更适合金融数据——因为 SASRec 专门为行为序列的噪声性和稀疏性优化过，金融数据恰好也是高噪声、低信噪比的。

**这是三个社区交叉的制高点**：推荐社区提供序列建模架构（SASRec/BERT4Rec）→ LLM 社区提供知识注入和预训练范式（tokenization + decoder-only）→ 金融社区提供场景和数据（K 线 + 基本面）。

---

## 📊 阅读路线

```
Week 1 — 理解期刊标准
  ├─ 论文 1：Relational Stock Selection（排序 > 回归，GNN + pairwise ranking）
  └─ 论文 2：Principled Simplicity in Financial GNNs（稀疏 > 稠密，简单 > 复杂）

Week 2 — 理解 LLM+金融 的 gap
  ├─ 论文 3：LLM Sentiment + TS Model（期刊当前模板：松耦合）
  └─ 论文 5：TimeRAG（会议前沿：LLM 紧耦合时序）

Week 3 — 理解 Agent 和对比学习
  ├─ 论文 4：TS-Agent（Agent 范式做时序建模）
  └─ 论文 6：FactorGCL（对比学习在金融中的应用）

Week 4 — 理解金融基础模型 frontier
  └─ 论文 7：Kronos（金融基础模型，SASRec 迁移的 target）
```

### 读完后的产出

一篇课题方案：「把 SASRec 因果自注意力架构迁移为轻量金融时序基础模型，用 LLM Agent 注入金融文本知识增强」的技术路线图——包含：
- 为什么 SASRec 而非通用 Transformer（行为序列建模的天然优势）
- 为什么因果 mask 而非双向注意力（金融时序的因果约束）
- 为什么 LightGCN 简化传播而非深层 GAT（金融 GNN 的「少即是多」原则）
- 为什么 BPR loss 而非 MSE（金融的本质是排序）
- LLM Agent 在哪个环节注入（特征增强 / 图结构构建 / 样本生成）

---

---

## 🤖 Agent 专项推荐

> Agent 是 LLM + 金融方向的另一个核心阵地。以下论文覆盖 Agent 交易框架、多Agent协作、Agent评估基准、市场模拟、以及关键警示。

---

### 一、核心 Agent 交易框架

#### 8. TradingAgents: Multi-Agents LLM Financial Trading Framework

- **会议**: ICML 2025 | CCF-A
- **arXiv**: [2412.20138](https://arxiv.org/abs/2412.20138)
- **项目页**: [tradingagents-ai.github.io](https://tradingagents-ai.github.io/)
- **代码**: `github.com/TauricResearch/TradingAgents`
- **作者**: Yijia Xiao, Edward Sun, Di Luo, Wei Wang（UCLA / MIT / Tauric Research）

**核心内容**：模拟真实交易公司的 7 个 LLM Agent，分四个团队：

| 团队 | Agent | 职责 |
|------|-------|------|
| **分析师团队** | 基本面 / 情感 / 新闻 / 技术分析师 | 并行收集多维度市场信息 |
| **研究员团队** | 牛方 / 熊方研究员 | 多轮结构化辩论，产出平衡评估 |
| **交易员** | 交易决策 Agent | 综合报告+辩论→交易时机/方向/仓位 |
| **风控团队** | 激进/中性/保守风控 + 基金经理 | 风险审查→最终批准 |

**架构亮点**：混合通信协议——结构化报告保数据完整性，自然语言辩论保推理深度。

**实验结果**（AAPL/GOOGL/AMZN，2024）：累计收益 23–27%，夏普比率 5.6–8.2，最大回撤仅 0.91–2.11%。

**与你的研究方向的关系**：TradingAgents 的 Agent 都在处理**非结构化信息**（新闻、社交媒体）。你可以在分析师团队中加入一个「序列建模分析师」——用 SASRec/BERT4Rec 分析股票历史序列模式，输出结构化的技术研判报告。这填补了当前 Agent 框架中**缺少专用时序建模 Agent**的空白。

---

#### 9. FinMem: A Performance-Enhanced LLM Trading Agent With Layered Memory and Character Design

- **期刊**: IEEE Transactions on Big Data, Vol. 11, Issue 6, pp. 3443–3459, 2025
- **DOI**: `10.1109/tbdata.2025.3593370`
- **作者**: Yangyang Yu, Haohang Li, Zhi Chen et al.（Stevens Institute of Technology）
- **荣誉**: IJCAI 2024 FinLLM Challenge 股票交易赛道冠军

**核心内容**：三层架构——**Profile**（角色：风险偏好自适应切换）+ **Memory**（工作记忆 + 三层长期记忆：浅层/中层/深层，不同衰减率和重要性权重）+ **Decision-making**（Buy/Sell/Hold + 完整推理日志）。

**记忆机制的精妙之处**：

| 记忆层 | 衰减率 | 存储内容 | 检索权重 |
|--------|--------|---------|---------|
| 浅层 | 高（快速遗忘） | 每日新闻、日内波动 | 0.8 新颖性权重 |
| 中层 | 中 | 中期事件、行业动态 | 平衡 recency + relevance |
| 深层 | 低（长期保留） | 年报、重大政策变化 | 0.8 重要性权重 |

记忆事件可以通过重要性评分从浅层**迁移到深层**。检索时综合新颖性、相关性和重要性三个维度打分。

**与你的研究方向的关系**：FinMem 的记忆机制是处理**金融时序非平稳性**的优雅方案——不同时间尺度的信息自然分层。你可以把这个分层记忆思路搬到 SASRec 的序列建模中：用浅层记忆处理短期市场噪声，用深层记忆保留长期的 regime 知识。这是推荐系统中 memory-augmented 序列模型（如 SR-GNN、SASRec with memory）在金融中的直接映射。

---

#### 10. FinRL-DeepSeek: LLM-Infused Risk-Sensitive Reinforcement Learning for Trading Agents

- **会议**: ICML 2025（相关工作）| CCF-A
- **链接**: [HAL](https://hal.science/hal-04934770v1)
- **作者**: Mostapha Benhenda

**核心内容**：CVaR-PPO（条件风险价值约束的 PPO）+ DeepSeek V3 / Qwen 2.5 / Llama 3.3 多模型金融新闻推理。LLM 提取的风险信号直接注入 RL 策略网络。

**与你的研究方向的关系**：展示了 LLM + RL 在交易中的深度融合范式。你的 SASRec 模型可以作为 RL 策略网络的一部分——SASRec 编码历史序列状态，LLM 注入外部知识，RL 优化交易动作。

---

### 二、Agent 评估基准与市场模拟

#### 11. Can Large Language Models Trade? Testing Financial Theories with LLM Agents in Market Simulations

- **arXiv**: [2504.10789](https://arxiv.org/abs/2504.10789)
- **代码**: [github.com/alejandroll10/llm_trading_sim](https://github.com/alejandroll10/llm_trading_sim)
- **作者**: Alejandro Lopez-Lira（University of Florida）

**核心内容**：构建合成股票市场，让不同策略的 LLM Agent（价值/动量/做市/逆向/投机/杠杆）竞价交易。三项核心发现：

> 1. **LLM 能持续执行交易策略**——它们会按指令挂单，即使亏钱也不会"止损逃跑"
> 2. **模拟市场展现真实市场动态**——价格发现、泡沫、反应不足从 Agent 互动中自然涌现
> 3. **Prompt 工程可以制造系统性风险**——标准化的 prompt 导致 Agent 行为高度相关

**最震感的结论**：**LLM "不在乎钱"，除非你明确让它在乎。** 它会忠实地执行一个有缺陷的策略直到亏光。

**与你的研究方向的关系**：这篇论文为 Agent 交易研究提供了方法论框架——合成市场 + 多Agent竞争 + 行为分析。你可以在 Lopez-Lira 的框架中插入一个「SASRec 驱动的技术分析师 Agent」，观察基于序列推荐的 Agent 在市场中的行为特征。

---

#### 12. Agent Market Arena (AMA): When Agents Trade — Live Multi-Market Trading Benchmark for LLM Agents

- **arXiv**: 2025 年 10 月
- **作者**: Lingfei Qian, Xueqing Peng et al.（Columbia / Harvard / Georgia Tech 等多机构）
- **核心发现**: **Agent 架构驱动性能差异 > 模型选择**——即怎么设计 Agent 比用什么 LLM 更重要

**与你的研究方向的关系**：这直接支持你的研究方向——**推荐系统的架构设计经验（怎么搭模型、怎么设计损失函数、怎么做特征交互）比单纯升级 LLM 更重要。** 你应该花精力在架构设计上，而不是追最新的 LLM。

---

#### 13. Agent Trading Arena: A Study on Numerical Understanding in LLM-Based Agents

- **会议**: EMNLP 2025 Findings | CCF-B
- **作者**: Tianmi Ma, Jiawei Du, Wenxin Huang, Wenjie Wang et al.

**核心发现**：
- LLM **文本数值推理很弱**（过度拟合最近值，忽略百分比变化）
- **图表视觉输入显著改善**性能
- **反思模块（Reflection）** 在波动市中增益最大

**与你的研究方向的关系**：验证了两个关键设计选择——（1）数值推理不可靠→应该依赖结构化的序列模型（SASRec）而非 LLM 直接读数字；（2）反思模块有效→你的 Agent 应该有一个回顾历史预测准确率的反思环节。

---

### 三、多Agent协作与人类交互

#### 14. MENTOR: A Multi-Agent Framework for Event and Narrative Trend Prediction with Optimized Reasoning

- **期刊**: FITEE, Vol. 26, Issue 10, pp. 1847–1861, 2025 | CCF-B，中科院一区
- **DOI**: [10.1631/FITEE.2500608](https://doi.org/10.1631/FITEE.2500608)
- **作者**: Liyuan Chen, Xiu Li et al.（清华大学深圳国际研究生院 + 易方达基金 + 曼彻斯特大学）

**核心内容**：基于 Shiller 叙事经济学，三阶段教师-学生迭代推理：

```
热点事件检测 → 未来事件预测 → 行业指数排名
（聚类+排序）  （叙事轨迹外推）（S&P 11 行业 / A 股 9 行业）
```

**关键创新**：TextGrad——用文本反馈做梯度式优化，不需要直接访问模型参数。~50% 准确率预测未来热点事件，超越 StkFEP 和 SEP 基线。

**与你的研究方向的关系**：Teacher-Student 迭代推理是你的 SASRec 模型的自然增强——Student Agent 用 SASRec 做序列预测，Teacher Agent（LLM）检查预测逻辑是否自洽，给出文本反馈，Student 据此调整下一轮预测。

---

#### 15. FinArena: A Human-Agent Collaboration Framework for Financial Market Analysis and Forecasting

- **arXiv**: [2503.02692](https://arxiv.org/abs/2503.02692)
- **作者**: Congluo Xu, Zhaobin Liu, Ziyang Li

**核心内容**：MoE 风格的人机协作框架——三个专业 Agent（时序/新闻/财报）→ 通用专家 Agent → 融入用户风险偏好 → 最终决策。自适应 RAG 减少幻觉。

**与你的研究方向的关系**：展示了 Agent 框架中「模块化」的威力——每个 Agent 专注一个数据模态。你可以把时序 Agent 升级为 SASRec 驱动的版本。

---

### 四、Agent 综述与关键警示

#### 16. LLM Agents in Finance: A Survey Bridging Research, Practice, and Real-World Deployment

- **会议**: EMNLP 2025 Findings | CCF-B
- **作者**: Yifei Dong, Fengyi Wu et al.（University of Washington）

**核心内容**：30+ 基准、20+ 模型的全面综述，5 大 Agent 领域分类：

| 领域 | 核心任务 | 代表工作 |
|------|---------|---------|
| 数据分析 Agent | 文本摘要、NER、关系抽取 | FinBERT, FinGPT |
| 投资研究 Agent | 事件分类、情感分析、时序预测 | FinMem, MENTOR |
| 交易 Agent | 策略执行、决策支持 | TradingAgents, FinRL |
| 投资管理 Agent | 组合优化、QA | MarketSenseAI |
| 风控 Agent | 欺诈检测、违约预测 | — |

开放挑战：数值推理不足、Prompt 敏感、缺乏实时适应性、隐私合规部署、多Agent协作在压力下的脆弱性。

**与你的研究方向的关系**：这篇综述明确指出「投资研究 Agent 中的时序预测」是五个核心领域之一，而当前的 Agent 框架**缺少专用的时序建模模块**。你的工作正好填补这个空白。

---

#### 17. The Losing Winner: An LLM Agent That Predicts the Market but Loses Money

- **会议**: NeurIPS 2025 | CCF-A

**核心内容**：微调 Qwen2.5-3B 获得更高分类准确率 → **但累计收益低于零样本基线**。揭示了 LLM 交易 Agent 中最致命的问题——**目标不匹配（Objective Mismatch）**：优化分类准确率 ≠ 优化投资收益。

**与你的研究方向的关系**：这篇论文是你在设计损失函数时最重要的警示。BPR loss 之所以优于 MSE/CE，正在于它直接优化排序质量而非逐点精度——排序质量才对应投资收益。这个洞见是你课题的**核心 motivation**。

---

## 📊 Agent 论文分类总览

| 类别 | 论文 | 对你的核心价值 |
|------|------|-------------|
| **交易框架** | TradingAgents, FinMem, FinRL-DeepSeek | 你的 SASRec 可以作为 Agent 的时序分析模块嵌入 |
| **评估基准** | Can LLMs Trade?, AMA, Agent Trading Arena | 评测方法论 + 架构>模型的核心论证 |
| **多Agent协作** | MENTOR, FinArena | Teacher-Student 迭代、人机协作模式 |
| **综述** | LLM Agents in Finance Survey | 确认「时序建模模块缺失」是公认 gap |
| **警示** | The Losing Winner | BPR loss 比 CE/MSE 更适合金融的底层原因 |

---

## 📊 更新后的整体阅读路线

```
Week 1 — 期刊标准 + Agent 全貌
  ├─ 论文 1：Relational Stock Selection（排序 > 回归）
  ├─ 论文 2：Principled Simplicity（稀疏 > 稠密）
  └─ 论文 16：LLM Agents in Finance Survey（Agent 全景图）

Week 2 — LLM+金融 的 gap + Agent 交易核心
  ├─ 论文 3：LLM Sentiment + Market Data（期刊松耦合模板）
  ├─ 论文 8：TradingAgents（Agent 交易标准范式）
  └─ 论文 9：FinMem（分层记忆——你最该迁移的机制）

Week 3 — Agent 评估 + 时序技术前沿
  ├─ 论文 11：Can LLMs Trade?（Agent 市场模拟方法论）
  ├─ 论文 12：Agent Market Arena（架构 > 模型的论证）
  └─ 论文 6：FactorGCL（对比学习在金融中的应用）

Week 4 — 时序 Agent + 基础模型 + 警示
  ├─ 论文 4：TS-Agent（Agent 直接做时序建模）
  ├─ 论文 7：Kronos（金融基础模型 = SASRec 的 target）
  └─ 论文 17：The Losing Winner（为什么 BPR > MSE）

Week 5 — 形成课题方案
  └─ 综合所有论文的洞见 → 完整技术路线图
```
