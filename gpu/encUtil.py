import pandas as pd
import sys

f=sys.argv[1]

def encUtil(f):
    with open (f, 'r+') as myfile:
        df_encUtil = pd.read_csv(f, names=["id", "encUtil", "timestamp", "util_in_%"])
        min_encUtil = df_encUtil['util_in_%'].min()
        max_encUtil = df_encUtil['util_in_%'].max()
        ave_encUtil = int(df_encUtil['util_in_%'].mean())
        #print(df_encUtil['util_in_%'])
    return min_encUtil, max_encUtil, ave_encUtil

def main():
    min_encUtil, max_encUtil, ave_encUtil = encUtil(f)
    print('Min. Encoder Utilization in % = ', min_encUtil)
    print('Ave. Encoder Utilization in % = ', ave_encUtil)
    print('Max. Encoder Utilization in % = ', max_encUtil)

if __name__ == '__main__':
    main()
