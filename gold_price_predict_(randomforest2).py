# -*- coding: utf-8 -*-
"""gold price predict (RandomForest2)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11kqpL8EMCARYJ-36k4tC2K_YsfQRJrzk
"""

# Importing libraries that will be used in this Notebook.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics
!pip install tensorflow

import warnings
warnings.filterwarnings('ignore')

gold_data = pd.read_csv('/content/model_one_dataset.csv')

gold_data

#Using hide_index() from the style function
gold_data.head().style.hide_index()

#Gradient background color for the numerical columns
gold_data.head(10).style.background_gradient(cmap='Reds')

# last 10 rows of the dataframe (Gradient background color)
gold_data.tail(10).style.background_gradient(cmap = 'Blues')

# number of rows(2290) and columns(6)
gold_data.shape

# the label of each column in the DataFrame
gold_data.columns

# Check for null values
gold_data.isnull().sum()

plt.rcParams['figure.figsize'] = [12, 8]#resize the plot
#plt.figure(figsize = (12, 8))

gold_data.plot()
plt.show()

# statistical Measures of the dataset
gold_data.describe()

# Transpose index and columns.(Gradient background color)
gold_data.describe().T.style.background_gradient(cmap = 'Blues')

#mean
gold_data.mean()

# drop the "date",after the cor
data = gold_data.drop(['Date'], axis=1)

#To check for duplicates
data.duplicated().sum()

# Check for null values
data.isnull().sum()

#checking the distribution of the Gold Price.about outliers
sns.displot(data['USO'], color='green')
plt.title('USO Distribution')
plt.xlabel('USO Price')
plt.ylabel('Occurrences')
plt.show()

q = data["USO"].quantile(0.98)
data[data["USO"] > q]
data = data[(data["USO"] < q)]

#checking the distribution of the Gold Price.about outliers
sns.displot(data['USO'], color='green')
plt.title('USO Distribution')
plt.xlabel('USO Price')
plt.ylabel('Occurrences')
plt.show()

#checking the distribution of the Gold Price.about outliers
sns.displot(data['SPX'], color='blue')
plt.title('SPX Distribution')
plt.xlabel('SPX Price')
plt.ylabel('Occurrences')
plt.show()

#checking the distribution of the Gold Price.about outliers
sns.displot(data['GLD'], color='gold')
plt.title('Gold Distribution')
plt.xlabel('Gold Price')
plt.ylabel('Occurrences')
plt.show()

#checking the distribution of the Gold Price.about outliers
sns.displot(data['SLV'], color='silver')
plt.title('SLV Distribution')
plt.xlabel('SLV Price')
plt.ylabel('Occurrences')
plt.show()

#checking the distribution of the Gold Price.about outliers
sns.displot(data['EUR/USD'], color='cyan')
plt.title('EUR/USD exchange-rate Distribution')
plt.xlabel('EUR/USD exchange-rate')
plt.ylabel('Occurrences')
plt.show()

"""correlation"""

# Compute pairwise correlation of columns
# to identity the highly correlated features.
correlation = data.corr()

# Construct a heatmap to undestand the correlation
plt.figure(figsize= (8,8))
sns.heatmap(correlation, cbar=True, square=True, fmt='.2f', annot=True, annot_kws={'size':10}, cmap='Greens')

# correlation values of Gold
print(correlation['GLD'])

# discard the gold and use the rest values as features
X = data.drop(['GLD'], axis=1)

# use the gold as the target
Y = data['GLD']

# The Features (input)
X
#The Features (input)(Gradient background color)
#X.style.background_gradient(cmap='Reds')

# The target
Y
# The target(Gradient background color)
#Y.style.background_gradient(cmap='Reds')

# Split arrays or matrices into random train and test subsets
#random_state #Testing the model with 20% of the dataset & training it with 80% of the model
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size= 0.2, random_state=0)

regressor = RandomForestRegressor(n_estimators=100)

# training the model
regressor.fit(X_train, Y_train)

# prediction on Test Data
test_data_prediction = regressor.predict(X_test)

print(test_data_prediction)

# R Squared error
error_score = metrics.r2_score(Y_test, test_data_prediction) # coefficient of determination, regression score function.
print('R squared error : ', error_score)

Y_test = np.array(Y_test)
#Y_test = list(Y_test) #Converting the actual values to a list,so that it can be in the same format as the test_data_prediction

plt.rcParams['figure.figsize'] = [10, 8]#resize the plot
plt.plot(Y_test, color='blue', label='Actual Value')
plt.title('Actual Price vs Predicted Price')
plt.xlabel('Number of values')
plt.ylabel('Golden Price')
plt.legend()
plt.show()

plt.plot(test_data_prediction, color='red', label='Predicted value')
plt.title('Actual Price vs Predicted Price')
plt.xlabel('Number of values')
plt.ylabel('Golden Price')
plt.legend()
plt.show()

plt.plot(Y_test, color='blue', label='Actual Value')
plt.plot(test_data_prediction, color='red', label='Predicted value')
plt.title('Actual Price vs Predicted Price')
plt.xlabel('Number of values')
plt.ylabel('Golden Price')
plt.legend()
plt.show()

plt.figure(figsize = (12,8))
plt.hist(Y_test, color='purple', label = 'Actual Value')
plt.hist(test_data_prediction, color='green', label='Predicted Value')
plt.title('Actual Price of Gold vs Predicted Price of Gold')
plt.xlabel('Number of values')
plt.ylabel('GOLD Price', rotation=30)
plt.legend()
plt.show()

def convertor(user_input):

    for i in range(len(user_input)):
        user_input[i] = float(user_input[i])

    print("values = ", tuple(user_input))
    return tuple(user_input)

print("how many values will you calculate: (NOTE: Press q to break)")
count = int(input())

while (count != 0):

    count = count-1
    input_string = input()
    user_input = input_string.split()
    if(input_string.lower() == "q"):
        print("END")
        break
    input_data = convertor(user_input)
    # changing input_data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)#search

    # implementing the trained model
    prediction = regressor.predict(input_data_reshaped)
    print(prediction)

    print('The cost of the gold is:', prediction[0])

#1310.5       70.550003   15.902     1.464794                           #row_15   - 88.169998
#1336.910034  69.800003   16.674999  1.483107                           #row_21   - 92.059998
#1556.219971  33.040001   28.02      1.298802                           #row_1144 - 152.990005

"""Convert the Model:
Use TensorFlow Lite Converter to convert your model to the TensorFlow Lite format. You'll need to specify the input and output formats and any optimizations you want to apply. Here's an example of how to convert a TensorFlow SavedModel:
"""

