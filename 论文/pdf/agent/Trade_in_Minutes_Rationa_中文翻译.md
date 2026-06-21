# Trade in Minutes! 面向量化金融交易的理性驱动智能体系统

发表于 ICLR 2026 会议论文

Zifan Song¹˒²，Kaitao Song²，Guosheng Hu³，Ding Qi¹，Junyao Gao¹，Xiaohua Wang⁴，Dongsheng Li²，Cairong Zhao¹*

¹同济大学  ²微软亚洲研究院  ³布里斯托大学  ⁴复旦大学

*通讯作者：zhaocairong@tongji.edu.cn。Zifan 在微软亚洲研究院实习期间完成本工作。

> 译注：本文档为 `Trade_in_Minutes_Rationa.pdf` 正文中文翻译。公式、模型名、指标缩写与引用标注尽量保留原文形式；参考文献作为书目信息保留原文。

## 摘要

大型语言模型（LLM）和智能体系统的最新进展展现出卓越的决策能力，揭示了其在自主金融中的重要潜力。当前的金融交易智能体大多模拟拟人化角色，这会无意中引入情绪偏差，并依赖外围信息，同时还受到部署阶段必须持续推理这一要求的限制。本文率先尝试协调智能体的策略深度与量化交易所需的机械理性。为此，我们提出 TiMi（Trade in Minutes），一种理性驱动的多智能体系统，在架构上将策略开发与分钟级部署解耦。TiMi 在完整的“策略-优化-部署”链条中利用 LLM 在语义分析、代码编程与数学推理方面的专门能力。具体而言，我们提出从宏观模式到微观定制的两层分析范式、用于交易机器人实现的分层编程设计，以及由数学反思驱动的闭环优化。在股票和加密货币市场 200 多个交易对上的大量评估从经验上验证了 TiMi 在波动市场动态下稳定盈利、行动效率与风险控制方面的有效性。

## 1 引言

大型语言模型（LLM）（OpenAI, 2023; Grattafiori et al., 2024）的近期突破已经展示出解决复杂任务的重要潜力。研究者不断通过模型架构创新（Cai et al., 2024; Guo et al., 2025）、训练范式（Ding et al., 2023; Wang et al., 2025）与数据扩展（Song et al., 2024; Zhu et al., 2025）来推进 LLM 的基础能力。与此同时，一种系统性研究范式正在形成：将 LLM 作为核心认知引擎，构建具备自主决策与执行能力的智能体系统（Zhang et al., 2025; Hu et al., 2024）。这种方法通过模块化架构设计和策略性任务分解，将语义理解、逻辑推理与工具使用能力整合进动态工作流，从而超越单模型改进的局限，面向真实场景中的长期挑战。

本文关注量化金融（Wilmott, 2013; Sun et al., 2023）。这一领域所需的复合能力（例如实时决策、风险控制和策略迭代）为自主智能体研究提供了一个高度实用但颇具挑战的场景。经典的基于规则的策略（Platen & Heath, 2006）虽然在特定市场模式下能保持稳定表现，但难以适应金融生态中的非线性波动、黑天鹅事件等复杂动态。值得注意的是，现有关于 LLM 驱动金融交易智能体的研究（Ding et al., 2024; Li et al., 2023; Xiao et al., 2025）强调角色扮演式的分析和决策，包括金融助手、新闻驱动或辩论驱动的变体。尽管这些拟人化方法有效利用了 LLM 处理文本信息的优势，却较少关注代码编程与数学推理能力的进展，而后两者可能是金融交易中实现机械理性的关键。

> “我们不让任何人预测市场——我们让模型说话。” —— James Simons

进一步来看，我们识别出推动这一探索的三个关键方面：

1. **市场分析范式**：以往研究中对人类交易组织的模拟（例如情绪/新闻分析师、具有不同风险偏好的交易员）会无意中引入由智能体模拟出的情绪偏差和主观判断干扰。
2. **支撑数据选择**：围绕目标交易对的非结构化外围信息（例如社交媒体上的异质新闻、项目报告）往往包含误导性信号和时间滞后。对散户而言，这一点尤其成问题，因为依赖这类公开信息可能导致错失交易机会，或在不利市场波动中暴露出较大风险。
3. **系统部署效率**：多个智能体之间冗长的推理和协商会显著增加实际部署中的计算成本和行动延迟。在高波动交易环境下，这可能表现为执行滑点和机会成本。

基于这些考虑，我们提出图 1 所示的 TiMi（Trade in Minutes），这是一种通过理性决策实现分钟级动态交易的新型智能体系统。在市场分析方面，我们设计顶层智能体来捕捉和分析模式，从技术指标中推导宏观策略，同时由专门智能体基于特定交易对特征在微观层面优化策略。在数据选择方面，我们使用目标交易对的客观技术指标（例如成交量和振幅），并采用动态更新的时间窗口来适应市场波动。为了提升部署效率，我们通过机器人进化智能体（即代码 LLM）将策略转化为程序化交易机器人，从而实现分析与执行的解耦。这种方法以低延迟支持分钟级量化交易，消除了持续多智能体推理所带来的计算成本和时间消耗。进一步地，我们收集部署反馈，并使用具备推理能力的反思智能体，从代表性案例中形式化数学问题（例如线性规划）以确定最优参数。这些参数随后提交给机器人进化智能体，在参数层、函数层和策略层进行层次化精炼。借助这一架构，我们有效利用智能体在语义分析、代码编程和数学推理方面的专门能力，建立了涵盖市场分析、策略定制、程序化部署和反馈迭代的完整闭环系统。

**图 1：** TiMi 系统架构包含策略、优化和部署三个阶段。TiMi 实现了解耦机制：前两个阶段在离线模拟中利用专门化 LLM 能力开发并优化原型交易机器人，部署阶段则在实盘交易中执行经过充分精炼、参数已调优的机器人。该范式将复杂推理与时间敏感执行分离，使系统在市场动态中同时具备全面策略开发能力和量化级效率。

我们在美国股指和加密货币市场的 200 多个交易对上进行了实盘交易实验，并报告了包括年化收益率、夏普比率和最大回撤在内的综合指标。所提出的 TiMi 相比量化方法、ML/RL 方法以及 LLM 智能体方法表现出竞争优势，尤其是在具有挑战性的山寨币市场中。更重要的是，我们展示了交易机器人的系统性演化，并通过可视化真实部署中的代表性交易进行深入分析，从而考察 TiMi 在多种市场动态下的能力。本文的核心贡献有三点：

- 我们提出 TiMi（Trade in Minutes），一种面向量化金融交易的理性驱动智能体系统，能够有效利用不同 LLM 变体在语义分析、代码编程和数学推理方面的互补能力。
- TiMi 系统开创了若干关键创新：（1）将策略开发与实时部署进行策略性解耦；（2）提出从宏观模式到微观定制的两层分析范式；（3）提出交易机器人实现的分层编程设计；（4）提出由数学反思驱动的闭环优化系统。
- 通过在 200 多个多样化交易对上的综合评估，我们从经验上验证了 TiMi 在盈利能力、部署效率和风险缓释方面的有效性，并为开发可定制的智能体交易系统提供了一种探索。

## 2 理性驱动的多智能体系统

### 2.1 预备知识

我们的目标是开发一个具备完整“策略-部署-优化”链条的智能体系统，用于应对市场动态。从理论上看，每个交易环境都可以建模为一个元组 `(M, W, S, F, J)`，其中 `M` 表示市场，`W` 表示目标时间窗口，`S` 定义策略空间，`F` 表示反馈信号，`J` 表示评价函数。交易系统预期实现以下三项功能：（1）分析：`M × W -> S`，即将观测到的市场模式转化为交易策略；（2）部署：`M × S -> F`，即将策略转化为交易行为并在行动过程中收集反馈；（3）优化：`S × F -> S*`，即基于交易反馈精炼策略。给定由参数 `Θ` 表征的交易策略 `π ∈ S`，TiMi 致力于通过后续章节所详述的理性驱动智能体系统来最大化 `J(π_Θ)`。

### 2.2 具有解耦分析与部署能力的多智能体架构

基于机械理性，我们构建了一种多智能体架构，利用 LLM 在语义分析、代码编程和数学推理方面的专门能力，从而缓解两类内在局限：基于规则方法缺乏适应性，拟人化模拟又会引入情绪偏差。同时，我们主张将分析与部署解耦，把策略准备从时间敏感的执行环节中分离出来。

