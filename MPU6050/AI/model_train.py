import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler,StandardScaler
from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import pickle

# Load dataset and store it in pandas dataframe and print first 5 rows
DATASET_PATH = "PATH_TO_CSV_TRAINING_DATA"
df = pd.read_csv(DATASET_PATH)
print(df.head())

# Separate data into train and test
train_data, test_data = train_test_split(df, random_state=12, test_size=0.25)
X_train = train_data.drop(['Target', 'AccCovX', 'AccCovY', 'AccCovZ', 'GyroCovX', 'GyroCovY', 'GyroCovZ'], axis='columns')
y_train = train_data['Target']
X_test = test_data.drop(['Target', 'AccCovX', 'AccCovY', 'AccCovZ', 'GyroCovX', 'GyroCovY', 'GyroCovZ'], axis='columns')
y_test = test_data['Target']
print("X_train shape: " + str(X_train.shape))
print("y_train shape: " + str(y_train.shape))
print("X_test shape: " + str(X_test.shape))
print("y_test shape: " + str(y_test.shape))

# Load model from sklearn, standardize data and fit it to the train data
from sklearn.svm import SVC
# from sklearn.linear_model import LogisticRegression
scaler = MinMaxScaler(feature_range=(-1,1))
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = SVC(gamma='auto', kernel='linear')
# model = LogisticRegression()
model.fit(X_train_scaled, y_train)
filename = 'svc_classifier_inertial.sav'
pickle.dump(model, open(filename, 'wb'))

# Make predictions and evaluate model
y_pred = model.predict(X_test_scaled)
print(confusion_matrix(y_test, y_pred))
print("Accuracy: ", accuracy_score(y_test, y_pred))
# sns.heatmap(confusion_matrix(y_test, y_pred), annot=True)
# plt.show()
