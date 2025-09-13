# https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

#Inspect the data 
print("Simple information: \n",df.info())
print("Describe the stats of the data set: \n",df.describe())

#Handel missing data
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

#Remove duplicates
df = df.drop_duplicates()
print("Modified dataset: \n",df.info())

#Filters data: passengers in 1st class
first_class = df[df["Pclass"]==1]
print("First class passengers: \n",first_class.head())

#Bar chart: Survival rate by class
def bar_chart():
    survival_data = df.groupby("Pclass")["Survived"].mean()
    survival_data.plot(kind="bar",color="skyblue")
    plt.title("Survival rate by class")
    plt.ylabel("Survival Rate")
    plt.show()

#Histogram: Age distribution
def histogram():
    sns.histplot(df["Age"],kde=True,bins=20,color="purple")
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()

#Scatter Plot: Age vs Fare
def scatter_plot():
    plt.scatter(df["Age"],df["Fare"],alpha=0.5,color="green")
    plt.title("Age Vs Fare")
    plt.xlabel("Age")
    plt.ylabel("Fare")
    plt.show()

print("1-->Bar chart | 2-->Histogram |3-->Scatter Plot |4-->Exit")
cond = True

while cond == True:
    choice = int(input("Enter your choice: "))
    if choice==1:
        bar_chart()
    elif choice==2:
        histogram()
    elif choice==3:
        scatter_plot()
    elif choice==4 :
        cond = False
    else:
        print("Invalid Input!!, try again")

print("Thank you,Sir")