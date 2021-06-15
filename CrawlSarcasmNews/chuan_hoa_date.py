from datetime import datetime
import pandas as pd
df = pd.read_csv('./crawled_data/ThePoke.csv')
print(df.head(10))
for i in range(len(df)):
    new_date = datetime.strptime(df.values[i][3],"%m/%d/%Y").strftime("%d/%m/%Y")
    df.loc[i,'posted_at'] = new_date
print(df.head(10))