import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
import plotly
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data=pd.read_csv("Social_Media_Engagement.csv")
print(data.head())
print(data.info())
data.drop(['Posts Per Week','Engagement Rate','Ad Spend (USD)','Conversion Rate','Campaign Reach'],axis=1,inplace=True)
print(data.info())
Platform=set(data['Platform'])
print(Platform)
data['Platform']=data['Platform'].map({'LinkedIn':0,"TikTok":1,'Facebook':2,"Twitter":3,"Instagram":4}).astype(int)
print(data.head())

SLAYd= pd.DataFrame(data.groupby("Platform")['Follower Count'].sum().nlargest(5).sort_values(ascending=False))
fig1 = px.scatter(SLAYd,x=SLAYd.index,y='Follower Count',size='Follower Count',size_max=50,color=SLAYd.index,title="MOST FOLLOWERS FOR EACH PLATFORMM")
fig1.write_html("Fig1.html",auto_open=True)

top5_YAY=pd.DataFrame(data.groupby('Follower Count')['Platform'].sum().nlargest(5).sort_values(ascending=False))
yay=px.bar(top5_YAY,x=top5_YAY.index,y='Platform',height=600,color='Platform',title='MOST PLATFORM FOR FLOWERES??',color_continuous_scale=px.colors.sequential.Viridis)
yay.write_html('YAYYAYAY.html',auto_open=True)