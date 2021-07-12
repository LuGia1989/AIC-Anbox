import pandas as pd
import sys

f=sys.argv[1]

def gpuUtil(f):
    with open (f, 'r+') as myfile:
        df_gpuUtil = pd.read_csv(f, names=["id", "gpuUtil", "timestamp", "util_in_%"])
        min_gpuUtil = df_gpuUtil['util_in_%'].min()
        max_gpuUtil = df_gpuUtil['util_in_%'].max()
        ave_gpuUtil = int(df_gpuUtil['util_in_%'].mean())
        #print(df_encUtil['util_in_%'])
    return min_gpuUtil, max_gpuUtil, ave_gpuUtil

def main():
    min_gpuUtil, max_gpuUtil, ave_gpuUtil = gpuUtil(f)
    print('Min. GPU Utilization in % = ', min_gpuUtil)
    print('Ave. GPU Utilization in % = ', ave_gpuUtil)
    print('Max. GPU Utilization in % = ', max_gpuUtil)

if __name__ == '__main__':
    main()
