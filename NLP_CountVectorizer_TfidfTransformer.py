#CountVectorizer 用于将一个或多个文本转换为词频矩阵
#将文本分词后，将所有文本中出现的所有词作为一个字典，每个文本的词向量的长度是该词典的长度，值是词频，即该词在该文本出现的次数。
#拿出每个文本词向量中不为0的部分就是该文本的词频统计
#参数设置：
#class sklearn.feature_extraction.text.CountVectorizer(input='content', encoding='utf-8', decode_error='strict', 
#                        strip_accents=None, lowercase=True, preprocessor=None, tokenizer=None, stop_words=None, 
#                        token_pattern='(?u)\b\w\w+\b', ngram_range=(1, 1), analyzer='word', max_df=1.0, min_df=1, 
#                        max_features=None, vocabulary=None, binary=False, dtype=<class 'numpy.int64'>)
# input, encoding，strip_accents使用默认设置
# decode_error: strict,遇到不能解码的会报错；ingore会忽略解码错误
# analyzer，可设为word/char/char_wb
# ngram_range:词组切分长度范围
# lowercase：将所有字符变成小写
# token_pattern：表示token的正则表达式，analyzer要设置为word,默认'(?u)\b\w\w+\b'，表示选择2个或两个以上的字母或数字作为token,标点符号默认为token分隔符，而不会作为token
# max_df: [0.0 1.0]的float，默认为1.0。这个参数的作用是作为一个阈值，当构造语料库的关键词集的时候，如果某个词的document frequence大于max_df，这个词不会被当作关键词。
# min_df：类似于max_df，不同之处在于如果某个词的document frequence小于min_df，则这个词不会被当作关键词
# max_features：默认为None，可设为int，对所有关键词的term frequency进行降序排序，只取前max_features个作为关键词集
# dtype：使用CountVectorizer类的fit_transform()或transform()将得到一个文档词频矩阵，dtype可以设置这个矩阵的数值类型
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
