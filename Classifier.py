import streamlit as st 
import numpy as np
import pandas as pd
from sklearn import datasets


st.title("Classifier Example")

st.write("""
### Explore Different Classifier
Which one is the best?
""")

#Selection of Dataset
Dataset = st.sidebar.selectbox("Select Dataset",("Iris","Breast Cancer","Wine Dataset"))
#Selection of Classifier
classifierName =  st.sidebar.selectbox("Select Dataset",("KNN","SVM","Random Forest"))

#loading the datset
def getDataset(Dataset):
    if Dataset== "Iris":
        data = datasets.load_iris()
    elif Dataset=="Breast Cancer":
        data =  datasets.load_breast_cancer()
    else:
        data=datasets.load_wine()
    X =  data.data
    y = data.target
    return X,y

#Getting the shape of our data
X, y = getDataset(Dataset)
st.write("Shape of the data",X.shape)
st.write("Number of Classes", len(np.unique(y)))

#Adding Parameters to the Classifier
def AddParameters(classifierName):
    params = dict()
    if classifierName=="KNN":
        K = st.sidebar.slider("K",1,15)
        params["K"]=K
    elif classifierName=="SVM":
        C = st.sidebar.slider("C",0.01,10.0)
        params["C"]=C
    else:
        max_depth = st.sidebar.slider("MaxDepth",2,15)
        NumberEst = st.sidebar.slider("Number of estimators",1,100)
        params["Max_depth"]=max_depth
        params["NEstimators"]=NumberEst
    return params

AddParameters(classifierName)
