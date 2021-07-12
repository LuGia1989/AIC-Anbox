import pandas as pd
import sys

f=sys.argv[1]

def pwrDraw(f):
    with open (f, 'r+') as myfile:
        df_pwrDraw = pd.read_csv(f, names=["id", "pwrDraw", "timestamp", "util_in_%"])
        min_pwrDraw = df_pwrDraw['util_in_%'].min()
        max_pwrDraw = df_pwrDraw['util_in_%'].max()
        ave_pwrDraw = int(df_pwrDraw['util_in_%'].mean())
        #print(df_pwrDraw['util_in_%'])
    return min_pwrDraw, max_pwrDraw, ave_pwrDraw

def main():
    min_pwrDraw, max_pwrDraw, ave_pwrDraw = pwrDraw(f)
    print('Min. Power Draw in Watts = ', min_pwrDraw)
    print('Ave. Power Draw in Watts = ', ave_pwrDraw)
    print('Max. Power Draw in Watts = ', max_pwrDraw)

if __name__ == '__main__':
    main()
