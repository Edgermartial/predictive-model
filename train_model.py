import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
#load dataset
data=pd.read_csv(r"C:\Users\edger\Desktop\AED PROJECT\archive\ai 2020.csv")
#select features and target variable
X=data[['Air temperature [K]','Process temperature [K]','Rotational speed [rpm]','Torque [Nm]','Tool wear [min]']]
y=data['Machine failure']
#split the data
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
#train model
model=RandomForestClassifier(random_state=42)
model.fit(X_train,y_train)
#save the model
joblib.dump(model,'machine_failure_model.pkl')