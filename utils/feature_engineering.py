import pandas as pd

def feature_engineering (df):

    #Compute rolling windows
    df["rolling_1Y"] =df["Open"].rolling(365*24).mean()
    df["rolling_90d"] =df["Open"].rolling(90*24).mean()
    df["rolling_30d"] =df["Open"].rolling(30*24).mean() 
    df["rolling_14d"] =df["Open"].rolling(14*24).mean() 
    df["rolling_7d"] =df["Open"].rolling(7*24).mean() 
    df["rolling_1d"] =df["Open"].rolling(24).mean() 
    df["rolling_12h"] =df["Open"].rolling(12).mean()
    df["rolling_3h"]=df["Open"].rolling(3).mean() 

    #Compute Low_high_delta (volatilité) 
    
    df["vol"] = df["High"].shift(1) - df["Low"].shift(1)
    df["vol_last_day"] = df["High"].rolling(24).max() - df["Low"].rolling(24).min()

    #Compute returns

    df["return_1h"] = df["Open"].pct_change(1)
    df["return_24h"] = df["Open"].pct_change(24) 

    
    return df