**多智能体设计。** 如图 1 左侧所示，TiMi 由四类专门智能体组成，它们在协调工作流中交互，将市场数据转化为可执行的交易行为：（1）**宏观分析智能体** `A_ma`：识别宏观层面的市场模式，并基于技术指标制定通用交易策略 `S`；（2）**策略适配智能体** `A_sa`：通过分析交易对 `P` 的特征，将宏观策略 `S` 定制为交易对特定规则 `S_P`，并初始化参数 `Θ_P`；（3）**机器人进化智能体** `A_be`：从交易策略和反馈反思中创建并优化程序化交易机器人 `B`；（4）**反馈反思智能体** `A_fr`：对行动反馈 `F` 进行反思，获得更精确且层次化的反馈 `F*`，并相对于 `B` 精炼参数 `Θ*`。令 `ϕ`、`ψ` 和 `γ` 分别表示语义分析、代码编程和数学推理能力，则完整的 TiMi 系统可表示为这些智能体函数的组合：

```text
A_ma ◦ ϕ ◦ ψ: M × W -> S
A_sa ◦ ϕ ◦ γ: S × P -> S_P × Θ_P
A_be ◦ ψ: S × Θ × L -> B
A_fr ◦ γ: B × F × Θ -> F* × Θ*

T(M, W) = A_be(A_sa(A_ma(M, W), P), L)(M; A_fr(B, F, Θ)).
```

其中 `◦` 表示功能上的概念性组合，即智能体通过调用嵌入的核心能力来完成定义好的映射任务；`T(M, W)` 表示系统在市场 `M` 和时间窗口 `W` 下运行；`L` 表示编程法则（详见第 2.4 节）。

**解耦机制。** 我们通过三阶段流程实现分析与部署的解耦：（1）**策略阶段**：复杂推理和策略开发发生在离线环境中，充分利用专门智能体的能力，包括 `A_ma`、`A_sa` 和 `A_be`，生成具有初始参数 `Θ` 的原型交易机器人 `B`；（2）**优化阶段**：原型机器人在离线环境（例如实盘或历史市场）中模拟，以收集反馈 `F`，包括技术执行回溯和风险边界案例；随后迭代地进行离线智能体交互，得到高级交易机器人 `B* = A_be(B; A_fr(B, F, Θ))`；（3）**部署阶段**：经过充分优化后，成功通过模拟测试的交易机器人可部署到实盘交易环境中，并具有低延迟和低执行成本（第 3 节将讨论具体实现）。

这一机制消除了实际部署中持续模型推理的需求，并带来效率优势，可量化为：

```text
η = (c_agent × n) / (c_policy + c_optimization + c_bot × n)
```

其中 `c_agent / c_bot` 分别表示每次交易的智能体/机器人推理成本，`n` 是交易动作数量，`c_analysis` 是离线分析成本。随着高波动市场中 `n` 的增加，效率比趋近于：

```text
lim_{n -> ∞} η = c_agent / c_bot
```

由于通常 `c_bot << c_agent`，这代表着随交易频率扩展的效率和响应性提升。同时，解耦还使优化阶段能够在没有时间约束的情况下进行深入策略精炼，从而提升有效性并带来更稳健的交易表现。

### 2.3 从宏观模式到微观定制的分析范式

我们实现了一种用于策略初始化的两层范式：从全市场分析到交易对特定定制。与单一整体方法相比，该设计旨在同时提供**统计显著性**与**策略适应性**方面的优势。

**宏观策略分析。** 从理论上看（Hasbrouck, 2007; Lo et al., 2000），金融市场在特定条件下（例如短期时间窗口内）本质上存在周期性行为模式，这些模式可以通过技术指标和统计方法的组合来识别。因此，我们系统的基础是宏观分析智能体 `A_ma`，它对市场模式进行理性分析。通过技术指标 `I` 的定义进行初始化后，`A_ma` 捕捉跨时间尺度 `W` 的所有可观测市场状态空间，从而生成面向具有统计显著性模式的通用策略集合 `S`。形式化地，`A_ma` 的运行机制可表示为：

```text
A_ma(M, W; I) = ϕ({ψ_i(M, w) | w ∈ W, i ∈ I}) -> S.
```

这里，函数 `ψ_i(M, w)` 表示一个编程过程：它提取时间窗口 `w` 内的相关市场数据，并应用指标 `i`，将这些数据转换为有分析价值的特征。

**交易对特定定制。** 不同交易对因其独特特征而经常表现出异质行为。为跟踪这种差异，我们引入策略适配智能体 `A_sa`，对通用策略集合进行系统精炼，使其适应具体交易对。方法包含两步：首先，执行语义分析 `ϕ(S, p) | p ∈ P -> S_p`，从通用集合 `S` 中选择并调整策略，生成交易对特定的策略候选 `S_p`；随后，执行数学推理 `γ(S_p, p) | p ∈ P -> Θ_p`，优化这些策略的参数集合 `Θ_p`。关键在于，这种定制涵盖基于历史表现的策略优先级排序、适配交易对特定波动率画像的参数校准，以及考虑市场流动性等关键因素的自适应风险管理规则。

### 2.4 采用分层编程设计实现交易机器人

为了将策略洞察转化为可执行的交易机器人，我们实现了一种分层编程策略，以增强模块化并促进系统性精炼。机器人进化智能体 `A_be` 通过将交易机器人 `B` 分解为三个层级来构建它们：策略层、函数层和参数层。策略层封装由 `S_p` 推导出的决策逻辑，包括信号生成、仓位规模和进出场标准。函数层提供策略所需的计算机制，实现技术指标、数据预处理和订单执行例程，这些机制可在不同策略之间复用。参数层管理可调参数，用于微调交易策略及其函数的行为。该架构使 `A_be` 能够高效地将交易对特定策略转化为算法过程，同时支持策略阶段与开发阶段之间的解耦机制。

**编程法则。** 我们提出三条核心法则 `L`，用于约束 `A_be` 的代码编程 `ψ`：（1）**功能内聚法则**：每个功能组件必须只承担一个职责；（2）**单向依赖法则**：依赖必须严格从高层流向低层；（3）**参数外部化法则**：所有可调值必须从实现代码中抽离，并集中管理。这些原则旨在让 `A_be` 能够系统性地构建交易机器人，使其支持由 `A_fr` 发起的反馈驱动精炼过程，同时在优化循环中保持架构完整性。

### 2.5 由数学反思驱动的闭环优化

在优化阶段，交易机器人会在实盘或历史市场中模拟，周期性收集行动反馈 `F`，其中包括交易表现指标、风险事件记录和执行统计。反馈反思智能体 `A_fr` 对这些反馈进行解构，并形成精确的优化计划，随后将其传递给 `A_be` 进行程序化精炼。通过这种方式，我们建立了一个面向稳健可靠系统的理性驱动演化过程。

**用于参数求解的数学推理。** 反馈反思智能体 `A_fr` 在三步优化过程中使用数学推理 `γ`：首先从反馈 `F` 中组织风险场景并将其转化为线性规划问题；然后求解可行参数解空间；最后在约束空间内优化参数以最大化表现。该优化可形式化表示为（附录 A 给出了示例）：

```text
Θ* = arg max_{Θ ∈ C(Θ)} Σ ω_i J_i(Θ, F)
s.t. C(Θ) = {Θ ∈ R^n | A(R)Θ ⪯ b(R)}.
```

其中 `C(Θ)` 定义可行参数空间，`ω_i` 和 `J_i` 分别表示第 `i` 个目标权重和评价指标（例如胜率），`A(R)` 和 `b(R)` 表示由风险场景 `R = γ(F)` 推导出的约束矩阵和阈值向量，并通过逐元素不等式 `⪯` 实施参数限制。该过程的关键在于 `A_fr` 能够识别相互竞争目标之间的权衡，并建立帕累托有效的参数配置。

**层次化优化。** 我们提出一种层次化优化方案，让精炼从参数层（即 `B` 的参数层）向上传播到整个交易系统。在参数层，我们关注在约束内微调数值。当参数调整不足以满足需求（例如无法通过风险模拟）时，`A_fr` 会升级到函数层并替换算法组件。最高层级的干预发生在策略层，此时 `S_p` 中编码的基本决策规则会经历结构性修改。图 2 中示例的这种分层方式具有双重优势：它遵循**最小干预**原则，优先进行保留策略连续性的低层级调整；同时建立自然的复杂度递进，使系统能先测试扰动较小的修改，再实施更根本的变更。

