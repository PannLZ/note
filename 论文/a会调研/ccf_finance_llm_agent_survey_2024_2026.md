# 2024--2026 CCF-A 会议中的金融相关论文调研

> 更新日期：2026-07-13；检索截止：2026-07-13。  
> 本版将 **LLM/Agent 从纳入条件改为兴趣标签**：所有题目均因其研究对象、数据或应用任务直接涉及金融/会计/银行/证券/投资/支付/保险/金融欺诈/加密资产而纳入；`★` 表示和 LLM 或 LLM Agent 直接相关，便于优先阅读。  
> 会议口径：CCF 第六版目录中的 A 类会议，优先系统检索最常发表计算金融研究的 AAAI、IJCAI、KDD、NeurIPS、ACL、WWW（及其正式 Findings / ADS / IAAI / Industry 等论文轨）。不把 CCF-B 会议混入主表。会议的 CCF 等级以 [CCF 第六版目录](https://www.ccf.org.cn/service/pj/2024-03-14/814278.shtml) 为准；track 沿用母会议等级，但不把 track 误作单独的 CCF 评级。

## 使用说明与边界

- **“金融相关”判定**：题目、摘要、数据集或实验任务明确面向股票/组合/交易、金融文本与报表、信贷与贷款、支付/保险/金融交易欺诈、监管、加密资产或金融基础模型。仅在引言里举“金融”例子、但没有金融任务/数据的通用方法不收录。
- **“尽可能全量”**：按上述可复核判定，对 2024 至截止日已公开的目标 A 会论文页、ACM/ACL/AAAI/IJCAI/NeurIPS 官方论文页逐项检索而得。它不是对全部 CCF 学科、所有附件/海报/工作坊的机械题名匹配；若后续发现同一口径下的正式论文，可直接按本表字段追加。
- **技术列**列出论文实际组合的主要技术，而不是只写最热门的一项；例如 LLM + RAG + 时序预测会全部并列。
- **场景**是细粒度的研究问题；**结果/产出**是用户要求新增的粗粒度列，描述最终希望提升或交付的业务/科研产出，而非保证真实投资收益。论文中的回测收益不构成投资建议。
- 为避免主表过宽，逐篇的**实验数据集/落地环境**及**论文报告的提升指标**集中列在后文“实验数据集/落地环境与论文报告提升”索引；该索引与主表共 61 篇论文一一对应。

### 标记

| 标记 | 含义 |
| --- | --- |
| `★ LLM/Agent` | 论文核心使用 LLM、MLLM、RAG 或 LLM Agent；本次兴趣方向 |
| `—` | 非 LLM/Agent 的金融计算论文，仍是主清单的重要组成 |

## 论文主表

### 2024

| 时间 | 会议（CCF-A） | 兴趣 | 题目和链接 | 涉及技术（全部主要技术） | 创新点 | 细粒度问题/应用场景 | 结果/产出（粗粒度） |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2024 | AAAI | — | [Market-GAN: Adding Control to Financial Market Data Generation with Semantic Context](https://ojs.aaai.org/index.php/AAAI/article/view/29531) | 条件 GAN + 自编码器 + 市场动态聚类 + 线性回归监督器 + 时间序列生成 | 用“市场语义状态”控制生成，并以双阶段机制保持动态一致性 | 受控金融市场序列/情景生成 | 生成更逼真的可控市场数据，服务数据增强、压力测试和仿真 |
| 2024 | AAAI | — | [CI-STHPAN: A Channel-Independent Spatio-Temporal Hypergraph Pre-trained Attention Network for Stock Selection](https://ojs.aaai.org/index.php/AAAI/article/view/28770) | Transformer + 超图注意力网络 + 动态时间规整 + 自监督预训练 + 排序学习 | 以通道独立时序编码和时变股票超图共同建模关联 | NASDAQ/NYSE 股票选择 | 提升选股质量、组合收益与夏普比率 |
| 2024 | AAAI | — | [StockMixer: A Simple yet Strong MLP-Based Architecture for Stock Price Forecasting](https://ojs.aaai.org/index.php/AAAI/article/view/28681) | MLP + 多尺度 patch + 指标混合 + 时间混合 + 股票交互混合 | 不依赖注意力，以三类 Mixer 显式分离技术指标、时间和股票关系 | 多股票价格/走势预测 | 提升预测精度，同时降低模型内存与运行开销 |
| 2024 | AAAI | — | [MDGNN: A Multi-Relation Discrete Graph Neural Network for Stock Investment](https://ojs.aaai.org/index.php/AAAI/article/view/29381) | 离散动态图神经网络 + 多关系图 + Transformer 时序编码 | 把连续股票关系离散化为可演化的多关系图 | 股票涨跌预测与投资决策 | 提升投资信号与组合表现 |
| 2024 | AAAI | — | [ECHO-GL: Earnings Call-based Hierarchical Graph Learning for Stock Movement Prediction](https://ojs.aaai.org/index.php/AAAI/article/view/29305) | 财报电话会议文本语义 + 异构/分层图学习 + 随机过程建模 | 将业绩电话会中的跨公司语义联系纳入股票图 | 财报期股票方向预测与交易 | 改善走势预测并提高交易组合盈利性 |
| 2024 | AAAI | — | [EarnHFT: Efficient Hierarchical Reinforcement Learning for High Frequency Trading](https://ojs.aaai.org/index.php/AAAI/article/view/29384) | 分层强化学习 + 动态规划 + Q 学习教师 + 专家/子智能体池 + 路由 | 三阶段训练使路由策略在不同市场状态调用合适的交易子策略 | 加密资产高频交易 | 提升高频交易的累计收益和稳健性 |
| 2024 | AAAI | — | [Revisiting Graph-Based Fraud Detection in the Era of Graph Neural Networks](https://ojs.aaai.org/index.php/AAAI/article/view/28773) | 半监督 GNN + 混合频率谱滤波 + 局部环境约束 | 以频域滤波缓解欺诈图中的异配性与噪声 | 金融交易/平台欺诈图检测 | 提升少数欺诈节点识别能力 |
| 2024 | AAAI | — | [DGA-GNN: Dynamic Group Aggregation Graph Neural Network for Fraud Detection](https://ojs.aaai.org/index.php/AAAI/article/view/29067) | GNN + 决策树分箱 + 动态分组 + 分层聚合 + 反馈更新 | 先按特征分布动态分群，再进行组内/组间信息聚合 | 金融交易与账户欺诈识别 | 提升欺诈识别的准确性与鲁棒性 |
| 2024 | AAAI | — | [Barely Supervised Learning for Graph-Based Fraud Detection](https://ojs.aaai.org/index.php/AAAI/article/view/29593) | 图表示学习 + 边信息解耦 + 弱/强数据增强 + 一致性正则化 | 针对极少标签的欺诈图，分离“有用边”与噪声边 | 标注稀缺的金融/交易欺诈检测 | 以极少人工标签维持较高欺诈检测效果 |
| 2024 | AAAI | — | [Pre-trained Online Contrastive Learning for Insurance Fraud Detection](https://ojs.aaai.org/index.php/AAAI/article/view/30259) | 对比预训练 + 在线/持续学习 + 时间记忆突触 | 在概念漂移下持续更新保险反欺诈模型 | 医疗保险欺诈识别 | 提升实时识别准确率并降低训练耗时 |
| 2024 | AAAI | — | [Provably Powerful Graph Neural Networks for Directed Multigraphs](https://ojs.aaai.org/index.php/AAAI/article/view/29069) | 有向多重图 GNN + 图同构表达力理论 + 消息传递 | 为有向多关系图给出更强表达力及理论保证 | 资金流/洗钱、金融犯罪与钓鱼账户识别 | 改善金融犯罪少数类的 F1 等检测指标 |
| 2024 | AAAI（IAAI） | — | [Accountable Loan Approval](https://ojs.aaai.org/index.php/AAAI/article/view/30310) | 规则系统 + 次模优化 + 可解释机器学习 + 生产部署 | 将可审计规则与优化结合，兼顾批贷效率、坏账率和可解释性 | 贷款审批/信用风险管理 | 在目标坏账约束下扩大贷款服务规模 |
| 2024 | IJCAI | `★ LLM/Agent` | [RisQNet: Measuring and Assessing the Financial Risk of Small and Medium-sized Enterprises with Temporal Graph Neural Networks](https://www.ijcai.org/proceedings/2024/817) | 时序 GNN + 风险传播图 + GPT-4 提示生成新闻报告 + 结构化风险特征 | 将企业关系网中的风险传播与 LLM 可读风险解释结合 | 中小企业信用风险/违约预警 | 提升风险识别 AUC，并产出可读的风险报告 |
| 2024 | IJCAI | — | [ADB-TRM: Adversarial Debiasing Temporal Relational Model for Stock Investment Recommendation](https://www.ijcai.org/proceedings/2024/221) | 时序关系模型 + 元学习 + 对抗样本生成 + 全局—局部交互 | 以元学习生成的对抗扰动削弱投资推荐中的偏差 | 股票投资推荐 | 提升累计收益与风险调整后收益 |
| 2024 | IJCAI | — | [IMM: Imitative Market Making](https://www.ijcai.org/proceedings/2024/663) | 模仿学习 + 强化学习 + 预测式表征学习 | 用历史做市行为构造可学习的市场做市策略 | 自动做市 | 改善做市策略学习和交易收益表现 |
| 2024 | IJCAI | — | [MacMic: Market Macro-Micro Hierarchical Reinforcement Learning for Iceberg Order Execution](https://www.ijcai.org/proceedings/2024/664) | 分层强化学习 + 因果堆叠 HMM + 宏观/微观状态建模 | 将市场宏观状态与微观订单簿状态分层用于冰山单执行 | 大单/冰山订单执行 | 降低执行成本、提升执行质量 |
| 2024 | IJCAI | — | [Trade When Opportunity Comes: Locality-Aware Representation Learning for Trading Signal Discovery](https://www.ijcai.org/proceedings/2024/678) | 局部感知注意力 + 度量学习 + 迭代式标签精炼 + 时序表示学习 | 从弱监督价格序列挖掘可复用的局部交易机会 | 股票、加密货币、ETF 的交易信号发现 | 提升可交易信号的可靠性和收益潜力 |
| 2024 | IJCAI | — | [Fraud Risk Mitigation in Real-Time Payments: A Strategic Agent-Based Analysis](https://www.ijcai.org/proceedings/2024/18) | 基于智能体仿真 + 博弈论 + 经验博弈分析 + 策略优化 | 建模支付参与方与欺诈者的策略互动，而非只做静态分类 | 实时支付欺诈风险控制 | 为银行/支付机构提供更优的风险干预策略 |
| 2024 | KDD | — | [FreQuant: A Reinforcement-Learning based Adaptive Portfolio Optimization with Multi-frequency Decomposition](https://dl.acm.org/doi/10.1145/3637528.3671668) | 深度强化学习 + 离散傅里叶变换 + 多频分解 + 投资组合优化 | 在频域而非纯时域学习市场状态以适应突发变动 | 股票组合优化/量化投资 | 提升年化收益、组合价值和市场变化下的稳定性 |
| 2024 | KDD | — | [MacroHFT: Memory Augmented Context-aware Reinforcement Learning On High Frequency Trading](https://dl.acm.org/doi/10.1145/3637528.3672064) | 多智能体/专家强化学习 + 条件适配器 + 记忆机制 + 市场趋势/波动分解 | 以子策略池和超智能体组合应对多种加密市场状态 | 分钟级加密资产高频交易 | 提升收益及夏普/卡玛等风险调整收益 |
| 2024 | KDD | `★ LLM/Agent` | [FinAgent: A Multimodal Foundation Agent for Financial Trading: Tool-Augmented, Diversified, and Generalist](https://dl.acm.org/doi/10.1145/3637528.3671801) | 多模态 LLM Agent + 工具调用 + 双层反思 + 多样记忆检索 + K 线/文本/数值融合 | 将“感知—工具—反思—记忆”闭环用于跨市场交易 | 股票与加密资产交易决策 | 提升交易盈利性与跨资产泛化能力 |
| 2024 | KDD（ADS） | — | [CompanyKG: A Large-Scale Heterogeneous Knowledge Graph for Company Intelligence](https://dl.acm.org/doi/10.1145/3637528.3671515) | 异构知识图谱 + 文本嵌入 + 图表示学习 + 实体/关系对齐 | 构建覆盖公司、人物、事件等的大规模企业情报图谱 | 私募市场映射、竞品发现、并购线索 | 提供企业情报基础设施，改善相似公司/关系检索 |
| 2024 | KDD（ADS） | — | [On Finding Bi-objective Pareto-optimal Fraud Prevention Rule Sets for Fintech Applications](https://dl.acm.org/doi/10.1145/3637528.3671521) | 多目标优化 + Pareto 前沿 + 可解释规则学习 | 同时优化拦截欺诈与业务/人工成本，输出规则集而非黑箱分数 | 金融科技反欺诈规则配置 | 找到可部署的风险—成本折中方案 |
| 2024 | KDD（ADS） | `★ LLM/Agent` | [Dólares or Dollars? Unraveling the Bilingual Prowess of Financial LLMs Between Spanish and English](https://dl.acm.org/doi/10.1145/3637528.3671554) | 金融 LLM + 双语继续预训练/指令微调 + 跨语言迁移 + 金融 NLP 评测 | 对比并改善英/西语金融知识和任务迁移 | 英语—西班牙语金融文本理解 | 提升非英语金融 NLP 的可用性 |
| 2024 | ACL | `★ LLM/Agent` | [BizBench: A Quantitative Reasoning Benchmark for Business and Finance](https://aclanthology.org/2024.acl-long.452/) | LLM + 程序合成 + 表格/文本数值推理 + 基准评测 | 用真实商业、财务材料检验 LLM 的定量推理而非纯文本问答 | 财务报表、商业数据的问答与计算 | 衡量并暴露金融数值推理能力缺口 |
| 2024 | ACL（Findings） | `★ LLM/Agent` | [FinTral: A Financial Large Language Model with Retrieval-Augmented Instruction Tuning](https://aclanthology.org/2024.findings-acl.774/) | 金融 Mistral LLM + 领域继续预训练 + 指令微调 + RLAIF + DPO + RAG/工具 | 把金融领域训练、偏好优化和检索工具统一到开源模型 | 金融文档分析、问答和推理 | 提升金融语言任务与工具使用能力 |
| 2024 | NeurIPS（Datasets & Benchmarks） | `★ LLM/Agent` | [FinBen: A Holistic Financial Benchmark for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/adb1d9fa8be4576d28703b396b82ba1b-Abstract-Datasets_and_Benchmarks_Track.html) | 金融 LLM 基准 + 42 数据集/24 任务 + RAG 评测 + Agent 交易评测 | 将信息抽取、文本、风控、预测、交易等金融任务置于统一评测 | 金融 LLM 全面能力评估 | 建立金融大模型比较基线，定位复杂推理/预测短板 |
| 2024 | WWW | — | [Reinforcement Learning with Maskable Stock Representation for Portfolio Management in Customizable Stock Pools](https://dl.acm.org/doi/10.1145/3589334.3645615) | 强化学习 + 掩码股票表示 + 自监督掩码重构 + 投资组合重加权 | 一次训练覆盖可动态变更的股票池，避免频繁重训 | 自定义股票池的组合管理 | 在不同股票池上提升组合收益（论文报告超过 40% 利润改进） |

### 2025

| 时间 | 会议（CCF-A） | 兴趣 | 题目和链接 | 涉及技术（全部主要技术） | 创新点 | 细粒度问题/应用场景 | 结果/产出（粗粒度） |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2025 | AAAI | — | [FactorGCL: Hypergraph Factor Modeling with Temporal Residual Contrastive Learning for Stock Return Prediction](https://ojs.aaai.org/index.php/AAAI/article/view/31993) | 超图因子模型 + 时间残差对比学习 + 级联残差超图 | 以时间残差对比目标学习隐藏影响因子及其关系 | 股票收益率预测 | 提升收益预测与因子表征质量 |
| 2025 | AAAI | — | [DHMoE: Diffusion-based Hierarchical Mixture of Experts for Stock Prediction](https://ojs.aaai.org/index.php/AAAI/article/view/33250) | 扩散模型 + 层次混合专家 + Inverted Transformer + 多模态条件输入 + 教师—学生决策 | 用扩散生成的专家层级来适配市场的多模态、非平稳状态 | 股票预测与投资组合 | 提升累计收益和风险调整后收益 |
| 2025 | AAAI | — | [AlphaForge: A Generative-Predictive Framework for Formulaic Alpha Mining](https://ojs.aaai.org/index.php/AAAI/article/view/33365) | 生成—预测神经网络 + 时间因子选择 + 动态权重学习 + 公式 Alpha 挖掘 | 同时产生、筛选并组合可解释的量化因子公式 | 量化因子挖掘/组合构建 | 提升因子有效性与组合收益 |
| 2025 | AAAI | `★ LLM/Agent` | [Linking Industry Sectors and Financial Statements Through Artificial Intelligence](https://ojs.aaai.org/index.php/AAAI/article/view/33806) | 机器学习 + 语言模型 + 财报数值表示 + 决策树/可解释分类 | 连接行业分类与财务报表结构，提供可解释推断 | 财报分析、审计和行业识别 | 改进财报/行业匹配与可解释分析 |
| 2025 | AAAI | — | [Unveiling Threat Fraud Gangs with Multi-Target Graph Injection Attacks](https://ojs.aaai.org/index.php/AAAI/article/view/33760) | 图注入攻击 + Transformer + 多目标优化 + 对抗鲁棒性评测 | 系统刻画欺诈团伙针对图反欺诈系统的多节点注入攻击 | 保险/交易欺诈图安全 | 评估并暴露反欺诈系统的安全风险 |
| 2025 | AAAI | — | [Context-aware Graph Neural Network for Fraud Detection with Label Scarcity](https://ojs.aaai.org/index.php/AAAI/article/view/33319) | GNN + 类别语义分解 + 去噪注意力 + 特征增强 + 熵/一致性正则 | 用上下文和一致性约束缓解少标签、噪声关系问题 | 金融账户/交易欺诈检测 | 提升低标注条件下的欺诈检测表现 |
| 2025 | AAAI | — | [Dynamic Neighborhood Modeling for Graph-based Fraud Detection](https://ojs.aaai.org/index.php/AAAI/article/view/33431) | 异常分数 + 节点—子图对比学习 + 动态邻域建模 + GNN | 把邻域随时间和风险变化的过程纳入图反欺诈表示 | 交易/账户欺诈检测 | 提升复杂关系网络中的欺诈识别效果 |
| 2025 | AAAI | — | [Label-free Heterophily Guided Learning for Graph-based Fraud Detection](https://ojs.aaai.org/index.php/AAAI/article/view/33356) | 异配性度量 + MLP/GNN + 排序学习 + 非对称对齐 | 在无标签场景用异配性结构学习欺诈排序 | 无标签金融交易欺诈检测 | 降低标注依赖并改善欺诈节点排序 |
| 2025 | IJCAI | `★ LLM/Agent` | [AI4Contracts: Transforming OTC Contracts into Common Domain Model with Large Language Models](https://www.ijcai.org/proceedings/2025/1034) | LLM + RAG + 模板驱动生成 + 分层检索 + Schema 校验 | 将非标准 OTC 合同自动转换为结构化 Common Domain Model | 场外衍生品合同标准化/运营 | 提升合同结构化、互操作和处理效率 |
| 2025 | IJCAI | — | [AlphaGAT: Cross-Asset Graph Attention and Factor Modeling for Portfolio Selection](https://www.ijcai.org/proceedings/2025/834) | TimeMixer + Conv1D + 跨资产注意力 + 图注意力网络 + 强化学习 | 将因子时序、跨资产关系和策略选择联合优化 | 股票组合选择 | 改善组合回报与稳健性 |
| 2025 | KDD | `★ LLM/Agent` | [CAMEF: Causal Augmented Multi-Modality Event-Driven Financial Forecasting](https://dl.acm.org/doi/10.1145/3711896.3736872) | 时序预测 + 文本/数值多模态融合 + 因果学习 + LLM 反事实事件增强 | 用因果约束和 LLM 构造反事实事件，减少事件数据稀缺与伪相关 | 宏观公告驱动的资产价格/事件影响预测 | 提升金融预测和事件冲击评估 |
| 2025 | KDD（ADS） | `★ LLM/Agent` | [Efficient Multi-Expert Tabular Language Model for Banking](https://dl.acm.org/doi/10.1145/3690624.3709400) | 表格语言模型 + 多专家 MoE + 分治预训练 + 稀疏激活微调 | 面向银行表格数据将专家路由与高效训练结合 | 银行风险评估、信息/利润评估 | 提升银行业务预测精度并降低计算成本 |
| 2025 | KDD（ADS） | — | [TEMPER: Capturing Consistent and Fluctuating TEMPoral User Behaviour for EtheReum Phishing Scam Detection](https://www.kdd.org/kdd2025/applied-data-science-ads-track-papers-2/) | 时序用户行为建模 + 图/表征学习 + 一致/波动行为分解 | 同时利用稳定行为画像与短期异常波动 | 以太坊钓鱼/加密资产诈骗识别 | 提升加密金融诈骗风险发现能力 |

### 2026（截至 2026-07-13 已公开论文）

| 时间 | 会议（CCF-A） | 兴趣 | 题目和链接 | 涉及技术（全部主要技术） | 创新点 | 细粒度问题/应用场景 | 结果/产出（粗粒度） |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026 | AAAI | `★ LLM/Agent` | [FinRpt: A Multi-Agent LLM Framework for Financial Report Generation](https://ojs.aaai.org/index.php/AAAI/article/view/37014)✔ | 多 Agent LLM + 监督微调 + 强化学习 + 多源金融数据融合 + 评价指标体系 | 面向财报生成划分角色并以多类数据、指标协作 | 上市公司/投资研究报告生成 | 提升报告生成质量、完整性和可核验性 |
| 2026 | AAAI | `★ LLM/Agent` | [Controllable Financial Market Generation with Diffusion Guided Meta Agent](https://ojs.aaai.org/index.php/AAAI/article/view/37009) | 条件扩散模型 + Meta Agent + 经济先验 + 订单流建模 + 市场仿真 | 用元智能体把经济约束转化为扩散生成的可控条件 | 金融订单流/市场情景生成 | 提高市场模拟的保真度和可控性 |
| 2026 | AAAI | `★ LLM/Agent` | [Kronos: A Financial Market Foundation Model for K-line Time Series](https://ojs.aaai.org/index.php/AAAI/article/view/39730) | 金融时序基础模型 + 专用 K 线 token 化 + 自回归预训练 + 多市场大数据训练 | 用金融专用离散表示在大规模 K 线数据上预训练 | K 线预测、波动率预测、序列生成 | 改善零样本预测、排序相关性和生成保真度 |
| 2026 | AAAI | `★ LLM/Agent` | [FinMMDocR: A Benchmark for Multimodal Long Financial Document Reasoning](https://ojs.aaai.org/index.php/AAAI/article/view/39785) | 多模态 LLM + 长文档理解 + OCR/表格/图像推理 + RAG 对比评测 | 提供中英双语、长财务文档的多步骤推理基准 | 年报、招股书等金融文档问答 | 评估并推动金融长文档多模态推理能力 |
| 2026 | AAAI | `★ LLM/Agent` | [TermGPT: Financial Regulatory Term Recognition with Multi-level Contrastive Fine-tuning](https://ojs.aaai.org/index.php/AAAI/article/view/37075)✔ | 语言模型 + 多层对比微调 + 句子图 + Token/句子对比学习 | 同时保留术语局部边界和法规语境关系 | 金融监管术语识别 | 提升监管文本结构化和合规信息提取 |
| 2026 | AAAI | `★ LLM/Agent` | [GARD: Generative AI Risk Detection for Financial Sensitive Information](https://ojs.aaai.org/index.php/AAAI/article/view/41498) | 金融敏感信息 taxonomy + 合成数据 + LLM/生成式 AI 风险检测 | 建立金融生成式 AI 的敏感信息分类和风险检测框架 | 金融生成式 AI 隐私/合规 | 提升敏感信息泄露风险识别能力 |
| 2026 | AAAI | — | [TRUST: Real-time Transaction Fraud Detection with Heterogeneous Graph and Sequential Transformer](https://ojs.aaai.org/index.php/AAAI/article/view/41450) | 异构 GNN + Transformer 时序建模 + 实时推理/部署 | 在生产约束下联合关系网络和交易序列 | 货到付款/退货到付交易反欺诈 | 提升线上实时拦截精度并满足低延迟 |
| 2026 | AAAI | `★ LLM/Agent` | [DGP: Dual-Granularity Prompting for Graph-Enhanced Large Language Models in Fraud Detection](https://ojs.aaai.org/index.php/AAAI/article/view/38541) | 图增强 LLM + 双粒度提示 + 邻居语义摘要 + 数值聚合 | 把图邻居的语义和统计信息转为 LLM 可利用的双粒度提示 | 异构金融/交易欺诈图检测 | 提升少数欺诈类的 AUPRC 等指标 |
| 2026 | AAAI | `★ LLM/Agent` | [Targeting Borderline Fraudsters: Temporal Hypergraph Learning with LLM-Guided Contrastive Learning](https://ojs.aaai.org/index.php/AAAI/article/view/38588) | 交易超图 + 时间超视图 + 超图注意力 + LLM 引导对比学习 | 聚焦最难区分的边界欺诈者，并用 LLM 提供对比监督 | 金融交易欺诈识别 | 改善边界样本和整体欺诈识别效果 |
| 2026 | AAAI | `★ LLM/Agent` | [CLER: Cross-MLLM Error Correction for Financial Multimodal Reasoning](https://ojs.aaai.org/index.php/AAAI/article/view/40303) | 多模态 LLM 推理 + 对比检索 + 跨模型纠错 + 分步反思 + 金融错误集 | 让多个 MLLM 互相发现、修正金融图表/文档推理错误 | 金融多模态问答与推理 | 以较低测试成本提高金融推理正确率 |
| 2026 | AAAI | `★ LLM/Agent` | [FinMathBench: Evaluating Large Language Models on Financial Formula Reasoning](https://ojs.aaai.org/index.php/AAAI/article/view/40358) | 金融公式库 + LLM 题目生成 + Mask-for-Solve + 层次树/DAG 评测 | 将多公式依赖和中间变量计算纳入专门基准 | 金融公式计算/分析师问答 | 衡量并定位金融数学推理能力缺口 |
| 2026 | AAAI | `★ LLM/Agent` | [ChameleonAttack: Attacking Financial Language Models via Adversarial Optimization](https://ojs.aaai.org/index.php/AAAI/article/view/41099) | 对抗优化 + 语义变换 + 黑盒攻击 + 金融 LLM 安全评测 | 专门衡量金融文本模型/事件驱动股价任务的对抗脆弱性 | 金融 LLM 与事件—股价预测安全 | 发现模型安全漏洞，支持后续防御设计 |
| 2026 | AAAI（IAAI） | `★ LLM/Agent` | [Agentic Solutions for IT Financial Operations](https://ojs.aaai.org/index.php/AAAI/article/view/42387) | LLM Agent + 数据工具调用 + 企业 FinOps 知识/工作流 | 将“与数据对话”的智能体用于云/IT 财务运营 | IT 成本、预算和 FinOps 运维 | 提升企业财务运营问答与决策自动化 |
| 2026 | AAAI | — | [Optimally Auditing Adversarial Agents](https://ojs.aaai.org/index.php/AAAI/article/view/38722) | 博弈论 + 对抗决策 + 审计策略优化 | 为会策略性规避的主体寻找最优审计政策 | 信贷/交易中的欺诈审计与合规稽核 | 提升有限审计资源下的风险发现能力 |
| 2026 | ACL | `★ LLM/Agent` | [MultiFinBen: A Multilingual and Multimodal Financial Benchmark for Large Language Models](https://aclanthology.org/2026.acl-long.770/) | 多语言/多模态金融 LLM 基准 + OCR + 语音/图像/文本理解 + 推理评测 | 扩展金融大模型评测到多语种和文本—视觉—语音模态 | 全球化金融文档/问答/推理 | 建立多语多模态金融模型的比较基线 |
| 2026 | ACL（Findings） | `★ LLM/Agent` | [FINCH: Benchmarking Financial and Accounting Enterprise Agent Workflows](https://aclanthology.org/2026.findings-acl.523/) | 企业 Agent + 工具使用 + 表格/邮件/PDF 处理 + 工作流评测 | 用真实办公材料构成多步骤财务会计 Agent 工作流基准 | 会计核对、财务运营和企业文档流程 | 评测智能体端到端完成财务工作流的能力 |
| 2026 | ACL（Findings） | `★ LLM/Agent` | [FinMRAGBench: A Benchmark for Financial Multi-Page, Cross-Document and Multimodal RAG](https://aclanthology.org/2026.findings-acl.187/) | 多模态 RAG + ReAct Agent + 动态工具调用 + 长文档检索 + 专家标注 QA | 面向跨页、跨文档财报问题，评估检索和工具规划 | 年报/财报多文档问答 | 改善复杂金融检索问答的可评测性 |
| 2026 | ACL（Findings） | `★ LLM/Agent` | [M-SAEA: Risk-First Evaluation of Multi-Agent Systems in Finance](https://aclanthology.org/2026.findings-acl.1934/) | 多 Agent 系统 + 金融风险评测 + 工作流交互 + 风险向量 | 从“能力优先”转为“风险优先”评估金融多智能体 | 金融智能体的流程与系统风险 | 量化并暴露多 Agent 协同的金融风险 |
| 2026 | ACL | `★ LLM/Agent` | [GBFR: Graph-Based Formula Reasoning for Financial Numerical Question Answering](https://aclanthology.org/2026.acl-long.1273/) | 指标知识图谱 + 图约束算子 + 跨路径验证 + 安全拒答 + LLM 推理 | 用公式/指标图限制 LLM 的数值推理路径，并允许安全弃答 | 财务指标计算与数字问答 | 提升正确计算率并降低错误自信回答 |
| 2026 | ACL（Industry） | `★ LLM/Agent` | [FinHarmBench: Benchmarking and Mitigating Harmful Financial Advice from Language Models](https://aclanthology.org/2026.acl-industry.117/) | 金融越狱基准 + 安全对齐/拒答蒸馏 + LLM 风险评测 | 针对诱导性金融建议构造攻击与缓解评测 | 金融建议安全与合规 | 降低模型输出有害金融建议的风险 |

## 实验数据集/落地环境与论文报告提升

这部分与上方主表逐条对应，补足“论文究竟在哪类数据上实验、提升了哪一类指标”。`未在公开摘要中列出具体名称`表示本文调研时没有从可公开核验的论文页写入未经验证的名称；不代表论文正文没有给出。对于交易论文，除特别说明外，“提升”均指其**历史回测或仿真实验**，不代表实盘保证。

### 2024

| 论文（对应主表） | 实验数据集/落地环境 | 论文报告的提升（相对对象/指标） |
| --- | --- | --- |
| Market-GAN | 真实金融市场历史时间序列；多种市场状态/条件的生成实验（公开摘要未列出具体市场名） | 相对生成基线，提高条件可控性与市场动态保真度；用于下游仿真/数据增强 |
| CI-STHPAN | NASDAQ、NYSE 股票池及历史价格/特征序列 | 相对选股基线，提高组合收益与 Sharpe 比率 |
| StockMixer | 多股票公开价格/技术指标基准（摘要未逐一列名） | 提高价格/走势预测精度，同时降低内存和计算开销 |
| MDGNN | 股票关系图与历史市场序列（摘要未列具体股票池） | 相对动态图/时序基线，改善投资信号和组合表现 |
| ECHO-GL | 上市公司 earnings call 文本、公司关系及对应股票价格 | 相对文本或图基线，改善走势预测和交易组合盈利性 |
| EarnHFT | 加密资产分钟级订单/价格序列 | 相对 HFT/RL 基线，提高累计收益及策略稳健性 |
| Revisiting Graph-Based Fraud Detection | 公开欺诈图基准（含金融/交易型图数据） | 相对 GNN 基线，提高少数欺诈节点检测指标 |
| DGA-GNN | 金融账户/交易欺诈图数据 | 相对静态聚合 GNN，提高欺诈识别准确性和鲁棒性 |
| Barely Supervised GFD | 极少标注的公开金融/交易欺诈图 | 相对半监督基线，在极低标注率下保持更高检测效果 |
| Online Contrastive Learning for Insurance Fraud | 医疗保险理赔/欺诈流式数据 | 相对离线或普通在线学习，提高持续识别准确率并缩短适配时间 |
| Directed Multigraph GNNs | 有向多重资金流/金融犯罪图及钓鱼图任务 | 相对既有 GNN，提高少数类 F1；同时给出表达力保证 |
| Accountable Loan Approval | 生产贷款审批数据与真实业务部署 | 在既定坏账约束下提升贷款服务规模；强调可审计性 |
| RisQNet | 中小企业关系网络、贷款/风险事件、新闻文本 | 相对风险模型，报告 87.1 AUC，并生成可读风险报告 |
| ADB-TRM | 股票投资推荐历史数据及时序关系 | 相对投资推荐基线，提高累计收益和风险调整后收益 |
| IMM | 历史做市行为/市场状态数据 | 相对模仿或 RL 做市基线，改善交易收益表现 |
| MacMic | 约 200 只股票的订单执行/市场状态数据 | 相对执行策略，降低执行成本、提高执行质量 |
| Trade When Opportunity Comes | 股票、加密货币、ETF 历史序列 | 相对信号发现基线，提高信号可靠性和可交易收益潜力 |
| Real-Time Payments Fraud | 实时支付参与方与欺诈者的仿真环境 | 相对静态策略，改善风险—业务成本权衡，不以分类 AUC 为唯一目标 |
| FreQuant | 股票组合历史信号/价格数据 | 相对时域投资组合方法，提高年化收益、组合价值和市场变化下稳定性 |
| MacroHFT | 多个加密货币市场的分钟级交易数据 | 相对 HFT/RL 基线，提高总收益、Sharpe、Calmar、Sortino 等 |
| FinAgent | 股票与加密资产市场数据；K 线、新闻/文本、数值和工具信息 | 相对交易基线，提高交易盈利性和跨资产泛化；重点核查成本和样本外设置 |
| CompanyKG | CompanyKG：约 117 万公司、5100 万边、15 类关系 | 在公司相似性、竞品/并购线索等企业情报任务中优于通用图谱检索基线 |
| Pareto Fraud Rule Sets | 金融科技反欺诈业务规则与交易样本 | 给出 Pareto 最优规则集，显式改善欺诈拦截率—业务/人工成本折中 |
| Dólares or Dollars? | 英语/西班牙语金融文本任务与金融指令数据 | 相对通用/单语模型，改善西班牙语金融 NLP 与跨语迁移 |
| BizBench | 真实商业和财务材料中的表格—文本定量问答 | 不是收益模型；量化比较 LLM 在计算、程序合成和推理上的能力缺口 |
| FinTral | 多个金融 NLP、文档分析和推理基准 | 相对金融/通用 LLM 基线，提高金融任务与检索工具使用能力 |
| FinBen | 42 个数据集、24 类金融任务；含交易、RAG、Agent 任务 | 不是单一方法增益；建立统一基线，揭示复杂推理、预测和交易的短板 |
| EarnMore | 美国股票市场 8 个自定义股票子池 | 相对 14 个组合管理基线，6 项金融指标提升；报告利润提升超过 40% |

### 2025

| 论文（对应主表） | 实验数据集/落地环境 | 论文报告的提升（相对对象/指标） |
| --- | --- | --- |
| FactorGCL | 股票收益预测与因子数据（公开摘要未逐一列名） | 相对因子/图预测基线，提高收益预测与隐因子表征质量 |
| DHMoE | 多模态股票数据与投资组合回测 | 相对混合专家、时序和投资基线，提高累计收益及风险调整收益 |
| AlphaForge | 历史市场数据和公式化 Alpha 因子池 | 相对 Alpha 挖掘/组合基线，提高因子有效性与组合收益 |
| Linking Industry Sectors and Financial Statements | 行业标签、财务报表文本和数值字段 | 相对传统分类，改善行业—报表匹配与可解释性；不直接报告交易收益 |
| MonTi Fraud-Gang Attack | 欺诈图（含保险/金融类欺诈场景） | 相对攻击方法，提高对多目标欺诈图注入攻击的有效性；用于评测防御风险 |
| Context-aware GNN Fraud | 少标签金融账户/交易欺诈图 | 相对少标签 GNN 基线，提高欺诈检测效果 |
| Dynamic Neighborhood GFD | 动态关系欺诈图 | 相对固定邻域图模型，提高复杂网络欺诈识别表现 |
| HALO Fraud | 无标签/弱标签欺诈图 | 相对无监督图方法，改善欺诈节点排序且降低标注依赖 |
| AI4Contracts | OTC 合同文本与 Common Domain Model 结构化目标 | 相对普通生成/RAG，提升合同结构化、Schema 合规和互操作性 |
| AlphaGAT | 跨资产股票/因子时序数据 | 相对单资产或非图组合策略，改善组合回报与稳健性 |
| CAMEF | 宏观公告事件与 5 个美国资产的文本—数值时序数据 | 相对事件预测/多模态基线，改善金融预测和事件冲击评估；LLM 用于反事实事件增强 |
| Multi-Expert Tabular LM for Banking | 银行表格数据，风险、信息和利润评估任务 | 相对表格模型，论文报告风险任务 P@0.6 提升 29.3%、部分任务准确率提升 16.5% |
| TEMPER | 以太坊用户时序行为与钓鱼诈骗数据 | 相对时序/行为基线，提高钓鱼诈骗发现能力 |

### 2026（截至 2026-07-13 已公开论文）

| 论文（对应主表） | 实验数据集/落地环境 | 论文报告的提升（相对对象/指标） |
| --- | --- | --- |
| FinRpt | 7 类金融数据源、11 项报告评价指标 | 相对报告生成基线，提高报告质量、完整性与可核验性；不是直接交易回测 |
| DigMA | 订单流/中间价收益率/订单到达率数据；下游高频交易仿真环境 | 相对生成模型，提高订单流生成保真度和可控性，并验证其作为 HFT 生成环境的有效性 |
| Kronos | 45 个全球交易所、超过 120 亿条 K 线记录及多个金融时序基准 | 相对最佳 TSFM，价格预测 RankIC 提升 93%；波动率 MAE 降低 9%；生成保真度提升 22% |
| FinMMDocR | 约 1200 个中英双语金融长文档多步骤问题；表格、图像、文字 | 不是收益模型；用于比较 MLLM/RAG 的金融长文档推理能力 |
| TermGPT | 来自官方监管文件的金融术语数据集 | 相对语言模型基线，提高术语判别和下游风险/合规文本理解 |
| GARD | 金融敏感信息 taxonomy 与合成风险样本 | 相对通用风险检测，提高金融敏感信息泄露发现能力 |
| TRUST | 货到付款/退货到付真实交易欺诈部署数据 | 相对 XGBoost 等基线，论文报告精度绝对提升 9.6 个百分点，并满足约 25 ms 延迟 |
| DGP | 异构金融/交易欺诈图 | 相对图/LLM 基线，AUPRC 最多提升 6.8 个百分点 |
| Targeting Borderline Fraudsters | 金融交易超图与时间超视图 | 相对欺诈检测基线，AUC 提升约 1.1–5.7 个百分点 |
| CLER | FinErrorSet 与金融图表/文档多模态推理任务 | 相对单 MLLM 或普通检索，提高推理正确性并降低测试成本 |
| FinMathBench | 金融公式库、多公式依赖问题与生成问题 | 不是收益模型；量化暴露 LLM 在多公式计算/依赖推理上的性能下降 |
| ChameleonAttack | 金融语言模型、事件驱动股价预测任务 | 相对攻击基线，攻击成功率最高报告 93.4%；用于评估安全脆弱性 |
| Agentic FinOps | ITBench FinOps 企业任务 | 论文报告约 90% 任务性能；提升 FinOps 数据问答/运营自动化 |
| Optimally Auditing Adversarial Agents | 信贷/交易审计的策略性主体仿真 | 相对非最优审计，提升有限稽核资源下的风险发现能力 |
| MultiFinBen | 多语言、多模态金融评测：文本、图像、OCR、语音等 | 不是收益模型；建立全球化金融 LLM 的能力基线 |
| FINCH | 172 个企业财务/会计工作流、384 项任务；表格、邮件、PDF | 不是收益模型；评测 Agent 端到端完成财务流程的成功率和可靠性 |
| FinMRAGBench | 887 个专家核验 QA；年报等跨页、跨文档、多模态材料 | 不是收益模型；比较多模态 RAG/Agent 的检索和回答质量 |
| M-SAEA | 金融多 Agent 工作流及风险向量 | 不是收益模型；量化多 Agent 交互的系统风险和失效模式 |
| GBFR | 金融指标知识图谱、公式数值问答数据 | 相对自由生成推理，提高正确计算率并减少高置信错误回答 |
| FinHarmBench | 金融有害建议/越狱提示基准 | 相对未对齐模型，降低产生有害金融建议的风险 |

## 按技术路线的观察

| 路线 | 代表论文 | 典型金融任务 | 变化趋势 |
| --- | --- | --- | --- |
| 时序预测/量化投资 | StockMixer、FactorGCL、DHMoE、Kronos | 股价/收益预测、选股 | 从单资产时序走向跨资产关系、因子和金融时序基础模型 |
| 强化学习/决策 | EarnHFT、FreQuant、MacroHFT、EarnMore、MacMic、AlphaGAT | 组合优化、高频交易、订单执行、做市 | 重点转向风险调整收益、市场状态适应与可控策略 |
| 图学习/反欺诈 | RisQNet、TRUST、DGP、Borderline Fraudsters | 信贷风险、支付/交易/保险欺诈、洗钱 | 动态/异构/超图以及少标签和对抗鲁棒性成为重点 |
| 金融 LLM/MLLM | FinTral、FinBen、FinMMDocR、MultiFinBen、GBFR | 金融问答、报表理解、数值/公式推理 | 从文本分类走向多模态、长文档、受约束数值推理 |
| LLM Agent/RAG | FinAgent、AI4Contracts、FinRpt、FINCH、FinMRAGBench | 交易、合同、报告生成、企业财务流程 | 从单轮问答走向工具调用、可审计工作流和端到端评测 |
| 生成与安全 | Market-GAN、扩散 Meta Agent、GARD、ChameleonAttack、FinHarmBench | 市场仿真、隐私、模型安全 | 一面生成可控情景，一面开始正视金融模型的隐私、攻击和有害建议风险 |

## 面向 LLM/Agent 兴趣的推荐阅读顺序

1. **FinBen（NeurIPS 2024）**：先建立金融 LLM 的任务地图；其 24 类任务能帮助判断后续论文究竟改进了什么。
2. **FinAgent（KDD 2024）**：最贴近“LLM Agent + 工具 + 反思 + 记忆 + 交易”的完整系统，适合理解 Agent 设计。
3. **FinTral（ACL 2024）**：了解金融 LLM 的领域继续训练、偏好优化、RAG 和工具使用如何组合。
4. **CAMEF（KDD 2025）**：重点看 LLM 与时序预测、因果事件增强如何真正组合，而不是把 LLM 当作孤立模块。
5. **AI4Contracts（IJCAI 2025）**：学习 RAG、层次检索、Schema 校验如何落到高价值、可验证的金融运营任务。
6. **FinRpt（AAAI 2026）与 FINCH（ACL 2026）**：对比“生成报告的多 Agent 系统”与“企业会计工作流 Agent”的评测/工程边界。
7. **FinMRAGBench（ACL 2026）与 FinMMDocR（AAAI 2026）**：若目标是年报、招股书、表格和图片上的 RAG/Agent，这是最直接的基准入口。
8. **GBFR（ACL 2026）、CLER（AAAI 2026）、FinMathBench（AAAI 2026）**：适合深入金融数值、公式和多模态推理的正确性问题。
9. **M-SAEA、FinHarmBench、GARD（2026）**：在部署金融 Agent 前必读，分别关注系统性风险、有害建议和敏感信息泄露。

## 建议的下一步筛选

- 若目标是**投研/交易 Agent**：优先 FinAgent → CAMEF → Kronos，并以 FinBen 的交易/预测任务做复现评测；同时把历史回测、滑点、风险调整收益和模型安全分开报告。
- 若目标是**金融文档/合规 Agent**：优先 AI4Contracts → FinMRAGBench → FINCH → GBFR；关注引用可追溯、Schema 校验、数值计算和拒答策略。
- 若目标是**银行/支付反欺诈**：优先 TRUST、DGP、RisQNet、Targeting Borderline Fraudsters；LLM 更适合解释、辅助标注或图信息摘要，不应取代低延迟的主风控模型。
