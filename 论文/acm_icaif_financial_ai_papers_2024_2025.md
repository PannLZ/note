# ACM ICAIF 金融 AI 论文统计（2024-2025）

范围：统计 DBLP 已收录的 ACM International Conference on AI in Finance（ICAIF）2024 与 2025 主会议 proceedings 论文。当前日期为 2026-06-10；2026 届 proceedings 尚未形成可核验的 DBLP/ACM 目录，因此未纳入。

来源：
- DBLP ICAIF 2024 目录：https://dblp.org/db/conf/icaif/icaif2024.html
- DBLP ICAIF 2025 目录：https://dblp.org/db/conf/icaif/icaif2025.html
- ACM 2024 proceedings DOI：https://doi.org/10.1145/3677052
- ACM 2025 proceedings DOI：https://doi.org/10.1145/3768292

说明：论文题名、年份、DOI 链接、会议分组来自 DBLP；“技术主类”和“创新点总结”为基于论文题名、DBLP 分组及公开元数据的保守归纳，采用互斥主类，便于计数。

## 总览

- 2024 年：99 篇
- 2025 年：111 篇
- 合计：210 篇

## 技术主类定义

| 技术主类 | 归类口径 |
|---|---|
| 大语言模型/NLP/RAG | LLM、金融文本理解、RAG/检索、问答、情感、报告/披露解析等。 |
| 智能体/多智能体/市场仿真 | Agentic workflow、多智能体协作、市场仿真、数字孪生、自动交易参与者等。 |
| 生成式模型/数据合成 | Diffusion/GAN/VAE/flow matching/Schrodinger bridge 等生成、去噪与合成数据方法。 |
| 图学习/知识图谱/网络分析 | GNN、图 Transformer、知识图谱、超图、金融网络/关系建模。 |
| 强化学习/在线决策 | RL/DRL/MARL、bandit、执行交易、做市、资产负债管理等序贯决策。 |
| 时间序列/预测/表征学习 | 金融时间序列、价格/收益/波动率预测、lead-lag、表示学习、Hawkes/状态空间等。 |
| 优化/投资组合/定价/风险 | 组合优化、资产配置、衍生品定价/对冲、风险管理、稳健优化、保险定价。 |
| 异常检测/欺诈/金融犯罪 | 欺诈、反洗钱、异常/错报/操纵检测、金融犯罪攻防。 |
| 可解释/公平/可信评测 | XAI、公平性、偏见、形式化验证、幻觉/鲁棒性评测、基准与不确定性。 |
| 其他机器学习/数据工程 | 聚类、表格数据、数据增强/蒸馏、联邦学习、通用 ML 工具等难以归入上述主类的工作。 |

## 技术主类数量统计

| 技术主类 | 2024 | 2025 | 合计 | 变化 |
|---|---:|---:|---:|---:|
| 大语言模型/NLP/RAG | 14 | 21 | 35 | +7 |
| 智能体/多智能体/市场仿真 | 5 | 10 | 15 | +5 |
| 生成式模型/数据合成 | 11 | 9 | 20 | -2 |
| 图学习/知识图谱/网络分析 | 6 | 8 | 14 | +2 |
| 强化学习/在线决策 | 12 | 11 | 23 | -1 |
| 时间序列/预测/表征学习 | 7 | 12 | 19 | +5 |
| 优化/投资组合/定价/风险 | 12 | 10 | 22 | -2 |
| 异常检测/欺诈/金融犯罪 | 8 | 7 | 15 | -1 |
| 可解释/公平/可信评测 | 6 | 13 | 19 | +7 |
| 其他机器学习/数据工程 | 18 | 10 | 28 | -8 |

## 发展趋势

- 大语言模型/NLP/RAG：从 14 篇增至 21 篇，是增长最明显的方向之一。
- 智能体/多智能体/市场仿真：从 5 篇增至 10 篇，是增长最明显的方向之一。
- 时间序列/预测/表征学习：从 7 篇增至 12 篇，是增长最明显的方向之一。
- 可解释/公平/可信评测：从 6 篇增至 13 篇，是增长最明显的方向之一。
- 其他机器学习/数据工程：从 18 篇降至 10 篇，说明相关主题在 2025 年更多被其他主类吸收或热度回落。
- 2025 年明显强化了 agentic finance：主会分组直接出现 Agent-Based Financial Systems、Agent-Based Simulation、Autonomous Agents 等主题，LLM 也从文本理解扩展到检索、研究助理、投资管理和 Agent-as-a-Judge。
- 可信 AI 从单点 explainability/fairness 扩展到 hallucination、bias、benchmark、ethical judgment 和 uncertainty quantification，反映金融场景对可控性、审计性和监管适配的要求上升。
- 生成式模型仍活跃，但用途从 2024 年的相关矩阵、欺诈样本、市场/价格序列合成，扩展到 2025 年的 diffusion/flow matching/VAE/GAN/Schrodinger bridge 等多路线，用于 LOB volume、波动率曲面、宏观情景和加密市场仿真。
- 强化学习继续集中在做市、执行、资产负债管理、再保险定价和交易策略；2025 年更强调 MARL、行为偏差、CVaR 约束和市场仿真结合。
- 图学习与知识图谱保持稳定存在，应用从反洗钱、债券推荐、图特征预处理，发展到 hypergraph、graph pruning、DeFi link prediction、金融知识图谱构建与图驱动套利。

## 全部论文表