**算法 1：用于 `B*` 的 TiMi 实现**

```text
输入：市场 M，分钟级部署时间 t。
参数：执行间隔 T1，回看周期 T2，
      成交量/波动率阈值 V_req / Φ_req，资本分配 A，
      价格/数量分布 M_P / M_Q，盈亏点 H。

for each 执行时间 t = t_e ∈ T1 do
    获取所有交易对的市场 M；
    选择交易对 P = {p | V_{p,t_e} ≥ V_req 且 Φ_{p,t_e} ≥ Φ_req}，
    其中波动率 Φ_{p,t_e} 由下式计算：
        (max_{t∈T2}{O_p(t), C_p(t)} - min_{t∈T2}{O_p(t), C_p(t)}) / C_p(t_e)

    for each 合格交易对 p ∈ P do
        for each 订单层级 i ∈ {1, 2, ..., m} do
            P_i = P_recent × (1 ± Φ_p)^{M_P[i]}
            Q_i = A × M_Q[i] × c_m × c_f
            放置限价单 (P_i, Q_i)

    while 存在 I ∈ T1: [t_e, t] ⊆ I do
        for each 持仓 do
            监控 P_entry × (1 ± Φ_{p,t})^{H[i]} 处的盈亏；
            当 P_entry × Q < A/λ 且盈利时平仓。

返回：行动反馈 F。
```

**图 2：交易机器人 `B` 的演化图。** 我们展示了相对于参数层、函数层和策略层的有意识优化循环（C1-C4），说明层次化优化如何逐步驱动更复杂的交易能力。

## 3 Trade in Minutes

本节展示高级交易机器人 `B*` 的一种具体实现（详见算法 1），说明所提出的 TiMi 系统如何实际部署，重点包括参数配置、订单执行逻辑、仓位管理和风险控制。

**参数配置。** TiMi 建立了若干关键参数变量来控制交易操作，包括定义分钟级执行间隔和波动率回看周期的时间约束 `T1, T2`，以及用于资本分配的风险分配金额 `A`。此外，最小交易量阈值 `V_req` 用于保证充足流动性，参数 `Φ_req` 则作为交易对筛选的波动率标准。系统还纳入矩阵化参数 `M_P = [p_1, p_2, ..., p_m]` 和 `M_Q = [q_1, q_2, ..., q_m]` 来控制订单分布，并使用数量缩放系数 `{c_m, c_f, c_e}` 调整市值、资金费率和持仓入场。这里，盈亏阈值 `H = [h_1, h_2, ..., h_k]` 用于仓位管理。

**订单执行逻辑。** 系统首先通过 API 端点获取市场数据，在执行周期 `[t_e, t_e + Δt_1] ∈ T1` 内计算关键指标，包括价格指标、波动率指数和资金费率。随后，交易对 `P = {p | V_{p,t_e} ≥ V_req ∧ Φ_{p,t_e} ≥ Φ_req}` 通过成交量和波动率要求筛选，估计公式为：

```text
Φ_{p,t_e} =
(max_{t∈T2}{O_p(t), C_p(t)} - min_{t∈T2}{O_p(t), C_p(t)}) / C_p(t_e)
```

其中 `T2 = {t_e - τ, t_e - τ + Δt_2, ..., t_e}` 表示由估计窗口 `τ` 和时间步长 `Δt_2` 决定的时间点序列，`O_p(t) / C_p(t)` 表示交易对 `p` 在区间 `[t - Δt_2, t]` 对应 K 线的开盘价/收盘价。具体而言，TiMi 实现了一种带分钟级动态的精密工程化网格策略，对选中的交易对在优化价格层级 `P_i = P_recent × (1 ± Φ)^{M_P[i]}` 放置订单。订单数量 `Q_i` 由 `Q_i = A × M_Q[i] × c_m × c_f` 计算。对于已持仓资产，当仓位发生移动时，TiMi 应用比例缩放因子 `(P / P_entry)^{c_e}` 来动态调整分配。

**仓位管理。** 部署期间，系统持续监控仓位和市场动态。当达到盈亏阈值 `P_entry × (1 ± Φ)^{H[i]}` 时，TiMi 通过渐进兑现方式执行部分平仓。同时，对于 `P_entry × Q < A/λ`（其中 `λ` 为仓位规模除数）的仓位，在盈利时会自动平仓，以优化资金效率。

**风险控制。** TiMi 集成了复杂的风险缓释机制，确保在多样市场动态下稳健交易。核心上，系统采用经数学优化的参数矩阵 `M_P` 和 `M_Q`，这些参数已通过反馈反思智能体 `A_fr` 严格精炼，并在由大量风险场景模拟推导出的受约束可行解空间中求解。同时，资本分配由参数 `A` 精确控制，用于限制单一资产敞口并防止集中风险。此外，TiMi 执行价格偏离控制，当最新价与标记价之间存在显著差异、代表异常市场条件时，系统会阻止下单。

## 4 实验

### 4.1 实现细节

**骨干 LLM。** 如第 2 节所述，TiMi 的核心设计理念是利用专门化的 LLM 能力。我们有策略地采用 DeepSeek-V3 进行语义分析，采用 Qwen2.5-Coder-32B-Instruct 进行代码编程，采用 DeepSeek-R1 进行数学推理。此外，我们开发了一种结合本地推理（小模型）和 API 推理（大模型）的混合实现，以支持灵活升级并获得最佳的性能-效率权衡。

**智能体实现。** 我们开发了一种混合通信协议，将基于 XML 的消息信封与 JSON 载荷结合起来，以促进智能体间的数据交换。XML 层封装关键元数据（例如发送者身份和上下文领域），JSON 载荷则承载特定领域内容。我们的智能体运行在具备系统级能力的确定性环境中，包括本地文件操作和可验证的 API 调用。关键在于，我们实现了程序化后验检查：TiMi 会在受控沙箱中以程序方式验证生成脚本和数学解，捕获执行回溯，确保计算输出和参数推导在部署前满足预定义约束。

**部署。** 受益于解耦机制，TiMi 在部署阶段只需要 CPU 运行环境。由智能体 `A_be` 和 `A_fr` 开发的交易机器人采用 Python 实现，并通过标准化连接器与交易所 API 集成。此外，TiMi 实现了错误处理例程，用于管理连接问题、速率限制和意外市场状况，从而在次优环境下保证运行连续性。

**模拟与实盘交易。** 我们在美国股指期货和加密货币市场进行了大量实验，以评估 TiMi 在不同市场条件下的通用性和稳健性。我们采用渐进式验证流程：首先使用历史数据进行初始策略开发，随后使用实时市场数据进行交易模拟，最终进行实盘交易评估。

### 表 1：2024 年历史数据上的回测比较

最优/次优结果在原文中分别以加粗/下划线标示。

| 方法 | 美国股指期货 ARR% | SR | MDD% | 主流币期货 ARR% | SR | MDD% | 山寨币期货 ARR% | SR | MDD% |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| MACD | 3.8 | 0.42 | 14.5 | 12.6 | 0.84 | 18.4 | 4.2 | 0.36 | 32.8 |
| Momentum | 8.0 | 0.73 | 16.8 | 15.7 | 0.93 | 21.4 | -2.8 | -0.40 | 38.3 |
| Grid Trading | -2.8 | -0.35 | 10.2 | -8.3 | -0.72 | 22.6 | 9.4 | 0.72 | 18.7 |
| Pairs Trading | 2.3 | 0.40 | 7.4 | -6.8 | -0.67 | 16.3 | -5.7 | -0.46 | 14.5 |
| ETF&PCA | 4.6 | 0.49 | 13.9 | 7.2 | 0.62 | 15.8 | 6.3 | 0.69 | 17.2 |
| TSMOM | 10.5 | 0.81 | 19.7 | 18.4 | 1.15 | 17.2 | 1.5 | 0.05 | 41.6 |
| OFI | 2.1 | 0.34 | 11.8 | 8.9 | 0.66 | 19.3 | 7.8 | 0.64 | 23.9 |
| LSTM | 3.2 | 0.36 | 15.3 | 9.4 | 0.88 | 17.8 | -16.8 | -0.89 | 25.4 |
| DQN | 8.3 | 0.69 | 18.6 | 9.7 | 0.83 | 20.5 | -9.3 | -0.80 | 38.7 |
| DDPG | 5.4 | 0.52 | 17.4 | 14.8 | 1.09 | 14.0 | 8.6 | 0.65 | 26.2 |
| Autoformer | 4.9 | 0.43 | 16.5 | 13.2 | 0.97 | 16.4 | 17.5 | 0.98 | 24.8 |
| PatchTST | 6.7 | 0.58 | 18.1 | 12.5 | 0.90 | 17.6 | 11.2 | 0.82 | 23.5 |
| FinGPT | 5.8 | 0.57 | 15.7 | 6.6 | 0.59 | 19.8 | 7.4 | 0.61 | 31.2 |
| FinMem | 5.2 | 0.54 | 14.8 | 11.3 | 0.96 | 17.4 | -8.9 | -0.60 | 19.6 |
| TradingAgents | 6.3 | 0.60 | 16.2 | 17.9 | 1.12 | 20.3 | 9.7 | 0.72 | 29.6 |
| TiMi（本文） | 8.9 | 0.84 | 10.5 | 16.5 | 1.25 | 12.1 | 23.7 | 1.27 | 26.0 |

