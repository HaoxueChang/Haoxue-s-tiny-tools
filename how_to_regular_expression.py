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

#边界符里面不能有贪婪匹配？贪婪匹配不生效？
re.sub(r'\bTest\b[.]*\s*[a-zA-Z0-9]*$', '----', 'test.... aaa0', flags=re.IGNORECASE)
# '----'
re.sub(r'\bTest|Test[.]*\b\s*[a-zA-Z0-9]*$', '----', 'test. aaa0', flags=re.IGNORECASE)
# '----. aaa0'
re.sub(r'\bTest[.]*\b\s*[a-zA-Z0-9]*$', '----', 'test. aaa0', flags=re.IGNORECASE)
# 'test. aaa0'

# （?u),该表达式打开re.U（re.UNICODE）标志,根据Unicode解释字符集
# https://docs.python.org/2/library/re.html#re.U
#re.I, ignore case, perform case-insenstive matching
#re.L,locale,做本地化识别
#re.M,mulitline,多行匹配，影响'^'和'$'
#re.S,使'.'可以匹配包括换行符在内的所有字符，不设置这个flag,'.'匹配除换行符之外的所有字符
#re.X,该标志可以使用更灵活的方式使表达式更易于理解。这一标志使得我们可以将表达式分开并添加注释。除了字符类中的空格，添加了转义符的空格，或者在token *?,(?:,(?P<...>中，别的空格会被忽略，
#当一行包含#，但#又不包含在字符类且前面没有转义符，#左侧到行末所有字符都会被忽略（被认为是注释）
a = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)
b = re.compile(r"\d+\.\d*")

# https://docs.python.org/2/library/re.html#
# https://docs.python.org/2/howto/regex.html#regex-howto

#正则表达式的() [] {} 有着不同的意思。
# （）是为了提取匹配字符串，表达式中有几个()就有几个相应的匹配字符串
# [] 是定义匹配的字符范围。比如[a-zA-Z0-9]表示相应位置的字符要匹配英文字符和数字。[\s*表示空格或者*号]
# {}一般是用来匹配的长度。比如\s{3}表示匹配三个空格，\s[1,3]表示匹配1到3个空格
# (0-9)匹配'0-9'本身。[0-9]*匹配数字（注意后面有*，可以为空）[0-9]+匹配数字(注意后面有+，不可以为空)，[0-9]{0,9}表示长度为0到9的数字字符串。

#下面式子表示匹配圆括号，方括号和花括号里面的内容，对转义符稍作修改也能实现，还不是很明白(),[],{}的用法
re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", x)

# ^在正则表达式中有两种用法，一是表达以什么开头，二是表达对什么取反。
# 可以用下面的代码进行测试
import re
s = ['abc-123-cba',       #'abc'在最前面
    '123-abc-aabbcc-123', #'abc'在中间
    'a-2-3-b-1',          #最前面是'a'
    'b-x-c-a-1',          #最前面是'b'
    'z-a-1',              #'a'在中间
    'x-y-z',              #字符串没有任何'a','b','c'
    'cbaabc'              #字符串全是'a','b','c'组成
]
st = r'abc'  
for i in s:
    m = re.search(st, i)
    if m:
        print(i)
# 'abc'表示字符串中有'abc'就匹配成功
# '[abc]'表示字符串中有'a'或'b'或'c'就匹配成功
# '^abc'表示字符串由'abc'开头就匹配成功
# '^[abc]'表示字符串由'a'或'b'或'c'开头的，
# '[^abc]'表示匹配'a','b','c'之外的字符。如果一个字符串是由'a','b','c'组合起来的，那就无法匹配到

# 常用的取反：
# '[^a-z]' 所有小写字母之外的字符
# '[^a-zA-Z]' 所有大写和小写字母之外的字符
# '[^0-9]' 所有数字之外的字符

