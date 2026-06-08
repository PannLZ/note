### todo

- [x] 使用recbole https://recbole.io/index.html 跑通LightGCN模型（协同过滤场景）和SASRec模型（序列推荐场景），数据集随便选recbole自带的
- [x] 尝试用自定义的数据加载的方式读入第三方自定义的数据集
- [x] 查看recbole评测指标的源码，理解recall，hit，ndcg，mrr这些常用指标的计算和实现方式
- [ ] 大致阅读recbole中LightGCN和SASRec模型部分的源码，看模型是怎么工作的，比如GNN和Transformer怎么调用，embedding怎么传进去的，loss怎么计算的。这部分可以对照着文章来看

### customize dataloaders

**什么时候需要自定义 DataLoader**

如果写了一个新模型，而这个模型对数据读取方式有特殊要求，比如不是普通的 user-item interaction batch，或者需要特殊采样、特殊 batch 组织方式，就需要自己写 DataLoader

**. RecBole 里两个抽象 DataLoader**

AbstractDataLoader

这是最基础的 DataLoader。它主要关心三个属性：

- pr：当前读取位置的指针
- batch_size：一个 batch 最多包含多少交互
- step：每次迭代指针前进多少

继承它时通常要实现 4 个方法：

- _init_batch_size_and_step()：初始化 batch_size 和 step
- pr_end：告诉 DataLoader 什么时候读完
- _shuffle()：如何打乱数据
- _next_batch_data()：如何取出下一个 batch，并返回 RecBole 的 Interaction 格式

NegSampleDataLoader

它继承自 AbstractDataLoader，主要用于**负采样**。它已经内置了 pair-wise sampling 和 point-wise sampling 的负采样逻辑

**Interaction** 一个 batch 的推荐数据容器，eg

