import cv2
from paddleocr import PaddleOCR
from matplotlib import pyplot as plt
import constants as c
#from process_image import *
from process_data import *
from datetime import datetime
import time
import pandas as pd
import numpy as np
from collections import Counter

ocr = PaddleOCR(lang='en',  use_angle_cls=False)

directory = '../frames/T27/'
result = []
df2_result = []
df3_result = []
ini = 0
quant = 9707



for i in range(ini,quant):
    
    
    row_result = []
    df2_row = []
    for key, param in c.inst_motor_T27.items():
        path = directory + key +'/'+ key +'_' + str(i) +'.png'
        image = cv2.imread(path)
        number = ocr.ocr(image, cls=False)

        if not number:
            row_result.append(None)
            df2_row.append(None)
        else:
            
            if number[0][1][1] < 0.8:
                df2_row.append(key + "_"+ str(i) + ".png " + str(number[0][1]))
                row_result.append(None)
            else:
                text = process_data(number[0][1][0], key)
                row_result.append(text)
                df2_row.append(None)


    result.append(row_result)
    df2_result.append(df2_row)
    print("\n\n#########################\t", str(i),"\t#########################\n\n" )
    

df = pd.DataFrame(result, columns=c.columns_t27)

path = 'csv/T27/T27_' + datetime.today().strftime('%m%d_%H%M') + '.csv'
df.to_csv(path, index= False)

df2 = pd.DataFrame(df2_result,  columns=c.columns_t27)
                           
path2 = 'csv/T27/T27_conf_' + datetime.today().strftime('%m%d_%H%M') + '.csv'
df2.to_csv(path2, index= False)