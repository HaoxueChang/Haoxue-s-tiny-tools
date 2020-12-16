import pandas as pd
import sys
def main(argv):
    data1 = pd.read_csv(argv[1])
    data2 = pd.read_csv(argv[2])
    
if __name__ == "__main__":
    main(sys.argv)
