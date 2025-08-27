#ml model training and evaluation
import streamlit as st
import pandas as pd
import numpy as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,precision_score,classification_report,roc_curve,auc,mean_squared_error,r2_score
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression,LinearRegression
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor
from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
import xgboost as xgb

def preprocess_data(data,target_column,encoding='none'):
    df=data.copy()

    #drop rows with missing target
    df =df.dropna(subset=[target_column])

    if encoding == 'label':
        label_encoder={}
        for col in df.select_dtypes(include=['object','category']).columns:
            le=LabelEncoder()
            df[col]=le.fit_transform(df[col].astype(str))
            label_encoder[col]=le
        return df,label_encoder
    elif encoding=='onehot':
        df = pd.get_dummies(df,drop_first=True)
        return df,None
    
    return df,None #if no encodig is done
