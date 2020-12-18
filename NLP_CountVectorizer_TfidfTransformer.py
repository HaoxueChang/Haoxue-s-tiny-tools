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


#tfidf的思想是，如果某个词或短语在一篇文章中出现的频率很高但在其他文章中很少出现，那么这个词或短语具有很好的区分能力，适合用来分类。
from sklearn.feature_extraction.text import TfidfTransformer
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus))
#'second'这个词只在第二个文本中出现，且出现两次，这个词可以很好的将第二个文本和别的文本区分开。所以tfidf值最大0.85
#'the'这个词在所有文本中都出现了，所以不具有任何区分能力，在每个文本中'the'的tfidf值都是最小的。每个文本中该值又都不一样，是因为每个文本的长度不一样导致的。
print (tfidf)
#   (0, 8)	0.4387767428592343
#   (0, 6)	0.35872873824808993
#   (0, 3)	0.4387767428592343
#   (0, 2)	0.5419765697264572
#   (0, 1)	0.4387767428592343
#   (1, 8)	0.2723014675233404
#   (1, 6)	0.22262429232510395
#   (1, 5)	0.8532257361452786
#   (1, 3)	0.2723014675233404
#   (1, 1)	0.2723014675233404
#   (2, 7)	0.5528053199908667
#   (2, 6)	0.2884767487500274
#   (2, 4)	0.5528053199908667
#   (2, 0)	0.5528053199908667
#   (3, 8)	0.4387767428592343
#   (3, 6)	0.35872873824808993
#   (3, 3)	0.4387767428592343
#   (3, 2)	0.5419765697264572
#   (3, 1)	0.4387767428592343
