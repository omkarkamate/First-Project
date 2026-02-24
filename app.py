from Src.Stress_Level.Logging import logging
from Src.Stress_Level.Exception import Cu_Exception
import sys
from Src.Stress_Level.Components.Data_Preprocessing import Data_preprocessing
import os

if __name__=="__main__":
    try:

        obj=Data_preprocessing()
        aa=obj.Data_Preprocess(os.path.join("artifacts","train_data"),os.path.join("artifacts","test_data"))
        print(aa)
        

    except(Exception) as e:
        raise Cu_Exception(e,sys)
