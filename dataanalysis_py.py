# -*- coding: utf-8 -*-
"""DataAnalysis.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZJMCvx6nfC90ipCw6yB1Wm8FKumh38D9
"""

import numpy as np
import pandas as pd
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv("bestsellers with categories.csv")
df

df.info()

df.head()

df.head(99)

df.sort_values("User Rating",ascending=False)

df.sort_values("Price",ascending=False)

df.sort_values("Price",ascending=True)

y = df["Price"].value_counts()
y.plot(kind="bar")

y = df["User Rating"].value_counts()
y.plot(kind="bar")

y = df["Genre"].value_counts()
y.plot(kind="bar")

y = df["User Rating"].value_counts()
y.plot(kind="line")

y = df["Price"].value_counts()
y.plot(kind="pie")

y = df["Price"].value_counts()
y.plot(kind="pie")

dg = df["Genre"]
dg

fig = px.histogram(df, x="User Rating",labels={'':'The Number of Books'},title="User Rating Histogram")
fig.show()

fig = px.histogram(df, x="Price",labels={'':'The Number of Books'},title="User Rating Histogram")
fig.show()

px.scatter(df['Name'],df['User Rating'])

px.scatter(df['Name'],df['Author'])

df['Name_len']=df['Name'].str.len()

px.scatter(df.sort_values(by='Year'),x='User Rating',y='Price', animation_frame='Year', color='Genre',size='Name_len', 
title="Over all book Rating & Price by every year")

correlation = df.corr()
plt.figure(figsize = (10,6))
sns.heatmap(correlation,annot=True)
plt.show()

correlation = df.corr()
plt.figure(figsize = (10,6))
sns.heatmap(correlation,annot=False)
plt.show()

from sklearn.model_selection import train_test_split

df['Name_len']=df['Name'].str.len()

px.bar(df,x='Year',y='User Rating',  color='Genre', barmode='group', title="User Rating by Year by Genre")

y = df["User Rating"].value_counts()
y.plot(kind="hist")

y = df["Price"].value_counts()
y.plot(kind="hist")

px.bar(df, x='Genre')

df.boxplot(column='Price',by = 'Genre')
plt.show()

df.plot(subplots = True)
plt.show()

