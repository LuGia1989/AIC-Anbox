import pandas as pd
import sys

f=sys.argv[1]

def temp(f):
    with open (f, 'r+') as myfile:
        df_temp = pd.read_csv(f, names=["id", "temp", "timestamp", "Temp in C"])
        min_temp = df_temp['Temp in C'].min()
        max_temp = df_temp['Temp in C'].max()
        ave_temp = int(df_temp['Temp in C'].mean())
        std_temp = float(df_temp['Temp in C'].std())
        #print(df_temp['Temp in C'])
    return min_temp, max_temp, ave_temp, std_temp

def main():
    min_temp, max_temp, ave_temp, std_temp = temp(f)
    print('Min. Temp in C = ', min_temp)
    print('Ave. Temp in C = ', ave_temp)
    print('Max. Temp in C = ', max_temp)
    print('Max. Temp in C = ', '{0:.2f}'.format(std_temp))

if __name__ == '__main__':
    main()
