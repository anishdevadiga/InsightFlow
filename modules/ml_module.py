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

