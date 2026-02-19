import os
import pandas as pd
from Src.Stress_Level.Exception import Cu_Exception
import sys
from Src.Stress_Level.Logging import logging


def Get_Data():
    logging.info("Reading dataset from File Explorer")
    df = pd.read_csv("E:\dataset\Smartphone_Usage_Productivity_Dataset_50000.csv")
    path=os.path.join("artifacts","raw.csv")
    os.makedirs("artifacts",exist_ok=True)
    df.to_csv(path,index=False)
    logging.info("Insert dataset to new file (artifacts/raw.csv)")
    return(df.head())