**评价指标。** 主要指标包括年化收益率（ARR），用于衡量一年内投资价值变化，定义为 `ARR = (V_final - V_initial) / V_initial`，其中 `V_final` 与 `V_initial` 表示最终价值和初始价值；夏普比率（SR），以 `SR = (R - R_f) / σ_p` 衡量单位风险下的超额收益，其中 `R` 是平均组合收益，`R_f` 是无风险利率，`σ_p` 是超额收益标准差；最大回撤（MDD），表示从峰值到谷值的最大跌幅，定义为 `MDD = (V_trough - V_peak) / V_peak`，其中 `V_peak` 和 `V_trough` 分别是最大跌幅发生前的最高值和之后的最低值。

**基线方法。** 我们将 TiMi 与三类代表性方法比较：（1）**量化方法**，包括用历史波动率优化的 MACD（Wang & Kim, 2018）、动量策略（Jegadeesh & Titman, 1993）、网格交易（Griffin et al., 2003）、配对交易（Gatev et al., 2006）、基于 ETF&PCA 的统计套利（Avellaneda & Lee, 2010）、时间序列动量（TSMOM）（Moskowitz et al., 2012）和订单流不平衡（OFI）策略（Cont & De Larrard, 2013）；（2）**ML&RL 方法**，涵盖时间序列预测（LSTM（Sunny et al., 2020）、Autoformer（Wu et al., 2021）、PatchTST（Nie et al., 2022））和强化学习（DQN（Mnih et al., 2013）、DDPG（Liu et al., 2020））；（3）**基于 LLM 的智能体**，包括新闻驱动的 FinGPT（Liu et al., 2023）、记忆增强的 FinMem（Yu et al., 2024a）以及多智能体 TradingAgents（Xiao et al., 2025）。

### 表 2：数据（类型与时长）需求及 Sortino 比率比较（山寨币）

`M` 表示市场指标，`N` 表示外围新闻。

| 方法 | 数据需求 | Sortino↑ |
|---|---|---:|
| Grid | M > 30m | 0.16 |
| ETF&PCA | M > 7d | -0.33 |
| DDPG | M > 12h | 0.57 |
| PatchTST | M > 3d | 0.67 |
| FinMem | M&N > 1d | 0.41 |
| TradingAgents | M&N > 3d | 0.58 |
| TiMi（本文） | M > 4h | 0.91 |

### 4.2 经验结果

**回测比较。** 我们在 2024 年历史数据上进行评估，以建立基准表现。如表 1 所示，趋势跟随方法（例如 TSMOM）能够利用主流币市场中由 ETF 驱动的趋势，而 LLM 智能体则利用新闻和潜在后验信息。关键在于，TiMi 兼顾高盈利能力和严格风险控制，实现了更优的稳定性和风险调整后收益（尤其是在山寨币上 SR 达到 1.27）。这凸显了我们的系统在高波动、强反身性资产上的稳健性，而传统动量方法或纯语义分析在这些资产上往往面临困难。

**实盘交易比较。** 表 2 和表 3 展示了实盘交易环境中的综合性能指标。TiMi 看起来优于竞争方法，在美国股指期货、主流加密货币和山寨币市场分别实现 6.4%、8.0% 和 13.7% 的 ARR。值得注意的是，我们的系统展示了稳定的风险调整后收益，具有较好的夏普与 Sortino 比率以及有竞争力的回撤控制，说明其交易可持续性较强。关键的是，分钟级交易频率使部署后的机器人能够捕捉日频方法必然忽视的短期市场无效性。此外，TiMi 广泛的市场覆盖范围（`NP = 213`）与量化方法相当，并超过此前的 ML&RL 与智能体方法；后者通常由于收敛挑战和交易行动数据需求而只能支持较少交易对（见表 2，m/h/d 分别表示分钟/小时/天）。这些经验结果因此证明了我们的理性驱动范式能够转化为市场动态中可展示的交易有效性。

### 表 3：2025 年 1 月至 4 月实盘交易比较

`TF` 和 `NP` 分别表示每种方法的交易频率和支持交易对数量；`*` 表示来自部分实验的估计结果。

| 方法 | 美国股指 ARR% | SR | MDD% | 主流币 ARR% | SR | MDD% | 山寨币 ARR% | SR | MDD% | NP↑ | TF |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| MACD | 2.1 | 0.32 | 22.4 | -5.9 | -0.66 | 38.3 | -12.5 | -0.85 | 41.3 | 213 | daily |
| Momentum | 1.5 | 0.23 | 25.5 | -6.2 | -0.58 | 31.0 | -8.4 | -0.67 | 37.5 | 213 | daily |
| Grid Trading | 3.2 | 0.42 | 17.2 | 3.2 | 0.25 | 25.9 | 1.8 | 0.15 | 28.4 | 213 | hourly |
| Pairs Trading | 0.8 | 0.08 | 11.0 | 2.8 | 0.22 | 27.4 | 4.5 | 0.49 | 25.6 | 213 | daily |
| ETF&PCA | 4.1 | 0.50 | 19.1 | -2.5 | -0.26 | 22.3 | -4.8 | -0.31 | 27.3 | 75 | minute |
| TSMOM | 3.8 | 0.44 | 24.9 | -9.5 | -0.77 | 40.8 | -10.2 | -0.78 | 42.9 | 213 | daily |
| OFI | -1.9 | -0.18 | 18.4 | 5.2 | 0.58 | 27.8 | 5.4 | 0.52 | 29.3 | 213 | second |
| LSTM | 1.2 | 0.12 | 18.4 | 1.8 | 0.14 | 28.5 | 2.8 | 0.26 | 28.2 | 70* | daily |
| DQN | 1.7 | 0.11 | 25.2 | -1.0 | -0.06 | 31.7 | -2.3 | -0.18 | 39.0 | 70* | daily |
| DDPG | 5.1 | 0.53 | 22.7 | 5.8 | 0.63 | 27.9 | 5.9 | 0.54 | 38.1 | 150* | daily |
| Autoformer | 4.4 | 0.48 | 21.1 | 4.9 | 0.47 | 28.4 | 8.3 | 0.66 | 42.5 | 120* | daily |
| PatchTST | 5.5 | 0.62 | 22.8 | 2.7 | 0.25 | 29.0 | 6.4 | 0.63 | 35.4 | 120* | daily |
| FinGPT | 5.1 | 0.57 | 22.6 | -3.7 | -0.31 | 29.5 | -6.2 | -0.60 | 30.6 | 81 | daily |
| FinMem | 3.6 | 0.45 | 19.7 | 4.4 | 0.45 | 27.3 | 3.8 | 0.39 | 23.7 | 50* | daily |
| TradingAgents | 4.8 | 0.50 | 20.4 | 5.4 | 0.63 | 25.6 | 5.5 | 0.57 | 28.3 | 28* | daily |
| TiMi（本文） | 6.4 | 0.74 | 20.3 | 8.0 | 0.79 | 25.1 | 13.7 | 0.86 | 32.8 | 213 | minute |

