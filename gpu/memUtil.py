import pandas as pd
import sys

f=sys.argv[1]

def memUtil(f):
    with open (f, 'r+') as myfile:
        df_memUtil = pd.read_csv(f, names=["id", "memUtil", "timestamp", "util_in_%"])
        min_memUtil = df_memUtil['util_in_%'].min()
        max_memUtil = df_memUtil['util_in_%'].max()
        ave_memUtil = int(df_memUtil['util_in_%'].mean())
        std_memUtil = float(df_memUtil['util_in_%'].std())
        #print(df_encUtil['util_in_%'])
    return min_memUtil, max_memUtil, ave_memUtil, std_memUtil

def main():
    min_memUtil, max_memUtil, ave_memUtil, std_memUtil = memUtil(f)
    print('Min. Memory Utilization in % = ', min_memUtil)
    print('Ave. Memory Utilization in % = ', ave_memUtil)
    print('Max. Memory Utilization in % = ', max_memUtil)
    print('Std. Memory Utilization in % = ', '{0:.2f}'.format(std_memUtil))

if __name__ == '__main__':
    main()
