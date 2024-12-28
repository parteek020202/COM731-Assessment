#!/usr/bin/env python
# coding: utf-8

# In[3]:


import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[4]:


def load_data_task_c(file_path): #loads function using the file path entered during first step data loading
    #user does not need to enter the file path or name again
    
    try:
        df_main = pd.read_csv(file_path, encoding="UTF-8")
        #returns the main dataframe which will be passed as a parameter to all the functions and used throughout the program
        return df_main
        
    except FileNotFoundError: #if the file is not present or path is incorrect
        print(f" Error! The File at {file_path} could not be found. Please check the location and try again.")
    except Exception as e: #if there is any other error
        print(f"An error has occured while loading the data: {e}") 
      


# In[5]:


def treatment_proportion_by_ethnicity(df_main, ethnicity): 
    try:
        ethnicity = ethnicity.strip().lower()  # .strip() removes the extra spaces and .lower() makes the input lower to tackle case insensitivity
        df_main["Ethnicity"] = df_main["Ethnicity"].str.lower()  #converts the values in ethnicity column into str and lowercase so that it matches the input
        
        df_ethnicity = df_main.loc[df_main["Ethnicity"]==ethnicity] 
        #makes a new series where only that data is present which meets our conditions
        df_treatments = df_ethnicity["Treatment"].value_counts() #retrieving the names of treatments present and how many times they are used
        #now in this series, treatment names are the index and values are their count

        if df_treatments.size==0:
            print("No Treatments found for entered ethnicity. Please check your input")
        treatment_labels = df_treatments.index.tolist() #converting the names of treatments into list to use as labels
        treatment_number = df_treatments.tolist() #converting the number of times each treatment is used into list
        
        fig = plt.figure(figsize =(10,6)) #setting the size and plotting the figure
        plt.pie(treatment_number,labels = treatment_labels, autopct = "%1.1f%%") #autopct converts the data into percentages
        plt.title(f"Proportion of Treatments for Ethnicity: {ethnicity}") #titile which changes according to the ethnicity entered by user
        plt.legend(loc = "best")  #automatically chooses the best location to plot the chart
        plt.show()
        return
        
    except Exception as e: #in case of any error
        print(f"An error has occured:{e}")


# In[6]:


def average_smoking_trend(df_main):
    try:
        df_group = df_main.groupby(["Stage","Ethnicity"])["Smoking_Pack_Years"].mean().reset_index() #resest the index to integer values eg 0,1,2,3...
        #grouped the data based on cancer stages and ethnicities and finding the averge smoking packs for each

        stages = df_group["Stage"].unique() #getting the different cancer stage names
        ethnicities = df_group["Ethnicity"].unique() #getting the different ethnicity names
        
        fig = plt.figure(figsize=(15,8)) #plotting the chart 
        
        for ethnicity in ethnicities:
            ethnicity_data = df_group[df_group["Ethnicity"]==ethnicity]
            #filters the data for current ethnicity
            #then plots the data for this ethnicity
            plt.plot(ethnicity_data["Stage"], ethnicity_data["Smoking_Pack_Years"], marker = 'o', label = ethnicity)
            #loops and does the same for each ethnicity
        
        
        plt.ylabel("Average Smoking packs (per year)") #labels for y axis
        plt.xlabel("Cancer Stages") #labels for x axis
        plt.title("Trend of average smoking packs Across cancer stages by Ethnicity") #title of the chart
        plt.legend(title= "Ethnicity", loc = "best") #setting the location as best
        plt.show() #shows the chart
        return
    except Exception as e: 
        print(f"An error has occured:{e}") #prints error message accordingly


# In[7]:


def blood_ppressure_comparison(df_main):
    try:
        df_group = df_main.groupby("Treatment")[["Blood_Pressure_Systolic", "Blood_Pressure_Diastolic", "Blood_Pressure_Pulse"]].mean() 
        #groups the data based on treatments and then find average for each blood pressure types
        
        x_axis = np.arange(len(df_group)) #creates an array of size equal to the number of treatments 
        
        bar_width =0.2 #setting the width of bar
        #instead of directly writing 0.2 in the plt.bar, created a variable so that it is easier to change the width later as per the requirement
        
        fig = plt.figure(figsize=(10,6)) #setting the figure size and plotting the chart

        #following are the 3 subbars for each blood pressure type
        plt.bar(x_axis-bar_width, df_group["Blood_Pressure_Systolic"], width = bar_width, label = "Systolic", color = "blue")  
        plt.bar(x_axis, df_group["Blood_Pressure_Diastolic"], width = bar_width, label = "Diastolic", color = "green")
        plt.bar(x_axis+bar_width, df_group["Blood_Pressure_Pulse"], width = bar_width, label = "Pulse", color = "red")
        #all bars are arranged according to the bar width
        
        plt.xticks(x_axis, df_group.index, rotation = 45) 
        #group's index are the treatment names
        #rotation of the label names is set to 45 so that it does not mix up
        
        plt.xlabel("Treatments") # main label for the x axis
        plt.ylabel("Average Blood Pressure") #main label for the y axis
        plt.title("Comparison of Average blood pressure across different treatment types") #title
        plt.legend()
        plt.tight_layout() #ensure everything is neatly spaced and does not go out of the chart
        plt.show()
        return
    except Exception as e:
        print(f"An error has occured:{e}") #prints error message accordingly


# In[1]:


def avg_platelets_by_stage(df_main):
    try:
        df_group = df_main.groupby("Stage")["Platelet_Count"].mean()
        #groups the data based on cancer stages and then find average platelets count for each stage
        
        x_axis = np.arange(len(df_group)) #creates an array of size equal to the number of stages
        
        bar_width =0.2 #setting the width of bar
        #instead of directly writing 0.2 in the plt.bar, created a variable so that it is easier to change the width later as per the requirement
        
        fig = plt.figure(figsize=(10,6))
        #setting the figure size and plotting the chart

        colors = ['blue', 'green', 'red', 'orange', 'purple', 'cyan', 'magenta'][:len(df_group)]
        #assigning different colours for different bars
        
        plt.bar(x_axis, df_group, width = bar_width, label = "Platelets Count", color = colors)  
        #plotting the bar
        
        plt.xticks(x_axis, df_group.index, rotation = 45) 
        #group's index are the stage names
        #rotation of the label names is set to 45 so that it does not mix up
        
        plt.xlabel("Cancer Stages") # main label for the x axis
        plt.ylabel("Average platelets Count") #main label for the y axis
        plt.title("Comparison of Average Platelets count for different Cancer Stages") #title
        plt.legend()
        plt.tight_layout() #ensure everything is neatly spaced and does not go out of the chart
        plt.show()
        return
    except Exception as e:
        print(f"An error has occured:{e}") #prints error message accordingly


# In[ ]:




