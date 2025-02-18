# Importing libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.experimental import enable_iterative_imputer  # Enables IterativeImputer
from sklearn.impute import IterativeImputer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from imblearn.over_sampling import RandomOverSampler
from sklearn.metrics import confusion_matrix
from imblearn.combine import SMOTEENN
from .models import models
from sklearn.model_selection import GridSearchCV
from user.to_csv import *
import os
# Ensure inline plots (useful in notebooks; can be removed for scripts)
# %matplotlib inline  # Comment this line for .py files
def scale(df,oversample=False):
    x = df[df.columns[:-1]].values
    y = df[df.columns[-1]].values
    scaler = StandardScaler()
    x = scaler.fit_transform(x)
    scaler = MinMaxScaler()
    x = scaler.fit_transform(x)
    y = y.astype(int)  # Ensure y is of integer type
    if oversample:
        
        # ros = TomekLinks()
        # ros = ADASYN()
        # ros = RandomOverSampler(random_state=41)
        # x, y = ros.fit_resample(x, y)
        ros=SMOTEENN()
        # ros=SMOTE()
        x, y = ros.fit_resample(x,y)
    #data = np.hstack([x,np.reshape(y,(-1,1))])
    return x, y
# Load the dataset
def corr_cleaned_ind(corr,data):
    threshold = 0.9
    # Get the upper triangle of the correlation matrix
    upper = corr.where(np.triu(np.ones(corr.shape), k=1).astype(bool))

    # Find columns with correlation greater than the threshold
    to_drop = [column for column in upper.columns if any(upper[column] > threshold)]

    # Drop the highly correlated features
    data_cleaned = data.drop(columns=to_drop)
    return data_cleaned
def corr_cleaned_de(corr, data):
    col = data.columns  # Define 'col' as the list of column names in 'data'
    for i in range(len(col)):
        column_corr = corr[col[i]].abs()  # Get the absolute correlation
        column_corr = column_corr[column_corr < 1]  # Ignore self-correlation
        if column_corr.max() < 0.1:
            data = data.drop(col[i], axis=1)
    return data  # Return the modified DataFrame

def model(num_pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, DiabetesPedigreeFunction, age):
    get_from_database()
    data = pd.read_csv("user/processed_data.csv")
    if os.path.getsize('user/output.csv') !=0:
        df = pd.read_csv('user/output.csv')
        data = pd.concat([data,df],axis=0)
        data.reset_index(drop=True,inplace=True)
    x = {
        'Pregnancies': num_pregnancies,
        'Glucose': glucose,
        'BloodPressure': blood_pressure,
        'SkinThickness': skin_thickness,
        'Insulin': insulin,
        'BMI': bmi,
        'DiabetesPedigreeFunction': DiabetesPedigreeFunction,
        'Age': age,
        'Outcome': 0
    }
    cols = data.columns
    x = pd.DataFrame([x],columns=cols)
    data = pd.concat([data,x],axis=0)
    data.reset_index(drop=True,inplace=True)
    correlation_matrix = data.corr()
    correlation_matrix = correlation_matrix.drop(columns='Outcome',axis=1)
    correlation_matrix = correlation_matrix.drop(correlation_matrix.index[-1],axis=0)
    data = corr_cleaned_ind(correlation_matrix,data)
    correlation_matrix = data.corr()
    data = corr_cleaned_de(correlation_matrix,data)
    x = data.iloc[-1, :]
    x = pd.DataFrame([x],columns=cols)
    data = data.drop(data.index[-1])
    # Splitting data into training and testing sets
    check=False
    while check==False:
        train,test = train_test_split(data,test_size=0.20)
        test = pd.concat([test,x],axis=0)
        test.reset_index(drop=True,inplace=True)
        x_train,y_train = scale(train,oversample=True)
        x_test,y_test = scale(test)
        # Initialize the SVM classifier
        svm = SVC()
        parameters = {
            'degree': [0, 1, 6],
            'C': [0.1, 1, 10],
            'gamma': [0.1, 1, 10,],
            'kernel': ['linear', 'rbf', 'poly']
        }
        grid_search = GridSearchCV(estimator = svm,  
                                param_grid = parameters,
                                scoring = 'accuracy',
                                cv = 5,
                                verbose=0)
        # Perform GridSearchCV for hyperparameter tuning with cross-validation
        grid_search.fit(x_train, y_train)
        y_pred = grid_search.predict(x_test)
    # After training your model and making predictions (y_pred), calculate the confusion matrix
        cm = confusion_matrix(y_test, y_pred)

        # Extract False Positives (Type I Error)
        type_i_error = cm[1, 0]
        if type_i_error <= 12:
            check=True
        else:
            pass
    # models.objects.last().diabetes_prediction = y_pred[0]
    # models.objects.last().save()
    return y_pred[-1]
def probability(num_pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, DiabetesPedigreeFunction, age): 
    m = []
    for i in range(25):
        m.append(model(num_pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, DiabetesPedigreeFunction, age))
    return m.count(1)/25, m.count(0)/25