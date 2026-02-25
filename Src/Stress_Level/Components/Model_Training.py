import pandas as pd
from dataclasses import dataclass
import os
import sys
from Src.Stress_Level.Exception import Cu_Exception
from Src.Stress_Level.Logging import logging
from sklearn.model_selection import train_test_split
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score

@dataclass

class model_train_config:
    MTConfig=os.path.join("artifacts","model.pkl")

class model_training:
    def __init__(self):
        self.Config=model_train_config()
    
    def initiate_model_training(self,path):
        raw_df=pd.read_csv(path)
        logging.info("Reading raw data")
        X=raw_df.drop("Stress_Level",axis=1)
        y=raw_df["Stress_Level"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)
        logging.info("Split data into train test")

        with open("artifacts/Data_Preprocessing.pkl", "rb") as file:
            preprocessor = pickle.load(file)

        X_train=preprocessor.fit_transform(X_train)
        X_test=preprocessor.transform(X_test)
        logging.info("preprocessing data")

        models={
            "LinearRegression":LinearRegression(),
            "KNN":KNeighborsRegressor(),
            "Tree":DecisionTreeRegressor()
        }
        report={}

        for i in range(len(models)):
            model=list(models.values())[i]
            model.fit(X_train,y_train)
            y_test_pred=model.predict(X_test)
            score=r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]]=score
    
        logging.info("applying various model ")

        best_model_score=max(report.values())
        best_model_name=list(report.keys())[list(report.values()).index(best_model_score)]
        best_model=models[best_model_name]
        logging.info(f"selected best model which is {best_model_name}")

        with open(self.Config.MTConfig, "wb") as f:
            pickle.dump(best_model,f)
        
        return best_model_name,best_model_score





