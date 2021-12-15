import numpy as np
import lda

X = lda.datasets.load_reuters()
print(X.shape)
vocab = lda.datasets.load_reuters_vocab()
print(len(vocab))
title = lda.datasets.load_reuters_titles()
print(title[:10])
# 模型训练
model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)
model.fit(X)
topic_word = model.topic_word_
print(topic_word.shape)
print(topic_word)
# 展示每个主题的前八个单词
for i, topic_dist in enumerate(topic_word):
    print(np.array(vocab)[np.argsort(topic_dist)][:-9:-1])
doc_topic = model.doc_topic_
print(doc_topic.shape)
print("第一个样本的主题分布是", doc_topic[0])
print("第一个样本的最终主题是", doc_topic[0].argmax())
