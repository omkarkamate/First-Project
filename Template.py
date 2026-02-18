import os
import logging

Project_name="Stress_Level"

files=[
    f"Src/{Project_name}",
    f"Src/{Project_name}/__init__.py",
    f"Src/{Project_name}/Components",
    f"Src/{Project_name}/Components/__init__.py",
    f"Src/{Project_name}/Components/Data_Ingestion.py",
    f"Src/{Project_name}/Components/Data_Preprocessing.py",
    f"Src/{Project_name}/Components/Data_Training.py",
    f"Src/{Project_name}/Pipeline",
    f"Src/{Project_name}/Pipeline/__init__.py",
    f"Src/{Project_name}/Pipeline/Training.py",
    f"Src/{Project_name}/Pipeline/Predicting.py",
    "app.py",
    f"Src/{Project_name}/utils.py",
    ".env"
]

for file in files:
    file_path=os.path.join(file)
    filedir,file_name=os.path.split(file_path)

    if(filedir!=""):
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Create directory{filedir}")

    if(not os.path.exists(file_path)):
        os.makedirs(file_path)
        logging.info(f"Create files{file_name}")
    
    else:
        logging.info("Already exists")
        
        