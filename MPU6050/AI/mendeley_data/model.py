import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns

# Load dataset and store it in pandas dataframe and print first 5 rows
DATASET_PATH = "E:\\Gustavo\\GENERA\\Direção Segura\\MPU6050\\AI\\mendeley_data\\Features By Window Size\\features_14.csv"
df = pd.read_csv(DATASET_PATH)
print(df.head())

# Separate data into train and test
train_data, test_data = train_test_split(df, random_state=12, test_size=0.25)
X_train = train_data.drop('Target', axis='columns')
y_train = train_data['Target']
X_test = test_data.drop('Target', axis='columns')
y_test = test_data['Target']

# Load model from sklearn, standardize data and fit it to the train data
from sklearn.svm import SVC
scaler = MinMaxScaler(feature_range=(-1,1))
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = SVC(gamma='auto', kernel='linear')
model.fit(X_train_scaled, y_train)

# Make predictions and evaluate model
y_pred = model.predict(X_test_scaled)
print(confusion_matrix(y_test, y_pred))
print("Accuracy: ", accuracy_score(y_test, y_pred))
# sns.heatmap(confusion_matrix(y_test, y_pred), annot=True)
# plt.show()