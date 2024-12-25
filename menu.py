#!/usr/bin/env python
# coding: utf-8

# In[5]:


import task_a
import task_b
import task_c


# In[6]:


def main_menu():
    #this is the main menu which further has sub menus for each tasks
   
    data_list= None 
    #initialized the data_list as None because the error handling used below only runs the required function when it is not none 
    # therefore, in case user forgets to load the data and directly choose option 2/3/4, it will ask the user to load the data first
    
    while True: 
        #used "while true" loop so that the menu is shown to the user without the need of running the function again and again 
        
        print("\n----MAIN MENU----") #used "\n" so that each time the menu is shown it has a space of one line before just to look clean and easy to read
        print("1. Load Data (REQUIRED)")
        print("2. Retrieve general Information about the patients (TASK A: Basic python functions)")
        print("3. Load and Analyse the Data (TASK B: Using pandas)")
        print("4. Visualise the Data (TASK C: Using matplotlib)")
        print("5. Exit the program")
        option = input("Please choose one option: ") #integer input is not used to avoid input error 
        #So that if user enters a string value (eg.a,b,xy) it runs the "else" statement from below and asks the user to enter a valid option 
       
        if option=="1":
             file_path = input("Please enter the file path/name:")
             data_list = task_a.load_data(file_path) #loads the data using function from module "task_a"
             if data_list is not None:   #checks if the data_list is empty or not 
                 print("Data Loaded Successfully!") 
             else:
                 print("Failed to Load data! Please check the entered file path.")
                 
        elif option=="2":
            if data_list is None: #runs only if data has been loaded
                print("Please load the data first using option 1") 
            else: #if the data has not been loaded using option 1, it asks the user to do it first
                menu_task_a(data_list)
                
        elif option=="3":
            if data_list is None:
                print("Please load the data first using option 1")
            else: 
                df_main = task_b.load_data_pandas(file_path) #automatically loads the dataframe first and then show the menu for task B
                #loads the data using file_path entered in option 1(load data)
                #so that the user does not need to enter it manually again
                menu_task_b(df_main)
                
        elif option=="4":
            if data_list is None:
                print("Please load the data first using option 1")
            else:
                df_main = task_c.load_data_task_c(file_path) #automatically loads the dataframe first and then shows the menu for task C
                #loads the data using file_path entered in option 1(load data)
                #so that the user does not need to enter it manually again
                menu_task_c(df_main)
                
        elif option=="5":
            print("Exiting the program! Bye Bye !")
            break #stops the "While True" Loop when user wants to exit

            
        else:
            print("Please select a valid option!") #when chosen option is not 1/2/3/4/5


# In[7]:


def menu_task_a(data_list):
    while True:
        #used "while true" loop so that the menu is shown to the user without the need of running the function again and again
        print("\n----MENU A----") #used "\n" so that each time the menu is shown it has a space of one line before just to look clean and easy to read
        print("1. Retrieve Patient's Info (Age, Gender, Smoking history and Ethnicity)")
        print("2. Retrieve Medical History based on Ethnicity")
        print("3. Retrieve Treatment details for patients who survived more than 100 months")
        print("4. Retrieve Cancer stage and more info for young patients(<45) with ")
        print("5. Return to the Main Menu")
        choice = input("Please choose one option")
        #integer input is not used to avoid input error 
        #So that if user enters a string value (eg.a,b,xy) it runs the "else" statement from below and asks the user to enter a valid option 
        if choice == "1":
            patient_id = input("Please enter the Patient ID:") #asks the user input which is passed as a parameter to the function 
            result = task_a.retrieve_patient_info(data_list, patient_id)
            print(result)

        #similar approach for all other choices
        
        elif choice =="2":
            ethnicity = input("Please enter the ethnicity")
            result = task_a.retrieve_medical_history_by_ethnicity(ethnicity, data_list)
            print(result)
            
            

        elif choice == "3":
            treatment_details = input("Please enter the Treatment Details")
            result = task_a.retrieve_treatment_details(data_list, treatment_details)
            print(result)
            
          
        elif choice == "4":
            comorbidity= input("Enter Comorbidity: Diabetes/Kidney")
            result = task_a.Cancer_stage_for_adults_comorbidity(data_list, comorbidity)
            print(result)
            
            
        elif choice == "5":
            print("Returning to the Main Menu!.....") #returns to the main menu
            break
    
        else:
            print("INVALID CHOICE! Please enter the correct input")


