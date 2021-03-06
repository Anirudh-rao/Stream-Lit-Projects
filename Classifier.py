import streamlit as st 
import numpy as np 

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split

from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score


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
def add_parameter_ui(clf_name):
    params = dict()
    if clf_name == 'SVM':
        C = st.sidebar.slider('C', 0.01, 10.0)
        params['C'] = C
    elif clf_name == 'KNN':
        K = st.sidebar.slider('K', 1, 15)
        params['K'] = K
    else:
        max_depth = st.sidebar.slider('max_depth', 2, 15)
        params['max_depth'] = max_depth
        n_estimators = st.sidebar.slider('n_estimators', 1, 100)
        params['n_estimators'] = n_estimators
    return params

params = add_parameter_ui(classifierName)

def GetClassifier(clf_name, params):
    clf = None
    if clf_name == 'SVM':
        clf = SVC(C=params['C'])
    elif clf_name == 'KNN':
        clf = KNeighborsClassifier(n_neighbors=params['K'])
    else:
        clf = clf = RandomForestClassifier(n_estimators=params['n_estimators'], 
            max_depth=params['max_depth'], random_state=1234)
    return clf


clf =  GetClassifier(classifierName,params)

#Building the Classifier
X_train, X_test, y_train, y_test =  train_test_split(X,y,test_size=0.2,random_state=1234)

#fitting to model to train set
clf.fit(X_train,y_train)
#prediction on test set
y_pred = clf.predict(X_test)

#Calculation of accuray
acc =  accuracy_score(y_test,y_pred)
#Printing accuracy
st.write(f'Classifier={classifierName}')
st.write(f'Accuracy:',acc)

pca= PCA(2)
X_projected = pca.fit_transform(X)

x1 = X_projected[:, 0]
x2 = X_projected[:, 1]

#Visualizations
fig  = plt.figure()
plt.scatter(x1,x2,c=y,alpha=0.8,cmap='viridis')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar()

#plt.show()
st.pyplot(fig)