**行动效率和资金管理。** 在图 3 左侧，我们记录了每个交易对一次行动周期的纯推理时间。受益于架构解耦，TiMi 实现了与量化方法相当的延迟，而这对于持续模型推理的方法而言从根本上难以实现。在图 3 右侧，我们将资金利用率计算为 `avg_P(已部署资金 / 可用资金)`。TiMi 在学习型方法中展现出明显优势，说明它能够在保持策略性仓位规模的同时，利用更广范围的交易机会。此外，我们给出了单位投入资金产生的利润/损失比率，TiMi 的比率为 1.53，优于 Grid（1.22）和 TradingAgents（1.32）。该指标意义重大，因为它量化了平衡盈利交易与亏损交易的效率。

**图 3：** 代表性方法的行动延迟（左）与资金利用率（右）比较。TiMi 的行动延迟为 137 ms，图中标注其相较部分 LLM 智能体方法约快 180 倍。

**图 4：** 不同方法在交易对上的年化收益率（ARR%）分布比较。图中显示 TiMi 的尾部风险事件小于 2%。

### 表 4：2024 年加密货币市场模拟中的组件级消融研究

| 方法 | 配置 | ARR%↑ | SR↑ | MDD%↓ | 实盘部署 |
|---|---|---:|---:|---:|---|
| TiMi | 完整系统 | 20.9 | 1.23 | 15.3 | 稳定 |
| `A_fr†` 变体 | 仅参数优化 | 12.5 | 0.92 | 16.3 | 逻辑不一致 |
| `A_fr‡` 变体 | 仅语义反思 | 1.1 | 0.05 | 25.1 | 稳定 |
| w/o `A_sa` | 统一策略 | 15.2 | 0.95 | 28.4 | 稳定 |
| w/o `A_fr` | 原型机器人 `B` | 1.1 | 0.05 | 25.1 | 运行不稳定 |
| w/o `A_sa` & `A_fr` | 最小基线 | -4.5 | -0.21 | 34.2 | 运行不稳定 |

### 4.3 分析研究

**表现分布的深入分析。** 根据图 4 的分布结果，最显著的是 TiMi 表现出明显的**性能稳定性**，方差更低（`σ = 11.03%`），尾部事件罕见（小于 2%），这表明与替代方法相比，它在市场动态中能取得更一致的回报。这一特征在算法交易中尤其有价值，因为灾难性回撤常常会抵消长期表现优势。与 DDPG 等 RL 方法对比时这一点很明显：尽管 DDPG 的中位收益具有竞争力，但其极端波动（`σ = 29.64%`）削弱了其在实际部署中的可靠性。TiMi 的理性驱动多智能体设计似乎能有效应对交易系统中回报最大化和风险最小化之间的内在权衡，并通过层次化优化和数学反思实现更有利的风险调整画像。

**智能体和优化的消融研究。** 以宏观分析智能体 `A_ma` 和机器人进化智能体 `A_be` 作为运行骨架，我们在 2024 年加密货币市场模拟中进行了细粒度的组件级消融实验，以隔离智能体专门化（即 `A_sa` 与 `A_fr`）和优化机制的贡献。如表 4 所量化，移除 `A_sa` 会使最大回撤几乎翻倍至 28.4%，凸显其在协调多样资产以获得一致风险敞口方面的关键作用（例如稳定型实用代币与高波动 meme 币）。在优化方面，仅语义的 `A_fr‡` 通过语法修复确保稳定性，但盈利能力停滞。相反，仅参数的 `A_fr†` 产生理论收益，却因代码-参数不一致而在实盘部署中表现出**逻辑不一致**；未经优化的基线则陷入**运行不稳定**。因此，只有完整系统能够维持“策略-部署-优化”链条，这一点也由图 5 中的演化轨迹证实：未经优化的 `B` 在盈亏平衡附近停滞，`B(1)` 尽管出现过短暂 35% 的峰值却发生退化，暴露出缺乏结构性适配的浅层参数调优之脆弱；而稳定后的 `B(3)` 最终形成 `B*`，实现超过 20% 的持续收益，验证了第 2.5 节和图 2 中详述的基于约束求解和层次化干预的迭代有效性。

**图 5：** 交易机器人变体 `B`、`B*` 及其中间版本（1/3 轮优化）在 2024 年加密货币市场模拟中的比较。

**交易可视化。** 图 6 展示了四个代表性加密货币交易对上分钟级交易的实证证据。K 线图展示了 `B*` 中实现的自适应订单策略，买入（↑）与卖出（↓）标记精确标示交易点。值得注意的是，SIGN/USDT（82.21%）和 OM/USDT（74.39%）等高波动交易对取得更优的盈利指标（PnL 分别为 +32.75% 与 +10.78%），并具有相应更高的订单密度（39 和 28 个有效订单），说明系统能够利用价格振荡获利。相反，TRUMP/USDT 和 XRP/USDT 等低波动资产呈现更保守的交易模式。这些可视化结果证明，通过具有数学反馈的深度优化循环调优后的参数矩阵 `M_P` 和 `M_Q` 能够有效地**按交易对特定波动率调节订单执行强度**，同时在包括持续方向性运动、盘整阶段和极端价格行为在内的多样市场条件下保持稳健风险管理。

**图 6：TiMi 在四个代表性加密货币交易对上的详细交易。**

- 案例 1：V 形反转，OM/USDT，2025-04-15；日内成交量 16.3 亿，日内波动率 74.39%，有效订单 61，已实现 PnL +10.78%。
- 案例 2：强上升趋势与盘整，XRP/USDT，2025-04-07；日内成交量 69.7 亿，日内波动率 20.39%，有效订单 2，已实现 PnL +1.19%。
- 案例 3：头肩顶形态，TRUMP/USDT，2025-04-24；日内成交量 17.1 亿，日内波动率 15.67%，有效订单 33，已实现 PnL +5.56%。
- 案例 4：隐性下跌与垂直反转，SIGN/USDT，2025-04-29；日内成交量 16.7 亿，日内波动率 82.21%，有效订单 45，已实现 PnL +32.75%。

这些 15 分钟 K 线图展示了市场运动，绿色蜡烛表示价格上涨，红色蜡烛表示价格下跌。TiMi 执行的买入（↑）与卖出（↓）动作标记在各图上，展示了其在上升趋势、下降趋势、盘整期和极端价格运动等多种市场动态下的稳健交易能力。

## 5 相关工作

**LLM 驱动的智能体系统。** 基于 LLM 构建的智能体系统可按自主性水平分为智能体工作流与自主智能体（Zhuge et al., 2023; Hong et al., 2024a; Zhang et al., 2024b）。前者遵循预定义流程并进行多次 LLM 调用，后者则采用灵活决策。智能体工作流可大致分为通用型和领域特定型。工作流进一步分为通用方法（Wei et al., 2022; Madaan et al., 2023）与领域特定方法，例如代码生成（Hong et al., 2024b; Zhong et al., 2024a）、数据分析（Xie et al., 2024; Li et al., 2024a）和数学问题求解（Zhong et al., 2024b; Xin et al., 2024）。研究还通过自动提示优化（Fernando et al., 2024; Yang et al., 2024）、超参数优化（Saad-Falcon et al., 2024）和工作流优化（Hu et al., 2024; Zhang et al., 2025）推进智能体优化。本文提出的金融交易 TiMi 是领域特定实现的一个例子，而其层次化反思也为智能体优化提供了启发；我们将持续探索理性驱动智能体系统作为通用系统的潜力。

**金融交易智能体。** 金融交易智能体可分为三种架构（Ding et al., 2024）：新闻驱动、反思驱动和因子优化框架。新闻驱动智能体（Zhang et al., 2023; Wang et al., 2024a）纳入最新新闻和事件以做出知情决策，代表方法包括 FinMem（Yu et al., 2024a）、FinAgent（Zhang et al., 2024c）和 CryptoTrade（Li et al., 2024b）。反思驱动智能体（Xing, 2025; Koa et al., 2024）通过反思和辩论增强决策。例如，StockAgent（Zhang et al., 2024a）和 TradingAgents（Xiao et al., 2025）实现多智能体框架，以模拟投资者交易行为并进行基于角色的协作；Fincon（Yu et al., 2024b）引入概念性语言强化以精炼决策。除了直接交易之外，其他智能体（Wang et al., 2024b; 2023）也作为量化策略的 alpha 因子优化器发挥作用。本文协调智能体的策略深度与量化交易所期望的机械理性，并开创一种解耦范式，强调渐进式策略开发和量化级部署。