# In[8]:


def menu_task_b(df_main):
    while True:
        print("\n----MENU----")#used "while true" loop so that the menu is shown to the user without the need of running the function again and again
        print("1. Identify the top 3 treatments for a certain ethnicity where patients have survived more than 100 months.")
        print("2. Find out the average WBC count for a specific treatment in a specific ethnicity.")
        print("3. Find out the average number of smoking packs for patients in each treatment group with a blood pressure(pulse) over 90 and a tumor size smaller than 15.0mm, based on tumor location.")
        print("4. Find out the survival rate of patients based on a specific treatment")
        print("5. Main Menu")
        choice =input("Please Select from the options above")
        #integer input is not used to avoid input error 
        #So that if user enters a string value (eg.a,b,xy) it runs the "else" statement from below and asks the user to enter a valid option 
       
        if choice== "1":
            ethnicity = input("What ethnicity do you want to find out the top 3 treatments for?:")
            result = task_b.top_3_treatments(df_main, ethnicity)
            print(f"Top 3 treatments for Ethnicity: {ethnicity}") #f-string to display the result in a easy to read format
            print(result)

        #similar approach for rest of the options
        elif choice== "2":
            ethnicity = input("Please enter the ethnicity you want to find out the average WBC for?:")
            treatment = input("Please enter the treatment you want to find out the average WBC for?:")
            result = task_b.average_wbc(df_main, ethnicity, treatment)
            print(result)
        
        elif choice== "3":
            tumor_location = input("Please enter the tumor location:")
            result = task_b.average_smoking_packs(df_main, tumor_location)
            
            print(result)
            
        
        elif choice== "4":
            treatment = input("What treatment do you want to find out the survival rate for?:")
            result = task_b.survival_rate_by_treatment(df_main, treatment)
            print(result)
        
        elif choice== "5":
            print("Returning to the Main Menu!.....") #returns to the main menu
            break #stops the while true loop
        
        else:
            print("INVALID CHOICE! Please enter the correct input")


# In[9]:


def menu_task_c(df_main):
    while True:
        print("\n----MENU----") #used "while true" loop so that the menu is shown to the user without the need of running the function again and again
        print("1. Proportion of Treatments used among a certain Ethnicity.")
        print("2. Trend of Average smoking packs across different cancer stages for each Ethnicity.")
        print("3. Comparison of Average Blood pressure across different treatment types")
        print("4. Age VS Survival rate by Treatment type")
        print("5. Main Menu")
        print("6. EXIT")
        choice = input("Please Select from the options above")
        #integer input is not used to avoid input error 
        #So that if user enters a string value (eg.a,b,xy) it runs the "else" statement from below and asks the user to enter a valid option 
       
        if choice== "1":
            ethnicity = input("What ethnicity do you want to find out the treatments proportion for?")
            result = task_c.treatment_proportion_by_ethnicity(df_main, ethnicity)
            print(result)

        #similar approach for rest of the options        
        elif choice=="2":
            result= task_c.average_smoking_trend(df_main)
            print(result)
                
        elif choice =="3":
            result= task_c.blood_ppressure_comparison(df_main)
            print(result)
    
        elif choice == "4":
            result = task_c.survival_rate_for_treatments(df_main)
            print(result)
                
        elif choice== "5":
            print("Returning to the Main Menu!.....")
            break #breaks the while true loop and returns to the main menu
        else:
            print("INVALID CHOICE! Please enter the correct input") #when chosen option is not 1/2/3/4/5
            


# In[ ]:




