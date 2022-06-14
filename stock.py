from datetime import datetime
import pandas as pd
import datetime

df=pd.read_csv('toyota_motor.csv')
print(df.head())

#日付けをdatetimeに変換
df['日付け']=df['日付け'].apply(lambda x: datetime.datetime.strptime(x,"%Y年%m月%d日"))

def del_num(x):
    #不要な文字を削除
    for s in [",","M","%"]:
        x=x.replace(s,"")

    return float(x)

for col in ["終値","始値","高値","安値","出来高","変化率 %"]:
    df[col]=df[col].apply(del_num)

print(df.head())