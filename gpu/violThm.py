import pandas as pd
import sys

f=sys.argv[1]

def violThm(f):
    with open (f, 'r+') as myfile:
        df_violThm  = pd.read_csv(f, names=["id", "violThm", "timestamp", "Violation Therm in boolean"])
        violThm     = df_violThm['Violation Therm in boolean'].max()
        #print(df_violThm['Violation Therm in boolean'])
        print('Violation Therm in boolean) = ', violThm)

def main():
    violThm(f)

if __name__ == '__main__':
    main()
