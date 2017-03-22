# My_nlp_test
some primary nlp codes....
涉及到很多基础的nlp算法

简述一下所做的事情吧

## 目的：

做两类文本的匹配：简历数据，招聘要求

- step 1:
 先对每条数据分词, 用```jieba```就好, 分词结果存起来

- step 2:
```tf-idf```提取关键字，我使用```gensim```的```tf-idf```, 简单粗暴的提取每个文本```tf-idf```值前10的词语，但是师兄说效果不太好，所以先不管这个结果

- step 3:
用```word2vec```
同样是使用```gensim```的```word2vec```
问了一下大概的思路：
w2v是将每个单词映射成一个向量，然后一条数据，就是把这个数据中的所有分词的向量加起来表示这个doc的向量
然后这里加分词的向量的时候加上了tf-idf的权重
> 49999 条**公司要求**的分词结果
>* 58713 bad datas
(就是有58713个词的vector由于与tf-idf的dictionary冲突，导致没能加到每个公司要求的向量中)


至此，得到了 每个公司要求的向量

- step 4: 
按照同样的方法去把简历信息的数据跑出来



## 问题：

>比如说我通过一家公司的要求去推荐简历：
我先拿到了这个要求的w2v向量v1
然后从建立的这个w2v集合里面去和每一个向量做，比如，余弦相似性的检测
然后，我得到了相似性的排序结果，
那我直接按照排序结果，比如取前10的推荐给公司不久好了么？
或者简单来说，是可以根据相似度最高的结点的聚类

是可以的，但是可能会有点low



> 我也和垚明讨论了一下，也是刚开始的时候我们考虑的一个问题，无监督的话，怎样去评判我们推荐的结果的好坏呢？

人工对公告打label，然后提取一些关键字，做监督训练
或者现在的做法就是简单的去做无监督，先去看什么效果

> 有监督的情况下怎样改进模型，无监督的情况又该怎样改进？

加权值吗？这个待解决....


