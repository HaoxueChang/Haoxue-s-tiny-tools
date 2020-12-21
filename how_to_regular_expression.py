import re
#匹配非字符或下划线开头的部分，并替换为空格
re.sub(r'[^\w]', ' ', text)
# text='.?\aoxue ella', output='   oxue ella'
# text='_好雪', output='_好雪'
#\a 的特殊含义？

#匹配一个或多个空格，替换为一个空格
re.sub(r' +', ' ',text)

#匹配'替换为空格
re.sub("'"," ",text)
#text="haoxue's tool",output='haoxue s tool'

#匹配'S或者's替换为S,两种写法实现的功能相同
re.sub(r'\'[Ss]', 'S', text)
re.sub(r"'[Ss]", 'S', text)
#text="'S", output = 'S'

#匹配字母数字与非字母数字
# https://blog.csdn.net/uvyoaa/article/details/80854459
# \b,\B是单词边界，不匹配任何字符
# \b表示字母数字与非字母数字的边界，非字母数字与字母数字的边界
# \B表示字母数字与字母数字的边界，非字母数字与非字母数字的边界
re.split('123\\b','==123!! abc123. 123. 123abc. 123')
re.split(r'123\b','==123!! abc123. 123. 123abc. 123')
# output:['==', '!! abc', '. ', '. 123abc. ', '']
re.split('\\b123\\b','123 ==123!! abc123.123.123abc.123')
# output:['', ' ==', '!! abc123.', '.123abc.', '']
re.split('\\b123=\\b','==123!! abc123,123,123=abc,123')
# output:['==123!! abc123,123,', 'abc,123']
re.split(r'pyc\B','1pycthon py5 2pyc342 pyc1py2py4 pyp3 3pyc# pyc')
# output:['1', 'thon py5 2', '342 ', '1py2py4 pyp3 3pyc# pyc']
#对比以下两个表达式：
re.split('\\b123=\\b','==123!! abc123,123,123==abc,123')  #output:['==123!! abc123,123,123==abc,123']
re.split('\\b123=\\B','==123!! abc123,123,123==abc,123')  #output:['==123!! abc123,123,', '=abc,123']
#下划线和字母数字算作一类
re.split('123_\\b','==123!! abc 123_123_. 123_. 123abc. 123') #output:['==123!! abc 123_', '. ', '. 123abc. 123']