## 6 结论

本文提出 TiMi，这是一种为算法交易而设计、具有机械理性的多智能体系统，它将复杂分析与时间敏感执行解耦。通过策略、优化和部署三个阶段，TiMi 在多样金融市场中展现出有前景且稳定的表现。我们的关键创新包括：（1）利用 LLM 在语义分析、代码编程和数学推理方面专门能力的多智能体架构；（2）分离分析与部署的解耦机制；（3）从宏观模式到微观定制的两层分析范式；（4）交易机器人实现的分层编程设计；（5）由数学反思驱动的闭环优化系统。

**局限性与伦理声明。** 优化阶段的必要性限制了由 TiMi 开发的交易机器人在迁移到新市场时的零样本表现。从更广阔的角度看，自动交易系统的进步可能影响市场动态和流动性供给，而市场公平性和可获得性问题也可能加大机构投资者与散户之间的差距。我们的目标是探索可定制智能体交易系统的发展，本文不构成投资建议——投资有风险，入市需谨慎。

## 7 致谢

本工作得到国家自然科学基金（编号 U25A20527、62473286）资助。本工作也得到上海市重大科技专项（编号 2025SHZDZX025G10）资助。

## 参考文献

Marco Avellaneda and Jeong-Hyun Lee. Statistical arbitrage in the us equities market. Quantitative Finance, 10(7):761-782, 2010.

Zheng Cai, Maosong Cao, Haojiong Chen, Kai Chen, Keyu Chen, Xin Chen, Xun Chen, Zehui Chen, Zhi Chen, Pei Chu, et al. Internlm2 technical report. arXiv preprint arXiv:2403.17297, 2024.

Rama Cont and Adrien De Larrard. Price dynamics in a markovian limit order market. SIAM Journal on Financial Mathematics, 4(1):1-25, 2013.

Han Ding, Yinheng Li, Junhao Wang, and Hang Chen. Large language model agent in financial trading: A survey. arXiv preprint arXiv:2408.06361, 2024.

Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, Yusheng Su, Shengding Hu, Yulin Chen, Chi-Min Chan, Weize Chen, et al. Parameter-efficient fine-tuning of large-scale pre-trained language models. Nature Machine Intelligence, 5(3):220-235, 2023.

Chrisantha Fernando, Dylan Sunil Banarse, Henryk Michalewski, Simon Osindero, and Tim Rocktaschel. Promptbreeder: Self-referential self-improvement via prompt evolution. In International Conference on Machine Learning, pp. 13481-13544. PMLR, 2024.

Evan Gatev, William N Goetzmann, and K Geert Rouwenhorst. Pairs trading: Performance of a relative-value arbitrage rule. The review of financial studies, 19(3):797-827, 2006.

Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The llama 3 herd of models. arXiv preprint arXiv:2407.21783, 2024.

John M Griffin, Jeffrey H Harris, and Selim Topaloglu. The dynamics of institutional and individual trading. The Journal of Finance, 58(6):2285-2320, 2003.

Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. arXiv preprint arXiv:2501.12948, 2025.

Joel Hasbrouck. Empirical market microstructure: The institutions, economics, and econometrics of securities trading. Oxford University Press, 2007.

Sirui Hong, Yizhang Lin, Bang Liu, Bangbang Liu, Binhao Wu, Ceyao Zhang, Chenxing Wei, Danyang Li, Jiaqi Chen, Jiayi Zhang, et al. Data interpreter: An llm agent for data science. arXiv preprint arXiv:2402.18679, 2024a.

Sirui Hong, Mingchen Zhuge, Jonathan Chen, Xiawu Zheng, Yuheng Cheng, Jinlin Wang, Ceyao Zhang, Zili Wang, Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu, and Jurgen Schmidhuber. Metagpt: Meta programming for A multi-agent collaborative framework. In ICLR. OpenReview.net, 2024b.

Shengran Hu, Cong Lu, and Jeff Clune. Automated design of agentic systems. arXiv preprint arXiv:2408.08435, 2024.

Narasimhan Jegadeesh and Sheridan Titman. Returns to buying winners and selling losers: Implications for stock market efficiency. The Journal of finance, 48(1):65-91, 1993.

Kelvin JL Koa, Yunshan Ma, Ritchie Ng, and Tat-Seng Chua. Learning to generate explainable stock predictions using self-reflective large language models. In Proceedings of the ACM Web Conference 2024, pp. 4304-4315, 2024.

Boyan Li, Yuyu Luo, Chengliang Chai, Guoliang Li, and Nan Tang. The dawn of natural language to SQL: are we fully ready? Proc. VLDB Endow., 17(11):3318-3331, 2024a.

Yang Li, Yangyang Yu, Haohang Li, Zhi Chen, and Khaldoun Khashanah. Tradinggpt: Multi-agent system with layered memory and distinct characters for enhanced financial trading performance. arXiv preprint arXiv:2309.03736, 2023.

Yuan Li, Bingqiao Luo, Qian Wang, Nuo Chen, Xu Liu, and Bingsheng He. Cryptotrade: A reflective llm-based agent to guide zero-shot cryptocurrency trading. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pp. 1094-1106, 2024b.

Xiao-Yang Liu, Hongyang Yang, Qian Chen, Runjia Zhang, Liuqing Yang, Bowen Xiao, and Christina Dan Wang. Finrl: A deep reinforcement learning library for automated stock trading in quantitative finance. arXiv preprint arXiv:2011.09607, 2020.

Xiao-Yang Liu, Guoxuan Wang, Hongyang Yang, and Daochen Zha. Fingpt: Democratizing internet-scale data for financial large language models. arXiv preprint arXiv:2307.10485, 2023.

Andrew W Lo, Harry Mamaysky, and Jiang Wang. Foundations of technical analysis: Computational algorithms, statistical inference, and empirical implementation. The journal of finance, 55(4):1705-1765, 2000.

Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al. Self-refine: Iterative refinement with self-feedback. In Thirty-seventh Conference on Neural Information Processing Systems, 2023.

Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Alex Graves, Ioannis Antonoglou, Daan Wierstra, and Martin Riedmiller. Playing atari with deep reinforcement learning. arXiv preprint arXiv:1312.5602, 2013.

Tobias J Moskowitz, Yao Hua Ooi, and Lasse Heje Pedersen. Time series momentum. Journal of financial economics, 104(2):228-250, 2012.

Yuqi Nie, Nam H Nguyen, Phanwadee Sinthong, and Jayant Kalagnanam. A time series is worth 64 words: Long-term forecasting with transformers. arXiv preprint arXiv:2211.14730, 2022.

OpenAI. Gpt-4 technical report. Technical report, 2023.

Eckhard Platen and David Heath. A benchmark approach to quantitative finance. Springer Science & Business Media, 2006.

Jon Saad-Falcon, Adrian Gamarra Lafuente, Shlok Natarajan, Nahum Maru, Hristo Todorov, Etash Guha, E. Kelly Buchanan, Mayee Chen, Neel Guha, Christopher Re, and Azalia Mirhoseini. Archon: An architecture search framework for inference-time techniques. arXiv preprint arXiv:2409.15254, 2024.

Zifan Song, Yudong Wang, Wenwei Zhang, Kuikun Liu, Chengqi Lyu, Demin Song, Qipeng Guo, Hang Yan, Dahua Lin, Kai Chen, et al. Alchemistcoder: Harmonizing and eliciting code capability by hindsight tuning on multi-source data. In The Thirty-eighth Annual Conference on Neural Information Processing Systems, 2024.

Shuo Sun, Molei Qin, Wentao Zhang, Haochong Xia, Chuqiao Zong, Jie Ying, Yonggang Xie, Lingxuan Zhao, Xinrun Wang, and Bo An. Trademaster: a holistic quantitative trading platform empowered by reinforcement learning. Advances in Neural Information Processing Systems, 36:59047-59061, 2023.

Md Arif Istiake Sunny, Mirza Mohd Shahriar Maswood, and Abdullah G Alharbi. Deep learning-based stock price prediction using lstm and bi-directional lstm model. In 2020 2nd novel intelligent and leading emerging sciences conference (NILES), pp. 87-92. IEEE, 2020.

