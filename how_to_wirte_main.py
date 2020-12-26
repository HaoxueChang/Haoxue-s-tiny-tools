# 方式1:参数不多时，可直接传入，使用sys.argv解析
import pandas as pd
import sys
def main(argv):
    data1 = pd.read_csv(argv[1])
    data2 = pd.read_csv(argv[2])
    
if __name__ == "__main__":
    main(sys.argv)
    
#方式2：参数较多时，使用yaml文件传入，使用python命令行解析包argparse解析
import argparse
import yaml
if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('--haoxue_conf_arg', type=int, default=2, help='flag_int')
    #只能传入add_argument里面设定好的参数，传入没有的会报错
    args1 = parse.parse_args()
    #可以传入add_argument里面m没有的参数，传入没有的不会报错,跟上面的其实一样
    args2 = parse.parse_known_args()
    #'haoxue_conf_arg'为存argument的yaml文件，传入后，用yaml load进来
    haoxue_conf_arg_path = args1.haoxue_conf_arg
    global conf_dic
    conf_dict = yaml.load(open(conf_path))
    main(conf_dict)
#将上面代码存入test.py文件，命令行执行方法：python test.py --haoxue_conf_arg '/data/haoxue_confg.yaml'
# yaml文件示例：
# cols load进去是list格式
# data_path:
# '/data/data_test/test.csv'
# data_path2: '/data/data_test/test2.csv'
# cols:
#   - 'col1'
#   - 'col2'
#   - 'col3'
