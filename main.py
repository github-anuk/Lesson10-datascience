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
data['race']=data['race'].map({' Black':0," Amer-Indian-Eskimo":1,' Asian-Pac-Islander':2," White":3," Other":4}).astype(int)
print(data.head())
marital=set(data['marital stat'])
print(marital)
data['marital stat']=data['marital stat'].map({' Divorced':0," Married-civ-spouse":1,' Widowed':2," Separated":3," Married-spouse-absent":4, ' Never-married':5,' Married-AF-spouse':6}).astype(int)
print(data.head())
workclasss=set(data['workclass'])
print(workclasss)
data['workclass']=data['workclass'].map({' Self-emp-not-inc':0," Federal-gov":1,' State-gov':2," Local-gov":3," Private":4, ' ?':5,' Never-worked':6,' Without-pay':7 ,' Self-emp-inc':8}).astype(int)
print(data.head())
eduuuu=set(data['eduction'])
print(eduuuu)
data['eduction']=data['eduction'].map({' 10th':0, ' 12th':1, ' 9th':2, ' Assoc-voc':3, ' Preschool':4, ' Bachelors':5, ' Some-college':6, ' 5th-6th':7, ' Masters':8, ' Doctorate':9, ' HS-grad':10, ' Prof-school':11, ' 1st-4th':12, ' 7th-8th':13, ' Assoc-acdm':14, ' 11th':15}).astype(int)
print(data.head())
loooo=set(data['occupation'])
print(loooo)
data['occupation']=data['occupation'].map({' Prof-specialty':0, ' Armed-Forces':1, ' Handlers-cleaners':2, ' Farming-fishing':3, ' ?':4, ' Other-service':5, ' Sales':6, ' Machine-op-inspct':7, ' Protective-serv':8, ' Transport-moving':9, ' Adm-clerical':10, ' Exec-managerial':11, ' Tech-support':12, ' Priv-house-serv':13, ' Craft-repair':14}).astype(int)
print(data.head())
rel=set(data['relationship'])
print(rel)
data['relationship']=data['relationship'].map({' Husband':0, ' Unmarried':1, ' Wife':2, ' Other-relative':3, ' Own-child':4, ' Not-in-family':5}).astype(int)
print(data.head())

#BAR GREPHHHH
data.groupby('eduction').income.mean().plot(kind="bar")
mp.show()
data.groupby('occupation').income.mean().plot(kind="bar")
mp.show()
data.groupby('workclass').income.mean().plot(kind="bar")
mp.show()
data.groupby('marital stat').income.mean().plot(kind="bar")
mp.show()
data.groupby('race').income.mean().plot(kind="bar")
mp.show()
data.groupby('gender').income.mean().plot(kind="bar")
mp.show()
data.groupby('relationship').income.mean().plot(kind="bar")
mp.show()