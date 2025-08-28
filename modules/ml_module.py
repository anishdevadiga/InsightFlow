#ml model training and evaluation
import streamlit as st
import pandas as pd
import numpy as np

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

def run_ml(data):
    target_column=st.selectbox("Select Tagret Column",data.columns)
    encoding =st.radio("Encoding for categorical features:",["none","label","onehot"],index=0)
     
    df,encoder=preprocess_data(data,target_column,encoding)

    # X and y initialization
    X =df.drop(columns=[target_column])
    y=df[target_column]

    #detect task type (classification if target has few unique values)
    task='regression'
    if y.nunique()<= 10 and y.dtype in [np.int64,np.int32,"category"]:  #removed np.object
        task='classification'
    
    st.write(f"Detected task: {task}")

    #train test split
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

    #model choice
    if task=='classification':
        model_choice=st.selectbox('Choose a classifier',
                                  ['Logisitic Regression',"Random Forest","Decision Tree","XGBoost"])
    else:
        model_choice=st.selectbox('Choose a classifier',
                                  ['Linear Regression',"Random Forest","Decision Tree","XGBoost"])
    if task=='classification':
        if model_choice=='Logisitic Regression':
            model=LogisticRegression(max_iter=1000)
        elif model_choice=="Random Forest":
            model=RandomForestClassifier()
        elif model_choice=="Decision Tree":
            model=DecisionTreeClassifier()
        else:
            model=xgb.XGBClassifier(use_label_encoder=False,eval_metric='logloss')

    #regression
    else:
        if model_choice=="Linear Regrssion":
            model=LinearRegression()
        elif model_choice=="Random Forest":
            model=RandomForestRegressor()
        elif model_choice=="Decision Tree":
            model=DecisionTreeRegressor()
        else:
            model=xgb.XGBRegressor()
    
    model.fit(X_train,y_train)
    y_pred=model.predict(X_test)

    st.subheader("Model Results")

    if task=="classification": 
        acc=accuracy_score(y_test,y_pred)
        prec=precision_score(y_test,y_pred,average="weighted")
        st.write("Accuracy",round(acc,3))
        st.write("Precision",round(prec,3))

        st.text("Classification Report:\n"+classification_report(y_test,y_pred))

        #Roc curve
        if len(np.unique(y_test))==2:
            y_proba=model.predict_proba(X_test)[:,1]
            fpr,tpr,_=roc_curve(y_test,y_proba)
            roc_auc=auc(fpr,tpr)

            fig,ax=plt.subplots()
            ax.plot(fpr,tpr,label=f'AUC = {roc_auc:.2f}')
            ax.plot([0,1],[0,1],linestyle="--")
            ax.set_xlabel("False Positive Rate")
            ax.set_ylabel("True Positive Rate")
            ax.set_title("ROC Curve")
            ax.legend(loc="lower right")
            st.pyplot(fig)
        
        else: #regression
            mse=mean_squared_error(y_test,y_pred)
            r2=r2_score(y_test,y_pred)
            st.write("Mean Squared Error",round(mse,3))
            st.write("R2 square",round(r2,3))

