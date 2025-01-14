#!/usr/bin/env python
# coding: utf-8

# In[5]:


import csv


# In[11]:


def load_data(file_path): # taking file_path as a parameter which would be asked from the user by menu function
    try:
        with open(file_path, mode = 'r', encoding = 'UTF-8') as file:
            csv_reader = csv.reader(file)
            data_list = list(csv_reader) # storing the data as a list which makes it easier to use in further tasks
        return data_list 

    except FileNotFoundError: 
        print("File not found! please enter the correct path/name.")
        return None
        
    except Exception as e:  # if there is any error other than FileNotFound
        print(f"An error occured: {e}")
        return None


# In[12]:


def retrieve_patient_info(data_list, patient_id):
    try:
        header =data_list[0] #first row of the data is heading/columns
        rows = data_list[1:] #storing rest of the rows as rows/data
        
        for row in rows:
            row_dictionary = dict(zip(header,row)) #converts the data into dictionary where column/header is the key and the row's data is value
            if row_dictionary.get("Patient_ID") == patient_id: # checks if it matches with the user input
                
                return{
                    "Age":row_dictionary.get("Age"),
                    "Gender":row_dictionary.get("Gender"),
                    "Smoking_History":row_dictionary.get("Smoking_History"),
                    "Ethnicity":row_dictionary.get("Ethnicity")} #returns the required info retrieved from the dictionary
                
        return "No match found!" #returns this message if no match found
        
    except ValueError as e:
        print(f"Error processing the data: {e}")
        return "Error Processing the data" # returns if there is any other error
        


# In[13]:


def retrieve_medical_history_by_ethnicity(ethnicity, data_list):
    try:
        ethnicity=ethnicity.lower() # converts all the input into lowercase to avoid error 
        header  = data_list[0]
        rows = data_list[1:]
        result= [] #  initializing an empty list so that retrieved information can be stored in it and then returned
        
        for row in rows:
            row_dictionary = dict(zip(header, row)) #converts the data into dictionary where column/header is the key and the row's data is value
            if row_dictionary.get("Ethnicity").lower() == ethnicity: # checks if it matches with the user input
                result.append({
                    "Patient ID": row_dictionary.get("Patient_ID"),
                    "Family History": row_dictionary.get("Family_History"),
                    "Comorbidity Diabetes": row_dictionary.get("Comorbidity_Diabetes"),
                    "Comorbidity Kidney Disease": row_dictionary.get("Comorbidity_Kidney_Disease"),
                    "Haemoglobin Level": row_dictionary.get("Haemoglobin_Level") #retrieves the required info from the dictionary
                })
        if result:
            clear_result = "\n\n".join([f"Patient Id: {r['Patient ID']}\n"
                                        f"Family History: {r['Family History']}\n"
                                        f"Comorbidity (Diabetes): {r['Comorbidity Diabetes']}\n"
                                        f"Comorbidity (Kidney Disease): {r['Comorbidity Kidney Disease']}\n"
                                        f"Haemoglobin Level: {r['Haemoglobin Level']}\n"
                                        for r in result])  # display the data in a clean and simple to read format
            return clear_result
        
        else:
            return "No Match found for the entered ethnicity!" # in case no match is found
   
    except Exception as e:
        print(f"An error occured: {e}") # if there is any error
        return "Error processing the Data" 
                


# In[14]:


def retrieve_treatment_details(data_list, treatment_details):
    try:
        treatment_details = treatment_details.lower() # converts all the input into lowercase to avoid error
        result=[] # initializing an emplty list to store the retrieved result
        header = data_list[0] #storing the columns/header
        rows = data_list[1:] #storing the rows/data
        
        for row in rows:
            row_dictionary = dict(zip(header,row)) #converts the data into dictionary where column/header is the key and the row's data is value
            survival_months = int(row_dictionary.get("Survival_Months",0)) 
            #added "0" to handle the missing values in "Survival_Months" column 
            #also converted it into integer as we need to do the comparison(>100)
            
            if survival_months>100 and row_dictionary.get("Treatment").lower() == treatment_details: #checks if it matches the entered details
                result.append({
                    "Age":row_dictionary.get("Age"),
                    "Tumor Size":row_dictionary.get("Tumor_Size_mm"),
                    "Tumor Location":row_dictionary.get("Tumor_Location"),
                    "Tumor Stage":row_dictionary.get("Stage"),
                    "Months Survived":row_dictionary.get("Survival_Months")
                }) #retrieving the info from dictionary
                
        if result:
            clear_result = "\n\n".join([f"Age: {r['Age']}\n"
                                        f"Tumor Size: {r['Tumor Size']}\n"
                                        f"Tumor Location: {r['Tumor Location']}\n"
                                        f"Tumor Stage: {r['Tumor Stage']}\n"
                                        f"Months Survived: {r['Months Survived']}\n"
                                        for r in result]) #displays the result in a clear and easy to read format
            return clear_result
            
        else:
            return "No data found for the entered treatment"
            
    except Exception as e:
        print(f"An error occured: {e}")
        return "Error Processing the data" # handles the error 


# In[15]:


def Cancer_stage_for_adults_comorbidity(data_list, comorbidity):
    try:
        comorbidity= comorbidity.lower() # converts all the input into lowercase to avoid error
        if comorbidity not in["diabetes", "kidney"]: #it is also in lowercase because all the input is converted into lowercase
            print(" Invalid Choice, Please Select one: Diabetes/Kidney")
            #checks if the entered info matches and prints the error message accordingly
            return None
        comorbidity_column = "Comorbidity_Diabetes" if comorbidity == "diabetes" else "Comorbidity_Kidney_Disease"
        # value of the comorbidity_column variable changes according to the user input
        
        header= data_list[0] #first row are columns
        rows = data_list[1:] #rest of the rows are data/rows
        result=[] #initializing an empty list to store the result
        
        for row in rows:
            row_dictionary= dict(zip(header,row)) #converts the data into dictionary where column/header is the key and the row's data is value
            Age = int(row_dictionary.get("Age",0))
            #using int to convert into integers as we need to compare it (Age<45)
            #used "0" to handle if there is any empty/missing value in Age 
            
            if row_dictionary.get(comorbidity_column).strip().lower() == "yes" and Age<45:
                #used "strip()" to remove any extra spaces
                #used "lower()" to convert it all in lower case and also set the condition to "=='yes'" which is in lowercase
                
                result.append({
                    "Age": row_dictionary.get("Age"),
                    "Cancer Stage": row_dictionary.get("Stage"),
                    "Months Survived":row_dictionary.get("Survival_Months")
                })
        if result:
            clear_result = "\n\n".join([f"Age: {r['Age']}\n"
                                        f"Cancer Stage: {r['Cancer Stage']}\n"
                                        f"Months Survived: {r['Months Survived']}\n"
                                        for r in result]) #displays the result in a clear and easy to read format
            return clear_result
        else:
            return "No Cancer patients aged below 45 found with the given Comorbidity!" 
    except Exception as e:
        print(f"An error occured: {e}")
        return "error processing the data" #to handle the error


# In[ ]:




