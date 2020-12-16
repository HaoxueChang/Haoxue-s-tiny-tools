import shutil
import os

if __name__=='main':
    fpath,fname=os.path.split(argv[1])
    new_path = '../data/'
    shutil.move(argv[1], new_path + fname)
