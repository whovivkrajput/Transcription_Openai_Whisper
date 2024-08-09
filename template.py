import os
import logging
from pathlib import Path


projectName = "SpeechtoText"

basePath = os.path.basename(os.getcwd())
list_Of_Files = [
    ".github/workflows/.gitkeep",
    "data/ingest.txt",
    "results/output.txt",
    "config/config.yaml"
    "scripts/inference.py"
    "main.py",
    "app.py",
    "setup.py",
    "requirements.txt",
    "research/poc.ipynb",
    "DockerFile",
    "readme.md"
]
# print(list_Of_Files)
for filePath in list_Of_Files:
    filePath = Path(filePath)
    fileDir, fileName = os.path.split(filePath)
    if fileDir != "":
        os.makedirs(fileDir, exist_ok = True)
        logging.info(f"Creating directory: {fileDir} for the filename: {fileName}")
    
    if not os.path.exists(filePath):
        with open(filePath, 'w') as file:
            pass 
            logging.info(f"Creating empty file: {filePath}")
    else:
        logging.info(f"{fileName} already exists")
