import cv2
from matplotlib import pyplot as plt
from paddleocr import PaddleOCR
import numpy as np
import statistics as stat
import pandas as pd
from datetime import datetime
import constants as c
from collections import Counter
from scipy import stats

ocr = PaddleOCR(lang='en',  use_angle_cls=True)

def processing_image(image):
    cropped_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cropped_image = cv2.bitwise_not(cropped_image)
    M = np.ones(cropped_image.shape, dtype="uint8") * 30
    cropped_image = cv2.subtract(cropped_image, M)
    
    return cropped_image

def final_value(list_value):
  if list_value:
    m = round(np.mean(list_value),1)
    mode = round(stat.mode((list_value)),1)
    if abs(m - mode)> 5:
      return None
    return m
  return None

def drop_outliers(angles):
  if angles:
      z = np.abs(stats.zscore(angles))
      #print(z)
      if np.all(np.isnan(z)):
          return angles
      new_angles = []
      for i in range(len(angles)):
          if z[i]<1.3 and z[i]> 0.3:
              new_angles.append(angles[i])
      return new_angles

def corr_scala(value, scale):
    if value:
        aux = value%scale
        value = value - aux
        if aux >= scale/2:
            value = value + scale
            
    return value

def select_result_OCR(result_ocr, table_scale, dist_scale):
    list_OCR  = []
    for linha in result_ocr:
        try:
            number = int(linha[1][0])
        except:
            number = None
        if number!= None and not number%table_scale:
            list_OCR.append((number, (linha[0][0][1] + linha[0][3][1])/2))
    
    list_OCR_validos = []
    idx_max = 0
    max = -1
    for i in range(len(list_OCR)-1):
        aux1 = []
        
        
        
        for j in range(i+1,len(list_OCR)):
            
            calc = round((list_OCR[j][1] - list_OCR[i][1])*table_scale/dist_scale) + list_OCR[j][0]
            calc = corr_scala(calc, table_scale)
            
            if list_OCR[i][0]== calc:
                aux1.append(list_OCR[j])
        if len(aux1):
            aux1.append(list_OCR[i])
            
            if len(aux1) >= max:
                max = len(aux1)
                idx_max = i
        list_OCR_validos.append(aux1)
    if list_OCR_validos:
        return list_OCR_validos[idx_max]
    else: 
        return None

def calc_ind(list_OCR_validos, table_scale, dist_scale, inst_scale, ref):
    list_result = []
    value = None
    if list_OCR_validos:
        for item in list_OCR_validos:
            result = round(item[0] + (item[1] - ref)*table_scale/dist_scale,0)
            list_result.append(result)
        list_result = drop_outliers(list_result)
        value = final_value(list_result)
        value = corr_scala(value, inst_scale)
        
    return value

directory = '../frames/C95/'
result = []
df2_result = []
df3_result = []
ini = 0
quant = 1800



for i in range(ini,quant):
    print("\n\n#################################### ", i, "####################################\n\n ")
    
    
    row_result = []
    
    for key, param in c.inst_voo_C95.items():
        #print(key)
        path = directory + 'v0_min_'+ key + '/' + key +"_" +  str(i) + '.png'
        #print(path)
        image = cv2.imread(path)
        image = processing_image(image)
        ref = image.shape[0]/2
        list_ocr = ocr.ocr(image, cls=False)
        #for line in list_ocr:
            #print(line)
        list_ocr = select_result_OCR(list_ocr, c.scale_table_C95[key], c.dist_scala_C95)
        #print("list_ocr:", list_ocr)
        number = calc_ind(list_ocr, c.scale_table_C95[key], c.dist_scala_C95,c.scale_voo_C95[key], ref)
        #print("number:", number)
        row_result.append(number)
        


    result.append(row_result)

df = pd.DataFrame(result, columns=["SPEED","ALT"])

path = 'csv/C95/C95_VOO_' + datetime.today().strftime('%m%d_%H%M') + '.csv'
df.to_csv(path, index= False)