Jiachen T Wang, Prateek Mittal, Dawn Song, and Ruoxi Jia. Data shapley in one training run. In The Thirteenth International Conference on Learning Representations, 2025.

Jian Wang and Junseok Kim. Predicting stock price trend using macd optimized by historical volatility. Mathematical Problems in Engineering, 2018(1):9280590, 2018.

Meiyun Wang, Kiyoshi Izumi, and Hiroki Sakaji. Llmfactor: Extracting profitable factors through prompts for explainable stock movement prediction. arXiv preprint arXiv:2406.10811, 2024a.

Saizhuo Wang, Hang Yuan, Leon Zhou, Lionel M Ni, Heung-Yeung Shum, and Jian Guo. Alpha-gpt: Human-ai interactive alpha mining for quantitative investment. arXiv preprint arXiv:2308.00016, 2023.

Saizhuo Wang, Hang Yuan, Lionel M Ni, and Jian Guo. Quantagent: Seeking holy grail in trading by self-improving large language model. arXiv preprint arXiv:2402.03755, 2024b.

Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. Advances in Neural Information Processing Systems, 35:24824-24837, 2022.

Paul Wilmott. Paul Wilmott on quantitative finance. John Wiley & Sons, 2013.

Haixu Wu, Jiehui Xu, Jianmin Wang, and Mingsheng Long. Autoformer: Decomposition transformers with auto-correlation for long-term series forecasting. Advances in neural information processing systems, 34:22419-22430, 2021.

Yijia Xiao, Edward Sun, Di Luo, and Wei Wang. Tradingagents: Multi-agents llm financial trading framework, 2025. URL https://arxiv.org/abs/2412.20138.

Yupeng Xie, Yuyu Luo, Guoliang Li, and Nan Tang. Haichart: Human and AI paired visualization system. Proc. VLDB Endow., 17(11):3178-3191, 2024.

Huajian Xin, Daya Guo, Zhihong Shao, Zhizhou Ren, Qihao Zhu, Bo Liu, Chong Ruan, Wenda Li, and Xiaodan Liang. Deepseek-prover: Advancing theorem proving in llms through large-scale synthetic data. arXiv preprint arXiv:2405.14333, 2024.

Frank Xing. Designing heterogeneous llm agents for financial sentiment analysis. arXiv preprint arXiv:2401.05799, 2025.

Chengrun Yang, Xuezhi Wang, Yifeng Lu, Hanxiao Liu, Quoc V. Le, Denny Zhou, and Xinyun Chen. Large language models as optimizers. In ICLR. OpenReview.net, 2024.

Yangyang Yu, Haohang Li, Zhi Chen, Yuechen Jiang, Yang Li, Denghui Zhang, Rong Liu, Jordan W Suchow, and Khaldoun Khashanah. Finmem: A performance-enhanced llm trading agent with layered memory and character design. In Proceedings of the AAAI Symposium Series, volume 3, pp. 595-597, 2024a.

Yangyang Yu, Zhiyuan Yao, Haohang Li, Zhiyang Deng, Yuechen Jiang, Yupeng Cao, Zhi Chen, Jordan Suchow, Zhenyu Cui, Rong Liu, et al. Fincon: A synthesized llm multi-agent system with conceptual verbal reinforcement for enhanced financial decision making. Advances in Neural Information Processing Systems, 37:137010-137045, 2024b.

Chong Zhang, Xinyi Liu, Zhongmou Zhang, Mingyu Jin, Lingyao Li, Zhenting Wang, Wenyue Hua, Dong Shu, Suiyuan Zhu, Xiaobo Jin, et al. When ai meets finance (stockagent): Large language model-based stock trading in simulated real-world environments. arXiv preprint arXiv:2407.18957, 2024a.

Haohan Zhang, Fengrui Hua, Chengjin Xu, Hao Kong, Ruiting Zuo, and Jian Guo. Unveiling the potential of sentiment: can large language models predict chinese stock price movements? arXiv preprint arXiv:2306.14222, 2023.

Jiayi Zhang, Chuang Zhao, Yihan Zhao, Zhaoyang Yu, Ming He, and Jianping Fan. Mobileexperts: A dynamic tool-enabled agent team in mobile devices. CoRR, abs/2407.03913, 2024b.

Jiayi Zhang, Jinyu Xiang, Zhaoyang Yu, Fengwei Teng, Xiong-Hui Chen, Jiaqi Chen, Mingchen Zhuge, Xin Cheng, Sirui Hong, Jinlin Wang, et al. Aflow: Automating agentic workflow generation. In The Thirteenth International Conference on Learning Representations, 2025.

Wentao Zhang, Lingxuan Zhao, Haochong Xia, Shuo Sun, Jiaze Sun, Molei Qin, Xinyi Li, Yuqing Zhao, Yilei Zhao, Xinyu Cai, et al. A multimodal foundation agent for financial trading: Tool-augmented, diversified, and generalist. In Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, pp. 4314-4325, 2024c.

Li Zhong, Zilong Wang, and Jingbo Shang. Debug like a human: A large language model debugger via verifying runtime execution step by step. In ACL (Findings), pp. 851-870. Association for Computational Linguistics, 2024a.

Qihuang Zhong, Kang Wang, Ziyang Xu, Juhua Liu, Liang Ding, Bo Du, and Dacheng Tao. Achieving > 97% on gsm8k: Deeply understanding the problems makes llms perfect reasoners. arXiv preprint arXiv:2404.14963, 2024b.

Lianghui Zhu, Xinggang Wang, and Xinlong Wang. Judgelm: Fine-tuned large language models are scalable judges. In The Thirteenth International Conference on Learning Representations, 2025.

Mingchen Zhuge, Haozhe Liu, Francesco Faccio, Dylan R Ashley, Robert Csordas, Anand Gopalakrishnan, Abdullah Hamdi, Hasan Abed Al Kader Hammoud, Vincent Herrmann, Kazuki Irie, et al. Mindstorms in natural language-based societies of mind. arXiv preprint arXiv:2305.17066, 2023.

## 附录 A 参数求解中的数学推理深入说明

本节提供 TiMi 对 `B*` 的三个实践案例。每个案例都展示了算法交易中常见的一种不同模式。通过这些代表性场景，我们旨在说明 TiMi 如何将定性风险转化为定量优化，从而弥合观测到的交易病灶与系统性参数精炼之间的差距。

### A.1 案例 1：市场波动下的仓位规模控制

经过一段模拟期后，系统收集在 OM/USDT 交易对上运行的交易机器人反馈 `F`。反馈以结构化数据组织，包括：（1）最终收益、最大回撤和夏普比率等**表现指标**；（2）包含有效交易和持仓详细记录的**交易日志**；（3）包含 OM/USDT K 线（通常包括分钟级和小时级数据）、波动率、流动性、资金费率变化和市值的**市场数据**。

反馈记录显示，在一次剧烈的 30 分钟市场下跌中，该机器人出现了超过 50% 的显著回撤。当价格下跌时，它执行了一系列过于密集的买单，导致仓位过大且深度浮亏。反馈反思智能体 `A_fr` 分析该反馈并识别出风险场景 `R = γ(F)`：**订单密度和规模对突发波动率飙升的适应不足**。

随后，`A_fr` 将这一风险场景转化为形式化数学约束（线性规划问题），目标是在未来类似情形中限制潜在损失。如第 3 节所述，相关参数似乎是订单数量分布矩阵 `M_Q = [q_1, q_2, ..., q_m]` 和资本分配 `A`，第 `i` 层订单的数量为 `Q_i = A × M_Q[i] × c_m × c_f`。因此，智能体可以对总仓位规模建立直接约束：在极端场景下所有成交买单的规模不得超过最大规模 `Q_max`。具体而言，我们得到关于参数 `q_i` 的线性不等式：

```text
Σ_{i=1}^{m} Q_i ≤ Q_max
=> Σ_{i=1}^{m} q_i ≤ Q_max / (A × c_m × c_f)
```

其中 `Q_max` 可由风险容忍度推导，即由全局资本和平行交易量决定。这构成了公式 3 中不等式 `A(R)Θ ⪯ b(R)` 的一个具体变体。在该案例中，参数向量 `Θ` 包含待优化元素 `q_i`，约束矩阵 `A(R)` 中对应行将为 `[1, 1, ..., 1]`，约束向量 `b(R)` 中对应值为 `Q_max / (A × c_m × c_f)`。

