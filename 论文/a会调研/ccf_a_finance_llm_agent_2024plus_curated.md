# 2024--2026 CCF-A 金融论文调研（LLM / Agent 优先）

> 更新：2026-07-13。本文是面向选题与精读的**精选、可复核清单**，不是对所有论文的穷尽式题名匹配；所有题目均链接至会议论文页、出版社 DOI 或 ACL Anthology。完整的宽口径清单可参见同目录的 `ccf_finance_llm_agent_survey_2024_2026.md`。
>
> 会议等级按 [CCF 第六版推荐国际学术会议和期刊目录](https://www.ccf.org.cn/service/pj/2024-03-14/814278.shtml) 的母会口径标注。`ACL Findings`、`ACL Demo`、`KDD ADS` 等属于母会的正式论文轨；它们不是单独的 CCF 分级。仅在 LLM/Agent 方向补入 1 篇 **CCF-B**（NAACL）论文，并明确标出。

## 先看结论

金融 AI 的主干并没有被 LLM 完全替代：股票/组合问题仍大量采用时序模型、图学习、因果学习和强化学习；反欺诈与信用风险则以异构/动态图为主。2024 年以后最值得关注的变化，是 LLM 从“情绪/新闻特征提取器”扩展到以下闭环：

| 技术主线 | 主要解决的金融问题 | 代表论文 |
| --- | --- | --- |
| 领域后训练、提示与数值推理 | 财报/表格问答、金融知识与公式计算 | FinTral、FinDAP、FinMathBench、GBFR |
| 金融 RAG 与长文档 | 10-K/年报检索、证据归因、幻觉控制 | FinTextQA、FinGEAR、FinLFQA、FinMRAGBench |
| 多模态 LLM | 图表、表格、文本和语音的联合理解 | FinMME、FCMR、MultiFinBen |
| LLM Agent / 多 Agent | 投研、交易、因子挖掘、报表和会计工作流 | FinCon、FinAgent、R&D-Agent(Q)、FinRpt、Finch |
| 可信与安全 | 可拒答数值推理、错误检测、越狱和时间泄漏风险 | GBFR、FinED-Bench、FinHarmBench |
| 非 LLM 对照技术 | 股价预测、量化交易、风控、反欺诈 | GNN/超图、Transformer、因果、RL、扩散/GAN |

## A 类核心：LLM / LLM Agent 优先论文

`★` 表示与 LLM、MLLM、RAG 或 LLM Agent 直接相关；`◇` 表示 LLM 是重要模块但不是全系统主体。每一行的“场景”是论文实际解决的任务，不把历史回测等同于实盘收益。

| 时间 | 发表会议 | 题目和链接 | 主要技术 | 创新点 | 论文解决问题的场景 |
| --- | --- | --- | --- | --- | --- |
| 2024 | NeurIPS (A) | ★ [FinBen: A Holistic Financial Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/adb1d9fa8be4576d28703b396b82ba1b-Abstract-Datasets_and_Benchmarks_Track.html) | 金融 LLM 基准；42 数据集、24 任务；RAG/Agent 评测 | 把抽取、QA、风控、预测、交易、双语等任务置于同一基准 | 金融大模型能力评估与选型 |
| 2024 | NeurIPS (A) | ★ [FinCon: A Synthesized LLM Multi-Agent System with Conceptual Verbal Reinforcement for Enhanced Financial Decision Making](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f7ae4fe91d96f50abc2211f09b6a7e49-Abstract-Conference.html) | 分层多 Agent；记忆；反思；语言化强化；风控 | 借鉴投研组织的经理--分析师层级，按需传播反思得到的“投资信念” | 股票交易与组合管理 |
| 2024 | KDD (A) | ★ [A Multimodal Foundation Agent for Financial Trading: Tool-Augmented, Diversified, and Generalist](https://dl.acm.org/doi/10.1145/3637528.3671801) | 多模态 Agent；工具调用；双层反思；多样记忆检索 | 形成“感知--工具--反思--记忆”闭环，同时融合 K 线、文本和数值 | 股票、加密资产的交易决策 |
| 2024 | KDD ADS (A) | ★ [Dólares or Dollars? Unraveling the Bilingual Prowess of Financial LLMs Between Spanish and English](https://dl.acm.org/doi/10.1145/3637528.3671554) | 双语金融 LLM；继续预训练；指令微调；跨语迁移 | 给出英/西语指令数据、FinMA-ES 和跨语金融评测 | 多语言金融文本理解与问答 |
| 2024 | ACL (A) | ★ [FinTextQA: A Dataset for Long-form Financial Question Answering](https://aclanthology.org/2024.acl-long.328/) | RAG；嵌入器、检索器、重排器、生成器；长答案 QA | 提供有来源归因的金融长回答数据，并系统比较 RAG 组件 | 金融教材、监管材料问答 |
| 2024 | ACL (A) | ★ [DocFinQA: A Long-Context Financial Reasoning Dataset](https://aclanthology.org/2024.acl-short.42/) | 长上下文 LLM；检索式 QA | 将 FinQA 的短片段扩展到完整文档（平均约 123k 词），暴露长文档瓶颈 | 长篇财务文档的数字推理 |
| 2024 | ACL (A) | ★ [BizBench: A Quantitative Reasoning Benchmark for Business and Finance](https://aclanthology.org/2024.acl-long.452/) | LLM；程序合成；表格/文本数值推理 | 以 8 类定量推理任务分离“读表、金融知识、代码计算”能力 | 财务报表、商业数据 QA 与计算 |
| 2024 | ACL Findings (A) | ★ [LLMFactor: Extracting Profitable Factors through Prompts for Explainable Stock Movement Prediction](https://aclanthology.org/2024.findings-acl.185/) | LLM 提示；顺序知识引导；新闻与价格文本化 | 让 LLM 从新闻中抽取可解释的影响因子，而非只做情感分类 | 美股/中国股票走势预测 |
| 2024 | ACL Findings (A) | ★ [FinTral: A Family of GPT-4 Level Multimodal Financial Large Language Models](https://aclanthology.org/2024.findings-acl.774/) | 金融 MLLM；领域预训练；指令微调；RLAIF/DPO；工具与检索 | 统一处理文本、数值、表格和图像，并提供 9 任务/25 数据集评测 | 金融文档分析、问答、实时辅助分析 |
| 2024 | EMNLP (A) | ★ [CryptoTrade: A Reflective LLM-based Agent to Guide Zero-shot Cryptocurrency Trading](https://aclanthology.org/2024.emnlp-main.63/) | LLM Agent；链上/链下信息融合；反思机制 | 以过去决策结果反思并更新每日交易决策 | 加密资产零样本交易 |
| 2024 | EMNLP (A) | ★ [FinDVer: Explainable Claim Verification over Long and Hybrid-content Financial Documents](https://aclanthology.org/2024.emnlp-main.818/) | 长文档 LLM；混合内容理解；可解释事实核验 | 4,000 条专家标注样本，要求给出可解释的断言核验 | 财报/金融材料事实核查 |
| 2024 | EMNLP Industry (A) | ★ [Greenback Bears and Fiscal Hawks: Finance is a Jungle and Text Embeddings Must Adapt](https://aclanthology.org/2024.emnlp-industry.26/) | 金融文本嵌入；对比训练；RAG 检索 | 以 14.3M 金融 query-passage 对训练专用 embedding | 财经文档检索与 FinanceBench QA |
| 2024 | IJCAI (A) | ◇ [RisQNet: Measuring and Assessing the Financial Risk of Small and Medium-sized Enterprises with Temporal Graph Neural Networks](https://www.ijcai.org/proceedings/2024/817) | 时序 GNN；风险传播图；GPT-4 报告生成 | 将企业关系网络风险传播与可读风险报告连接 | 中小企业信用风险/违约预警 |
| 2025 | IJCAI (A) | ★ [AI4Contracts: Transforming OTC Contracts into Common Domain Model with Large Language Models](https://www.ijcai.org/proceedings/2025/1034) | LLM；RAG；模板生成；分层检索；Schema 校验 | 自动将非标准 OTC 合同转为 Common Domain Model，强调结构约束 | 场外衍生品合同标准化与运营 |
| 2025 | KDD (A) | ★ [CAMEF: Causal-Augmented Multi-Modality Event-Driven Financial Forecasting](https://dl.acm.org/doi/10.1145/3711896.3736872) | 因果学习；文本/时序多模态；LLM 反事实事件增强 | 从宏观公告与价格中建模因果关系，并用 LLM 造反事实事件缓解样本稀缺 | 宏观公告驱动的资产价格预测 |
| 2025 | ACL (A) | ★ [FinMME: Benchmark Dataset for Financial Multi-Modal Reasoning Evaluation](https://aclanthology.org/2025.acl-long.1426/) | MLLM；图表理解；幻觉惩罚式评测 | 11,000+ 样本覆盖 18 个金融领域、6 类资产、10 大图表类型 | 投研图表/报告多模态推理评测 |
| 2025 | ACL (A) | ★ [FCMR: Robust Evaluation of Financial Cross-Modal Multi-Hop Reasoning](https://aclanthology.org/2025.acl-long.1138/) | MLLM；文本-表格-图表三跳推理 | 构造必须同时使用多种模态的困难样例，并定位检索阶段瓶颈 | 财务报告跨模态多跳问答 |
| 2025 | EMNLP Findings (A) | ★ [FinGEAR: Financial Mapping-Guided Enhanced Answer Retrieval](https://aclanthology.org/2025.findings-emnlp.382/) | 金融 RAG；披露层级索引；词典引导；cross-encoder 重排 | 以 10-K 的 Item 层级和金融术语约束检索，而不是扁平向量检索 | 10-K/FinQA 证据检索与问答 |
| 2025 | EMNLP Findings (A) | ★ [FinLFQA: Evaluating Attributed Text Generation of LLMs in Financial Long-Form Question Answering](https://aclanthology.org/2025.findings-emnlp.908/) | 长答案 LLM；归因评测；数值推理链 | 把“支持证据、中间计算、领域知识”分开评价，衡量可核查性 | 金融长答案生成与事实归因 |
| 2025 | EMNLP (A) | ★ [Demystifying Domain-adaptive Post-training for Financial LLMs](https://aclanthology.org/2025.emnlp-main.1579/) | 领域后训练；继续预训练；指令微调；偏好数据蒸馏 | FinCap/FinRec/FinTrain/FinEval 给出金融 LLM 后训练的可复用配方 | 训练/适配金融领域 LLM |
| 2025 | EMNLP Findings (A) | ★ [Automate Strategy Finding with LLM in Quant Investment](https://aclanthology.org/2025.findings-emnlp.1005/) | LLM；风险感知多 Agent；因子生成；动态权重优化 | 让 Agent 生成可执行因子、在多模态市场状态下筛选并组合 | 自动化 Alpha 发现与量化组合 |
| 2025 | EMNLP Findings (A) | ★ [Large Language Model Agents in Finance: A Survey Bridging Research, Practice, and Real-World Deployment](https://aclanthology.org/2025.findings-emnlp.972/) | Agent 综述；任务/基准/部署 taxonomy | 以实践与研究双视角归纳数据、投研、交易、资管、风控五类场景 | 选题地图与部署约束梳理 |
| 2025 | NeurIPS (A) | ★ [R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ac5c2b6e423883cbcacbcccf88491b78-Abstract-Datasets_and_Benchmarks_Track.html) | 多 Agent；代码生成；回测反馈；多臂老虎机调度 | 将研究假设、因子挖掘、模型研发和回测反馈组成共同优化循环 | 自动化量化研发与因子-模型协同 |
| 2025 | NAACL (B，补充) | ★ [FinEval: A Chinese Financial Domain Knowledge Evaluation Benchmark for Large Language Models](https://aclanthology.org/2025.naacl-long.318/) | 中文金融 LLM 基准；知识与实务 Agent 评测 | 纳入金融知识、股票、公司分析、金融 Agent 等中文任务 | 中文金融大模型能力评估 |
| 2026 | AAAI (A) | ★ [FinRpt: Dataset, Evaluation System and LLM-based Multi-agent Framework for Equity Research Report Generation](https://ojs.aaai.org/index.php/AAAI/article/view/37014) | LLM 多 Agent；数据集；报告评价 | 用分工 Agent 生成并评估多源信息驱动的投研报告 | Equity research 报告生成 |
| 2026 | AAAI (A) | ★ [Navigating the Alpha Jungle: An LLM-Powered MCTS Framework for Formulaic Alpha Factor Mining](https://ojs.aaai.org/index.php/AAAI/article/view/37069) | LLM；MCTS；公式化 Alpha；回测反馈 | 由量化反馈引导 MCTS 探索并去重，迭代生成可解释因子公式 | Alpha 因子挖掘与组合研究 |
| 2026 | AAAI (A) | ★ [FinMathBench: A Formula-Driven Benchmark for Evaluating LLMs’ Math Reasoning Capabilities in Finance](https://ojs.aaai.org/index.php/AAAI/article/view/40358) | LLM；金融公式库；Mask-for-Solve；DAG 难度控制 | 用公式依赖图自动构造单/多公式题，诊断复杂计算能力 | 财务指标计算、分析师数字问答 |
| 2026 | AAAI (A) | ★ [Interpreting Fedspeak with Confidence: A LLM-Based Uncertainty-Aware Framework Guided by Monetary Policy Transmission Paths](https://ojs.aaai.org/index.php/AAAI/article/view/40739) | LLM；政策传导路径；不确定性解码 | 把宏观经济传导机制编码进推理，并预测模型置信度 | 美联储表态/货币政策立场分析 |
| 2026 | ACL Demo (A) | ★ [QFinZero: A Unified Financial Toolchain for LLM-Based Trading Agents](https://aclanthology.org/2026.acl-demo.7/) | Agent 工具链；市场/衍生品数据；新闻检索；券商仿真 | 统一数据、事件与订单生命周期接口，降低交易 Agent 的不可复现性 | 带工具调用的量化交易 Agent |
| 2026 | ACL (A) | ★ [MultiFinBen: Benchmarking Large Language Models for Multilingual and Multimodal Financial Application](https://aclanthology.org/2026.acl-long.770/) | 多语 MLLM；OCR；文本/视觉/语音评测 | 首个专家标注的五语种、文本-视觉-语音金融基准 | 跨国金融文档、扫描件和会议音频理解 |
| 2026 | ACL (A) | ★ [FinKario: Event-Enhanced Automated Construction of Financial Knowledge Graph](https://aclanthology.org/2026.acl-long.446/) | LLM；事件增强知识图谱；投研报告信息抽取 | 用事件驱动方式维护大规模金融 KG，减少静态知识库滞后 | 投研报告检索、公司关系与事件分析 |
| 2026 | ACL (A) | ★ [Achieving Multi-Hop Calculation and Safe Abstention in Financial Numerical Reasoning by Metric Graph Constrained LLMs](https://aclanthology.org/2026.acl-long.1273/) | 神经符号 LLM；指标知识图；图约束算子；安全拒答 | 限制推理只能沿可验证指标图进行，并区分“缺数据”与“检索失败” | 财务指标多跳计算与可靠问答 |
| 2026 | ACL Industry (A) | ★ [FinHarmBench: Financial Jailbreak Benchmark and Unsupervised Safety Fine-Tuning via Refusal Steering Distillation](https://aclanthology.org/2026.acl-industry.117/) | 金融越狱基准；拒答方向蒸馏；安全对齐 | 同时测试有害金融建议与易混淆良性请求，并在表示层蒸馏拒答能力 | 金融建议安全、合规与越狱防护 |
| 2026 | ACL Findings (A) | ★ [Finch: Benchmarking Finance & Accounting across Spreadsheet-Centric Enterprise Workflows](https://aclanthology.org/2026.findings-acl.523/) | 企业 Agent；表格/邮件/PDF；跨文件检索；工作流评测 | 从真实企业工作区构造长程多步骤会计/财务流程，而非单轮问答 | 预算、交易、资管、财务运营与会计 |
| 2026 | ACL Findings (A) | ★ [FinMRAGBench: A Realistic and Complex Benchmark for Multi-Modal RAG in Financial Document Analysis](https://aclanthology.org/2026.findings-acl.187/) | 多模态 RAG；跨页/跨文档检索；Agent 规划 | 用真实复杂财务材料评价检索、工具规划和答案生成的端到端协作 | 年报/财报的跨页跨文档分析 |
| 2026 | ACL Findings (A) | ★ [Are Large Language Models Reliable Reviewers? A Benchmark for Error Detection in Financial Documents](https://aclanthology.org/2026.findings-acl.1481/) | 金融错误检测基准；LLM；监督微调 | 覆盖 9 类真实情境、3 个认知难度，直接测“发现错误”而非只测问答 | 财务文档审阅、合规与质量控制 |
| 2026 | ACL (A) | ★ [KG-MuLQA: A Framework for KG-based Multi-Level QA Extraction and Long-Context LLM Evaluation](https://aclanthology.org/2026.acl-long.151/) | 知识图谱；长上下文 LLM；多层 QA 抽取 | 基于金融信贷协议构造 20,139 个可控难度 QA，测集合比较与多跳检索 | 信贷合同的长文档分析 |

## A 类核心：非 LLM 技术对照（代表性）

这些论文用于建立金融任务本身的技术基线；如果后续做 LLM/Agent，通常应与相应的时序、图学习、RL 或生成模型进行比较，而不是只与通用 LLM 比。

| 时间 | 发表会议 | 题目和链接 | 主要技术 | 创新点 | 论文解决问题的场景 |
| --- | --- | --- | --- | --- | --- |
| 2024 | AAAI (A) | [Market-GAN: Adding Control to Financial Market Data Generation with Semantic Context](https://ojs.aaai.org/index.php/AAAI/article/view/29531) | 条件 GAN；自编码器；市场状态聚类 | 以市场语义状态控制生成，并保持市场动态一致性 | 市场序列生成、压力测试、数据增强 |
| 2024 | AAAI (A) | [CI-STHPAN: A Channel-Independent Spatio-Temporal Hypergraph Pre-trained Attention Network for Stock Selection](https://ojs.aaai.org/index.php/AAAI/article/view/28770) | Transformer；超图；自监督预训练；排序学习 | 分别编码通道时序与时变股票关系 | NASDAQ/NYSE 选股 |
| 2024 | AAAI (A) | [StockMixer: A Simple yet Strong MLP-Based Architecture for Stock Price Forecasting](https://ojs.aaai.org/index.php/AAAI/article/view/28681) | MLP-Mixer；多尺度 patch；时间/股票交互 | 不依赖注意力，显式混合指标、时间和股票维度 | 多股票价格/走势预测 |
| 2024 | AAAI (A) | [ECHO-GL: Earnings Call-based Hierarchical Graph Learning for Stock Movement Prediction](https://ojs.aaai.org/index.php/AAAI/article/view/29305) | 电话会文本；分层图学习 | 将跨公司的电话会语义关系纳入股票图 | 财报期股价方向预测 |
| 2024 | AAAI (A) | [EarnHFT: Efficient Hierarchical Reinforcement Learning for High Frequency Trading](https://ojs.aaai.org/index.php/AAAI/article/view/29384) | 分层 RL；专家策略池；路由 | 按市场状态选择合适的交易子策略 | 加密资产高频交易 |
| 2024 | IJCAI (A) | [MacMic: Market Macro-Micro Hierarchical Reinforcement Learning for Iceberg Order Execution](https://www.ijcai.org/proceedings/2024/664) | 分层 RL；因果堆叠 HMM | 将宏观市场状态与订单簿微观状态联合决策 | 冰山单/大单执行 |
| 2024 | IJCAI (A) | [Fraud Risk Mitigation in Real-Time Payments: A Strategic Agent-Based Analysis](https://www.ijcai.org/proceedings/2024/18) | Agent 仿真；博弈论；策略优化 | 从参与方与欺诈者的策略互动而非静态分类建模风险 | 实时支付反欺诈 |
| 2024 | KDD (A) | [FreQuant: A Reinforcement-Learning based Adaptive Portfolio Optimization with Multi-frequency Decomposition](https://dl.acm.org/doi/10.1145/3637528.3671668) | 深度 RL；傅里叶多频分解；组合优化 | 在频域学习市场状态以适应突发变化 | 股票组合优化 |
| 2024 | KDD (A) | [MacroHFT: Memory Augmented Context-aware Reinforcement Learning On High Frequency Trading](https://dl.acm.org/doi/10.1145/3637528.3672064) | 多专家 RL；记忆；市场状态分解 | 通过专家池和上下文适配覆盖不同加密市场状态 | 加密资产高频交易 |
| 2024 | KDD ADS (A) | [CompanyKG: A Large-Scale Heterogeneous Knowledge Graph for Company Intelligence](https://dl.acm.org/doi/10.1145/3637528.3671515) | 异构知识图谱；文本嵌入；实体对齐 | 构建公司、人物、事件之间的大规模企业情报图 | 竞品发现、私募市场映射、并购线索 |
| 2024 | WWW (A) | [Reinforcement Learning with Maskable Stock Representation for Portfolio Management in Customizable Stock Pools](https://dl.acm.org/doi/10.1145/3589334.3645615) | RL；掩码股票表征；自监督重构 | 一次训练支持动态变化的股票池 | 可定制股票池的组合管理 |
| 2025 | AAAI (A) | [FactorGCL: Hypergraph Factor Modeling with Temporal Residual Contrastive Learning for Stock Return Prediction](https://ojs.aaai.org/index.php/AAAI/article/view/31993) | 超图因子模型；时间残差对比学习 | 从残差中学习隐含影响因子及其关系 | 股票收益率预测 |
| 2025 | AAAI (A) | [DHMoE: Diffusion-based Hierarchical Mixture of Experts for Stock Prediction](https://ojs.aaai.org/index.php/AAAI/article/view/33250) | 扩散模型；层次 MoE；Transformer | 生成式专家层级适配非平稳的多模态市场 | 股票预测与投资组合 |
| 2025 | AAAI (A) | [AlphaForge: A Generative-Predictive Framework for Formulaic Alpha Mining](https://ojs.aaai.org/index.php/AAAI/article/view/33365) | 生成-预测网络；时序因子选择 | 同时生成、筛选、组合可解释 Alpha 公式 | 量化因子挖掘 |
| 2025 | IJCAI (A) | [AlphaGAT: Cross-Asset Graph Attention and Factor Modeling for Portfolio Selection](https://www.ijcai.org/proceedings/2025/834) | TimeMixer；跨资产 GAT；因子建模；RL | 联合建模因子时序、资产关系和策略选择 | 股票组合选择 |
| 2025 | KDD ADS (A) | [Efficient Multi-Expert Tabular Language Model for Banking](https://dl.acm.org/doi/10.1145/3690624.3709400) | 表格语言模型；MoE；稀疏微调 | 为银行表格数据设计高效专家路由与训练策略 | 银行风险、信息和利润评估 |
| 2025 | KDD ADS (A) | [TEMPER: Capturing Consistent and Fluctuating TEMPoral User Behaviour for EtheReum Phishing Scam Detection](https://www.kdd.org/kdd2025/applied-data-science-ads-track-papers-2/) | 时序行为表征；一致/波动行为分解 | 同时利用长期行为画像与短期异常波动 | 以太坊钓鱼诈骗检测 |

## 推荐阅读：按你的 LLM / LLM Agent 兴趣排序

| 优先级 | 论文 | 推荐理由与阅读重点 |
| --- | --- | --- |
| 1 | [FinBen](https://proceedings.neurips.cc/paper_files/paper/2024/hash/adb1d9fa8be4576d28703b396b82ba1b-Abstract-Datasets_and_Benchmarks_Track.html) | 先建立任务地图。重点看其任务划分、时间切分和 Agent/RAG 评测协议；这是避免“只挑一个容易任务”的起点。 |
| 2 | [FinCon](https://proceedings.neurips.cc/paper_files/paper/2024/hash/f7ae4fe91d96f50abc2211f09b6a7e49-Abstract-Conference.html) | 金融多 Agent 的架构代表。重点看层级通信、记忆更新与风险控制怎样进入决策闭环。 |
| 3 | [FinAgent](https://dl.acm.org/doi/10.1145/3637528.3671801) | 最贴近“能动手复现的交易 Agent”。重点看工具调用、双层反思、数据模态对齐和回测假设。 |
| 4 | [FinGEAR](https://aclanthology.org/2025.findings-emnlp.382/) | 强烈建议把它作为金融 RAG 入口：披露目录层级、领域术语和重排比单纯换 LLM 更像真实问题。 |
| 5 | [FinMME](https://aclanthology.org/2025.acl-long.1426/) + [FCMR](https://aclanthology.org/2025.acl-long.1138/) | 若偏多模态投研，这一对先定义“图表/表格/文本联合推理”该如何测，再决定模型。 |
| 6 | [Demystifying Domain-adaptive Post-training for Financial LLMs](https://aclanthology.org/2025.emnlp-main.1579/) | 适合想做金融 LLM 本体或小模型适配。重点看继续预训练、指令训练、偏好数据各自带来的能力变化。 |
| 7 | [R&D-Agent-Quant](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ac5c2b6e423883cbcacbcccf88491b78-Abstract-Datasets_and_Benchmarks_Track.html) | 面向“Agent 自动做量化研究”的近期代表。重点审阅代码生成、真实回测、反馈选择和数据泄漏防护。 |
| 8 | [FinRpt](https://ojs.aaai.org/index.php/AAAI/article/view/37014) | 如果不想被交易回测束缚，投研报告生成提供更可评估、更接近工作流的多 Agent 课题。 |
| 9 | [GBFR](https://aclanthology.org/2026.acl-long.1273/) + [FinMathBench](https://ojs.aaai.org/index.php/AAAI/article/view/40358) | 很适合做可靠性选题：图约束计算、安全弃答、公式依赖评测都可形成清晰的消融实验。 |
| 10 | [Finch](https://aclanthology.org/2026.findings-acl.523/) + [QFinZero](https://aclanthology.org/2026.acl-demo.7/) | 面向落地型 Agent：前者定义会计/财务工作流评测，后者解决交易 Agent 的工具接口和复现环境。 |
| 11 | [FinHarmBench](https://aclanthology.org/2026.acl-industry.117/) | 所有涉及投资建议、风控解释或自动执行的 Agent 都应补读；“有用”不能代替“安全”。 |

### 建议的最短阅读链

`FinBen → FinCon → FinAgent → FinGEAR → FinMME/FCMR → R&D-Agent-Quant → GBFR/FinHarmBench`。

对应三个相对可做的选题切口：

1. **证据可追溯的金融 RAG**：以 FinGEAR/FinLFQA 为基线，研究长年报中“检索正确但计算错误”或“答案正确但归因错误”的分离评测。
2. **受约束的量化研究 Agent**：以 R&D-Agent(Q)/FinAgent 为起点，在时间切分、交易成本、工具白名单、代码/回测审计轨迹上加强，而不是只比较累计收益。
3. **多模态财报可靠推理**：以 FinMME/FCMR 为评测，以 GBFR 的安全弃答思想约束图表/表格多跳计算。

## 使用时的三个核查点

- **时间安全**：新闻、公告、价格和标签必须按可获得时刻切分；回测须纳入交易成本、滑点、退市股票处理，避免未来信息泄漏。
- **证据安全**：金融问答/报告需要保存来源片段、计算过程和版本时间；不要只用 LLM-as-judge 判断正确性。
- **执行安全**：将 Agent 的“建议、模拟、下单”分级；真实交易工具应有权限、额度、人工确认与可审计日志。本文不构成投资建议。
