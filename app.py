from Src.Stress_Level.Logging import logging
from Src.Stress_Level.Exception import Cu_Exception
import sys
import pickle
import os
import pandas as pd

if __name__=="__main__":
    try:

        with open("artifacts/Data_Preprocessing.pkl","rb") as f:
            preprocessor=pickle.load(f) 
        
        with open("artifacts/model.pkl","rb") as file:
            model=pickle.load(file)

        data={}
        data["Age"]=[input("Enter Age : ")]
        aa=input("Enter Gender: \n""0->Male\n1->Female\n""Choose an option (0 or 1): " )
        if(aa==0):
            gender="Male"
        else:
            gender="Female"
        data["Gender"]=[gender]
        ab=occupation = input(
            "Enter Occupation:\n"
            "0 -> Professional\n"
            "1 -> Student\n"
            "2 -> Business Owner\n"
            "3 -> Freelancer\n"
            "Choose an option (0-3): "
        )

        if(ab==0):
            Occupation="Professional"
        elif(ab==1):
            Occupation="Student"
        elif(ab==2):
            Occupation="Business Owner"
        else:
            Occupation="Freelancer"

        data["Occupation"]=[Occupation]
        ac=input("Enter Device_Type: \n""0->Android\n""1->iOS\n""Choose an option (0 or 1): ")
        if(ac==0):
            Device_Type="Android"
        else:
            Device_Type="iOS"

        data["Device_Type"]=[Device_Type]
        data["Daily_Phone_Hours"]=[input("Enter Daily_Phone_Hours : ")]
        data["Social_Media_Hours"]=[input("Enter Social_Media_Hours : ")]
        data["Work_Productivity_Score"]=[input("Enter Work_Productivity_Score(0 to 10) : ")]
        data["Sleep_Hours"]=[input("Enter Sleep_Hours : ")]
        data["Caffeine_Intake_Cups"]=[input("Enter Caffeine_Intake_Cups : ")]
        data["App_Usage_Count"]=[input("Enter App_Usage_Count : ")]
        data["Weekend_Screen_Time_Hours"]=[input("Enter Weekend_Screen_Time_Hours : ")]

        df=pd.DataFrame(data)

        preprocessed_df=preprocessor.transform(df)

        pred=model.predict(preprocessed_df)

        print(pred)

        

    except(Exception) as e:
        raise Cu_Exception(e,sys)
