#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[4]:


def load_data_task_c(file_path):
    try:
        df_main = pd.read_csv(file_path, encoding="UTF-8")
        return df_main
        
    except FileNotFoundError:
        print(f" Error! The File at {file_path} could not be found. Please check the location and try again.")
    except Exception as e:
        print(f"An error has occured while loading the data: {e}")
    return None  


# In[5]:


def treatment_proportion_by_ethnicity(df_main, ethnicity):
    try:
        df_ethnicity = df_main.loc[df_main["Ethnicity"]==ethnicity]
        df_treatments = df_ethnicity["Treatment"].value_counts()
        treatment_labels = df_treatments.index.tolist()
        treatment_number = df_treatments.tolist()
        fig = plt.figure(figsize =(10,6))
        plt.pie(treatment_number,labels = treatment_labels, autopct = "%1.1f%%")
        plt.title(f"Proportion of Treatments for Ethnicity: {ethnicity}")
        plt.legend(loc = "best")
        plt.show()
    except Exception as e:
        print(f"An error has occured:{e}")


# In[6]:


def average_smoking_trend(df_main):
    try:
        df_group = df_main.groupby(["Stage","Ethnicity"])["Smoking_Pack_Years"].mean().unstack()
        fig = plt.figure(figsize=(15,8))
        for ethnicity in df_group.columns:
           plt.plot(df_group[ethnicity], df_group.index, marker = 'o', label = ethnicity)
        plt.xlabel("Average Smoking packs")
        plt.ylabel("Cancer Stages")
        plt.title("Trend of average smoking packs Across cancer stages by Ethnicity")
        plt.legend(title= "Ethnicity", loc = "best")
        plt.grid(axis = "both", linestyle = "--", alpha = 0.7)
        plt.show()
    except Exception as e:
        print(f"An error has occured:{e}")


# In[7]:


def blood_ppressure_comparison(df_main):
    try:
        df_group = df_main.groupby("Treatment")[["Blood_Pressure_Systolic", "Blood_Pressure_Diastolic", "Blood_Pressure_Pulse"]].mean()
        x_axis = np.arange(len(df_group))
        bar_width =0.2
        fig = plt.figure(figsize=(10,6))
        plt.bar(x_axis-bar_width, df_group["Blood_Pressure_Systolic"], width = bar_width, label = "Systolic", color = "blue")
        plt.bar(x_axis, df_group["Blood_Pressure_Diastolic"], width = bar_width, label = "Diastolic", color = "green")
        plt.bar(x_axis+bar_width, df_group["Blood_Pressure_Pulse"], width = bar_width, label = "Pulse", color = "red")
        plt.xticks(x_axis, df_group.index, rotation = 45)
        plt.xlabel("Treatments")
        plt.ylabel("Average Blood Pressure")
        plt.title("Comparison of Average blood pressure across different treatment types")
        plt.legend()
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"An error has occured:{e}")


# In[8]:


def age_vs_survival_for_treatments(df_main):
    try:
        plt.figure(figsize=(10,6))
        for treatment_name in df_main["Traetment"].unique():
            filtered_data = df_main[df_main["Treatment"]==treatment_name]
            plt.scatter(filtered_data["Age"], filtered_data["Survival_Months"],label = treatment_name, alpha = 0.6 , edgecolors = 'w', s = 100)
            plt.xlabel("Age")
            plt.ylabel("Survival Rate (In Months)")
            plt.title("Age VS Survival rate by Treatment Type")
            plt.legend(title = "Treatment Type")
            plt.show()
    except Exception as e:
        print(f"An error has occured:{e}")
            


# In[ ]:




