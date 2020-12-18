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
