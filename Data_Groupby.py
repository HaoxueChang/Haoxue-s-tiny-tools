#对数据分组并在各组上应用一个函数（聚合或转换）是数据分析工作中的常用操作。
#数据准备好后，通常需要进行计算分组统计或生成透视表， pandas的groupby可以实现对数据进行切片，切块，摘要等操作
#结构化查询语言SQL可以方便的进行连接，过滤，转换和聚合，但是其执行分组运算的能力有限。python以其强大的表达能力能执行复杂的多的分组运算操作(任何接受pandas对象或numpy数组的函数)

#分组运算的过程描述：split-apply-combine,拆分-应用-合并
