import pandas as pd
import sys

f=sys.argv[1]

def decUtil(f):
    with open (f, 'r+') as myfile:
        df_decUtil = pd.read_csv(f, names=["id", "decUtil", "timestamp", "util_in_%"])
        min_decUtil = df_decUtil['util_in_%'].min()
        max_decUtil = df_decUtil['util_in_%'].max()
        ave_decUtil = int(df_decUtil['util_in_%'].mean())
        #print(df_decUtil['util_in_%'])
    return min_decUtil, max_decUtil, ave_decUtil

def main():
    min_decUtil, max_decUtil, ave_decUtil = decUtil(f)
    print('Min. Decoder Utilization in % = ', min_decUtil)
    print('Ave. Decoder Utilization in % = ', ave_decUtil)
    print('Max. Decoder Utilization in % = ', max_decUtil)

if __name__ == '__main__':
    main()
