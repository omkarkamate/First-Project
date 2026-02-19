import os
import pandas as pd
from Src.Stress_Level.Exception import Cu_Exception
import sys
from Src.Stress_Level.Logging import logging
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def Get_Data():
    logging.info("Reading dataset from File Explorer")
    df = pd.read_csv("E:\dataset\Smartphone_Usage_Productivity_Dataset_50000.csv")
    df["Stress_Level"]=(
        df["Social_Media_Hours"]*0.4 -
        df["Sleep_Hours"]*0.7 +
        df["Weekend_Screen_Time_Hours"]*0.2 -
        df["Age"]*0.2 -
        df["Caffeine_Intake_Cups"]*0.2 +
        df["Daily_Phone_Hours"]*0.3 -
        df["Work_Productivity_Score"]*0.3
    )

    MMScaler=MinMaxScaler()
    df["Stress_Level"]=MMScaler.fit_transform(df[["Stress_Level"]])*10

    df["Stress_Level"]=np.round(df["Stress_Level"],3)


    path=os.path.join("artifacts","raw.csv")
    os.makedirs("artifacts",exist_ok=True)
    df.to_csv(path,index=False)
    logging.info("Insert dataset to new file (artifacts/raw.csv)")
    return(df.head())