Interaction({
    "user_id": tensor([1, 1, 2, 3]),
    "item_id": tensor([10, 20, 15, 8]),
    "rating": tensor([5, 4, 3, 5])
}

```python 
class UserDataLoader(AbstractDataLoader):
    """:class:`UserDataLoader` will return a batch of data which only contains user-id when it is iterated.

    Args:
        config (Config): The config of dataloader.
        dataset (Dataset): The dataset of dataloader.
        sampler (Sampler): The sampler of dataloader.
        shuffle (bool, optional): Whether the dataloader will be shuffle after a round. Defaults to ``False``.

    Attributes:
        shuffle (bool): Whether the dataloader will be shuffle after a round.
            However, in :class:`UserDataLoader`, it's guaranteed to be ``True``.
    """

    dl_type = DataLoaderType.ORIGIN

    def __init__(self, config, dataset, sampler, shuffle=False):
        if shuffle is False:
            shuffle = True
            self.logger.warning('UserDataLoader must shuffle the data.')

        self.uid_field = dataset.uid_field
        """dataset.uid_field 是用户 id 字段名，之前在配置文件中写过该字段"""
        self.user_list = Interaction({self.uid_field: torch.arange(dataset.user_num)})

        super().__init__(config, dataset, sampler, shuffle=shuffle)

    def _init_batch_size_and_step(self):
        batch_size = self.config['train_batch_size']
        self.step = batch_size
        self.set_batch_size(batch_size)

    @property
    def pr_end(self):
        return len(self.user_list)

    def _shuffle(self):
        self.user_list.shuffle()

    def _next_batch_data(self):
        cur_data = self.user_list[self.pr:self.pr + self.step]
        self.pr += self.step
        return cur_data
"""
维护一个 user_id 列表
每次按 batch_size 切一段
返回 RecBole 标准格式 Interaction
如Interaction({
    "user_id": tensor([3, 0])
})
"""
```

**TrainDataLoader**

collate_fn：PyTorch DataLoader 会传进来一批样本下标->转成 numpy array->对 batch 做 RecBole 内部 transform->

### 评测指标

```python
class TopkMetric
    used_info()负责从评测数据结构里取出rec.topk
        pos_index: 每个用户 top-k 推荐列表中，每个位置是否命中正样本
        pos_len: 每个用户真实正样本数量
        rec_mat = dataobject.get("rec.topk")
        topk_idx, pos_len_list = torch.split(rec_mat, [max(self.topk), 1], dim=1)
        return topk_idx.to(torch.bool).numpy(), pos_len_list.squeeze(-1).numpy()
    topk_result() 负责把每个用户、每个 k 的结果取平均
    	avg_result = value.mean(axis=0)
        for k in self.topk:
            key = "{}@{}".format(metric, k)
            metric_dict[key] = round(avg_result[k - 1], self.decimal_place)
```



#### recall

召回率。看用户真实喜欢的物品里，有多少被推荐进了前 K 个。

```python 
metric_info()
	return np.cumsum(pos_index, axis=1) / pos_len.reshape(-1, 1)

```

#### hit

命中率。看推荐**前 K 里面**()是否至少有一个真实相关物品。

只要命中 >= 1，Hit@K = 1
否则 Hit@K = 0

```python 
metric_info()
    result = np.cumsum(pos_index, axis=1)(cumsum前缀和)
    return (result > 0).astype(int)
```

#### ndcg

归一化折损累计增益。它不仅看有没有命中，还看命中的位置靠不靠前。

- DCG：模型实际推荐列表的折扣累计收益
- IDCG：理想情况下的最大 DCG

```python 
metric_info()
    iranks = np.zeros_like(pos_index, dtype=np.float)
    iranks[:, :] = np.arange(1, pos_index.shape[1] + 1)
    
    ranks = np.zeros_like(pos_index, dtype=np.float)
    ranks[:, :] = np.arange(1, pos_index.shape[1] + 1)
    dcg = 1.0 / np.log2(ranks + 1)
"""dcg保存每个位置的折扣权重"""
	dcg = np.cumsum(np.where(pos_index, dcg, 0), axis=1)
    idcg = np.cumsum(1.0 / np.log2(iranks + 1), axis=1)
    result = dcg / idcg
```



#### mrr

平均倒数排名。看第一个命中的真实物品出现在第几位。

```python 
metric_info()
	idxs = pos_index.argmax(axis=1)
    找第一个命中的位置，然后取倒数排名
```



### LightGCN

```PYTHON
self.user_embedding = torch.nn.Embedding(
	num_embeddings=self.n_users, embedding_dim=self.latent_dim
)
self.norm_adj_matrix = self.get_norm_adj_mat().to(self.device)
    self.interaction_matrix = dataset.inter_matrix(form="coo")用户-物品交互矩阵 R
LightGCN 不是直接在 R 上传播，而是把用户和物品看成一张图，如果用户 u 和物品 i 有交互，就在图里连一条边
A = [ 0    R  ]
    [ R^T  0  ]
上半部分表示 user 到 item，
下半部分表示 item 到 user

user_embeddings = self.user_embedding.weight
item_embeddings = self.item_embedding.weight
ego_embeddings = torch.cat([user_embeddings, item_embeddings], dim=0)
[n_users + n_items, embedding_size]

all_embeddings = torch.sparse.mm(self.norm_adj_matrix, all_embeddings)
用归一化后的 user-item 图邻接矩阵，去更新所有 user 和 item 的 embedding
每个节点的新 embedding = 它所有邻居 embedding 的加权求和

        # calculate BPR Loss
        pos_scores = torch.mul(u_embeddings, pos_embeddings).sum(dim=1)
        neg_scores = torch.mul(u_embeddings, neg_embeddings).sum(dim=1)
        mf_loss = self.mf_loss(pos_scores, neg_scores)

        # calculate regularization Loss
        u_ego_embeddings = self.user_embedding(user)
        pos_ego_embeddings = self.item_embedding(pos_item)
        neg_ego_embeddings = self.item_embedding(neg_item)
MyDataLoader / TrainDataLoader

→ 产生 user_id, item_id, neg_item_id
→ LightGCN.forward()
→ 得到传播后的 user/item embedding
→ 取出当前 batch 的 user、正 item、负 item embedding
→ 点积得到 pos_scores 和 neg_scores
→ BPRLoss(pos_scores, neg_scores) 
	-log(sigmoid(pos_score - neg_score))
→ 加上 EmbLoss 正则（loss = mf_loss + self.reg_weight * reg_loss）
→ 返回最终 loss
```

**让用户向自己交互过的物品学习，让物品向喜欢过它的用户学习，多传几轮后，把每一轮的表示加权平均，再用用户向量和物品向量的内积做推荐**

### SASrec

```python
模型初始化
self.item_embedding = nn.Embedding(
    self.n_items, self.hidden_size, padding_idx=0
)
self.position_embedding = nn.Embedding(self.max_seq_length, self.hidden_size)
self.trm_encoder = TransformerEncoder(...)
输入
position_ids = torch.arange(item_seq.size(1), device=item_seq.device)
position_ids = position_ids.unsqueeze(0).expand_as(item_seq)
position_embedding = self.position_embedding(position_ids)
position_embedding: [B, L, H]
input_emb = item_emb + position_embedding
input_emb = self.LayerNorm(input_emb)
input_emb = self.dropout(input_emb)
inpu调用 Transformert embedding = item embedding + positional embedding
调用 Transformer
extended_attention_mask = self.get_attention_mask(item_seq)
trm_output = self.trm_encoder(
    input_emb, extended_attention_mask, output_all_encoded_layers=True
)
用 Q 和 K 算每个历史 item 对当前位置的重要性
经过 mask 和 softmax 得到 attention 权重
再用权重加权 V
```

训练 SASRec 时，模块调用顺序大致是：

```
DataLoader → Interaction → SASRec.calculate_loss() → SASRec.forward() → item embedding / position embedding → attention mask → TransformerEncoder → TransformerLayer → MultiHeadAttention → FeedForward → gather_indexes() → prediction layer → loss function → backward / optimizer
```

更具体一点：

**1. DataLoader 构造训练 batch**

RecBole 先用序列推荐 DataLoader 构造 batch，里面主要有：

```
item_id_list item_length item_id
```

含义是：

```
item_id_list  用户历史序列 item_length   有效序列长度 item_id       真实下一个 item，也就是正样本
```

如果是 BPR loss，还会有：

```
neg_item_id
```

**2. Trainer 调用模型 loss**

训练循环中调用：

```
loss = model.calculate_loss(interaction)
```

进入：

```
SASRec.calculate_loss()
```

**3. calculate_loss 取出序列数据**

```
item_seq = interaction[self.ITEM_SEQ] item_seq_len = interaction[self.ITEM_SEQ_LEN] seq_output = self.forward(item_seq, item_seq_len) pos_items = interaction[self.POS_ITEM_ID]
```

这里进入 forward()。

**4. forward 中先做 embedding**

```
item_emb = self.item_embedding(item_seq) position_embedding = self.position_embedding(position_ids) input_emb = item_emb + position_embedding
```

也就是：

```
物品序列 ID → item embedding → 加上 position embedding
```

然后：

```
input_emb = self.LayerNorm(input_emb) input_emb = self.dropout(input_emb)
```

**5. 生成 attention mask**

```
extended_attention_mask = self.get_attention_mask(item_seq)
```

这个 mask 用来：

```
屏蔽 padding 位置 屏蔽未来位置，防止模型偷看答案
```

**6. 调用 TransformerEncoder**

```
trm_output = self.trm_encoder(    input_emb,    extended_attention_mask,    output_all_encoded_layers=True )
```

进入：

```
TransformerEncoder
```

它内部会按层循环：

```
for layer_module in self.layer:    hidden_states = layer_module(hidden_states, attention_mask)
```

**7. 每个 TransformerLayer 调用两个子模块**

每层 TransformerLayer 包括：

```
MultiHeadAttention FeedForward
```

即：

```
attention_output = self.multi_head_attention(hidden_states, attention_mask) feedforward_output = self.feed_forward(attention_output)
```

**8. MultiHeadAttention 内部**

MultiHeadAttention 会调用：

```
query linear key linear value linear scaled dot-product attention softmax dropout dense linear residual connection LayerNorm
```

核心是：

```
Q = self.query(input_tensor) K = self.key(input_tensor) V = self.value(input_tensor) attention_scores = Q @ K attention_scores = attention_scores / sqrt(head_size) attention_scores = attention_scores + attention_mask attention_probs = softmax(attention_scores) context = attention_probs @ V
```

**9. FeedForward 内部**

FeedForward 会调用：

```
Linear activation Linear dropout residual connection LayerNorm
```

代码逻辑是：

```
hidden_states = dense_1(input) hidden_states = activation(hidden_states) hidden_states = dense_2(hidden_states) hidden_states = dropout(hidden_states) hidden_states = LayerNorm(hidden_states + input)
```

**10. 取最后一个有效位置**

Transformer 输出是：

```
[B, sequence_length, hidden_size]
```

SASRec 取每条序列最后一个有效 item 的 hidden state：

```
output = self.gather_indexes(output, item_seq_len - 1)
```

得到：

```
seq_output: [B, hidden_size]
```

**11. 计算 loss**

如果是 RecBole 默认 SASRec 的 CE loss：

```
test_item_emb = self.item_embedding.weight logits = seq_output @ test_item_emb.T loss = CrossEntropyLoss(logits, pos_items)
```

意思是：

```
用序列表示预测所有 item 真实下一个 item 是分类标签
```

如果是 BPR loss：

```
pos_score = seq_output · pos_item_emb neg_score = seq_output · neg_item_emb loss = BPRLoss(pos_score, neg_score)
```

意思是：

```
让真实下一个 item 分数高于负样本 item
```

**12. Trainer 反向传播**

最后回到 Trainer：

```
loss.backward() optimizer.step()
```

参数被更新，包括：

```
item_embedding position_embedding TransformerEncoder 中的 Q/K/V Linear FeedForward Linear LayerNorm 参数
```

一句话总结：训练 SASRec 时，先由 DataLoader 生成用户历史序列 batch，然后 calculate_loss() 调用 forward()，序列经过 embedding、causal self-attention、feed-forward 和最后位置提取，得到用户当前兴趣表示，再和 item embedding 计算预测分数并计算 loss，最后反向传播更新参数