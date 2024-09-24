import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name= "financial_data"

list_of_files = [
    "data/test",
    "config/setting.py",
    "requirements.txt",
    "main.py"
    ]

for filepath in list_of_files:
    filepath = Path(filepath)
    if not filepath.parent.exists():
        logging.info(f"Creating directory: {filepath.parent}")
        os.makedirs(filepath.parent)
    else:
        logging.info(f"Directory already exists: {filepath.parent}")
    if not filepath.exists():
        logging.info(f"Creating file: {filepath}")
        filepath.touch()
    else:
        logging.info(f"File already exists: {filepath}")