### A.2 案例 2：价格暴涨事件中的订单边界校准

在 DOGE/USDT 上的机器人经过一段模拟交易期后，TiMi 收集结构化反馈 `F`，包括：（1）显示投资组合灾难性下降和最大回撤过大的**表现指标**；（2）显示最高层级卖单在价格继续暴涨时被触发、导致亏损快速累积的**交易日志**；（3）包含捕捉价格暴涨事件的分钟级 K 线信息的**市场数据**。

首先，反馈反思智能体 `A_fr` 分析该反馈并识别出关键风险场景 `R = γ(F)`：**订单组的上边界未能根据失败事件中观测到的波动率进行充分校准**。随后，`A_fr` 将该风险场景转化为形式化数学约束。

根据算法 1，价格层级由订单分布矩阵 `M_P = [p_1, p_2, ..., p_m]` 决定。因此，智能体可以针对暴涨过程中的绝对峰值价格，对最高价格指数建立约束：

```text
P_before × (1 + Φ)^{p_m} > P_peak
```

取对数后，可得到关于参数 `p_m` 的可求解不等式：

```text
p_m > log(P_peak / P_before) / log(1 + Φ)
```

其中 `P_peak` 和 `P_before` 从市场数据中提取。该约束在不等式系统 `A(R)Θ ⪯ b(R)` 中为 `p_m` 建立了基于证据的下界。

### A.3 案例 3：趋势市场条件下的自适应止盈

在 NQ 股指期货上经过一段模拟期后，系统从交易机器人收集结构化反馈 `F`，包括：（1）最终收益、利润因子和与买入并持有收益比较等**表现指标**；（2）包含详细记录的**交易日志**，这些记录表明盈利多头仓位存在系统性过早平仓；（3）NQ 期货 K 线、趋势强度指标（例如 ADX）以及趋势期与震荡期历史波动率等**市场数据**。

反馈表明，已部署机器人虽然持续获取小额利润，但在一次持续市场上涨中表现不佳。其利润因子较高，但总收益低于简单的买入并持有策略。对交易日志的分析显示，盈利多头仓位平仓过早，只捕捉到实际向上价格运动的一小部分。反馈反思智能体 `A_fr` 分析该反馈，并识别出风险场景（或机会成本）`R = γ(F)`：**止盈阈值过于保守，未能适应强趋势持续性**。

随后，`A_fr` 将这一机会成本场景转化为形式化数学约束。如第 3 节所述，相关参数包括盈亏阈值矩阵 `H = [h_1, h_2, ..., h_k]`，它决定退出点 `P_entry × (1 ± Φ)^{H[i]}`。因此，智能体可以对最低止盈水平建立约束：任意仓位的第一止盈目标必须设置得足够宽，以捕捉先前趋势阶段中观测到的平均价格运动。

接下来，我们得到关于参数 `h_1` 的线性不等式。第一止盈价格 `P_1 = P_entry × (1 + Φ)^{h_1}` 必须满足：

```text
P_1 - P_entry ≥ ΔP_trend
```

其中 `ΔP_trend` 表示市场趋势期间的平均盈利运动。这得到不等式：

```text
(1 + Φ)^{h_1} ≥ 1 + ΔP_trend / P_entry
```

取对数后可简化为：

```text
h_1 ≥ log_{1+Φ}(1 + ΔP_trend / P_entry)
```

## 附录 B 部署实现细节

**可复现性声明。** 为便于复现，我们提供 TiMi 系统的更多实现细节，涵盖订单细节、交易所选择、风险控制机制、交易成本建模和行动延迟控制。这些技术细节展示了在实盘交易环境中部署该系统所需的实践考虑。关键的是，我们将开源用于部署的 TiMi 产品实现，并发布关键边界案例列表（来自回测模拟和实盘部署）。

**订单类型与交易所选择。** TiMi 为特定交易功能采用三类订单：（1）LIMIT 订单作为基于波动率推导公式开仓的唯一机制；（2）TAKE PROFIT 和 STOP 订单在仓位监控期间动态放置和取消；（3）MARKET 订单用于风险管理目的，包括清算低风险仓位和执行全局盈亏事件。我们选择高流动性的一线交易所，即股指期货使用 CME，加密货币使用 Binance。

**交易成本和滑点建模。** 我们建模并缓释两类主要成本：订单费用和周期性资金费率。TiMi 使用 LIMIT 订单入场，以获取有利的 maker 费率并消除入场滑点。除静态费用外，TiMi 还按交易对适应资金费率。例如，较高的资金费率会触发订单减少（甚至停用），以避免积累持有成本过高的仓位。系统还会进行交易前价格偏离检查，以防止在极端波动和潜在滑点期间发生非预期行动。真实交易成本记录见补充材料。

### 表 5：已部署 TiMi 的行动延迟分解（毫秒）

| 延迟来源 | 平均值 | 标准差 | P99 |
|---|---:|---:|---:|
| 市场检索 | 85 | 12 | 115 |
| 内部逻辑 | 5 | <1 | 5 |
| 交易请求 | 47 | 8 | 65 |
| 端到端总计 | 137 | 15 | 185 |

**行动延迟控制。** 表 5 给出了包含方差的详细延迟记录。延迟以及更重要的尾部延迟的主要来源是**外部因素**：与交易所往返时间（RTT）相关的网络 I/O。在稳定网络环境中，TiMi 的行动延迟是稳健的。为跟踪外部问题，TiMi 逐步实现了工程优化（例如图 2 所示的动态缓存和线程执行器），并配备一系列保护措施，包括超时、状态检查和熔断器。

**错误处理的故障转移机制。** 在函数层，所有外部 API 交互都封装在带有速率限制管理的异常处理逻辑中。在进程层，并发任务中的失败被隔离，以保证服务连续性。此外，TiMi 集成了价格偏离检查，并定期清除孤儿订单，以防止市场异常下的错误行动。在系统层，状态信息直接从交易所获取，从而实现无状态执行逻辑。这使机器人可以随时恢复，而不会丢失交易上下文。

## 附录 C 智能体组件消融分析

总体而言，TiMi 系统被设计为一种**高度协同**的架构。各智能体并非组件集合而已，它们的功能深度联结，用于执行“策略-部署-优化”链条。为进一步理解每个智能体的贡献，我们在下文提供组件级消融研究。

- **宏观分析智能体 `A_ma` 与机器人进化智能体 `A_be`**：`A_ma` 从市场数据中提供初始策略假设，`A_be` 将抽象策略转化为可执行代码，作为通向部署的关键桥梁。因此，这些智能体构成 TiMi **不可或缺的骨架**，缺少它们将导致整个系统无法运行，因而无法对其进行消融。
- **策略适配智能体 `A_sa`**：表 6 进一步给出了在 2025 年山寨币期货市场中模拟的 `A_sa` 消融结果。关键洞见是，尽管 `A_sa` 能改善风险调整后收益，但其最关键贡献是降低跨交易对收益方差，从而在多样市场中增强稳健性和表现一致性。
- **反馈反思智能体 `A_fr`**：`A_fr` 的有效性由表 4 和图 5 中的消融研究从经验上验证。缺少优化阶段的原型机器人 `B` 在接近盈亏平衡处停滞。相比之下，经由 `A_fr` 渐进精炼的高级机器人 `B*` 实现了持续增长，最终收益超过 20%。关键在于，`A_fr` 在所提出的层次化优化方案中实现参数求解。如第 2.5 节并在图 2 中可视化所示，该方案的必要性由以下对比确认：仅经过浅层参数级调优的机器人会出现不稳定的短暂收益，而在更高函数层和策略层被精炼的机器人则能保持持续盈利。

### 表 6：2025 年山寨币市场中策略适配智能体 `A_sa` 的消融研究

`σ_ARR` 表示各交易对年化收益的标准差，用于衡量跨交易对稳定性。

| 方法 | 配置 | ARR%↑ | SR↑ | MDD%↓ | σARR%↓ |
|---|---|---:|---:|---:|---:|
| TiMi | 完整系统 | 13.7 | 0.86 | 32.8 | 11.0 |
| w/o `A_sa` | 统一策略 | 10.4 | 0.71 | 38.2 | 19.5 |

## 附录 D 大型语言模型（LLM）的使用

我们仅使用 LLM 检查语法并润色写作。重要的是，LLM 没有参与研究问题的构思，也没有参与核心方法的发展。
