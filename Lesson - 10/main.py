import numpy as np
import pandas as pd
import matplotlib.pyplot as mp

data=pd.read_csv("adult.csv")

data.columns=["age","workclass",'id','eduction','edu.no','marital-status','occupation','relationship','race','gender','capital-gain','capital-loss','hours-per-week','native-country','income']
data.rename(columns={"capital-gain":"capital gain","capital-loss":'capital loss','marital-status':'marital stat','native-country':'native country'},inplace=True)
print(data.describe())#description of numerical data ie mean,std,min,25%etc
print(data.info())
print(data.isnull().sum())
print(data.isin(['?']).sum(axis=0))
#data.drop will help remove pieces of data when is unesscessary
data.drop(['edu.no','age','hours-per-week','id','capital gain','capital loss','native country'],axis=1,inplace=True)
print(data.info())
#SET-a dat structure which helps u get unique values
income=set(data["income"])
print(income)

#mappin using map function into numerical data

data['income'] = data['income'].map({" <=50K":0,' >50K':1,}).astype(int)
print(data.head())

data['gender']=data['gender'].map({" Male":0,' Female':1,}).astype(int)
print(data.head())
race=set(data['race'])
print(race)
data['race']=data['race'].map({' Black':0," Amer-Indian-Eskimo":1,' Asian-Pac-Islander':2," White":3," Other":4})
print(data.head())
maritaljstat=set(data['marital stat'])
print(maritaljstat)