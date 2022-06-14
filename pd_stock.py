from datetime import datetime
import pandas as pd
import datetime
from pandas_datareader import data
import os

name=[
    "^DJI",
    "AAPL",
    "7203.T"

]


def make_file(df,name):
    fn='output_files/' +  name + '_dow.csv'
    df.to_csv(fn)

def work():
    for i in range(len(name)):
        df=data.DataReader(name[i],"yahoo")
        make_file(df,name[i])

def git():
    os.system('git add .')
    td=datetime.date.today()
    d1=td.strftime("%y-%m-%d")
    gcm='git commit -m ' + d1
    os.system(gcm)


def main():
    work()
    git()
if __name__ == '__main__':
    main()
