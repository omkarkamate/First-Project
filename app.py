from Src.Stress_Level.Logging import logging
from Src.Stress_Level.Exception import Cu_Exception
import sys

if __name__=="__main__":
    try:
        a=1/0

    except(Exception) as e:
        raise Cu_Exception(e,sys)
