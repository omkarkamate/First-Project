from Src.Stress_Level.Logging import logging
from Src.Stress_Level.Exception import Cu_Exception
import sys
from Src.Stress_Level.Components.Data_Ingestion import Get_Data

if __name__=="__main__":
    try:
        obj=Get_Data()
        print("Featurs :- ")
        print(obj.columns)
        print("\nFirst five Rows : \n")
        print(obj) 

    except(Exception) as e:
        raise Cu_Exception(e,sys)