# 正则表达式中问号的用法：
# 用法1：可选匹配,其实就是match 0次或1次
# 有无数字均可匹配
content = 'hello 1234567 world this a demo'
result = re.match('^hel.*(\d+)?.*demo$',content)
result.group(0)
# 'hello 1234567 world this a demo'
content = 'hello world this a demo'
result = re.match('^hel.*(\d+)?.*demo$',content)
result.group(0)
# 'hello world this a demo'
# 用法2：实现非贪婪匹配
# 下面例子问号是对.*起作用的，使它进行非贪婪匹配
content = 'hello 1234567 world this a demo'
result = re.match('^hel.*?(\d+).*demo$',content)
result.group(0)
# 'hello 1234567 world this a demo'
result.group(1)
# '1234567'
result = re.match('^hel.*(\d+).*demo$',content)
result.group(0)
#'hello 1234567 world this a demo'
result.group(1)
#'7'
# ?, 贪婪匹配模式，match 0次或1次，ab?会匹配a或ab
# *, 贪婪匹配模式，match 0次或多次，ab*会匹配a或ab或abbbbbb,任意多个b
# +, 贪婪匹配模式，match 1次或多次，ab*会匹配ab或abbbbbb,任意多个b
# *?,+?,??, 非贪婪匹配模式，match到最近的一个

# 下面表达式匹配开头有两个以上非数字字符后面以5个以上数字或空格结尾的字符串，r'\1'表示取出第一个圆括号内匹配到的pattern,即两个以上非数字字符部分，可以清洗掉字符串尾部的连续5个空格或数字
re.sub(r'(^[^0-9]{2,}?)([0-9 ]{5,})$', r'\1', text)
# 下面表达式匹配开头有两个以上非数字字符后面以0个或多个数字或空格结尾的字符串，r'\1'表示取出第一个圆括号内匹配到的pattern,即两个以上非数字字符部分，可以清洗掉字符串尾部的0个或多个空格或数字
re.sub(r'(^[^0-9]{4,}?)([0-9 ]*)$', r'\1', text)

#值得精读的博文： https://blog.csdn.net/LaoYuanPython/article/details/100045507
#                https://blog.csdn.net/LaoYuanPython/article/details/99752968

# .	匹配任意1个字符（除了\n）,打开DOTALL flag, 可以匹配newline
# [ ]	匹配[ ]中列举的字符
# \d	匹配数字，即0-9
# \D	匹配非数字，即不是数字
# \s	匹配空白，即 空格，tab键
# \S	匹配非空白
# \w	匹配非特殊字符，即a-z、A-Z、0-9、_、汉字
# \W	匹配特殊字符，即非字母、非数字、非汉字、非_

#正则表达式识别重复字符串：
#https://blog.csdn.net/weixin_43758603/article/details/109137653
pattern = r'^(\w+)\1+$'
# ^:以匹配内容开头
# $:以匹配内容结尾
# (一组字符)
# \w:一个数字,或大小写字母
# +:出现至少一次
# \1:重复前面的部分一次

#对比以下输出差异：
re.sub(r'\b(.{5,})(\1\b)+', r'\1', 'abcdef abcdef ')
#'abcdef abcdef '
re.sub(r'\b(.{5,})(\1\b)+', r'\1', 'CITY OF ACITY OF A')
#'CITY OF A'
re.sub(r'(.{5,})(\1)+', r'\1', 'abcdef abcdef ')
#'abcdef '
re.sub(r'(.{5,})(\1)+', r'\1', 'abcdef abcdef abcdef abcdef abcdef ')
#'abcdef abcdef abcdef '
re.sub(r'(.{5,}?)(\1)+', r'\1', 'abcdef abcdef abcdef abcdef abcdef ')
#'abcdef '
pa
# (?:)
# (?=) 前向断言，haoxue(?=ABC),会匹配出现在ABC之前的haoxue
# (?!) 负向先行断言，haoxue(?!=ABC),会匹配后面不是ABC的haoxue
# (?<=) 正向后向断言，(?<=ABC)haoxue,会匹配前面是ABC的haoxue,后向断言的括号里的pattern不能超过３个字符，且不支持组的引用，比如a*,a{3,4}均不支持
# (?!<) 负向后向断言，the contained pattern must only match strings of some fixed length and shouldn’t contain group references
