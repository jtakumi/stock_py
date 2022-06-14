from datetime import datetime
import pandas as pd
import datetime
from pandas_datareader import data
import os


def make_file(df,name):
    fn='output_files/' +  name + '_dow.csv'
    df.to_csv(fn)

def work():
    name='yahoo'
    df=data.DataReader("^DJI",name)
    make_file(df,name)
    print(df)

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