| 年份 | 会议分组 | 论文 | 链接 | 技术主类 | 创新点总结 |
|---:|---|---|---|---|---|
| 2024 | Asset Allocation, Robustness, and Risk | Denoising Diffusion Probabilistic Model for Realistic Financial Correlation Matrices | [DOI](https://doi.org/10.1145/3677052.3698640) | 生成式模型/数据合成 | 用生成式建模增强金融 AI 应用，重点解决稀缺数据、去噪或场景生成问题。 |
| 2024 | Asset Allocation, Robustness, and Risk | Generational Knowledge Transfer for Model Robustness & Agility: Label Augmentation for Time-Sensitive Financial Services Applications | [DOI](https://doi.org/10.1145/3677052.3698663) | 可解释/公平/可信评测 | 提升或评测金融 AI 应用中的可解释、公平、偏见识别、鲁棒性或审计可靠性。 |
| 2024 | Asset Allocation, Robustness, and Risk | Hopfield networks for asset allocation | [DOI](https://doi.org/10.1145/3677052.3698605) | 优化/投资组合/定价/风险 | 围绕资产配置改进优化、定价、对冲或风险约束下的决策质量。 |
| 2024 | Asset Allocation, Robustness, and Risk | Reducing Return Volatility in Neural Network-Based Asset Allocation via Formal Verification and Certified Training | [DOI](https://doi.org/10.1145/3677052.3698678) | 可解释/公平/可信评测 | 提升或评测资产配置中的可解释、公平、偏见识别、鲁棒性或审计可靠性。 |
| 2024 | Fairness, Explainability and Other | FairNNV: The Neural Network Verification Tool For Certifying Fairness | [DOI](https://doi.org/10.1145/3677052.3698677) | 可解释/公平/可信评测 | 提出或评测 FairNNV，将可信 AI、可解释性或评测方法用于金融网络分析。 |
| 2024 | Fairness, Explainability and Other | Open Set Recognition for Random Forest | [DOI](https://doi.org/10.1145/3677052.3698631) | 其他机器学习/数据工程 | 将通用机器学习或数据工程方法用于金融 AI 应用，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Fairness, Explainability and Other | TADACap: Time-series Adaptive Domain-Aware Captioning | [DOI](https://doi.org/10.1145/3677052.3698690) | 大语言模型/NLP/RAG | 提出或评测 TADACap，将LLM、NLP 或检索增强方法用于金融时间序列建模。 |
| 2024 | Fairness, Explainability and Other | Why Groups Matter: Necessity of Group Structures in Attributions | [DOI](https://doi.org/10.1145/3677052.3698667) | 其他机器学习/数据工程 | 围绕“Why Groups Matter: Necessity of Group Structures in Attributions”提出实证问题，检验通用机器学习或数据工程方法在金融 AI 应用中的有效性与边界。 |
| 2024 | Generative models | A Financial Time Series Denoiser Based on Diffusion Models | [DOI](https://doi.org/10.1145/3677052.3698649) | 生成式模型/数据合成 | 用生成式建模增强金融时间序列建模，重点解决稀缺数据、去噪或场景生成问题。 |
| 2024 | Generative models | Adversarial Inverse Reinforcement Learning for Market Making | [DOI](https://doi.org/10.1145/3677052.3698641) | 强化学习/在线决策 | 把序贯奖励学习用于做市策略，强调策略自适应和风险约束。 |
| 2024 | Generative models | FraudDiffuse: Diffusion-aided Synthetic Fraud Augmentation for Improved Fraud Detection | [DOI](https://doi.org/10.1145/3677052.3698658) | 异常检测/欺诈/金融犯罪 | 提出或评测 FraudDiffuse，将异常检测和金融犯罪识别用于欺诈检测。 |
| 2024 | Generative models | NeuralFactors: A Novel Factor Learning Approach to Generative Modeling of Equities | [DOI](https://doi.org/10.1145/3677052.3698647) | 生成式模型/数据合成 | 提出或评测 NeuralFactors，将生成式模型和合成数据技术用于金融 AI 应用。 |
| 2024 | Generative models and data-driven simulation | A Case Study on Enhancing Inquiry Response in a Non-Life Insurance Company Using Generative AI | [DOI](https://doi.org/10.1145/3677052.3698626) | 生成式模型/数据合成 | 用生成式建模增强保险/再保险定价，重点解决稀缺数据、去噪或场景生成问题。 |
| 2024 | Generative models and data-driven simulation | A Financial Market Simulation Environment for Trading Agents Using Deep Reinforcement Learning | [DOI](https://doi.org/10.1145/3677052.3698639) | 强化学习/在线决策 | 构建面向交易策略的框架/系统，把强化学习或在线序贯决策接入实际金融流程。 |
| 2024 | Generative models and data-driven simulation | Can GANs Learn the Stylized Facts of Financial Time Series? | [DOI](https://doi.org/10.1145/3677052.3698661) | 时间序列/预测/表征学习 | 围绕“Can GANs Learn the Stylized Facts of Financial Time Series?”提出实证问题，检验时间序列建模和表征学习在金融时间序列建模中的有效性与边界。 |
| 2024 | Generative models and data-driven simulation | FinLlama: LLM-Based Financial Sentiment Analysis for Algorithmic Trading | [DOI](https://doi.org/10.1145/3677052.3698696) | 大语言模型/NLP/RAG | 提出或评测 FinLlama，将LLM、NLP 或检索增强方法用于交易策略。 |
| 2024 | Generative models and data-driven simulation | Generative-CNN for Pattern Recognition in Finance | [DOI](https://doi.org/10.1145/3677052.3698622) | 生成式模型/数据合成 | 用生成式建模增强金融 AI 应用，重点解决稀缺数据、去噪或场景生成问题。 |
| 2024 | Generative models and data-driven simulation | Macroeconomic Conditioned Synthetic Financial Markets | [DOI](https://doi.org/10.1145/3677052.3698606) | 生成式模型/数据合成 | 用生成式建模增强宏观情景预测，重点解决稀缺数据、去噪或场景生成问题。 |
| 2024 | Generative models and data-driven simulation | Simulating the Economic Impact of Rationality through Reinforcement Learning and Agent-Based Modelling | [DOI](https://doi.org/10.1145/3677052.3698621) | 强化学习/在线决策 | 把序贯奖励学习用于金融 AI 应用，强调策略自适应和风险约束。 |
| 2024 | Generative models and data-driven simulation | Tax Credits and Household Behavior: The Roles of Myopic Decision-Making and Liquidity in a Simulated Economy | [DOI](https://doi.org/10.1145/3677052.3698599) | 优化/投资组合/定价/风险 | 提出或评测 Tax Credits and Household Behavior，将优化、定价、对冲或风险计算用于流动性行为分析。 |
| 2024 | Graph theory and Clustering | Cluster-driven Hierarchical Representation of Large Asset Universes for Optimal Portfolio Construction | [DOI](https://doi.org/10.1145/3677052.3698676) | 优化/投资组合/定价/风险 | 围绕投资组合构建与管理改进优化、定价、对冲或风险约束下的决策质量。 |
| 2024 | Graph theory and Clustering | Functional Mixed-type Clustering of Investors' Daily Returns During a Market Shock Change-point and Recovery | [DOI](https://doi.org/10.1145/3677052.3698633) | 图学习/知识图谱/网络分析 | 将图学习、知识图谱或网络分析用于金融 AI 应用，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Graph theory and Clustering | Identifying Money Laundering Subgraphs on the Blockchain | [DOI](https://doi.org/10.1145/3677052.3698635) | 异常检测/欺诈/金融犯罪 | 面向反洗钱与链上犯罪识别改进异常检测，强调稀缺标签、结构线索或合成样本利用。 |
| 2024 | Graph theory and Clustering | Time-aware Graph Attention Networks for Multiperiod Default Prediction | [DOI](https://doi.org/10.1145/3677052.3698619) | 图学习/知识图谱/网络分析 | 利用金融实体关系结构改进预测任务，突出结构依赖和传播模式。 |
| 2024 | Graphs, Clustering, and Spoofing | Can an unsupervised clustering algorithm reproduce a categorization system? | [DOI](https://doi.org/10.1145/3677052.3698616) | 其他机器学习/数据工程 | 围绕“Can an unsupervised clustering algorithm reproduce a categorization system?”提出实证问题，检验通用机器学习或数据工程方法在金融 AI 应用中的有效性与边界。 |
| 2024 | Graphs, Clustering, and Spoofing | Graph Feature Preprocessor: Real-time Subgraph-based Feature Extraction for Financial Crime Detection | [DOI](https://doi.org/10.1145/3677052.3698674) | 异常检测/欺诈/金融犯罪 | 提出或评测 Graph Feature Preprocessor，将异常检测和金融犯罪识别用于金融犯罪检测。 |
| 2024 | Graphs, Clustering, and Spoofing | Rolling Forward: Enhancing LightGCN with Causal Graph Convolution for Credit Bond Recommendation | [DOI](https://doi.org/10.1145/3677052.3698683) | 图学习/知识图谱/网络分析 | 提出或评测 Rolling Forward，将图学习、知识图谱或网络分析用于金融关系建模。 |
| 2024 | Graphs, Clustering, and Spoofing | The Effect of Liquidity on the Spoofability of Financial Markets | [DOI](https://doi.org/10.1145/3677052.3698634) | 其他机器学习/数据工程 | 将通用机器学习或数据工程方法用于流动性行为分析，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Large Language Models and Counterfactual Explanations | Adaptive and Explainable Margin Trading via Large Language Models on Portfolio Management | [DOI](https://doi.org/10.1145/3677052.3698681) | 大语言模型/NLP/RAG | 提升投资组合构建与管理中的可解释、公平、偏见识别或形式化可靠性。 |
| 2024 | Large Language Models and Counterfactual Explanations | ECC Analyzer: Extracting Trading Signal from Earnings Conference Calls using Large Language Model for Stock Volatility Prediction | [DOI](https://doi.org/10.1145/3677052.3698689) | 大语言模型/NLP/RAG | 提出或评测 ECC Analyzer，将LLM、NLP 或检索增强方法用于波动率建模。 |
| 2024 | Large Language Models and Counterfactual Explanations | FinQAPT: Empowering Financial Decisions with End-to-End LLM-driven Question Answering Pipeline | [DOI](https://doi.org/10.1145/3677052.3698682) | 大语言模型/NLP/RAG | 提出或评测 FinQAPT，将LLM、NLP 或检索增强方法用于金融问答。 |
| 2024 | Large Language Models and Counterfactual Explanations | TABCF: Counterfactual Explanations for Tabular Data Using a Transformer-Based VAE | [DOI](https://doi.org/10.1145/3677052.3698673) | 生成式模型/数据合成 | 提出或评测 TABCF，将生成式模型和合成数据技术用于金融 AI 应用。 |
| 2024 | LLMs and Graphs | A Dutch Financial Large Language Model | [DOI](https://doi.org/10.1145/3677052.3698628) | 大语言模型/NLP/RAG | 将LLM、NLP 或检索增强方法用于金融 AI 应用，突出金融场景下的建模、决策或评估改进。 |
| 2024 | LLMs and Graphs | FraudGT: A Simple, Effective, and Efficient Graph Transformer for Financial Fraud Detection | [DOI](https://doi.org/10.1145/3677052.3698648) | 异常检测/欺诈/金融犯罪 | 提出或评测 FraudGT，将异常检测和金融犯罪识别用于欺诈检测。 |
| 2024 | LLMs and Graphs | Lending an Ear: How LLMs Hear Your Banking Intentions | [DOI](https://doi.org/10.1145/3677052.3698608) | 其他机器学习/数据工程 | 提出或评测 Lending an Ear，将通用机器学习或数据工程方法用于金融 AI 应用。 |
| 2024 | LLMs and Graphs | TAT-LLM: A Specialized Language Model for Discrete Reasoning over Financial Tabular and Textual Data | [DOI](https://doi.org/10.1145/3677052.3698685) | 大语言模型/NLP/RAG | 提出或评测 TAT-LLM，将LLM、NLP 或检索增强方法用于金融 AI 应用。 |
| 2024 | Pricing, Hedging, and Fraud | Fast Deep Hedging with Second-Order Optimization | [DOI](https://doi.org/10.1145/3677052.3698604) | 优化/投资组合/定价/风险 | 围绕对冲决策改进优化、定价、对冲或风险约束下的决策质量。 |
| 2024 | Pricing, Hedging, and Fraud | Retrieval Augmented Fraud Detection | [DOI](https://doi.org/10.1145/3677052.3698692) | 异常检测/欺诈/金融犯罪 | 面向欺诈检测改进异常检测，强调稀缺标签、结构线索或合成样本利用。 |
| 2024 | Pricing, Hedging, and Fraud | Stable Multilevel Deep Neural Networks for Option Pricing and xVAs Using Forward-Backward Stochastic Differential Equations | [DOI](https://doi.org/10.1145/3677052.3698598) | 优化/投资组合/定价/风险 | 围绕期权/衍生品定价改进优化、定价、对冲或风险约束下的决策质量。 |
| 2024 | Reinforcement learning | Adaptive Risk-Based Control in Financial Trading | [DOI](https://doi.org/10.1145/3677052.3698652) | 优化/投资组合/定价/风险 | 围绕交易策略改进优化、定价、对冲或风险约束下的决策质量。 |
| 2024 | Reinforcement learning | Autoregressive DRL with Learned Intrinsic Rewards for Portfolio Optimisation | [DOI](https://doi.org/10.1145/3677052.3698670) | 强化学习/在线决策 | 把序贯奖励学习用于投资组合构建与管理，强调策略自适应和风险约束。 |
| 2024 | Reinforcement learning | Dynamic Reinforced Ensemble using Bayesian Optimization for Stock Trading | [DOI](https://doi.org/10.1145/3677052.3698595) | 优化/投资组合/定价/风险 | 围绕交易策略改进优化、定价、对冲或风险约束下的决策质量。 |
| 2024 | Reinforcement learning | EX-DRL: Hedging Against Heavy Losses with EXtreme Distributional Reinforcement Learning | [DOI](https://doi.org/10.1145/3677052.3698668) | 强化学习/在线决策 | 提出或评测 EX-DRL，将强化学习或在线序贯决策用于对冲决策。 |
| 2024 | Time Series and Networks | Contrastive Learning of Asset Embeddings from Financial Time Series | [DOI](https://doi.org/10.1145/3677052.3698610) | 时间序列/预测/表征学习 | 将时间序列建模和表征学习用于金融时间序列建模，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Time Series and Networks | DySTAGE: Dynamic Graph Representation Learning for Asset Pricing via Spatio-Temporal Attention and Graph Encodings | [DOI](https://doi.org/10.1145/3677052.3698680) | 图学习/知识图谱/网络分析 | 提出或评测 DySTAGE，将图学习、知识图谱或网络分析用于金融关系建模。 |
| 2024 | Time Series and Networks | Extracting Alpha from Financial Analyst Networks | [DOI](https://doi.org/10.1145/3677052.3698630) | 图学习/知识图谱/网络分析 | 将图学习、知识图谱或网络分析用于金融网络分析，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Time Series and Networks | Unveiling Recurring Financial Patterns: Novel unsupervised filtering algorithms for enhanced forecasting | [DOI](https://doi.org/10.1145/3677052.3698596) | 时间序列/预测/表征学习 | 提出或评测 Unveiling Recurring Financial Patterns，将时间序列建模和表征学习用于预测任务。 |
| 2024 | Poster Session | AI in Investment Analysis: LLMs for Equity Stock Ratings | [DOI](https://doi.org/10.1145/3677052.3698694) | 其他机器学习/数据工程 | 提出或评测 AI in Investment Analysis，将通用机器学习或数据工程方法用于金融 AI 应用。 |
| 2024 | Poster Session | Analyzing Cascading Outbreak of GameStop Event: A Practical Approach Using Network Analysis and Large Language Models | [DOI](https://doi.org/10.1145/3677052.3698636) | 大语言模型/NLP/RAG | 将LLM、NLP 或检索增强方法用于金融网络分析，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Poster Session | ARL-Based Multi-Action Market Making with Hawkes Processes and Variable Volatility | [DOI](https://doi.org/10.1145/3677052.3698695) | 强化学习/在线决策 | 把序贯奖励学习用于波动率建模，强调策略自适应和风险约束。 |
| 2024 | Poster Session | Augmenting Equity Factor Investing with Global Macro Regimes | [DOI](https://doi.org/10.1145/3677052.3698620) | 时间序列/预测/表征学习 | 将时间序列建模和表征学习用于金融 AI 应用，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Poster Session | Bankruptcy Prediction: Data Augmentation, LLMs and the Need for Auditor's Opinion | [DOI](https://doi.org/10.1145/3677052.3698627) | 异常检测/欺诈/金融犯罪 | 提出或评测 Bankruptcy Prediction，将异常检测和金融犯罪识别用于破产风险预测。 |
| 2024 | Poster Session | Cross-Sector Market Regime Forecasting with LLM-Augmented News Analysis | [DOI](https://doi.org/10.1145/3677052.3698642) | 大语言模型/NLP/RAG | 将LLM、NLP 或检索增强方法用于预测任务，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Poster Session | Customized FinGPT Search Agents Using Foundation Models | [DOI](https://doi.org/10.1145/3677052.3698637) | 其他机器学习/数据工程 | 将通用机器学习或数据工程方法用于金融 AI 应用，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Poster Session | Data-driven Derivative Hedging with Quadratic Variation Penalty | [DOI](https://doi.org/10.1145/3677052.3698664) | 优化/投资组合/定价/风险 | 围绕衍生品设计或对冲改进优化、定价、对冲或风险约束下的决策质量。 |
| 2024 | Poster Session | Deep Learning for Options Trading: An End-To-End Approach | [DOI](https://doi.org/10.1145/3677052.3698624) | 其他机器学习/数据工程 | 提出或评测 Deep Learning for Options Trading，将通用机器学习或数据工程方法用于期权/衍生品定价。 |
| 2024 | Poster Session | Designing Expressive and Liquid Financial Options Markets via Linear Programming and Automated Market Making | [DOI](https://doi.org/10.1145/3677052.3698687) | 强化学习/在线决策 | 将强化学习或在线序贯决策用于期权/衍生品定价，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Poster Session | Detecting Collective Liquidity Taking Distributions | [DOI](https://doi.org/10.1145/3677052.3698643) | 其他机器学习/数据工程 | 将通用机器学习或数据工程方法用于流动性行为分析，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Poster Session | Dynamic Pricing in Securities Lending Market: Application in Revenue Optimization for an Agent Lender Portfolio | [DOI](https://doi.org/10.1145/3677052.3698611) | 智能体/多智能体/市场仿真 | 将智能体系统或市场仿真框架用于投资组合构建与管理，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Poster Session | Enhanced Local Explainability and Trust Scores with Random Forest Proximities | [DOI](https://doi.org/10.1145/3677052.3698615) | 可解释/公平/可信评测 | 提升或评测金融 AI 应用中的可解释、公平、偏见识别、鲁棒性或审计可靠性。 |
| 2024 | Poster Session | Enhancing Financial Question Answering with a Multi-Agent Reflection Framework | [DOI](https://doi.org/10.1145/3677052.3698686) | 智能体/多智能体/市场仿真 | 构建面向金融问答的框架/系统，把智能体系统或市场仿真框架接入实际金融流程。 |
| 2024 | Poster Session | Enhancing Investment Analysis: Optimizing AI-Agent Collaboration in Financial Research | [DOI](https://doi.org/10.1145/3677052.3698645) | 智能体/多智能体/市场仿真 | 提出或评测 Enhancing Investment Analysis，将智能体系统或市场仿真框架用于金融 AI 应用。 |
| 2024 | Poster Session | Entity-based Financial Tabular Data Synthesis with Diffusion Models | [DOI](https://doi.org/10.1145/3677052.3698625) | 生成式模型/数据合成 | 用生成式建模增强金融 AI 应用，重点解决稀缺数据、去噪或场景生成问题。 |
| 2024 | Poster Session | Evaluating Fairness in Transaction Fraud Models: Fairness Metrics, Bias Audits, and Challenges | [DOI](https://doi.org/10.1145/3677052.3698666) | 可解释/公平/可信评测 | 构建评测或指标体系，衡量可信 AI、可解释性或评测方法在欺诈检测中的可靠性。 |
| 2024 | Poster Session | Evaluating Financial Relational Graphs: Interpretation Before Prediction | [DOI](https://doi.org/10.1145/3677052.3698644) | 时间序列/预测/表征学习 | 提出或评测 Evaluating Financial Relational Graphs，将时间序列建模和表征学习用于预测任务。 |
| 2024 | Poster Session | FinDKG: Dynamic Knowledge Graphs with Large Language Models for Detecting Global Trends in Financial Markets | [DOI](https://doi.org/10.1145/3677052.3698603) | 大语言模型/NLP/RAG | 提出或评测 FinDKG，将LLM、NLP 或检索增强方法用于金融关系建模。 |
| 2024 | Poster Session | FinVision: A Multi-Agent Framework for Stock Market Prediction | [DOI](https://doi.org/10.1145/3677052.3698688) | 智能体/多智能体/市场仿真 | 提出或评测 FinVision，将智能体系统或市场仿真框架用于预测任务。 |
| 2024 | Poster Session | FISHNET: Financial Intelligence from Sub-querying, Harmonizing, Neural-Conditioning, Expert Swarms, and Task Planning | [DOI](https://doi.org/10.1145/3677052.3698597) | 智能体/多智能体/市场仿真 | 提出或评测 FISHNET，将智能体系统或市场仿真框架用于金融 AI 应用。 |
| 2024 | Poster Session | GARCH-Informed Neural Networks for Volatility Prediction in Financial Markets | [DOI](https://doi.org/10.1145/3677052.3698600) | 时间序列/预测/表征学习 | 将时间序列建模和表征学习用于波动率建模，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Poster Session | HybridRAG: Integrating Knowledge Graphs and Vector Retrieval Augmented Generation for Efficient Information Extraction | [DOI](https://doi.org/10.1145/3677052.3698671) | 大语言模型/NLP/RAG | 提出或评测 HybridRAG，将LLM、NLP 或检索增强方法用于金融关系建模。 |
| 2024 | Poster Session | Imb-FinDiff: Conditional Diffusion Models for Class Imbalance Synthesis of Financial Tabular Data | [DOI](https://doi.org/10.1145/3677052.3698659) | 生成式模型/数据合成 | 提出或评测 Imb-FinDiff，将生成式模型和合成数据技术用于金融 AI 应用。 |
| 2024 | Poster Session | Is Small Really Beautiful for Central Bank Communication? Evaluating Language Models for Finance: Llama-3-70B, GPT-4, FinBERT-FOMC, FinBERT, and VADER | [DOI](https://doi.org/10.1145/3677052.3698675) | 大语言模型/NLP/RAG | 围绕“Is Small Really Beautiful for Central Bank Communication? Evaluating Language Models for Finance: Llama-3-70B, GPT-4, FinBERT-FOMC, FinBERT, and VADER”提出实证问题，检验LLM、NLP 或检索增强方法在金融 AI 应用中的有效性与边界。 |
| 2024 | Poster Session | Machine Learning-based Relative Valuation of Municipal Bonds | [DOI](https://doi.org/10.1145/3677052.3698650) | 其他机器学习/数据工程 | 将通用机器学习或数据工程方法用于金融 AI 应用，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Poster Session | Market Making with Learned Beta Policies | [DOI](https://doi.org/10.1145/3677052.3698623) | 强化学习/在线决策 | 将强化学习或在线序贯决策用于做市策略，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Poster Session | Market-Making and Hedging with Market Impact using Deep Reinforcement Learning | [DOI](https://doi.org/10.1145/3677052.3698646) | 强化学习/在线决策 | 把序贯奖励学习用于对冲决策，强调策略自适应和风险约束。 |
| 2024 | Poster Session | Mechanistic interpretability of large language models with applications to the financial services industry | [DOI](https://doi.org/10.1145/3677052.3698612) | 可解释/公平/可信评测 | 提升或评测金融 AI 应用中的可解释、公平、偏见识别、鲁棒性或审计可靠性。 |
| 2024 | Poster Session | Mixtures of Experts for Scaling up Neural Networks in Order Execution | [DOI](https://doi.org/10.1145/3677052.3698691) | 强化学习/在线决策 | 将强化学习或在线序贯决策用于订单执行，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Poster Session | Modality-aware Transformer for Financial Time series Forecasting | [DOI](https://doi.org/10.1145/3677052.3698654) | 时间序列/预测/表征学习 | 将时间序列建模和表征学习用于金融时间序列建模，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Poster Session | Navigating the Difficulty of Achieving Global Optimality under Variance-Induced Time Inconsistency | [DOI](https://doi.org/10.1145/3677052.3698657) | 其他机器学习/数据工程 | 将通用机器学习或数据工程方法用于金融 AI 应用，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Poster Session | Neural Term Structure of Additive Process for Option Pricing | [DOI](https://doi.org/10.1145/3677052.3698672) | 优化/投资组合/定价/风险 | 围绕期权/衍生品定价改进优化、定价、对冲或风险约束下的决策质量。 |
| 2024 | Poster Session | Numin: Weighted-Majority Ensembles for Intraday Trading | [DOI](https://doi.org/10.1145/3677052.3698656) | 其他机器学习/数据工程 | 提出或评测 Numin，将通用机器学习或数据工程方法用于交易策略。 |
| 2024 | Poster Session | Online Personalizing White-box LLMs Generation with Neural Bandits | [DOI](https://doi.org/10.1145/3677052.3698651) | 其他机器学习/数据工程 | 把序贯奖励学习用于金融 AI 应用，强调策略自适应和风险约束。 |
| 2024 | Poster Session | Optimizing Sequential Predictions for Order Execution: a Decision Focused Learning Approach | [DOI](https://doi.org/10.1145/3677052.3698665) | 强化学习/在线决策 | 将强化学习或在线序贯决策用于订单执行，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Poster Session | Quantile Regression using Random Forest Proximities | [DOI](https://doi.org/10.1145/3677052.3698632) | 其他机器学习/数据工程 | 将通用机器学习或数据工程方法用于金融 AI 应用，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Poster Session | Quantum Generative Models of Mid-Price Movement in Limit Order Books | [DOI](https://doi.org/10.1145/3677052.3698679) | 生成式模型/数据合成 | 用生成式建模增强金融 AI 应用，重点解决稀缺数据、去噪或场景生成问题。 |
| 2024 | Poster Session | AI versus AI in Financial Crimes & Detection: GenAI Crime Waves to Co-Evolutionary AI | [DOI](https://doi.org/10.1145/3677052.3698655) | 异常检测/欺诈/金融犯罪 | 面向金融犯罪检测改进异常检测，强调稀缺标签、结构线索或合成样本利用。 |
| 2024 | Poster Session | RiskMiner: Discovering Formulaic Alphas via Risk Seeking Monte Carlo Tree Search | [DOI](https://doi.org/10.1145/3677052.3698613) | 优化/投资组合/定价/风险 | 提出或评测 RiskMiner，将优化、定价、对冲或风险计算用于金融 AI 应用。 |
| 2024 | Poster Session | Simulate and Optimise: A two-layer mortgage simulator for designing novel mortgage assistance products | [DOI](https://doi.org/10.1145/3677052.3698607) | 优化/投资组合/定价/风险 | 提出或评测 Simulate and Optimise，将优化、定价、对冲或风险计算用于按揭产品设计。 |
| 2024 | Poster Session | Simulating Asset Prices using Conditional Time-Series GAN | [DOI](https://doi.org/10.1145/3677052.3698638) | 生成式模型/数据合成 | 用生成式建模增强金融时间序列建模，重点解决稀缺数据、去噪或场景生成问题。 |
| 2024 | Poster Session | Sovereign Risk Summarization | [DOI](https://doi.org/10.1145/3677052.3698669) | 大语言模型/NLP/RAG | 将LLM、NLP 或检索增强方法用于金融 AI 应用，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Poster Session | Stock Index Forecasting Using an Explainable TAFT Model with Online Data-Driven Social Sentiment Index | [DOI](https://doi.org/10.1145/3677052.3698618) | 大语言模型/NLP/RAG | 提升金融情感分析中的可解释、公平、偏见识别或形式化可靠性。 |
| 2024 | Poster Session | Stock Recommendations for Individual Investors: A Temporal Graph Network Approach with Mean-Variance Efficient Sampling | [DOI](https://doi.org/10.1145/3677052.3698662) | 图学习/知识图谱/网络分析 | 提出或评测 Stock Recommendations for Individual Investors，将图学习、知识图谱或网络分析用于股票推荐。 |
| 2024 | Poster Session | Tab-Distillation: Impacts of Dataset Distillation on Tabular Data For Outlier Detection | [DOI](https://doi.org/10.1145/3677052.3698660) | 异常检测/欺诈/金融犯罪 | 提出或评测 Tab-Distillation，将异常检测和金融犯罪识别用于金融 AI 应用。 |
| 2024 | Poster Session | To Compete or Collude: Bidding Incentives in Ethereum Block Building Auctions | [DOI](https://doi.org/10.1145/3677052.3698629) | 其他机器学习/数据工程 | 围绕“To Compete or Collude: Bidding Incentives in Ethereum Block Building Auctions”提出实证问题，检验通用机器学习或数据工程方法在以太坊区块构建机制分析中的有效性与边界。 |
| 2024 | Poster Session | Transformers and attention-based networks in quantitative trading: a comprehensive survey | [DOI](https://doi.org/10.1145/3677052.3698684) | 其他机器学习/数据工程 | 系统综述通用机器学习或数据工程方法在交易策略中的方法谱系与应用场景。 |
| 2024 | Poster Session | Transforming Unstructured Sensitive Information into Structured Knowledge | [DOI](https://doi.org/10.1145/3677052.3698602) | 其他机器学习/数据工程 | 将通用机器学习或数据工程方法用于金融 AI 应用，突出金融场景下的建模、决策或评估改进。 |
| 2024 | Poster Session | WallStreetFeds: Client-Specific Tokens as Investment Vehicles in Federated Learning | [DOI](https://doi.org/10.1145/3677052.3698653) | 其他机器学习/数据工程 | 提出或评测 WallStreetFeds，将通用机器学习或数据工程方法用于金融 AI 应用。 |
| 2024 | Poster Session | Whack-a-mole Online Learning: Physics-Informed Neural Network for Intraday Implied Volatility Surface | [DOI](https://doi.org/10.1145/3677052.3698601) | 优化/投资组合/定价/风险 | 提出或评测 Whack-a-mole Online Learning，将优化、定价、对冲或风险计算用于波动率建模。 |
| 2024 | Poster Session | XBRL Agent: Leveraging Large Language Models for Financial Report Analysis | [DOI](https://doi.org/10.1145/3677052.3698614) | 强化学习/在线决策 | 提出或评测 XBRL Agent，将强化学习或在线序贯决策用于财报结构化分析。 |
| 2025 | Agent-Based Financial Systems | AuditAgent: Expert-Guided Multi-Agent Reasoning for Cross-Document Fraudulent Evidence Discovery | [DOI](https://doi.org/10.1145/3768292.3770383) | 智能体/多智能体/市场仿真 | 提出或评测 AuditAgent，将智能体系统或市场仿真框架用于欺诈检测。 |
| 2025 | Agent-Based Financial Systems | FinSearch: A Temporal-Aware Search Agent Framework for Real-Time Financial Information Retrieval with Large Language Models | [DOI](https://doi.org/10.1145/3768292.3770382) | 智能体/多智能体/市场仿真 | 提出或评测 FinSearch，将智能体系统或市场仿真框架用于金融 AI 应用。 |
| 2025 | Agent-Based Financial Systems | JaxMARL-HFT: GPU-Accelerated Large-Scale Multi-Agent Reinforcement Learning for High-Frequency Trading | [DOI](https://doi.org/10.1145/3768292.3770416) | 强化学习/在线决策 | 提出或评测 JaxMARL-HFT，将强化学习或在线序贯决策用于高频交易。 |
| 2025 | Agent-Based Simulation for Market Design | FABS: An Extensible and High-Performance Digital Twin Framework of AI-Driven Financial Systems | [DOI](https://doi.org/10.1145/3768292.3770369) | 智能体/多智能体/市场仿真 | 提出或评测 FABS，将智能体系统或市场仿真框架用于金融 AI 应用。 |
| 2025 | Agent-Based Simulation for Market Design | Interpretable Market Simulations via Optimal Transport: Power Law Decomposition and Implications for Market Design | [DOI](https://doi.org/10.1145/3768292.3770338) | 智能体/多智能体/市场仿真 | 提升金融 AI 应用中的可解释、公平、偏见识别或形式化可靠性。 |
| 2025 | Agent-Based Simulation for Market Design | Market Selection with Midpoint Matching: A Strategic Agent-Based Analysis | [DOI](https://doi.org/10.1145/3768292.3770419) | 智能体/多智能体/市场仿真 | 提出或评测 Market Selection with Midpoint Matching，将智能体系统或市场仿真框架用于金融 AI 应用。 |
| 2025 | Anomaly and Fraud Detection in Financial Systems | A Multimodal Alignment-Based Anomaly Detection Method for Bankruptcy Prediction | [DOI](https://doi.org/10.1145/3768292.3770380) | 异常检测/欺诈/金融犯罪 | 面向破产风险预测改进异常检测，强调稀缺标签、结构线索或合成样本利用。 |
| 2025 | Anomaly and Fraud Detection in Financial Systems | Financial Statement Fraud Detection with a Categorical-to-Numerical Data Representation | [DOI](https://doi.org/10.1145/3768292.3770372) | 异常检测/欺诈/金融犯罪 | 面向欺诈检测改进异常检测，强调稀缺标签、结构线索或合成样本利用。 |
| 2025 | Anomaly and Fraud Detection in Financial Systems | TSTR for Financial Fraud: Learning to Detect Manipulation Without Real Data | [DOI](https://doi.org/10.1145/3768292.3770393) | 异常检测/欺诈/金融犯罪 | 提出或评测 TSTR for Financial Fraud，将异常检测和金融犯罪识别用于欺诈检测。 |
| 2025 | Autonomous Agents and Financial Manipulation | Algorithmic pricing with independent learners and relative experience replay | [DOI](https://doi.org/10.1145/3768292.3770357) | 优化/投资组合/定价/风险 | 围绕金融 AI 应用改进优化、定价、对冲或风险约束下的决策质量。 |
| 2025 | Autonomous Agents and Financial Manipulation | The Accidental Pump and Dump: When Agentic AI Meets Autonomous Trading | [DOI](https://doi.org/10.1145/3768292.3770424) | 异常检测/欺诈/金融犯罪 | 提出或评测 The Accidental Pump and Dump，将异常检测和金融犯罪识别用于操纵性交易风险识别。 |
| 2025 | Autonomous Agents and Financial Manipulation | Tracing Positional Bias in Financial Decision-Making: Mechanistic Insights from Qwen2.5 | [DOI](https://doi.org/10.1145/3768292.3770394) | 可解释/公平/可信评测 | 提升或评测金融 AI 应用中的可解释、公平、偏见识别、鲁棒性或审计可靠性。 |
| 2025 | Decision-Aware Portfolio Optimization | Estimating Covariance for Global Minimum Variance Portfolio: A Decision-Focused Learning Approach | [DOI](https://doi.org/10.1145/3768292.3770378) | 优化/投资组合/定价/风险 | 围绕投资组合构建与管理改进优化、定价、对冲或风险约束下的决策质量。 |
| 2025 | Decision-Aware Portfolio Optimization | Return Prediction for Mean-Variance Portfolio Selection: How Decision-Focused Learning Shapes Forecasting Models | [DOI](https://doi.org/10.1145/3768292.3770423) | 优化/投资组合/定价/风险 | 围绕投资组合构建与管理改进优化、定价、对冲或风险约束下的决策质量。 |
| 2025 | Decision-Aware Portfolio Optimization | Scaling Conditional Autoencoders for Portfolio Optimization via Uncertainty-Aware Factor Selection | [DOI](https://doi.org/10.1145/3768292.3770415) | 优化/投资组合/定价/风险 | 围绕投资组合构建与管理改进优化、定价、对冲或风险约束下的决策质量。 |
| 2025 | Ethics and Bias in LLM-driven Finance | Evaluating the Ethical Judgment of Large Language Models in Financial Market Abuse Cases | [DOI](https://doi.org/10.1145/3768292.3770439) | 可解释/公平/可信评测 | 构建评测或指标体系，衡量可信 AI、可解释性或评测方法在市场滥用识别中的可靠性。 |
| 2025 | Ethics and Bias in LLM-driven Finance | Query Generation Pipeline with Enhanced Answerability Assessment for Financial Information Retrieval | [DOI](https://doi.org/10.1145/3768292.3770354) | 大语言模型/NLP/RAG | 构建评测或指标体系，衡量LLM、NLP 或检索增强方法在金融 AI 应用中的可靠性。 |
| 2025 | Ethics and Bias in LLM-driven Finance | Your AI, Not Your View: The Bias of LLMs in Investment Analysis | [DOI](https://doi.org/10.1145/3768292.3770375) | 可解释/公平/可信评测 | 提出或评测 Your AI, Not Your View，将可信 AI、可解释性或评测方法用于金融 AI 应用。 |
| 2025 | Evaluation and Robustness in Financial NLP | FAITH: A Framework for Assessing Intrinsic Tabular Hallucinations in Finance | [DOI](https://doi.org/10.1145/3768292.3770433) | 其他机器学习/数据工程 | 提出或评测 FAITH，将通用机器学习或数据工程方法用于金融 AI 应用。 |
| 2025 | Evaluation and Robustness in Financial NLP | FinMR: A Knowledge-Intensive Multimodal Benchmark for Advanced Financial Reasoning | [DOI](https://doi.org/10.1145/3768292.3770365) | 可解释/公平/可信评测 | 提出或评测 FinMR，将可信 AI、可解释性或评测方法用于金融 AI 应用。 |
| 2025 | Evaluation and Robustness in Financial NLP | Quantifying Semantic Shift in Financial NLP: Robust Metrics for Market Prediction Stability | [DOI](https://doi.org/10.1145/3768292.3770403) | 可解释/公平/可信评测 | 构建评测或指标体系，衡量可信 AI、可解释性或评测方法在预测任务中的可靠性。 |
| 2025 | Explainable and Interpretable in Finance | Case-based Explainability for Random Forest: Prototypes, Critics, Counter-factuals and Semi-factuals | [DOI](https://doi.org/10.1145/3768292.3770381) | 可解释/公平/可信评测 | 提出或评测 Case-based Explainability for Random Forest，将可信 AI、可解释性或评测方法用于金融 AI 应用。 |
| 2025 | Explainable and Interpretable in Finance | NeuralBeta: Estimating Beta Using Deep Learning | [DOI](https://doi.org/10.1145/3768292.3770373) | 其他机器学习/数据工程 | 提出或评测 NeuralBeta，将通用机器学习或数据工程方法用于金融 AI 应用。 |
| 2025 | Explainable and Interpretable in Finance | ProtoHedge: Interpretable Hedging with Market Prototypes | [DOI](https://doi.org/10.1145/3768292.3770347) | 可解释/公平/可信评测 | 提出或评测 ProtoHedge，将可信 AI、可解释性或评测方法用于对冲决策。 |
| 2025 | Generative Models for Financial Forecasting | Discrete Flow Matching is a Surprisingly Effective Post-training Method to Address Compound Error in Autoregressive Models | [DOI](https://doi.org/10.1145/3768292.3770442) | 生成式模型/数据合成 | 将生成式模型和合成数据技术用于金融 AI 应用，突出金融场景下的建模、决策或评估改进。 |
| 2025 | Generative Models for Financial Forecasting | LLM Embedding for Regression Priors | [DOI](https://doi.org/10.1145/3768292.3770437) | 大语言模型/NLP/RAG | 将LLM、NLP 或检索增强方法用于金融 AI 应用，突出金融场景下的建模、决策或评估改进。 |
| 2025 | Generative Models for Financial Forecasting | TF-GAN: Topology-Aware Generative Adversarial Network for Financial Time Series Forecasting | [DOI](https://doi.org/10.1145/3768292.3770429) | 生成式模型/数据合成 | 提出或评测 TF-GAN，将生成式模型和合成数据技术用于金融时间序列建模。 |
| 2025 | Generative Models for Financial Forecasting | BMI-GP: Unsupervised Breach Merchant Identification via Adaptive Graph Pruning | [DOI](https://doi.org/10.1145/3768292.3770422) | 异常检测/欺诈/金融犯罪 | 提出或评测 BMI-GP，将异常检测和金融犯罪识别用于金融关系建模。 |
| 2025 | Generative Models for Financial Forecasting | Graph Neural Networks for Bridge Swap Link Prediction in Uniswap v3 | [DOI](https://doi.org/10.1145/3768292.3770392) | 图学习/知识图谱/网络分析 | 利用金融实体关系结构改进预测任务，突出结构依赖和传播模式。 |
| 2025 | Generative Models for Financial Forecasting | LAS-GNN: A Graph Neural Network for Temporal Money Laundering Motif Detection | [DOI](https://doi.org/10.1145/3768292.3770410) | 异常检测/欺诈/金融犯罪 | 提出或评测 LAS-GNN，将异常检测和金融犯罪识别用于反洗钱与链上犯罪识别。 |
| 2025 | Knowledge Graphs and Financial Data Imputation | ACT-Tensor: Tensor Completion Framework for Financial Dataset Imputation | [DOI](https://doi.org/10.1145/3768292.3770408) | 图学习/知识图谱/网络分析 | 提出或评测 ACT-Tensor，将图学习、知识图谱或网络分析用于金融 AI 应用。 |
| 2025 | Knowledge Graphs and Financial Data Imputation | BForTFin: A Financial Domain-Aware Multiscale Evaluation Method for Time-Series Foundation Models | [DOI](https://doi.org/10.1145/3768292.3770402) | 时间序列/预测/表征学习 | 提出或评测 BForTFin，将时间序列建模和表征学习用于金融时间序列建模。 |
| 2025 | Knowledge Graphs and Financial Data Imputation | FinReflectKG: Agentic Construction and Evaluation of Financial Knowledge Graphs | [DOI](https://doi.org/10.1145/3768292.3770363) | 智能体/多智能体/市场仿真 | 提出或评测 FinReflectKG，将智能体系统或市场仿真框架用于金融关系建模。 |
| 2025 | LLMs for Financial Text Understanding | Can AI Read Like a Financial Analyst? A Financial Touchstone for Frontier Language Models Such as Gemini 2.5 Pro, o3, and Grok 4 on Long-Context Annual Report Comprehension | [DOI](https://doi.org/10.1145/3768292.3770417) | 大语言模型/NLP/RAG | 围绕“Can AI Read Like a Financial Analyst? A Financial Touchstone for Frontier Language Models Such as Gemini 2.5 Pro, o3, and Grok 4 on Long-Context Annual Report Comprehension”提出实证问题，检验LLM、NLP 或检索增强方法在年报理解中的有效性与边界。 |
| 2025 | LLMs for Financial Text Understanding | Reasoning or Overthinking: Evaluating Large Language Models on Financial Sentiment Analysis | [DOI](https://doi.org/10.1145/3768292.3770341) | 大语言模型/NLP/RAG | 提出或评测 Reasoning or Overthinking，将LLM、NLP 或检索增强方法用于金融情感分析。 |
| 2025 | LLMs for Financial Text Understanding | Two Sides of the Same Coin: How LLMs Reveal Dual Narratives in Annual Reports | [DOI](https://doi.org/10.1145/3768292.3770435) | 大语言模型/NLP/RAG | 将LLM、NLP 或检索增强方法用于年报理解，突出金融场景下的建模、决策或评估改进。 |
| 2025 | LLMs for Macroeconomic Forecasting | Decoding the Beige Book: LLM-Powered Sentiment Analysis for Real-Time Recession Forecasting | [DOI](https://doi.org/10.1145/3768292.3770425) | 大语言模型/NLP/RAG | 提出或评测 Decoding the Beige Book，将LLM、NLP 或检索增强方法用于金融情感分析。 |
| 2025 | LLMs for Macroeconomic Forecasting | Democratizing Alpha: LLM-Driven Portfolio Construction for Retail Investors Using Public Financial Media | [DOI](https://doi.org/10.1145/3768292.3770376) | 大语言模型/NLP/RAG | 提出或评测 Democratizing Alpha，将LLM、NLP 或检索增强方法用于投资组合构建与管理。 |
| 2025 | LLMs for Macroeconomic Forecasting | Prompting for Policy: Forecasting Macroeconomic Scenarios with Synthetic LLM Personas | [DOI](https://doi.org/10.1145/3768292.3770385) | 大语言模型/NLP/RAG | 提出或评测 Prompting for Policy，将LLM、NLP 或检索增强方法用于宏观情景预测。 |
| 2025 | Reinforcement Learning in Finanical Decision-Making | Behavioural Reinforcement Learning (Beyond Rationality: RL Under Investor Bias) | [DOI](https://doi.org/10.1145/3768292.3770436) | 可解释/公平/可信评测 | 提出或评测 Behavioural Reinforcement Learning (Beyond Rationality，将可信 AI、可解释性或评测方法用于金融 AI 应用。 |
| 2025 | Reinforcement Learning in Finanical Decision-Making | ClauseLens: Clause-Grounded, CVaR-Constrained Reinforcement Learning for Trustworthy Reinsurance Pricing | [DOI](https://doi.org/10.1145/3768292.3770356) | 强化学习/在线决策 | 提出或评测 ClauseLens，将强化学习或在线序贯决策用于保险/再保险定价。 |
| 2025 | Reinforcement Learning in Finanical Decision-Making | Continuous-Time Reinforcement Learning for Asset-Liability Management | [DOI](https://doi.org/10.1145/3768292.3770337) | 强化学习/在线决策 | 把序贯奖励学习用于金融 AI 应用，强调策略自适应和风险约束。 |
| 2025 | Robust Optimization and Insurance Pricing | Learning to Manage Investment Portfolios beyond Simple Utility Functions | [DOI](https://doi.org/10.1145/3768292.3770426) | 优化/投资组合/定价/风险 | 围绕投资组合构建与管理改进优化、定价、对冲或风险约束下的决策质量。 |
| 2025 | Robust Optimization and Insurance Pricing | Parametric Phi-Divergence-Based Distributionally Robust Optimization for Insurance Pricing | [DOI](https://doi.org/10.1145/3768292.3770404) | 优化/投资组合/定价/风险 | 构建评测或指标体系，衡量优化、定价、对冲或风险计算在保险/再保险定价中的可靠性。 |
| 2025 | Robust Optimization and Insurance Pricing | Similarity-based Conformal Prediciton using Random Forest Proximities | [DOI](https://doi.org/10.1145/3768292.3770379) | 可解释/公平/可信评测 | 提升或评测金融 AI 应用中的可解释、公平、偏见识别、鲁棒性或审计可靠性。 |
| 2025 | Statistical Arbitrage and Trading Strategy Learning | Attention Factors for Statistical Arbitrage | [DOI](https://doi.org/10.1145/3768292.3770398) | 优化/投资组合/定价/风险 | 围绕金融 AI 应用改进优化、定价、对冲或风险约束下的决策质量。 |
| 2025 | Statistical Arbitrage and Trading Strategy Learning | Deep Mean-Reversion: A Physics-Informed Contrastive Approach to Pairs Trading | [DOI](https://doi.org/10.1145/3768292.3770406) | 时间序列/预测/表征学习 | 提出或评测 Deep Mean-Reversion，将时间序列建模和表征学习用于交易策略。 |
| 2025 | Statistical Arbitrage and Trading Strategy Learning | ISEPT: Image-Based Selection and Execution Framework for Pair Trading | [DOI](https://doi.org/10.1145/3768292.3770346) | 优化/投资组合/定价/风险 | 提出或评测 ISEPT，将优化、定价、对冲或风险计算用于交易策略。 |
| 2025 | Time-Series Modeling and Forecasting | DeltaLag: Learning Dynamic Lead-Lag Patterns in Financial Markets | [DOI](https://doi.org/10.1145/3768292.3770421) | 时间序列/预测/表征学习 | 提出或评测 DeltaLag，将时间序列建模和表征学习用于金融 AI 应用。 |
| 2025 | Time-Series Modeling and Forecasting | Factor-Driven Network Informed Restricted Vector Autoregression | [DOI](https://doi.org/10.1145/3768292.3770412) | 时间序列/预测/表征学习 | 将时间序列建模和表征学习用于金融网络分析，突出金融场景下的建模、决策或评估改进。 |
| 2025 | Time-Series Modeling and Forecasting | Online Ensemble Learning for Sector Rotation: A Gradient-Free Framework | [DOI](https://doi.org/10.1145/3768292.3770420) | 时间序列/预测/表征学习 | 构建面向金融 AI 应用的框架/系统，把时间序列建模和表征学习接入实际金融流程。 |
| 2025 | Volatility and Derivatives Modeling | Neural Network-Driven Volatility Drag Mitigation under Aggressive Leverage | [DOI](https://doi.org/10.1145/3768292.3770370) | 其他机器学习/数据工程 | 将通用机器学习或数据工程方法用于波动率建模，突出金融场景下的建模、决策或评估改进。 |
| 2025 | Volatility and Derivatives Modeling | Probability‑Density‑Consistent Physics-Informed Neural Networks for Stochastic Local Volatility Model Calibration | [DOI](https://doi.org/10.1145/3768292.3770350) | 优化/投资组合/定价/风险 | 围绕波动率建模改进优化、定价、对冲或风险约束下的决策质量。 |
| 2025 | Volatility and Derivatives Modeling | Repurposing Language Models for FX Volatility Forecasting: A Data-Efficient and Context-Aware Approach | [DOI](https://doi.org/10.1145/3768292.3770386) | 大语言模型/NLP/RAG | 将LLM、NLP 或检索增强方法用于波动率建模，突出金融场景下的建模、决策或评估改进。 |
| 2025 | Poster Session | A Data-Driven Asset Relation Extraction and Portfolio Optimization Method through Convolution | [DOI](https://doi.org/10.1145/3768292.3770353) | 图学习/知识图谱/网络分析 | 将图学习、知识图谱或网络分析用于投资组合构建与管理，突出金融场景下的建模、决策或评估改进。 |
| 2025 | Poster Session | A Role-Aware Multi-Agent Framework for Financial Education QA | [DOI](https://doi.org/10.1145/3768292.3770345) | 智能体/多智能体/市场仿真 | 构建面向金融问答的框架/系统，把智能体系统或市场仿真框架接入实际金融流程。 |
| 2025 | Poster Session | Adaptive Quantum Channels as Long-Memory Generative Models | [DOI](https://doi.org/10.1145/3768292.3770440) | 生成式模型/数据合成 | 用生成式建模增强金融 AI 应用，重点解决稀缺数据、去噪或场景生成问题。 |
| 2025 | Poster Session | Adaptive Sample Weighting with Regime-Aware Meta-Learning Framework for Financial Forecasting | [DOI](https://doi.org/10.1145/3768292.3770374) | 其他机器学习/数据工程 | 构建面向预测任务的框架/系统，把通用机器学习或数据工程方法接入实际金融流程。 |
| 2025 | Poster Session | Aligning Language Models with Investor and Market Behavior for Financial Recommendations | [DOI](https://doi.org/10.1145/3768292.3770399) | 大语言模型/NLP/RAG | 将LLM、NLP 或检索增强方法用于金融 AI 应用，突出金融场景下的建模、决策或评估改进。 |
| 2025 | Poster Session | Arbitrage-Free Implied Volatility Surface Smoothing via Generative Adversarial Networks | [DOI](https://doi.org/10.1145/3768292.3771252) | 生成式模型/数据合成 | 用生成式建模增强波动率建模，重点解决稀缺数据、去噪或场景生成问题。 |
| 2025 | Poster Session | Attention-Based Multi-Asset Order Flow Networks for Enhanced Mid-Price Prediction | [DOI](https://doi.org/10.1145/3768292.3770430) | 时间序列/预测/表征学习 | 将时间序列建模和表征学习用于预测任务，突出金融场景下的建模、决策或评估改进。 |
| 2025 | Poster Session | CMS-VAE: A Strategy-aware Variational AutoEncoder for High-Fidelity Crypto Market Simulation | [DOI](https://doi.org/10.1145/3768292.3771253) | 生成式模型/数据合成 | 提出或评测 CMS-VAE，将生成式模型和合成数据技术用于金融 AI 应用。 |
| 2025 | Poster Session | Constrained Tabular Diffusion for Finance | [DOI](https://doi.org/10.1145/3768292.3770358) | 生成式模型/数据合成 | 用生成式建模增强金融 AI 应用，重点解决稀缺数据、去噪或场景生成问题。 |
| 2025 | Poster Session | Contextual Time Series Embedding: A State Space Perspective for Financial Data | [DOI](https://doi.org/10.1145/3768292.3771255) | 时间序列/预测/表征学习 | 提出或评测 Contextual Time Series Embedding，将时间序列建模和表征学习用于金融时间序列建模。 |
| 2025 | Poster Session | Curriculum-Guided Reinforcement Learning for Synthesizing Gas-Efficient Financial Derivatives Contracts | [DOI](https://doi.org/10.1145/3768292.3770397) | 强化学习/在线决策 | 把序贯奖励学习用于衍生品设计或对冲，强调策略自适应和风险约束。 |
| 2025 | Poster Session | Data-Driven Trade Flow Decomposition for Exchange-Traded Funds and their Constituents | [DOI](https://doi.org/10.1145/3768292.3770434) | 其他机器学习/数据工程 | 将通用机器学习或数据工程方法用于金融 AI 应用，突出金融场景下的建模、决策或评估改进。 |
| 2025 | Poster Session | Demystifying TCFD Disclosures: An AI-Powered Framework for Enhanced Transparency and Trust | [DOI](https://doi.org/10.1145/3768292.3770400) | 可解释/公平/可信评测 | 提出或评测 Demystifying TCFD Disclosures，将可信 AI、可解释性或评测方法用于公司披露分析。 |
| 2025 | Poster Session | DiffVolume: Diffusion Models for Volume Generation in Limit Order Books | [DOI](https://doi.org/10.1145/3768292.3770413) | 生成式模型/数据合成 | 提出或评测 DiffVolume，将生成式模型和合成数据技术用于金融 AI 应用。 |
| 2025 | Poster Session | Extracting the Structure of Press Releases for Predicting Earnings Announcement Returns | [DOI](https://doi.org/10.1145/3768292.3770344) | 大语言模型/NLP/RAG | 将LLM、NLP 或检索增强方法用于业绩公告/电话会分析，突出金融场景下的建模、决策或评估改进。 |
| 2025 | Poster Session | FactorMAD: A Multi-Agent Debate Framework Based on Large Language Models for Interpretable Stock Alpha Factor Mining | [DOI](https://doi.org/10.1145/3768292.3770377) | 智能体/多智能体/市场仿真 | 提出或评测 FactorMAD，将智能体系统或市场仿真框架用于金融 AI 应用。 |
| 2025 | Poster Session | Fast Monitoring of Systemic Risk in Financial Networks with Credit Default Swaps | [DOI](https://doi.org/10.1145/3768292.3770401) | 图学习/知识图谱/网络分析 | 构建面向金融网络分析的框架/系统，把图学习、知识图谱或网络分析接入实际金融流程。 |
| 2025 | Poster Session | Federated Financial Reasoning Distillation: Training A Small Financial Expert by Learning From Multiple Teachers | [DOI](https://doi.org/10.1145/3768292.3770339) | 其他机器学习/数据工程 | 提出或评测 Federated Financial Reasoning Distillation，将通用机器学习或数据工程方法用于金融 AI 应用。 |
| 2025 | Poster Session | FinAgentBench: A Benchmark Dataset for Agentic Retrieval in Financial Question Answering | [DOI](https://doi.org/10.1145/3768292.3770362) | 可解释/公平/可信评测 | 提出或评测 FinAgentBench，将可信 AI、可解释性或评测方法用于金融问答。 |
| 2025 | Poster Session | FinDER: Financial Dataset for Question Answering and Evaluating Retrieval-Augmented Generation | [DOI](https://doi.org/10.1145/3768292.3770361) | 大语言模型/NLP/RAG | 提出或评测 FinDER，将LLM、NLP 或检索增强方法用于金融问答。 |
| 2025 | Poster Session | FinDPO: Financial Sentiment Analysis for Algorithmic Trading through Preference Optimization of LLMs | [DOI](https://doi.org/10.1145/3768292.3770367) | 大语言模型/NLP/RAG | 提出或评测 FinDPO，将LLM、NLP 或检索增强方法用于交易策略。 |
| 2025 | Poster Session | FinResearchBench: A Logic Tree based Agent-as-a-Judge Evaluation Framework for Financial Research Agents | [DOI](https://doi.org/10.1145/3768292.3770364) | 智能体/多智能体/市场仿真 | 提出或评测 FinResearchBench，将智能体系统或市场仿真框架用于金融 AI 应用。 |
| 2025 | Poster Session | From Constituents to Index: Interpretable Price Movement Prediction via Cross-Asset Order Flow | [DOI](https://doi.org/10.1145/3768292.3770432) | 时间序列/预测/表征学习 | 提出或评测 From Constituents to Index，将时间序列建模和表征学习用于预测任务。 |
| 2025 | Poster Session | From News to Returns: A Granger-Causal Hypergraph Transformer on the Sphere | [DOI](https://doi.org/10.1145/3768292.3770414) | 图学习/知识图谱/网络分析 | 提出或评测 From News to Returns，将图学习、知识图谱或网络分析用于金融关系建模。 |
| 2025 | Poster Session | Fusing Narrative Semantics for Financial Volatility Forecasting | [DOI](https://doi.org/10.1145/3768292.3771256) | 大语言模型/NLP/RAG | 将LLM、NLP 或检索增强方法用于波动率建模，突出金融场景下的建模、决策或评估改进。 |
| 2025 | Poster Session | Graph Learning for Foreign Exchange Rate Prediction and Statistical Arbitrage | [DOI](https://doi.org/10.1145/3768292.3770418) | 图学习/知识图谱/网络分析 | 利用金融实体关系结构改进预测任务，突出结构依赖和传播模式。 |
| 2025 | Poster Session | Hypergraph Neural Networks to Predict Stock Movements By Exploring Higher-order Relationships | [DOI](https://doi.org/10.1145/3768292.3770389) | 图学习/知识图谱/网络分析 | 利用金融实体关系结构改进金融关系建模，突出结构依赖和传播模式。 |
| 2025 | Poster Session | IKNet: Interpretable Stock Price Prediction via Keyword-Guided Integration of News and Technical Indicators | [DOI](https://doi.org/10.1145/3768292.3770343) | 时间序列/预测/表征学习 | 提出或评测 IKNet，将时间序列建模和表征学习用于预测任务。 |
| 2025 | Poster Session | Is BTC Enough? A New Perspective on Cryptocurrency Price Formation | [DOI](https://doi.org/10.1145/3768292.3770351) | 其他机器学习/数据工程 | 围绕“Is BTC Enough? A New Perspective on Cryptocurrency Price Formation”提出实证问题，检验通用机器学习或数据工程方法在金融 AI 应用中的有效性与边界。 |
| 2025 | Poster Session | Language Models for Automated Market Commentary from Corporate Disclosures | [DOI](https://doi.org/10.1145/3768292.3770438) | 大语言模型/NLP/RAG | 将LLM、NLP 或检索增强方法用于公司披露分析，突出金融场景下的建模、决策或评估改进。 |
| 2025 | Poster Session | Large Language Model Agents for Investment Management: Foundations, Benchmarks, and Research Frontiers | [DOI](https://doi.org/10.1145/3768292.3770387) | 大语言模型/NLP/RAG | 构建评测或指标体系，衡量LLM、NLP 或检索增强方法在金融 AI 应用中的可靠性。 |
| 2025 | Poster Session | LatentGraph: From Latent States to Rule-based Expressions for Explainable Financial Forecasting | [DOI](https://doi.org/10.1145/3768292.3770428) | 其他机器学习/数据工程 | 提出或评测 LatentGraph，将通用机器学习或数据工程方法用于预测任务。 |
| 2025 | Poster Session | Learning to Scalp: A Reinforcement Learning Agent-Based Study | [DOI](https://doi.org/10.1145/3768292.3770396) | 强化学习/在线决策 | 提出或评测 Learning to Scalp，将强化学习或在线序贯决策用于金融 AI 应用。 |
| 2025 | Poster Session | Learning to Trade with Preferences: Interpretable Execution via Mixture-of-Experts | [DOI](https://doi.org/10.1145/3768292.3770390) | 强化学习/在线决策 | 提出或评测 Learning to Trade with Preferences，将强化学习或在线序贯决策用于金融 AI 应用。 |
| 2025 | Poster Session | LENS: Large Pre-trained Transformer for Exploring Financial Time Series Regularities | [DOI](https://doi.org/10.1145/3768292.3770349) | 时间序列/预测/表征学习 | 提出或评测 LENS，将时间序列建模和表征学习用于金融时间序列建模。 |
| 2025 | Poster Session | Leveraging Deep Learning Optimization for Monte Carlo Calibration of (Rough) Stochastic Volatility Models | [DOI](https://doi.org/10.1145/3768292.3771250) | 优化/投资组合/定价/风险 | 围绕波动率建模改进优化、定价、对冲或风险约束下的决策质量。 |
| 2025 | Poster Session | Long-Term Financial Forecasting and Trading via Multi-Agent Reinforcement Learning | [DOI](https://doi.org/10.1145/3768292.3770411) | 强化学习/在线决策 | 把序贯奖励学习用于交易策略，强调策略自适应和风险约束。 |
| 2025 | Poster Session | MacroVAE: Counterfactual Financial Scenario Generation via Macroeconomic Conditioning | [DOI](https://doi.org/10.1145/3768292.3770360) | 其他机器学习/数据工程 | 提出或评测 MacroVAE，将通用机器学习或数据工程方法用于宏观情景预测。 |
| 2025 | Poster Session | Mean Variance Efficient Collaborative Filtering for Stock Recommendations | [DOI](https://doi.org/10.1145/3768292.3770427) | 其他机器学习/数据工程 | 将通用机器学习或数据工程方法用于股票推荐，突出金融场景下的建模、决策或评估改进。 |
| 2025 | Poster Session | Multi-Agent Reinforcement Learning for Market Making: Competition without Collusion | [DOI](https://doi.org/10.1145/3768292.3770388) | 强化学习/在线决策 | 把序贯奖励学习用于做市策略，强调策略自适应和风险约束。 |
| 2025 | Poster Session | Multilingual BERT-based Classification and Recommendation Model for Supporting Innovation Finance Decisions | [DOI](https://doi.org/10.1145/3768292.3770384) | 大语言模型/NLP/RAG | 将LLM、NLP 或检索增强方法用于金融 AI 应用，突出金融场景下的建模、决策或评估改进。 |
| 2025 | Poster Session | Natural-gas storage modelling by deep reinforcement learning | [DOI](https://doi.org/10.1145/3768292.3770348) | 强化学习/在线决策 | 把序贯奖励学习用于金融 AI 应用，强调策略自适应和风险约束。 |
| 2025 | Poster Session | Norm-Salvaged Embedding: Improving Condition Alignment of Synthetic Time Series Generation in Finance | [DOI](https://doi.org/10.1145/3768292.3770342) | 生成式模型/数据合成 | 提出或评测 Norm-Salvaged Embedding，将生成式模型和合成数据技术用于金融时间序列建模。 |
| 2025 | Poster Session | On the Potential of Tool-Enhanced Small Language Models to Match Large Models in Finance | [DOI](https://doi.org/10.1145/3768292.3770409) | 大语言模型/NLP/RAG | 将LLM、NLP 或检索增强方法用于金融 AI 应用，突出金融场景下的建模、决策或评估改进。 |
| 2025 | Poster Session | Optimizing Large Language Models for ESG Activity Detection in Financial Texts | [DOI](https://doi.org/10.1145/3768292.3770371) | 大语言模型/NLP/RAG | 将LLM、NLP 或检索增强方法用于ESG 文本识别，突出金融场景下的建模、决策或评估改进。 |
| 2025 | Poster Session | Positive-Unlabeled Learning for Financial Misstatement Detection under Realistic Constraints | [DOI](https://doi.org/10.1145/3768292.3770366) | 异常检测/欺诈/金融犯罪 | 面向财务错报检测改进异常检测，强调稀缺标签、结构线索或合成样本利用。 |
| 2025 | Poster Session | Predictive Uncertainty Quantification for Financial DNN Using Regular Vine Copula | [DOI](https://doi.org/10.1145/3768292.3771254) | 可解释/公平/可信评测 | 提升或评测金融 AI 应用中的可解释、公平、偏见识别、鲁棒性或审计可靠性。 |
| 2025 | Poster Session | Quantum Optimization of Currency Arbitrage via Graph-Informed Entanglement Strategies | [DOI](https://doi.org/10.1145/3768292.3770352) | 图学习/知识图谱/网络分析 | 利用金融实体关系结构改进金融关系建模，突出结构依赖和传播模式。 |
| 2025 | Poster Session | Regret-Optimized Portfolio Enhancement through Deep Reinforcement Learning and Future Looking Rewards | [DOI](https://doi.org/10.1145/3768292.3770340) | 强化学习/在线决策 | 把序贯奖励学习用于投资组合构建与管理，强调策略自适应和风险约束。 |
| 2025 | Poster Session | Right Place, Right Time: Market Simulation-based RL for Execution Optimisation | [DOI](https://doi.org/10.1145/3768292.3770405) | 强化学习/在线决策 | 提出或评测 Right Place, Right Time，将强化学习或在线序贯决策用于金融 AI 应用。 |
| 2025 | Poster Session | Robust time series generation via Schrödinger Bridge: a comprehensive evaluation | [DOI](https://doi.org/10.1145/3768292.3770391) | 生成式模型/数据合成 | 构建评测或指标体系，衡量生成式模型和合成数据技术在金融时间序列建模中的可靠性。 |
| 2025 | Poster Session | Shock-Biased Attention: Enhancing Transformer Hawkes Processes with Amplitude-Driven Temporal Kernels | [DOI](https://doi.org/10.1145/3768292.3770431) | 时间序列/预测/表征学习 | 提出或评测 Shock-Biased Attention，将时间序列建模和表征学习用于金融 AI 应用。 |
| 2025 | Poster Session | Structured Agentic Workflows for Financial Time-Series Modelling with LLMs and Reflective Feedback | [DOI](https://doi.org/10.1145/3768292.3771251) | 智能体/多智能体/市场仿真 | 将智能体系统或市场仿真框架用于金融时间序列建模，突出金融场景下的建模、决策或评估改进。 |
| 2025 | Poster Session | Time-Varying Factor-Augmented Models for Volatility Forecasting | [DOI](https://doi.org/10.1145/3768292.3770407) | 时间序列/预测/表征学习 | 将时间序列建模和表征学习用于波动率建模，突出金融场景下的建模、决策或评估改进。 |
| 2025 | Poster Session | Unified Item Segmentation for 10-Q and 10-K Filings Using Item-Aware Document-Level Auxiliary Tasks | [DOI](https://doi.org/10.1145/3768292.3770359) | 大语言模型/NLP/RAG | 将LLM、NLP 或检索增强方法用于监管申报解析，突出金融场景下的建模、决策或评估改进。 |
| 2025 | Poster Session | Unmasking Bias in Financial AI: A Robust Framework for Evaluating and Mitigating Hidden Biases in LLMs | [DOI](https://doi.org/10.1145/3768292.3770355) | 可解释/公平/可信评测 | 提出或评测 Unmasking Bias in Financial AI，将可信 AI、可解释性或评测方法用于金融 AI 应用。 |
| 2025 | Poster Session | Vision, Voice, and Text: Pioneering Zero-shot Multimodal LLMs for Sentiment-driven Investment | [DOI](https://doi.org/10.1145/3768292.3770368) | 大语言模型/NLP/RAG | 提出或评测 Vision, Voice, and Text，将LLM、NLP 或检索增强方法用于金融情感分析。 |

## DBLP 原始会议分组数量

| 年份 | DBLP/会议分组 | 论文数 |
|---:|---|---:|
| 2024 | Asset Allocation, Robustness, and Risk | 4 |
| 2024 | Fairness, Explainability and Other | 4 |
| 2024 | Generative models | 4 |
| 2024 | Generative models and data-driven simulation | 8 |
| 2024 | Graph theory and Clustering | 4 |
| 2024 | Graphs, Clustering, and Spoofing | 4 |
| 2024 | LLMs and Graphs | 4 |
| 2024 | Large Language Models and Counterfactual Explanations | 4 |
| 2024 | Poster Session | 52 |
| 2024 | Pricing, Hedging, and Fraud | 3 |
| 2024 | Reinforcement learning | 4 |
| 2024 | Time Series and Networks | 4 |
| 2025 | Agent-Based Financial Systems | 3 |
| 2025 | Agent-Based Simulation for Market Design | 3 |
| 2025 | Anomaly and Fraud Detection in Financial Systems | 3 |
| 2025 | Autonomous Agents and Financial Manipulation | 3 |
| 2025 | Decision-Aware Portfolio Optimization | 3 |
| 2025 | Ethics and Bias in LLM-driven Finance | 3 |
| 2025 | Evaluation and Robustness in Financial NLP | 3 |
| 2025 | Explainable and Interpretable in Finance | 3 |
| 2025 | Generative Models for Financial Forecasting | 6 |
| 2025 | Knowledge Graphs and Financial Data Imputation | 3 |
| 2025 | LLMs for Financial Text Understanding | 3 |
| 2025 | LLMs for Macroeconomic Forecasting | 3 |
| 2025 | Poster Session | 57 |
| 2025 | Reinforcement Learning in Finanical Decision-Making | 3 |
| 2025 | Robust Optimization and Insurance Pricing | 3 |
| 2025 | Statistical Arbitrage and Trading Strategy Learning | 3 |
| 2025 | Time-Series Modeling and Forecasting | 3 |
| 2025 | Volatility and Derivatives Modeling | 3 |
