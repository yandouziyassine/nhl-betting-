import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

from google.colab import files
uploaded = files.upload()

dataset = pd.read_excel(io.BytesIO(uploaded['tableau stat nhl.xlsx']))
dataset.head()
sns.distplot(dataset['COTE SPORTIVE'])
dataset.shape
dataset.isna().sum()
dataset.duplicated().any()

x = dataset[['Pourcentage de victoire']]
y = dataset['COTE SPORTIVE']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 100)

slr= LinearRegression()
slr.fit(x_train, y_train)
print('Intercept: ', slr.intercept_)
print('Coefficient:', slr.coef_)

y_pred_slr= slr.predict(x_test)
x_pred_slr= slr.predict(x_train)
print("Prediction for test set: {}".format(y_pred_slr))

