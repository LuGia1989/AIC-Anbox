import pandas as pd
import sys

f=sys.argv[1]

def violPwr(f):
    with open (f, 'r+') as myfile:
        df_violPwr = pd.read_csv(f, names=["id", "violPwr", "timestamp", "Pwr Viol time (ns)"])
        min_violPwr = df_violPwr['Pwr Viol time (ns)'].min()
        max_violPwr = df_violPwr['Pwr Viol time (ns)'].max()
        ave_violPwr = int(df_violPwr['Pwr Viol time (ns)'].mean())
        #print(df_violPwr['Pwr Viol time (ns)'])
    return min_violPwr, max_violPwr, ave_violPwr

def main():
    min_violPwr, max_violPwr, ave_violPwr = violPwr(f)
    print('Min. Pwr Viol time (ns) = ', min_violPwr)
    print('Ave. Pwr Viol time (ns) = ', ave_violPwr)
    print('Max. Pwr Viol time (ns) = ', max_violPwr)

if __name__ == '__main__':
    main()
