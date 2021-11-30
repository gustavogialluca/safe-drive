import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler,StandardScaler
import pickle
from math import pi

# Read data from txt file, transform Gyro data into degrees/second and store it into pandas dataframe
df = pd.read_csv("PATH_TO_CSV_DATA_FOR_INFERENCE")
print(df.head())
df.iloc[:, -3:] = df.iloc[:,-3:].apply(lambda x: 180*x/pi)
print(df.head())

# columns = ['AccMeanX','AccMeanY','AccMeanZ','AccCovX','AccCovY','AccCovZ','AccSkewX','AccSkewY','AccSkewZ','AccKurtX','AccKurtY','AcKurtZ','AccSumX','AccSumY','AccSumZ','AccMinX','AccMinY','AccMinZ',
#             'AccMaxX','AccMaxY','AccMaxZ','AccVarX','AccVarY','AccVarZ','AccMedianX','AccMedianY','AccMedianZ','AccStdX','AccStdY','AccStdZ','GyroMeanX','GyroMeanY','GyroMeanZ','GyroCovX','GyroCovY','GyroCovZ',
#                 'GyroSkewX','GyroSkewY','GyroSkewZ','GyroSumX','GyroSumY','GyroSumZ','GyroKurtX','GyroKurtY','GyroKurtZ','GyroMinX','GyroMinY','GyroMinZ','GyroMaxX','GyroMaxY','GyroMaxZ','GyroVarX','GyroVarY',
#                     'GyroVarZ','GyroMedianX','GyroMedianY','GyroMedianZ','GyroStdX','GyroStdY','GyroStdZ']

columns = ['AccMeanX','AccMeanY','AccMeanZ','AccSkewX','AccSkewY','AccSkewZ','AccKurtX','AccKurtY','AcKurtZ','AccSumX','AccSumY','AccSumZ','AccMinX','AccMinY','AccMinZ',
            'AccMaxX','AccMaxY','AccMaxZ','AccVarX','AccVarY','AccVarZ','AccMedianX','AccMedianY','AccMedianZ','AccStdX','AccStdY','AccStdZ','GyroMeanX','GyroMeanY','GyroMeanZ',
                'GyroSkewX','GyroSkewY','GyroSkewZ','GyroSumX','GyroSumY','GyroSumZ','GyroKurtX','GyroKurtY','GyroKurtZ','GyroMinX','GyroMinY','GyroMinZ','GyroMaxX','GyroMaxY','GyroMaxZ',
                    'GyroVarX','GyroVarY','GyroVarZ','GyroMedianX','GyroMedianY','GyroMedianZ','GyroStdX','GyroStdY','GyroStdZ']

list_input = []

# Acceleration
list_input.append(df['ax'].mean())
list_input.append(df['ay'].mean())
list_input.append(df['az'].mean())

# list_input.append(df['ax'].cov(other=df['ax']))
# list_input.append(df['ay'].cov(other=df['az']))
# list_input.append(df['az'].cov(other=df['ax']))

list_input.append(df['ax'].skew())
list_input.append(df['ay'].skew())
list_input.append(df['az'].skew())

list_input.append(df['ax'].kurt())
list_input.append(df['ay'].kurt())
list_input.append(df['az'].kurt())

list_input.append(df['ax'].sum())
list_input.append(df['ay'].sum())
list_input.append(df['az'].sum())

list_input.append(df['ax'].min())
list_input.append(df['ay'].min())
list_input.append(df['az'].min())

list_input.append(df['ax'].max())
list_input.append(df['ay'].max())
list_input.append(df['az'].max())

list_input.append(df['ax'].var())
list_input.append(df['ay'].var())
list_input.append(df['az'].var())

list_input.append(df['ax'].median())
list_input.append(df['ay'].median())
list_input.append(df['az'].median())

list_input.append(df['ax'].std())
list_input.append(df['ay'].std())
list_input.append(df['az'].std())

# Gyro
list_input.append(df['gx'].mean())
list_input.append(df['gy'].mean())
list_input.append(df['gz'].mean())

# list_input.append(df['gx'].cov())
# list_input.append(df['gy'].cov())
# list_input.append(df['gz'].cov())

list_input.append(df['gx'].skew())
list_input.append(df['gy'].skew())
list_input.append(df['gz'].skew())

list_input.append(df['gx'].kurt())
list_input.append(df['gy'].kurt())
list_input.append(df['gz'].kurt())

list_input.append(df['gx'].sum())
list_input.append(df['gy'].sum())
list_input.append(df['gz'].sum())

list_input.append(df['gx'].min())
list_input.append(df['gy'].min())
list_input.append(df['gz'].min())

list_input.append(df['gx'].max())
list_input.append(df['gy'].max())
list_input.append(df['gz'].max())

list_input.append(df['gx'].var())
list_input.append(df['gy'].var())
list_input.append(df['gz'].var())

list_input.append(df['gx'].median())
list_input.append(df['gy'].median())
list_input.append(df['gz'].median())

list_input.append(df['gx'].std())
list_input.append(df['gy'].std())
list_input.append(df['gz'].std())

# Transform list of data into pandas dataframe
df_input = pd.DataFrame([list_input])
print(df_input.head())

# Scale data and load model to make predictions
scaler = MinMaxScaler(feature_range=(-1,1))
X_test_scaled = scaler.fit_transform(df_input)
filename = 'lr_classifier_inertial.sav'
model = pickle.load(open(filename, 'rb'))
prediction = model.predict(X_test_scaled)
prediction_prob = model.predict_proba(X_test_scaled)
print("PREDICTION: " + str(prediction))
print("PREDICTION PROBABILITY: " + str(prediction_prob))
