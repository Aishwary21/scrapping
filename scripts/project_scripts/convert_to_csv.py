from scripts.db_utility.connection import conne
import pandas as pd
import os
def convert(tweet):   
    df = pd.DataFrame(tweet)
    if os.stat("data.csv").st_size == 0:
        df.to_csv("data.csv",mode="a+",index=False,header=True)
    else:
        df.to_csv("data.csv",mode="a+",index=False,header=False)
    conne(df)