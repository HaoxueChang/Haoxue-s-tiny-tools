# TfidfVectorizer()的功能是CountVectorizer()和TfdifTransformer()的总和
# CountVectorizer()是将文本向量化，即将文本分词后转换为相应的词频矩阵或词向量
# TfidfTransformer()是对词频矩阵计算相应的tfidf值
# TfidfVectorizer()则同时实现计算词频矩阵和计算tfidf的功能
# class sklearn.feature_extraction.text.TfidfVectorizer(input='content', encoding='utf-8', decode_error='strict', strip_accents=None, lowercase=True,
#                             preprocessor=None, tokenizer=None, analyzer='word', stop_words=None, token_pattern='(?u)\b\w\w+\b', ngram_range=(1, 1),
#                             max_df=1.0, min_df=1, max_features=None, vocabulary=None, binary=False, dtype=<class 'numpy.int64'>, norm='l2', use_idf=True, 
#                             smooth_idf=True, sublinear_tf=False)
# norm：默认为'l2'，可设为'l1'或None，计算得到tf-idf值后，如果norm='l2'，则整行权值将归一化，即整行权值向量为单位向量，如果norm=None，则不会进行归一化。大多数情况下，使用归一化是有必要的。
from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [          'This is the first document.',
		'This is the second second document.',
		'And the third one.',
		'Is this the first document?',]
tfidf2 = TfidfVectorizer()
re = tfidf2.fit_transform(corpus)
print(re)
#输出结果与CountVectorizer() + CountVectorizer()一致
#   (0, 8)        0.438776742859
#   (0, 3)        0.438776742859
#   (0, 6)        0.358728738248
#   (0, 2)        0.541976569726
#   (0, 1)        0.438776742859
#   (1, 8)        0.272301467523
#   (1, 3)        0.272301467523
#   (1, 6)        0.222624292325
#   (1, 1)        0.272301467523
#   (1, 5)        0.853225736145
#   (2, 6)        0.28847674875
#   (2, 0)        0.552805319991
#   (2, 7)        0.552805319991
#   (2, 4)        0.552805319991
#   (3, 8)        0.438776742859
#   (3, 3)        0.438776742859
#   (3, 6)        0.358728738248
#   (3, 2)        0.541976569726
#   (3, 1)        0.438776742859
