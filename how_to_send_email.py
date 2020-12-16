import os
attach_path1 = '../data/Haoxue_test1.csv/'
attach_path2 = '../data/Haoxue_test2.csv/'
email_lst = 'haoxuechang@126.com haoxuechang@163.com haoxuechang@qq.com'
os.system("echo 'Hello! \nBest,\nHaoxue' | mail -s 'Test Mail' -a %s -a %s %s" % (attach_path1,attach_path2,email_lst))
