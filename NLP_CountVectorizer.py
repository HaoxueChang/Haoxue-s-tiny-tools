#CountVectorizer 用于将一个或多个文本转换为词频矩阵
#将文本分词后，将所有文本中出现的所有词作为一个字典，每个文本的词向量的长度是该词典的长度，值是词频，即该词在该文本出现的次数。
#拿出每个文本词向量中不为0的部分就是该文本的词频统计
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(min_df=1)
corpus = [ 'This is the first document.',
           'This is the second second document.',
           'And the third one.',
           'Is this the first document?',]
X = vectorizer.fit_transform(corpus)
feature_name = vectorizer.get_feature_names()

print(X.toarray())
#array([[0, 1, 1, 1, 0, 0, 1, 0, 1],
#        [0, 1, 0, 1, 0, 2, 1, 0, 1],
#        [1, 0, 0, 0, 1, 0, 1, 1, 0],
#        [0, 1, 1, 1, 0, 0, 1, 0, 1]], dtype=int64)

# 大部分文本都只包含了整个文本库中的少量词汇，因此词向量中有大量的0，即词向量是稀疏向量，
print(X)
#   (0, 8)	1
#   (0, 3)	1
#   (0, 6)	1
#   (0, 2)	1
#   (0, 1)	1
#   (1, 8)	1
#   (1, 3)	1
#   (1, 6)	1
#   (1, 1)	1
#   (1, 5)	2
#   (2, 6)	1
#   (2, 0)	1
#   (2, 7)	1
#   (2, 4)	1
#   (3, 8)	1
#   (3, 3)	1
#   (3, 6)	1
#   (3, 2)	1
#   (3, 1)	1
print(feature_name)
# ['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third', 'this']
