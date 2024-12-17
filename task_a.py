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
        
        return "No match found!"
    except ValueError as e:
        print(f"Error processing the data: {e}")


# In[ ]:




