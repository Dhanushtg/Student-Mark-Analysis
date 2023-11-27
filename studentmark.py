import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_column',None)
df = pd.read_csv("Expanded_data_with_more_features.csv")
print("\n Raw DataSet \n")
print(df.describe())
print(df.info())
print(df.isnull().sum())
df= df.drop('Unnamed: 0',axis=1)
print(df.head())
print("\n Removed the unwanted Column \n ")
plt.figure(figsize=(6,5))
ax= sns.countplot(data= df,x="Gender")
ax.bar_label(ax.containers[0])
plt.title("Gender ContPlot")
plt.show()
print("\n Plotted the graph based on Gender \n ")
gp =df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gp)
sns.heatmap(gp, annot=True)
plt.title("Realation Between Parent Edu and Student Score")
plt.show()
print(" \n Grouped by parent education and the students scores \n ")
gp1=df.groupby("ParentMaritalStatus").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
print(gp1)
sns.heatmap(gp1,annot=True)
plt.title("Realation Between Parent marital status and Student Score")
plt.show()
print("\n Grouped by parent marital status and the students scores \n ")
print("\n Plotting boxplot to find outliers in the student score \n")
sns.boxplot(data=df,x="MathScore")
plt.title("Outlier Detection on MathScore")
plt.show()
sns.boxplot(data=df,x="ReadingScore")
plt.title("Outlier Detection on ReadingScore")
plt.show()
sns.boxplot(data=df,x="WritingScore")
plt.title("Outlier Detection on WritingScore")
plt.show()
print("\n Printing the unique values of Ethinic group \n")
print(df["EthnicGroup"].unique())
print("\n Counting the ethinicgroup and creating pie chatr \n")
groupA = df.loc[(df["EthnicGroup"]=="group A")].count()
groupB = df.loc[(df["EthnicGroup"]=="group B")].count()
groupC = df.loc[(df["EthnicGroup"]=="group C")].count()
groupD = df.loc[(df["EthnicGroup"]=="group D")].count()
groupE = df.loc[(df["EthnicGroup"]=="group E")].count()
l=["group A","group B","group C","group D","group E"]
mlist=[groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]
plt.title("\n Percentage of students in different EthincGroup \n ")
plt.pie(mlist,labels=l,autopct="%1.2f%%")
print(mlist)
plt.show()
ad= sns.countplot(data=df,x="EthnicGroup")
ad.bar_label(ad.containers[0])
plt.title("CountPlot for the EthnicGroups")
plt.show()







 