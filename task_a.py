#!/usr/bin/env python
# coding: utf-8

# In[5]:


import csv 


# In[4]:


def load_data(file_path):
    try:
        with open(file_path, mode = 'r', encoding = 'UTF-8') as file:
            csv_reader = csv.reader(file)
            data_list = list(csv_reader)
        return data_list

    except FileNotFoundError:
        print("File not found! please enter the correct path/name.")
        return None
    except Exception as e:
        print(f"An error occured: {e}")
        return None


# In[6]:


def retrieve_patient_info(data_list, patient_id):
    try:
        header =data_list[0]
        rows = data_list[1:]
        for row in rows:
            row_dictionary = dict(zip(header,row))
            if row_dictionary.get("Patient_ID") == patient_id:
                return{
                    "Age":row_dictionary.get("Age"),
                    "Gender":row_dictionary.get("Gender"),
                    "Smoking_History":row_dictionary.get("Smoking_History"),
                    "Ethnicity":row_dictionary.get("Ethnicity")
                }
    except ValueError as e:
        print(f"Error processing the data: {e}")
        return "No match found!"


# In[9]:


def retrieve_medical_history_by_ethnicity(ethnicity, data_list):
    try:
        header  = data_list[0]
        rows = data_list[1:]
        result= []
        for row in rows:
            row_dictionary = dict(zip(header, row))
            if row_dictionary.get("Ethnicity") == ethnicity:
                result.append({
                    "Patient ID": row_dictionary.get("Patient ID"),
                    "Family_History": row_dictionary.get("Family_History"),
                    "Comorbidity_Diabetes": row_dictionary.get("Comorbidity_Diabetes"),
                    "Comorbidity_Kidney_Disease": row_dictionary.get("Comorbidity_Kidney_Disease"),
                    "Haemoglobin_Level": row_dictionary.get("Haemoglobin_Level")
                })
        return result
    except Exception as e:
        print(f"An error occured: {e}")
        return None
                


# In[4]:


def retrieve_treatment_details(data_list, treatment_details):
    try:
        result=[]
        header = data_list[0]
        rows = data_list[1:]
        for row in rows:
            row_dictionary = dict(zip(header,row))
            survival_months = int(row_dictionary.get("Survival_Months",0))
            if survival_months>100 and row_dictionary.get("Treatment") == treatment_details:
                result.append({
                    "Age":row_dictionary.get("Age"),
                    "Tumor Size":row_dictionary.get("Tumor_Size_mm"),
                    "Tumor Location":row_dictionary.get("Tumor_Location"),
                    "Tumor Stage":row_dictionary.get("Stage"),
                    "Months Survived":row_dictionary.get("Survival_Months")
                })
        return result if result else "No Records Found!"
    except Exception as e:
        print(f"An error occured: {e}")
        return None


# In[5]:


def Cancer_stage_for_young_with_comorbidity(data_list):
    try:
        comorbidity= input("Enter Comorbidity: Diabetes/Kidney").strip().capitalize()
        if comorbidity not in["Diabetes", "Kidney"]:
            print(" Invalid Choice, Please Select one: Diabetes/Kidney")
            return None
        comorbidity_column = "Comorbidity_Diabetes" if comorbidity == "Diabetes" else "Comorbidity_Kidney_Disease"
        header= data_list[0]
        rows = data_list[1:]
        result=[]
        
        for row in rows:
            row_dictionary= dict(zip(header,row))
            Age = int(row_dictionary.get("Age",0))
            if row_dictionary.get(comorbidity_column) == "Yes" and Age<30:
                result.append({
                    "Age": row_dictionary.get("Age"),
                    "Cancer Stage": row_dictionary.get("Stage"),
                    "Months Survived":row_dictionary.get("Survival_Months")
                })
        return result if result else "No Records Found"
    except Exception as e:
        print(f"An error occured: {e}")
        return None


# In[ ]:




