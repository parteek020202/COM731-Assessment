#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd


# In[2]:


def load_data_pandas(file_path): #loads function using the file path entered during first step data loading
    #user does not need to enter the file path or name again
    try:
        df_main = pd.read_csv(file_path, encoding="UTF-8")
        return df_main #returns the main dataframe which will be passed as a parameter to all the functions and used throughout the program
        
    except FileNotFoundError: #if the file is not present or path is incorrect
        print(f" Error! The File at {file_path} could not be found. Please check the location and try again.")
    except Exception as e:
        print(f"An error has occured while loading the data: {e}") #if there is any other error
    return None  


# In[3]:


def top_3_treatments(df_main, ethnicity):
    try:
        ethnicity = ethnicity.strip().lower() # .strip() removes the extra spaces and .lower() makes the input lower to tackle case insensitivity
        df_main["Ethnicity"]= df_main["Ethnicity"].str.lower() #converts the values in ethnicity column into str and lowercase so that it matches the input
        df_ethnicity_survival = df_main.loc[(df_main["Ethnicity"]==ethnicity) & (df_main["Survival_Months"]>100)] 
        #makes a new series where only that data is present which meets our conditions
        
        top_treatments = (df_ethnicity_survival["Treatment"].value_counts().head(3)) # .value_counts() automatically sorts the values in descending order
        
        if top_treatments.empty: #in case the data is not available 
            return f"No top treatments found for the Ehnicity {ethnicity} where Survival months > 100" 
            
        clear_result = "\n".join([f"{treatment}: {count}" for treatment, count in top_treatments.items()]) 
        #display the result in a clean and easy to read format
        return clear_result
        
    except Exception as e: #if there is any error
        print(f"An error occurred: {e}")
        return None


# In[4]:


def average_wbc(df_main, ethnicity, treatment):
    try:
        ethnicity = ethnicity.strip().lower() # .strip() removes the extra spaces and .lower() makes the input lower to tackle case insensitivity
        treatment = treatment.strip().lower()
        df_main["Ethnicity"]= df_main["Ethnicity"].str.lower() #converts the values in ethnicity column into str and lowercase so that it matches the input
        df_main["Treatment"]= df_main["Treatment"].str.lower()
        
        df_ethnicity_treatment = df_main.loc[(df_main["Ethnicity"]==ethnicity) & (df_main["Treatment"]==treatment)]
        #makes a new series where only that data is present which meets our conditions
        df_avg_wbc = df_ethnicity_treatment["White_Blood_Cell_Count"].dropna().mean() #dropna() drops the empty values 

        if pd.isna(df_avg_wbc): #checks if the data is empty and returns the message accordingly
            return "No data available for entered ethnicity & treatment"
        
        return f"Average White blood cell count for Ethnicity:{ethnicity} and Treatment:{treatment} is {df_avg_wbc:.2f}"
        #display a clear and easy to read result 
        
    except Exception as e:
        print(f"An error occurred: {e}") #prints error message accordingly
        return None 


# In[5]:


def average_smoking_packs(df_main, tumor_location):
    try:
        tumor_location = tumor_location.strip().lower() # .strip() removes the extra spaces and .lower() makes the input lower to tackle case insensitivity
        df_main["Tumor_Location"] = df_main["Tumor_Location"].str.lower() #converts the values in ethnicity column into str and lowercase so that it matches the input
        
        df_bp_tumor = df_main.loc[(df_main["Blood_Pressure_Pulse"]>90) & (df_main["Tumor_Size_mm"]<15) & (df_main["Tumor_Location"] == tumor_location)]
        #makes a new series where only that data is present which meets our conditions
        df_avg_smoking_packs = df_bp_tumor.groupby("Treatment")["Smoking_Pack_Years"].mean()
        #groups the data based on treatments and then shows the average smoking packs for each treatment
        
        if df_avg_smoking_packs.size==0: #checks if the series is empty 
            return "No data found for entered tumor location"
        
        clear_result = "\n".join([f"{treatment}: {avg_packs:.2f}" for treatment,avg_packs in df_avg_smoking_packs.items()])
        return f"Average Smoking packs for Tumor Location:{tumor_location}:\n{clear_result}"  #displays a clear and easy to read result
        
    except Exception as e:
        print(f"An error occurred: {e}") #prints error message accordingly
        return None


# In[6]:


def survival_rate_by_treatment(df_main, treatment):
    try:
        treatment = treatment.strip().lower() # .strip() removes the extra spaces and .lower() makes the input lower to tackle case insensitivity
        df_main["Treatment"] = df_main["Treatment"].str.lower() #converts the values in ethnicity column into str and lowercase so that it matches the input
        df_treatment = df_main.loc[df_main["Treatment"]==treatment]
        #makes a new series where only that data is present which meets our conditions
        
        df_survival_rate = df_treatment["Survival_Months"].dropna().mean() #drops the empty values and then calculates the mean
        if pd.isna(df_survival_rate): #checks if the data is empty 
            return "No data available for provided treatment"
            
        return f"Patients survived for an average of {df_survival_rate:.2f} with the treatment:{treatment}" #returns an easy to read result
        
    except Exception as e:
        print(f"An error occurred: {e}") #prints error message accordingly
        return None


# In[ ]:





# In[ ]:




