
"""
FOLDER :2025-10-20 (实验日期)_expN
虚拟环境 ：默认airbnb_env


任务描述（今天干了什么，为什么）


使用的数据范围
数据描述
数据处理方式
实验内容+耗时
数据和结果储存路径


A FARIE


"""
import os
import pandas as pd
import time
from tqdm import tqdm 
import matplotlib.pyplot as plt
import seaborn as sns  
from datetime import datetime
import argparse
import re


today_str = datetime.now().strftime("%Y-%m-%d")



    
if __name__=="__main__":
    parser=argparse.ArgumentParser('transformer PDF en RIS')
    parser.add_argument("--pdf_folder", help="chemin de dossier rtf")#->_automatiquement !
    parser.add_argument("--csv_output",default="output.csv")
    args = parser.parse_args()#prend les variables entrées 

    start_time=time.time()
    csv_dir=os.path.dirname(args.csv_output) or '.'
    os.makedirs(csv_dir, exist_ok=True)


