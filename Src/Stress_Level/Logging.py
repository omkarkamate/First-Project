from datetime import datetime
import os
import logging

file_dir=os.path.join(os.getcwd(),"Log")
os.makedirs(file_dir,exist_ok=True)

file=f"{datetime.now().strftime("%H-%M-%S-%d-%m-%y")}.log"

log_file_path=os.path.join(file_dir,file)

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
