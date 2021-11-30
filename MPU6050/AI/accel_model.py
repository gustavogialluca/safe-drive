import numpy as np
import pandas as pd

# Read data from txt file and store it into pandas dataframe
df = pd.read_csv("E:\\Gustavo\\GENERA\\Direção Segura\\MPU6050\\dados\\testes_dia_2\\15_desaceleracao_brusca.txt")
print(df.head())

columns = ['Target','AccMeanX','AccMeanY','AccMeanZ','AccCovX','AccCovY','AccCovZ','AccSkewX','AccSkewY','AccSkewZ','AccKurtX','AccKurtY','AcKurtZ','AccSumX','AccSumY','AccSumZ','AccMinX','AccMinY','AccMinZ',
            'AccMaxX','AccMaxY','AccMaxZ','AccVarX','AccVarY','AccVarZ','AccMedianX','AccMedianY','AccMedianZ','AccStdX','AccStdY','AccStdZ','GyroMeanX','GyroMeanY','GyroMeanZ','GyroCovX','GyroCovY','GyroCovZ',
                'GyroSkewX','GyroSkewY','GyroSkewZ','GyroSumX','GyroSumY','GyroSumZ','GyroKurtX','GyroKurtY','GyroKurtZ','GyroMinX','GyroMinY','GyroMinZ','GyroMaxX','GyroMaxY','GyroMaxZ','GyroVarX','GyroVarY',
                    'GyroVarZ','GyroMedianX','GyroMedianY','GyroMedianZ','GyroStdX','GyroStdY','GyroStdZ']

df_final = pd.DataFrame(columns=columns)

print(df_final.head())