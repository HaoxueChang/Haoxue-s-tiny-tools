import os
import pandas as pd
import multiprocessing
import glob
import sys


def read_csv_file(x):
    return pd.read_csv(x)
def read_splitted_csv(file_path):
    dfs=[file_path+'/'+e for e in os.listdir(file_path) if 'csv' in e and 'crc' not in e]
   
    p=multiprocessing.Pool(30)
    results=p.map(read_csv_file,dfs)
    p.close()
    return pd.concat(results).sample(frac=1).reset_index(drop=True) 
