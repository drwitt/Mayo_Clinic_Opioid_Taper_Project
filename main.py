#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 11:05:22 2019

@author: dannywitt
"""
import pandas as pd 
import numpy as np


# import xlwt 
# from xlwt import Workbook 

# from patient_information import Patient
# from opioid_dose_taper import Taper
# from print_report import Print_monthly_report
# from prescription import Prescription

# from medication import (Hydrocodone_Acetaminophen, 
#                         Hydromorphone_Immediate_Release,
#                         Morphine_Immediate_Release,
#                         Morphine_Extended_Release,
#                         Oxycodone_Immediate_Release,
#                         Oxycodone_Extended_Release, 
#                         Oxycodone_Acetaminophen, 
#                         Tramadol_Immediate_Release
#                         )

# #Functions:

# def Assign_med_class(opioid_med_string):
#         drug_name_to_object_dictionary = {'Hydrocodone_Acetaminophen': Hydrocodone_Acetaminophen(),
#                                       'Hydromorphone_Immediate_Release': Hydromorphone_Immediate_Release(),
#                                       'Morphine_Immediate_Release': Morphine_Immediate_Release(),
#                                       'Morphine_Extended_Release': Morphine_Extended_Release(),
#                                       'Oxycodone_Immediate_Release': Oxycodone_Immediate_Release(),
#                                       'Oxycodone_Extended_Release': Oxycodone_Extended_Release(),
#                                       'Oxycodone_Acetaminophen': Oxycodone_Acetaminophen(),
#                                       'Tramadol_Immediate_Release': Tramadol_Immediate_Release(),
#                                       None : None}
        
#         for drug_name in drug_name_to_object_dictionary:
#             if drug_name == opioid_med_string:
#                 return drug_name_to_object_dictionary[drug_name]
#             else:
#                 pass
#             pass
#         pass
    
# ###################################################################

# opioid_df = pd.read_excel("/Users/dannywitt/Desktop/Opioid_project/Opioid_data.xlsx") 

# ##Importing excel files########
# #from patient_information import Patient

# #Input correct number of active patients in trial (corresponding to Excel file):
# number_of_patients = 3

# #Generate patient identification for individual patient instances:
# instanceNames = []
# for patient_row in range(1,number_of_patients+1):
#     instanceNames.append('Patient_{}'.format(patient_row))
  
# patient_instances = []
# for patient_row in range(number_of_patients):
#     #Initialize a patient instance:
#     #Include ID number, First name, Last name:
#     patient_instances.append(Patient(opioid_df.iloc[patient_row]['Patient_ID'],
#                                      opioid_df.iloc[patient_row]['Patient_First_Name'],
#                                      opioid_df.iloc[patient_row]['Patient_Last_Name']))
   
#     patient_instances[patient_row].primary_opioid_med = Assign_med_class((opioid_df.iloc[patient_row]['Med_1']))
#     patient_instances[patient_row].primary_opioid_med_name = opioid_df.iloc[patient_row]['Med_1']
    
#     #Load constant daily episode dose information:
#     patient_instances[patient_row].primary_opioid_episode_dose =  opioid_df.iloc[patient_row]['Dose_med_1_constant_daily_episode_dose']
#     patient_instances[patient_row].primary_opioid_captab_per_episode_dose = opioid_df.iloc[patient_row]['Count_tabs_or_capsules_med_1_constant_daily_episode_dose']
#     patient_instances[patient_row].primary_opioid_interdose_duration = opioid_df.iloc[patient_row]['Frequency_dose_med_1']
#     patient_instances[patient_row].primary_opioid_unit_dose = opioid_df.iloc[patient_row]['Constant_dose_med_1_unit_dose']
#     if opioid_df.iloc[patient_row]['Different_daily_episode_doses_med_1?'] == 'Yes, episode doses differ during day.':
#         patient_instances[patient_row].different_daily_episode_doses_med_1 = 'Yes'
#         pass
#     elif opioid_df.iloc[patient_row]['Different_daily_episode_doses_med_1?'] == 'No, each episode dose is the same.':
#         patient_instances[patient_row].different_daily_episode_doses_med_1 = 'No'
#         pass
#     else:
#         pass
            
#     #Load non-constant daily episode dose information:
    
#     patient_instances[patient_row].primary_opioid_dif_dose_episode_dose_1 =  opioid_df.iloc[patient_row]['Nonconstant_dose_med_1_episode_dose_1']
#     patient_instances[patient_row].primary_opioid_dif_dose_episode_dose_2 =  opioid_df.iloc[patient_row]['Nonconstant_dose_med_1_episode_dose_2']
#     patient_instances[patient_row].primary_opioid_dif_dose_episode_dose_3 =  opioid_df.iloc[patient_row]['Nonconstant_dose_med_1_episode_dose_3']
#     patient_instances[patient_row].primary_opioid_dif_dose_episode_dose_4 =  opioid_df.iloc[patient_row]['Nonconstant_dose_med_1_episode_dose_4']
    
#     patient_instances[patient_row].primary_opioid_dif_dose_captab_per_episode_dose_1 =  opioid_df.iloc[patient_row]['Nonconstant_dose_count_tabs_or_capsules_med_1_episode_dose_1']
#     patient_instances[patient_row].primary_opioid_dif_dose_captab_per_episode_dose_2 =  opioid_df.iloc[patient_row]['Nonconstant_dose_count_tabs_or_capsules_med_1_episode_dose_2']
#     patient_instances[patient_row].primary_opioid_dif_dose_captab_per_episode_dose_3 =  opioid_df.iloc[patient_row]['Nonconstant_dose_count_tabs_or_capsules_med_1_episode_dose_3']
#     patient_instances[patient_row].primary_opioid_dif_dose_captab_per_episode_dose_4 =  opioid_df.iloc[patient_row]['Nonconstant_dose_count_tabs_or_capsules_med_1_episode_dose_4']
    
#     patient_instances[patient_row].primary_opioid_dif_dose_ep_1_unit_dose = opioid_df.iloc[patient_row]['Nonconstant_dose_med_1_unit_dose_episode_1']
#     patient_instances[patient_row].primary_opioid_dif_dose_ep_2_unit_dose = opioid_df.iloc[patient_row]['Nonconstant_dose_med_1_unit_dose_episode_2']
#     patient_instances[patient_row].primary_opioid_dif_dose_ep_3_unit_dose = opioid_df.iloc[patient_row]['Nonconstant_dose_med_1_unit_dose_episode_3']
#     patient_instances[patient_row].primary_opioid_dif_dose_ep_4_unit_dose = opioid_df.iloc[patient_row]['Nonconstant_dose_med_1_unit_dose_episode_4']
    
#     #Load constant daily episode dose information:
    
#     patient_instances[patient_row].secondary_opioid_med = Assign_med_class(opioid_df.iloc[patient_row]['Med_2'])
#     patient_instances[patient_row].secondary_opioid_med_name = opioid_df.iloc[patient_row]['Med_2']
#     patient_instances[patient_row].secondary_opioid_episode_dose =  opioid_df.iloc[patient_row]['Dose_med_2_constant_daily_episode_dose']
#     patient_instances[patient_row].secondary_opioid_captab_per_episode_dose = opioid_df.iloc[patient_row]['Count_tabs_or_capsules_med_2_constant_daily_episode_dose']
#     patient_instances[patient_row].secondary_opioid_interdose_duration = opioid_df.iloc[patient_row]['Frequency_dose_med_2']
#     patient_instances[patient_row].secondary_opioid_unit_dose = opioid_df.iloc[patient_row]['Constant_dose_med_2_unit_dose']
#     if opioid_df.iloc[patient_row]['Different_daily_episode_doses_med_2?'] == 'Yes, episode doses differ during day.':
#         patient_instances[patient_row].different_daily_episode_doses_med_2 = 'Yes'
#         pass
#     elif opioid_df.iloc[patient_row]['Different_daily_episode_doses_med_2?'] == 'No, each episode dose is the same.':
#         patient_instances[patient_row].different_daily_episode_doses_med_2 = 'No'
#         pass
#     else:
#         pass
    
# #    #Convert 'nan' string to None object if present in episode dose or capsule count:
# #    if np.isnan(patient_instances[patient_row].secondary_opioid_episode_dose):
# #        patient_instances[patient_row].secondary_opioid_episode_dose = None
# #        pass
# #    else:
# #        pass
# #    
# #    if np.isnan(patient_instances[patient_row].secondary_opioid_captab_per_episode_dose):
# #        patient_instances[patient_row].secondary_opioid_captab_per_episode_dose = None
# #        pass
# #    else:
# #        pass
    

    
#     if opioid_df.iloc[patient_row]['Different_daily_episode_doses_med_2?'] == 'Yes, episode doses differ during day.':
#         patient_instances[patient_row].different_daily_episode_doses_med_2 = 'Yes'
#         pass
#     elif opioid_df.iloc[patient_row]['Different_daily_episode_doses_med_2?'] == 'No, each episode dose is the same.':
#         patient_instances[patient_row].different_daily_episode_doses_med_2 = 'No'
#         pass
#     else:
#         pass
    
#     #Load non-constant daily episode dose information: 
    
#     patient_instances[patient_row].secondary_opioid_dif_dose_episode_dose_1 =  opioid_df.iloc[patient_row]['Nonconstant_dose_med_2_episode_dose_1']
#     patient_instances[patient_row].secondary_opioid_dif_dose_episode_dose_2 =  opioid_df.iloc[patient_row]['Nonconstant_dose_med_2_episode_dose_2']
#     patient_instances[patient_row].secondary_opioid_dif_dose_episode_dose_3 =  opioid_df.iloc[patient_row]['Nonconstant_dose_med_2_episode_dose_3']
#     patient_instances[patient_row].secondary_opioid_dif_dose_episode_dose_4 =  opioid_df.iloc[patient_row]['Nonconstant_dose_med_2_episode_dose_4']
    

#     patient_instances[patient_row].secondary_opioid_dif_dose_captab_per_episode_dose_1 =  opioid_df.iloc[patient_row]['Nonconstant_dose_count_tabs_or_capsules_med_2_episode_dose_1']
#     patient_instances[patient_row].secondary_opioid_dif_dose_captab_per_episode_dose_2 =  opioid_df.iloc[patient_row]['Nonconstant_dose_count_tabs_or_capsules_med_2_episode_dose_2']
#     patient_instances[patient_row].secondary_opioid_dif_dose_captab_per_episode_dose_3 =  opioid_df.iloc[patient_row]['Nonconstant_dose_count_tabs_or_capsules_med_2_episode_dose_3']
#     patient_instances[patient_row].secondary_opioid_dif_dose_captab_per_episode_dose_4 =  opioid_df.iloc[patient_row]['Nonconstant_dose_count_tabs_or_capsules_med_2_episode_dose_4']
    
#     patient_instances[patient_row].secondary_opioid_dif_dose_ep_1_unit_dose = opioid_df.iloc[patient_row]['Nonconstant_dose_med_2_unit_dose_episode_1']
#     patient_instances[patient_row].secondary_opioid_dif_dose_ep_2_unit_dose = opioid_df.iloc[patient_row]['Nonconstant_dose_med_2_unit_dose_episode_2']
#     patient_instances[patient_row].secondary_opioid_dif_dose_ep_3_unit_dose = opioid_df.iloc[patient_row]['Nonconstant_dose_med_2_unit_dose_episode_3']
#     patient_instances[patient_row].secondary_opioid_dif_dose_ep_4_unit_dose = opioid_df.iloc[patient_row]['Nonconstant_dose_med_2_unit_dose_episode_4']
    
#     episode_dose_list = [patient_instances[patient_row].primary_opioid_episode_dose,
#                           patient_instances[patient_row].primary_opioid_dif_dose_episode_dose_1,
#                           patient_instances[patient_row].primary_opioid_dif_dose_episode_dose_2,
#                           patient_instances[patient_row].primary_opioid_dif_dose_episode_dose_3,
#                           patient_instances[patient_row].primary_opioid_dif_dose_episode_dose_4,
#                           patient_instances[patient_row].secondary_opioid_episode_dose,
#                           patient_instances[patient_row].secondary_opioid_dif_dose_episode_dose_1,
#                           patient_instances[patient_row].secondary_opioid_dif_dose_episode_dose_2,
#                           patient_instances[patient_row].secondary_opioid_dif_dose_episode_dose_3,
#                           patient_instances[patient_row].secondary_opioid_dif_dose_episode_dose_4
#                           ]
    
#     captab_list = [patient_instances[patient_row].primary_opioid_captab_per_episode_dose,
#                   patient_instances[patient_row].primary_opioid_dif_dose_captab_per_episode_dose_1,
#                   patient_instances[patient_row].primary_opioid_dif_dose_captab_per_episode_dose_2,
#                   patient_instances[patient_row].primary_opioid_dif_dose_captab_per_episode_dose_3,
#                   patient_instances[patient_row].primary_opioid_dif_dose_captab_per_episode_dose_4,
#                   patient_instances[patient_row].secondary_opioid_captab_per_episode_dose,
#                   patient_instances[patient_row].secondary_opioid_dif_dose_captab_per_episode_dose_1,
#                   patient_instances[patient_row].secondary_opioid_dif_dose_captab_per_episode_dose_2,
#                   patient_instances[patient_row].secondary_opioid_dif_dose_captab_per_episode_dose_3,
#                   patient_instances[patient_row].secondary_opioid_dif_dose_captab_per_episode_dose_4
#                   ]
    
#     unit_dose_list = [patient_instances[patient_row].primary_opioid_unit_dose,
#                       patient_instances[patient_row].primary_opioid_dif_dose_ep_1_unit_dose,
#                       patient_instances[patient_row].primary_opioid_dif_dose_ep_2_unit_dose,
#                       patient_instances[patient_row].primary_opioid_dif_dose_ep_3_unit_dose,
#                       patient_instances[patient_row].primary_opioid_dif_dose_ep_4_unit_dose,
#                       patient_instances[patient_row].secondary_opioid_unit_dose,
#                       patient_instances[patient_row].secondary_opioid_dif_dose_ep_1_unit_dose,
#                       patient_instances[patient_row].secondary_opioid_dif_dose_ep_2_unit_dose,
#                       patient_instances[patient_row].secondary_opioid_dif_dose_ep_3_unit_dose,
#                       patient_instances[patient_row].secondary_opioid_dif_dose_ep_4_unit_dose
#                       ]
#     #Remove nans:
#     for i, var in enumerate(episode_dose_list):
#         if np.isnan(var):
#             episode_dose_list[i] = None
#             pass
#         else:
#             pass
#         pass
     
#     for i, var in enumerate(captab_list):
#         if np.isnan(var):
#             captab_list[i] = None
#             pass
#         else:
#             pass
#         pass
      
#     #Make all unit doses into list objects:
    
#     for i, var in enumerate(unit_dose_list):
#         if isinstance(var, float):
#             if np.isnan(var):
#                 #print(var)
#                 unit_dose_list[i] = None
#                 pass
#             else:
#                 unit_dose_list[i] = var
#                 pass
#             pass
#         elif isinstance(var, str):
#             x =  var.strip('(').strip(')').replace(' ', '').split(',')
#             if '' in x:
#                 x.remove('')
#                 pass
#             else:
#                 pass
#             unit_dose_list[i] = list(map(float, x))
#             pass
#         else:
#             unit_dose_list[i] = var
#             pass
#         pass

#     #Generate updated cleaned variables:
#     patient_instances[patient_row].primary_opioid_episode_dose = episode_dose_list[0]
#     patient_instances[patient_row].primary_opioid_dif_dose_episode_dose_1 = episode_dose_list[1]
#     patient_instances[patient_row].primary_opioid_dif_dose_episode_dose_2 = episode_dose_list[2]
#     patient_instances[patient_row].primary_opioid_dif_dose_episode_dose_3 = episode_dose_list[3]
#     patient_instances[patient_row].primary_opioid_dif_dose_episode_dose_4 = episode_dose_list[4]
#     patient_instances[patient_row].secondary_opioid_episode_dose = episode_dose_list[5]
#     patient_instances[patient_row].secondary_opioid_dif_dose_episode_dose_1 = episode_dose_list[6]
#     patient_instances[patient_row].secondary_opioid_dif_dose_episode_dose_2 = episode_dose_list[7]
#     patient_instances[patient_row].secondary_opioid_dif_dose_episode_dose_3 = episode_dose_list[8]
#     patient_instances[patient_row].secondary_opioid_dif_dose_episode_dose_4 = episode_dose_list[9]
                          
    
#     patient_instances[patient_row].primary_opioid_captab_per_episode_dose = captab_list[0]
#     patient_instances[patient_row].primary_opioid_dif_dose_captab_per_episode_dose_1 = captab_list[1]
#     patient_instances[patient_row].primary_opioid_dif_dose_captab_per_episode_dose_2 = captab_list[2]
#     patient_instances[patient_row].primary_opioid_dif_dose_captab_per_episode_dose_3 = captab_list[3]
#     patient_instances[patient_row].primary_opioid_dif_dose_captab_per_episode_dose_4 = captab_list[4]
#     patient_instances[patient_row].secondary_opioid_captab_per_episode_dose = captab_list[5]
#     patient_instances[patient_row].secondary_opioid_dif_dose_captab_per_episode_dose_1 = captab_list[6]
#     patient_instances[patient_row].secondary_opioid_dif_dose_captab_per_episode_dose_2 = captab_list[7]
#     patient_instances[patient_row].secondary_opioid_dif_dose_captab_per_episode_dose_3 = captab_list[8]
#     patient_instances[patient_row].secondary_opioid_dif_dose_captab_per_episode_dose_4 = captab_list[9]
                
    
#     patient_instances[patient_row].primary_opioid_unit_dose = unit_dose_list[0]
#     patient_instances[patient_row].primary_opioid_dif_dose_ep_1_unit_dose = unit_dose_list[1]
#     patient_instances[patient_row].primary_opioid_dif_dose_ep_2_unit_dose = unit_dose_list[2]
#     patient_instances[patient_row].primary_opioid_dif_dose_ep_3_unit_dose = unit_dose_list[3]
#     patient_instances[patient_row].primary_opioid_dif_dose_ep_4_unit_dose = unit_dose_list[4]
#     patient_instances[patient_row].secondary_opioid_unit_dose = unit_dose_list[5]
#     patient_instances[patient_row].secondary_opioid_dif_dose_ep_1_unit_dose = unit_dose_list[6]
#     patient_instances[patient_row].secondary_opioid_dif_dose_ep_2_unit_dose = unit_dose_list[7]
#     patient_instances[patient_row].secondary_opioid_dif_dose_ep_3_unit_dose = unit_dose_list[8]
#     patient_instances[patient_row].secondary_opioid_dif_dose_ep_4_unit_dose = unit_dose_list[9]
    
#     pass

# patient_dictionary = dict(zip(instanceNames, patient_instances))


# ###########
# def print_all_reports(patient):
 
#      #Step 1: Print monthly report #1 (Month 1 for given patient)
     
#      #Month 1:
#      Print_monthly_report(patient)
     
#      first_patient_row = Generate_first_patient_month_list(patient,
#                                                            month=1)
     
#      #Step 3: For months 2-12, print reports for months 2-12 for given patient:
      
#      print('________________________________________________________________')   
     
#      #Month 2-12:
#      patient.main_prescription_list = []
#      patient.main_prescription_list.append(first_patient_row)
     
#      for month in range(2,14):
#          #Execute new month:
#          patient.research_study_timer.New_month()
     
#          #Execute Taper:
#          taper = Taper(patient)
         
#          #Execute prescription object HERE:
#          prescription = Prescription(patient,
#                                      taper)
#          #Print report:
#          Print_monthly_report(patient)
         
#          #Generate dataframe:
#          new_patient_row = Generate_patient_month_list(patient,
#                                                month,
#                                                prescription)
         
#          patient.main_prescription_list.append(new_patient_row)
#          print('------------------------------------------------------------')
#          pass
#      pass

# ###################################################

# #for patient in patient_dictionary:
# #    if patient == 'Patient_3':
# #        print_all_reports(patient_dictionary[patient])
# #        pass
# #    else:
# #        pass
     
# def Generate_first_patient_month_list(patient, month=1):
    
#     patient_ID_number = patient.ID_number
#     patient_last_name = patient.last_name
#     patient_first_name = patient.first_name
#     med_1 = patient.primary_opioid_med_name
#     total_med_1_24_hr_dose = patient.Primary_total_dose_per_24_hr()
#     total_med_1_24_hr_MME = patient.Calculate_med_MME_24_hr(patient.primary_opioid_med)
#     med_2 = patient.secondary_opioid_med_name
#     total_med_2_24_hr_dose = patient.Secondary_total_dose_per_24_hr()
#     total_med_2_24_hr_MME = patient.Calculate_med_MME_24_hr(patient.secondary_opioid_med)
#     pre_taper_mme = total_med_1_24_hr_MME + total_med_2_24_hr_MME
#     total_mme = pre_taper_mme
#     percent_mme_decrease = 0
    
#     #PRIMARY MED FIRST:
    
#     if patient.primary_opioid_med != None:
    
#         #Episode 1:
        
#         #Primary Med:
#         if patient.different_daily_episode_doses_med_1 == 'Yes':
#              Med_1_Episode_1 = patient.primary_opioid_med_name
#              Med_1_Episode_1_Dose = patient.primary_opioid_dif_dose_episode_dose_1 
#              Med_1_Episode_1_Dose_Frequency = patient.primary_opioid_interdose_duration
#              Med_1_Episode_1_Unit_Dose = patient.primary_opioid_dif_dose_ep_1_unit_dose
#              Med_1_Episode_1_Active_Capsules = patient.primary_opioid_dif_dose_captab_per_episode_dose_1
#              Med_1_Episode_1_Placebo_Capsules = 0
#              Med_1_Episode_1_Total_Capsules = patient.primary_opioid_dif_dose_captab_per_episode_dose_1
#              pass
#         elif patient.different_daily_episode_doses_med_1 != 'Yes':
#             Med_1_Episode_1 = patient.primary_opioid_med_name
#             Med_1_Episode_1_Dose = patient.primary_opioid_episode_dose
#             Med_1_Episode_1_Dose_Frequency = patient.primary_opioid_interdose_duration
#             Med_1_Episode_1_Unit_Dose = patient.primary_opioid_unit_dose 
#             Med_1_Episode_1_Active_Capsules = patient.primary_opioid_captab_per_episode_dose
#             Med_1_Episode_1_Placebo_Capsules = 0
#             Med_1_Episode_1_Total_Capsules = patient.primary_opioid_captab_per_episode_dose
#             pass
#         else:
#             pass
        
#         if patient.primary_opioid_interdose_duration <= 12:
#             #Episode 2:
            
#             #Primary Med:
#             if patient.different_daily_episode_doses_med_1 == 'Yes':
#                  Med_1_Episode_2 = patient.primary_opioid_med_name
#                  Med_1_Episode_2_Dose = patient.primary_opioid_dif_dose_episode_dose_2 
#                  Med_1_Episode_2_Dose_Frequency = patient.primary_opioid_interdose_duration
#                  Med_1_Episode_2_Unit_Dose = patient.primary_opioid_dif_dose_ep_2_unit_dose
#                  Med_1_Episode_2_Active_Capsules = patient.primary_opioid_dif_dose_captab_per_episode_dose_2
#                  Med_1_Episode_2_Placebo_Capsules = 0
#                  Med_1_Episode_2_Total_Capsules = patient.primary_opioid_dif_dose_captab_per_episode_dose_2
#                  pass
#             elif patient.different_daily_episode_doses_med_1 != 'Yes':
#                 Med_1_Episode_2 = patient.primary_opioid_med_name
#                 Med_1_Episode_2_Dose = patient.primary_opioid_episode_dose
#                 Med_1_Episode_2_Dose_Frequency = patient.primary_opioid_interdose_duration
#                 Med_1_Episode_2_Unit_Dose = patient.primary_opioid_unit_dose 
#                 Med_1_Episode_2_Active_Capsules = patient.primary_opioid_captab_per_episode_dose
#                 Med_1_Episode_2_Placebo_Capsules = 0
#                 Med_1_Episode_2_Total_Capsules = patient.primary_opioid_captab_per_episode_dose
#                 pass
#             else:
#                 pass
#             pass
#         else:
#             Med_1_Episode_2 = None
#             Med_1_Episode_2_Dose = None
#             Med_1_Episode_2_Dose_Frequency = None
#             Med_1_Episode_2_Unit_Dose = None
#             Med_1_Episode_2_Active_Capsules = None
#             Med_1_Episode_2_Placebo_Capsules = None
#             Med_1_Episode_2_Total_Capsules = None
#             pass
        
#         if patient.primary_opioid_interdose_duration <= 8:
#             #Episode 3:
            
#             #Primary Med:
#             if patient.different_daily_episode_doses_med_1 == 'Yes':
#                  Med_1_Episode_3 = patient.primary_opioid_med_name
#                  Med_1_Episode_3_Dose = patient.primary_opioid_dif_dose_episode_dose_3
#                  Med_1_Episode_3_Dose_Frequency = patient.primary_opioid_interdose_duration
#                  Med_1_Episode_3_Unit_Dose = patient.primary_opioid_dif_dose_ep_3_unit_dose
#                  Med_1_Episode_3_Active_Capsules = patient.primary_opioid_dif_dose_captab_per_episode_dose_3
#                  Med_1_Episode_3_Placebo_Capsules = 0
#                  Med_1_Episode_3_Total_Capsules = patient.primary_opioid_dif_dose_captab_per_episode_dose_3
#                  pass
#             elif patient.different_daily_episode_doses_med_1 != 'Yes':
#                 Med_1_Episode_3 = patient.primary_opioid_med_name
#                 Med_1_Episode_3_Dose = patient.primary_opioid_episode_dose
#                 Med_1_Episode_3_Dose_Frequency = patient.primary_opioid_interdose_duration
#                 Med_1_Episode_3_Unit_Dose = patient.primary_opioid_unit_dose 
#                 Med_1_Episode_3_Active_Capsules = patient.primary_opioid_captab_per_episode_dose
#                 Med_1_Episode_3_Placebo_Capsules = 0
#                 Med_1_Episode_3_Total_Capsules = patient.primary_opioid_captab_per_episode_dose
#                 pass
#             else:
#                 pass
#             pass
#         else:
#             Med_1_Episode_3 = None
#             Med_1_Episode_3_Dose = None
#             Med_1_Episode_3_Dose_Frequency = None
#             Med_1_Episode_3_Unit_Dose = None
#             Med_1_Episode_3_Active_Capsules = None
#             Med_1_Episode_3_Placebo_Capsules = None
#             Med_1_Episode_3_Total_Capsules = None
#             pass
        
#         if patient.primary_opioid_interdose_duration <= 6:
#             #Episode 4:
            
#             #Primary Med:
#             if patient.different_daily_episode_doses_med_1 == 'Yes':
#                  Med_1_Episode_4 = patient.primary_opioid_med_name
#                  Med_1_Episode_4_Dose = patient.primary_opioid_dif_dose_episode_dose_4 
#                  Med_1_Episode_4_Dose_Frequency = patient.primary_opioid_interdose_duration
#                  Med_1_Episode_4_Unit_Dose = patient.primary_opioid_dif_dose_ep_4_unit_dose
#                  Med_1_Episode_4_Active_Capsules = patient.primary_opioid_dif_dose_captab_per_episode_dose_4
#                  Med_1_Episode_4_Placebo_Capsules = 0
#                  Med_1_Episode_4_Total_Capsules = patient.primary_opioid_dif_dose_captab_per_episode_dose_4
#                  pass
#             elif patient.different_daily_episode_doses_med_1 != 'Yes':
#                 Med_1_Episode_4 = patient.primary_opioid_med_name
#                 Med_1_Episode_4_Dose = patient.primary_opioid_episode_dose
#                 Med_1_Episode_4_Dose_Frequency = patient.primary_opioid_interdose_duration
#                 Med_1_Episode_4_Unit_Dose = patient.primary_opioid_unit_dose 
#                 Med_1_Episode_4_Active_Capsules = patient.primary_opioid_captab_per_episode_dose
#                 Med_1_Episode_4_Placebo_Capsules = 0
#                 Med_1_Episode_4_Total_Capsules = patient.primary_opioid_captab_per_episode_dose
#                 pass
#             else:
#                 pass
#             pass
#         else:
#             Med_1_Episode_4 = None
#             Med_1_Episode_4_Dose = None
#             Med_1_Episode_4_Dose_Frequency = None
#             Med_1_Episode_4_Unit_Dose = None
#             Med_1_Episode_4_Active_Capsules = None
#             Med_1_Episode_4_Placebo_Capsules = None
#             Med_1_Episode_4_Total_Capsules = None
#             pass
#         pass
            
#     else:
#          Med_1_Episode_1 = None
#          Med_1_Episode_1_Dose = None
#          Med_1_Episode_1_Dose_Frequency = None
#          Med_1_Episode_1_Unit_Dose = None
#          Med_1_Episode_1_Active_Capsules = None
#          Med_1_Episode_1_Placebo_Capsules = None
#          Med_1_Episode_1_Total_Capsules = None
#          Med_1_Episode_2 = None
#          Med_1_Episode_2_Dose = None
#          Med_1_Episode_2_Dose_Frequency = None
#          Med_1_Episode_2_Unit_Dose = None
#          Med_1_Episode_2_Active_Capsules = None
#          Med_1_Episode_2_Placebo_Capsules = None
#          Med_1_Episode_2_Total_Capsules = None
#          Med_1_Episode_3 = None
#          Med_1_Episode_3_Dose = None
#          Med_1_Episode_3_Dose_Frequency = None
#          Med_1_Episode_3_Unit_Dose = None
#          Med_1_Episode_3_Active_Capsules = None
#          Med_1_Episode_3_Placebo_Capsules = None
#          Med_1_Episode_3_Total_Capsules = None
#          Med_1_Episode_4 = None
#          Med_1_Episode_4_Dose = None
#          Med_1_Episode_4_Dose_Frequency = None
#          Med_1_Episode_4_Unit_Dose = None
#          Med_1_Episode_4_Active_Capsules = None
#          Med_1_Episode_4_Placebo_Capsules = None
#          Med_1_Episode_4_Total_Capsules = None
#          pass
    
#     #NEXT, SECONDARY MED:
    
#     if patient.secondary_opioid_med != None:
#         #Secondary Med:
#         if patient.different_daily_episode_doses_med_2 == 'Yes':
#              Med_2_Episode_1 = patient.secondary_opioid_med_name
#              Med_2_Episode_1_Dose = patient.secondary_opioid_dif_dose_episode_dose_1 
#              Med_2_Episode_1_Dose_Frequency = patient.secondary_opioid_interdose_duration
#              Med_2_Episode_1_Unit_Dose = patient.secondary_opioid_dif_dose_ep_1_unit_dose
#              Med_2_Episode_1_Active_Capsules = patient.secondary_opioid_dif_dose_captab_per_episode_dose_1
#              Med_2_Episode_1_Placebo_Capsules = 0
#              Med_2_Episode_1_Total_Capsules = patient.secondary_opioid_dif_dose_captab_per_episode_dose_1
#              pass
#         elif patient.different_daily_episode_doses_med_2 != 'Yes':
#             Med_2_Episode_1 = patient.secondary_opioid_med_name
#             Med_2_Episode_1_Dose = patient.secondary_opioid_episode_dose
#             Med_2_Episode_1_Dose_Frequency = patient.secondary_opioid_interdose_duration
#             Med_2_Episode_1_Unit_Dose = patient.secondary_opioid_unit_dose 
#             Med_2_Episode_1_Active_Capsules = patient.secondary_opioid_captab_per_episode_dose
#             Med_2_Episode_1_Placebo_Capsules = 0
#             Med_2_Episode_1_Total_Capsules = patient.secondary_opioid_captab_per_episode_dose
#             pass
#         else:
#             pass
        
#         if patient.secondary_opioid_interdose_duration <= 12:
#             #Episode 2
        
            
#             #Secondary Med:
#             if patient.different_daily_episode_doses_med_2 == 'Yes':
#                  Med_2_Episode_2 = patient.secondary_opioid_med_name
#                  Med_2_Episode_2_Dose = patient.secondary_opioid_dif_dose_episode_dose_2
#                  Med_2_Episode_2_Dose_Frequency = patient.secondary_opioid_interdose_duration
#                  Med_2_Episode_2_Unit_Dose = patient.secondary_opioid_dif_dose_ep_2_unit_dose
#                  Med_2_Episode_2_Active_Capsules = patient.secondary_opioid_dif_dose_captab_per_episode_dose_2
#                  Med_2_Episode_2_Placebo_Capsules = 0
#                  Med_2_Episode_2_Total_Capsules = patient.secondary_opioid_dif_dose_captab_per_episode_dose_2
#                  pass
#             elif patient.different_daily_episode_doses_med_2 != 'Yes':
#                 Med_2_Episode_2 = patient.secondary_opioid_med_name
#                 Med_2_Episode_2_Dose = patient.secondary_opioid_episode_dose
#                 Med_2_Episode_2_Dose_Frequency = patient.secondary_opioid_interdose_duration
#                 Med_2_Episode_2_Unit_Dose = patient.secondary_opioid_unit_dose 
#                 Med_2_Episode_2_Active_Capsules = patient.secondary_opioid_captab_per_episode_dose
#                 Med_2_Episode_2_Placebo_Capsules = 0
#                 Med_2_Episode_2_Total_Capsules = patient.secondary_opioid_captab_per_episode_dose
#                 pass
#             else:
#                 pass
#             pass
#         else:
#             Med_2_Episode_2 = None
#             Med_2_Episode_2_Dose = None
#             Med_2_Episode_2_Dose_Frequency = None
#             Med_2_Episode_2_Unit_Dose = None
#             Med_2_Episode_2_Active_Capsules = None
#             Med_2_Episode_2_Placebo_Capsules = None
#             Med_2_Episode_2_Total_Capsules = None
#             pass
        
#         if patient.secondary_opioid_interdose_duration <= 8:
#             #Episode 3
    
#             #Secondary Med:
#             if patient.different_daily_episode_doses_med_2 == 'Yes':
#                  Med_2_Episode_3 = patient.secondary_opioid_med_name
#                  Med_2_Episode_3_Dose = patient.secondary_opioid_dif_dose_episode_dose_3
#                  Med_2_Episode_3_Dose_Frequency = patient.secondary_opioid_interdose_duration
#                  Med_2_Episode_3_Unit_Dose = patient.secondary_opioid_dif_dose_ep_3_unit_dose
#                  Med_2_Episode_3_Active_Capsules = patient.secondary_opioid_dif_dose_captab_per_episode_dose_3
#                  Med_2_Episode_3_Placebo_Capsules = 0
#                  Med_2_Episode_3_Total_Capsules = patient.secondary_opioid_dif_dose_captab_per_episode_dose_3
#                  pass
#             elif patient.different_daily_episode_doses_med_2 != 'Yes':
#                 Med_2_Episode_3 = patient.secondary_opioid_med_name
#                 Med_2_Episode_3_Dose = patient.secondary_opioid_episode_dose
#                 Med_2_Episode_3_Dose_Frequency = patient.secondary_opioid_interdose_duration
#                 Med_2_Episode_3_Unit_Dose = patient.secondary_opioid_unit_dose 
#                 Med_2_Episode_3_Active_Capsules = patient.secondary_opioid_captab_per_episode_dose
#                 Med_2_Episode_3_Placebo_Capsules = 0
#                 Med_2_Episode_3_Total_Capsules = patient.secondary_opioid_captab_per_episode_dose
#                 pass
#             else:
#                 pass
#             pass
#         else:
#             Med_2_Episode_3 = None
#             Med_2_Episode_3_Dose = None
#             Med_2_Episode_3_Dose_Frequency = None
#             Med_2_Episode_3_Unit_Dose = None
#             Med_2_Episode_3_Active_Capsules = None
#             Med_2_Episode_3_Placebo_Capsules = None
#             Med_2_Episode_3_Total_Capsules = None
#             pass
        
#         if patient.secondary_opioid_interdose_duration <= 6:
#             #Episode 4
    
#             #Secondary Med:
#             if patient.different_daily_episode_doses_med_2 == 'Yes':
#                  Med_2_Episode_4 = patient.secondary_opioid_med_name
#                  Med_2_Episode_4_Dose = patient.secondary_opioid_dif_dose_episode_dose_4
#                  Med_2_Episode_4_Dose_Frequency = patient.secondary_opioid_interdose_duration
#                  Med_2_Episode_4_Unit_Dose = patient.secondary_opioid_dif_dose_ep_4_unit_dose
#                  Med_2_Episode_4_Active_Capsules = patient.secondary_opioid_dif_dose_captab_per_episode_dose_4
#                  Med_2_Episode_4_Placebo_Capsules = 0
#                  Med_2_Episode_4_Total_Capsules = patient.secondary_opioid_dif_dose_captab_per_episode_dose_4
#                  pass
#             elif patient.different_daily_episode_doses_med_2 != 'Yes':
#                 Med_2_Episode_4 = patient.secondary_opioid_med_name
#                 Med_2_Episode_4_Dose = patient.secondary_opioid_episode_dose
#                 Med_2_Episode_4_Dose_Frequency = patient.secondary_opioid_interdose_duration
#                 Med_2_Episode_4_Unit_Dose = patient.secondary_opioid_unit_dose 
#                 Med_2_Episode_4_Active_Capsules = patient.secondary_opioid_captab_per_episode_dose
#                 Med_2_Episode_4_Placebo_Capsules = 0
#                 Med_2_Episode_4_Total_Capsules = patient.secondary_opioid_captab_per_episode_dose
#                 pass
#             else:
#                 pass
#             pass
#         else:
#             Med_2_Episode_4 = None
#             Med_2_Episode_4_Dose = None
#             Med_2_Episode_4_Dose_Frequency = None
#             Med_2_Episode_4_Unit_Dose = None
#             Med_2_Episode_4_Active_Capsules = None
#             Med_2_Episode_4_Placebo_Capsules = None
#             Med_2_Episode_4_Total_Capsules = None
#             pass
#         pass
    
#     else:
#          Med_2_Episode_1 = None
#          Med_2_Episode_1_Dose = None
#          Med_2_Episode_1_Dose_Frequency = None
#          Med_2_Episode_1_Unit_Dose = None
#          Med_2_Episode_1_Active_Capsules = None
#          Med_2_Episode_1_Placebo_Capsules = None
#          Med_2_Episode_1_Total_Capsules = None
#          Med_2_Episode_2 = None
#          Med_2_Episode_2_Dose = None
#          Med_2_Episode_2_Dose_Frequency = None
#          Med_2_Episode_2_Unit_Dose = None
#          Med_2_Episode_2_Active_Capsules = None
#          Med_2_Episode_2_Placebo_Capsules = None
#          Med_2_Episode_2_Total_Capsules = None
#          Med_2_Episode_3 = None
#          Med_2_Episode_3_Dose = None
#          Med_2_Episode_3_Dose_Frequency = None
#          Med_2_Episode_3_Unit_Dose = None
#          Med_2_Episode_3_Active_Capsules = None
#          Med_2_Episode_3_Placebo_Capsules = None
#          Med_2_Episode_3_Total_Capsules = None
#          Med_2_Episode_4 = None
#          Med_2_Episode_4_Dose = None
#          Med_2_Episode_4_Dose_Frequency = None
#          Med_2_Episode_4_Unit_Dose = None
#          Med_2_Episode_4_Active_Capsules = None
#          Med_2_Episode_4_Placebo_Capsules = None
#          Med_2_Episode_4_Total_Capsules = None
#          pass
     
#     new_first_row =[patient_ID_number,
#                    month,
#                    patient_last_name,
#                    patient_first_name,
#                    med_1,
#                    total_med_1_24_hr_dose,
#                    total_med_1_24_hr_MME,
#                    med_2,
#                    total_med_2_24_hr_dose,
#                    total_med_2_24_hr_MME,
#                    pre_taper_mme,
#                    total_mme,
#                    percent_mme_decrease,
#     #               number_episodes,
#     #               frequency_doses,
#                    Med_1_Episode_1,
#                    Med_1_Episode_1_Dose,
#                    Med_1_Episode_1_Dose_Frequency,
#                    Med_1_Episode_1_Unit_Dose,
#                    Med_1_Episode_1_Active_Capsules,
#                    Med_1_Episode_1_Placebo_Capsules,
#                    Med_1_Episode_1_Total_Capsules,
#                    Med_2_Episode_1,
#                    Med_2_Episode_1_Dose,
#                    Med_2_Episode_1_Dose_Frequency,
#                    Med_2_Episode_1_Unit_Dose,
#                    Med_2_Episode_1_Active_Capsules,
#                    Med_2_Episode_1_Placebo_Capsules,
#                    Med_2_Episode_1_Total_Capsules,
#                    Med_1_Episode_2,
#                    Med_1_Episode_2_Dose,
#                    Med_1_Episode_2_Dose_Frequency,
#                    Med_1_Episode_2_Unit_Dose,
#                    Med_1_Episode_2_Active_Capsules,
#                    Med_1_Episode_2_Placebo_Capsules,
#                    Med_1_Episode_2_Total_Capsules,
#                    Med_2_Episode_2,
#                    Med_2_Episode_2_Dose,
#                    Med_2_Episode_2_Dose_Frequency,
#                    Med_2_Episode_2_Unit_Dose,
#                    Med_2_Episode_2_Active_Capsules,
#                    Med_2_Episode_2_Placebo_Capsules,
#                    Med_2_Episode_2_Total_Capsules,
#                    Med_1_Episode_3,
#                    Med_1_Episode_3_Dose,
#                    Med_1_Episode_3_Dose_Frequency,
#                    Med_1_Episode_3_Unit_Dose,
#                    Med_1_Episode_3_Active_Capsules,
#                    Med_1_Episode_3_Placebo_Capsules,
#                    Med_1_Episode_3_Total_Capsules,
#                    Med_2_Episode_3,
#                    Med_2_Episode_3_Dose,
#                    Med_2_Episode_3_Dose_Frequency,
#                    Med_2_Episode_3_Unit_Dose,
#                    Med_2_Episode_3_Active_Capsules,
#                    Med_2_Episode_3_Placebo_Capsules,
#                    Med_2_Episode_3_Total_Capsules,
#                    Med_1_Episode_4,
#                    Med_1_Episode_4_Dose,
#                    Med_1_Episode_4_Dose_Frequency,
#                    Med_1_Episode_4_Unit_Dose,
#                    Med_1_Episode_4_Active_Capsules,
#                    Med_1_Episode_4_Placebo_Capsules,
#                    Med_1_Episode_4_Total_Capsules,
#                    Med_2_Episode_4,
#                    Med_2_Episode_4_Dose,
#                    Med_2_Episode_4_Dose_Frequency,
#                    Med_2_Episode_4_Unit_Dose,
#                    Med_2_Episode_4_Active_Capsules,
#                    Med_2_Episode_4_Placebo_Capsules,
#                    Med_2_Episode_4_Total_Capsules
#                    ]
  
#     return new_first_row


# def Generate_patient_month_list(patient,
#                                 month,
#                                 prescription_object):
#     #Assign variables:
#     patient_ID = patient.ID_number
#     patient_last_name = patient.last_name
#     patient_first_name = patient.first_name
    
#     med_1 = patient.primary_opioid_med_name
#     total_med_1_24_hr_dose = prescription_object.aggregate_primary_med['Total Primary Med 24hr Dose']
#     total_med_1_24_hr_MME = prescription_object.aggregate_primary_med['Total Primary Med 24hr MME']
# #    total_med_1_24_hr_capsule_count = prescription_object.aggregate_primary_med['Total Primary Med 24hr All Med Capsule Count']
# #    total_med_1_24_hr_active_capsule_count = prescription_object.aggregate_primary_med['Total Primary Med 24hr Active Capsule Count']
# #    total_med_1_24_hr_placebo_capsule_count = prescription_object.aggregate_primary_med['Total Primary Med 24hr Placebo Capsule Count']
    
#     med_2 = patient.secondary_opioid_med_name
#     total_med_2_24_hr_dose = prescription_object.aggregate_secondary_med['Total Secondary Med 24hr Dose']
#     total_med_2_24_hr_MME = prescription_object.aggregate_secondary_med['Total Secondary Med 24hr MME']
# #    total_med_2_24_hr_capsule_count = prescription_object.aggregate_secondary_med['Total Secondary Med 24hr All Med Capsule Count']
# #    total_med_2_24_hr_active_capsule_count = prescription_object.aggregate_secondary_med['Total Secondary Med 24hr Active Capsule Count']
# #    total_med_2_24_hr_placebo_capsule_count = prescription_object.aggregate_secondary_med['Total Secondary Med 24hr Placebo Capsule Count']
    
    
#     pre_taper_mme = prescription_object.ideal_vs_actual_MME_calculations['Pre-taper total MME']
#     post_taper_ideal_mme = prescription_object.ideal_vs_actual_MME_calculations['Post-taper ideal total MME']
#     total_mme = prescription_object.aggregate_all_med['Total All Med 24hr MME']
#     percent_mme_decrease = prescription_object.ideal_vs_actual_MME_calculations['Actual percent MME decrease']
    
#     #All episode dictionary:
#     all_episode_dictionary = prescription_object.actual_episodes
    
#     #Number of dose episodes in 24 hr:
#     #number_episodes = prescription_object.number_episodes
    
#     #Frequency of Dose Episodes:
#     #frequency_doses = prescription_object.aggregate_interdose_duration
    
#     ######################## EPISODE 1 ########################################
#     #Episode 1:
#     Episode_1 = all_episode_dictionary['Episode 1']
    
#     #Primary Med Episode 1:
#     Primary_Med_Episode_1 = Episode_1['Primary Opioid Med Episode 1']
    
#     #Med 1 name:
#     Med_1_Episode_1 = Primary_Med_Episode_1['Primary Med Name']
        
#     #Med 1 episode dose:
#     Med_1_Episode_1_Dose = Primary_Med_Episode_1['Primary Med Episode Dose 1']
    
#     #Med 1 dose frequency:
#     Med_1_Episode_1_Dose_Frequency = patient.primary_opioid_interdose_duration
    
#     #Med 1 unit dose:
#     Med_1_Episode_1_Unit_Dose = Primary_Med_Episode_1['Primary Med Episode Unit Dose 1']
    
#     #Med 1 active capsules:
#     Med_1_Episode_1_Active_Capsules = Primary_Med_Episode_1['Primary Med Active Capsules Episode 1']
    
#     #Med 1 placebo capsules:
#     Med_1_Episode_1_Placebo_Capsules = Primary_Med_Episode_1['Primary Med Placebo Capsules Episode 1']
    
#     #Med 1 total capsules:
#     Med_1_Episode_1_Total_Capsules = Primary_Med_Episode_1['Primary Med Total Capsules Episode 1']
        
#     #Primary Med Episode 1:
#     Secondary_Med_Episode_1 = Episode_1['Secondary Opioid Med Episode 1']
    
#     #Med 2 name:
#     Med_2_Episode_1 = Secondary_Med_Episode_1['Secondary Med Name']
        
#     #Med 2 episode dose:
#     Med_2_Episode_1_Dose = Secondary_Med_Episode_1['Secondary Med Episode Dose 1']
    
#     #Med 2 dose frequency:
#     Med_2_Episode_1_Dose_Frequency = patient.secondary_opioid_interdose_duration
    
#     #Med 2 unit dose:
#     Med_2_Episode_1_Unit_Dose = Secondary_Med_Episode_1['Secondary Med Episode Unit Dose 1']
    
#     #Med 2 active capsules:
#     Med_2_Episode_1_Active_Capsules = Secondary_Med_Episode_1['Secondary Med Active Capsules Episode 1']
    
#     #Med 2 placebo capsules:
#     Med_2_Episode_1_Placebo_Capsules = Secondary_Med_Episode_1['Secondary Med Placebo Capsules Episode 1']
    
#     #Med 2 total capsules:
#     Med_2_Episode_1_Total_Capsules = Secondary_Med_Episode_1['Secondary Med Total Capsules Episode 1']
    
#     ######################## EPISODE 2 ########################################
    
#     #Episode 2:
#     Episode_2 = all_episode_dictionary['Episode 2']
    
#     #Primary Med Episode 2:
#     Primary_Med_Episode_2 = Episode_2['Primary Opioid Med Episode 2']
    
#     #Med 1 name:
#     Med_1_Episode_2 = Primary_Med_Episode_2['Primary Med Name']
        
#     #Med 1 episode dose:
#     Med_1_Episode_2_Dose = Primary_Med_Episode_2['Primary Med Episode Dose 2']
    
#     #Med 1 dose frequency:
#     Med_1_Episode_2_Dose_Frequency = patient.primary_opioid_interdose_duration
    
#     #Med 1 unit dose:
#     Med_1_Episode_2_Unit_Dose = Primary_Med_Episode_2['Primary Med Episode Unit Dose 2']
    
#     #Med 1 active capsules:
#     Med_1_Episode_2_Active_Capsules = Primary_Med_Episode_2['Primary Med Active Capsules Episode 2']
    
#     #Med 1 placebo capsules:
#     Med_1_Episode_2_Placebo_Capsules = Primary_Med_Episode_2['Primary Med Placebo Capsules Episode 2']
    
#     #Med 1 total capsules:
#     Med_1_Episode_2_Total_Capsules = Primary_Med_Episode_2['Primary Med Total Capsules Episode 2']
        
#     #Secondary Med Episode 2:
#     Secondary_Med_Episode_2 = Episode_2['Secondary Opioid Med Episode 2']
    
#     #Med 2 name:
#     Med_2_Episode_2 = Secondary_Med_Episode_2['Secondary Med Name']
        
#     #Med 2 episode dose:
#     Med_2_Episode_2_Dose = Secondary_Med_Episode_2['Secondary Med Episode Dose 2']
    
#     #Med 2 dose frequency:
#     Med_2_Episode_2_Dose_Frequency = patient.secondary_opioid_interdose_duration
    
#     #Med 2 unit dose:
#     Med_2_Episode_2_Unit_Dose = Secondary_Med_Episode_2['Secondary Med Episode Unit Dose 2']
    
#     #Med 2 active capsules:
#     Med_2_Episode_2_Active_Capsules = Secondary_Med_Episode_2['Secondary Med Active Capsules Episode 2']
    
#     #Med 2 placebo capsules:
#     Med_2_Episode_2_Placebo_Capsules = Secondary_Med_Episode_2['Secondary Med Placebo Capsules Episode 2']
    
#     #Med 2 total capsules:
#     Med_2_Episode_2_Total_Capsules = Secondary_Med_Episode_2['Secondary Med Total Capsules Episode 2']
    
#     ######################## EPISODE 3 ########################################
    
#     #Episode 3:
#     if 'Episode 3' in all_episode_dictionary.keys():
#         Episode_3 = all_episode_dictionary['Episode 3']
        
#         #Primary Med Episode 3:
#         Primary_Med_Episode_3 = Episode_3['Primary Opioid Med Episode 3']
        
#         if Primary_Med_Episode_3 != None:
        
#             #Med 1 name:
#             Med_1_Episode_3 = Primary_Med_Episode_3['Primary Med Name']
                
#             #Med 1 episode dose:
#             Med_1_Episode_3_Dose = Primary_Med_Episode_3['Primary Med Episode Dose 3']
            
#             #Med 1 dose frequency:
#             Med_1_Episode_3_Dose_Frequency = patient.primary_opioid_interdose_duration
            
#             #Med 1 unit dose:
#             Med_1_Episode_3_Unit_Dose = Primary_Med_Episode_3['Primary Med Episode Unit Dose 3']
            
#             #Med 1 active capsules:
#             Med_1_Episode_3_Active_Capsules = Primary_Med_Episode_3['Primary Med Active Capsules Episode 3']
            
#             #Med 1 placebo capsules:
#             Med_1_Episode_3_Placebo_Capsules = Primary_Med_Episode_3['Primary Med Placebo Capsules Episode 3']
            
#             #Med 1 total capsules:
#             Med_1_Episode_3_Total_Capsules = Primary_Med_Episode_3['Primary Med Total Capsules Episode 3']
#             pass
#         else:
#             #Med 1 name:
#             Med_1_Episode_3 = None
                
#             #Med 1 episode dose:
#             Med_1_Episode_3_Dose = None
            
#             #Med 1 dose frequency:
#             Med_1_Episode_3_Dose_Frequency = None
            
#             #Med 1 unit dose:
#             Med_1_Episode_3_Unit_Dose = None
            
#             #Med 1 active capsules:
#             Med_1_Episode_3_Active_Capsules = None
            
#             #Med 1 placebo capsules:
#             Med_1_Episode_3_Placebo_Capsules = None
            
#             #Med 1 total capsules:
#             Med_1_Episode_3_Total_Capsules = None
            
#             pass
            
#         #Secondary Med Episode 3:
#         Secondary_Med_Episode_3 = Episode_3['Secondary Opioid Med Episode 3']
        
#         if Secondary_Med_Episode_3 != None:
            
#             #Med 2 name:
#             Med_2_Episode_3 = Secondary_Med_Episode_3['Secondary Med Name']
                
#             #Med 2 episode dose:
#             Med_2_Episode_3_Dose = Secondary_Med_Episode_3['Secondary Med Episode Dose 3']
            
#             #Med 2 dose frequency:
#             Med_2_Episode_3_Dose_Frequency = patient.secondary_opioid_interdose_duration
            
#             #Med 2 unit dose:
#             Med_2_Episode_3_Unit_Dose = Secondary_Med_Episode_3['Secondary Med Episode Unit Dose 3']
            
#             #Med 2 active capsules:
#             Med_2_Episode_3_Active_Capsules = Secondary_Med_Episode_3['Secondary Med Active Capsules Episode 3']
            
#             #Med 2 placebo capsules:
#             Med_2_Episode_3_Placebo_Capsules = Secondary_Med_Episode_3['Secondary Med Placebo Capsules Episode 3']
            
#             #Med 2 total capsules:
#             Med_2_Episode_3_Total_Capsules = Secondary_Med_Episode_3['Secondary Med Total Capsules Episode 3']
            
#             pass
        
#         else:
#             #Med 2 name:
#             Med_2_Episode_3 = None
                
#             #Med 2 episode dose:
#             Med_2_Episode_3_Dose = None
            
#             #Med 2 dose frequency:
#             Med_2_Episode_3_Dose_Frequency = None
        
#             #Med 2 unit dose:
#             Med_2_Episode_3_Unit_Dose = None
            
#             #Med 2 active capsules:
#             Med_2_Episode_3_Active_Capsules = None
            
#             #Med 2 placebo capsules:
#             Med_2_Episode_3_Placebo_Capsules = None
            
#             #Med 2 total capsules:
#             Med_2_Episode_3_Total_Capsules = None
            
#             pass
#         pass
#     else:
#         #Med 1 name:
#         Med_1_Episode_3 = None
            
#         #Med 1 episode dose:
#         Med_1_Episode_3_Dose = None
        
#         #Med 1 dose frequency:
#         Med_1_Episode_3_Dose_Frequency = None
        
#         #Med 1 unit dose:
#         Med_1_Episode_3_Unit_Dose = None
        
#         #Med 1 active capsules:
#         Med_1_Episode_3_Active_Capsules = None
        
#         #Med 1 placebo capsules:
#         Med_1_Episode_3_Placebo_Capsules = None
        
#         #Med 1 total capsules:
#         Med_1_Episode_3_Total_Capsules = None
        
#         #Secondary Med Episode 4:
#         Secondary_Med_Episode_3 = None
        
#         #Med 2 name:
#         Med_2_Episode_3 = None
            
#         #Med 2 episode dose:
#         Med_2_Episode_3_Dose = None
        
#         #Med 2 dose frequency:
#         Med_2_Episode_3_Dose_Frequency = None
        
#         #Med 2 unit dose:
#         Med_2_Episode_3_Unit_Dose = None
        
#         #Med 2 active capsules:
#         Med_2_Episode_3_Active_Capsules = None
        
#         #Med 2 placebo capsules:
#         Med_2_Episode_3_Placebo_Capsules = None
        
#         #Med 2 total capsules:
#         Med_2_Episode_3_Total_Capsules = None
        
#         pass
        
#     ######################## EPISODE 4 ########################################
    
#     #Episode 4:
#     if 'Episode 4' in all_episode_dictionary.keys():
#         Episode_4 = all_episode_dictionary['Episode 4']
        
#         #Primary Med Episode 4:
#         Primary_Med_Episode_4 = Episode_4['Primary Opioid Med Episode 4']
    
#         if Primary_Med_Episode_4 != None:
    
#             #Med 1 name:
#             Med_1_Episode_4 = Primary_Med_Episode_4['Primary Med Name']
                
#             #Med 1 episode dose:
#             Med_1_Episode_4_Dose = Primary_Med_Episode_4['Primary Med Episode Dose 4']
            
#             #Med 1 dose frequency:
#             Med_1_Episode_4_Dose_Frequency = patient.primary_opioid_interdose_duration
            
#             #Med 1 unit dose:
#             Med_1_Episode_4_Unit_Dose = Primary_Med_Episode_4['Primary Med Episode Unit Dose 4']
            
#             #Med 1 active capsules:
#             Med_1_Episode_4_Active_Capsules = Primary_Med_Episode_4['Primary Med Active Capsules Episode 4']
            
#             #Med 1 placebo capsules:
#             Med_1_Episode_4_Placebo_Capsules = Primary_Med_Episode_4['Primary Med Placebo Capsules Episode 4']
            
#             #Med 1 total capsules:
#             Med_1_Episode_4_Total_Capsules = Primary_Med_Episode_4['Primary Med Total Capsules Episode 4']
        
#         else:
        
#             #Med 1 name:
#             Med_1_Episode_4 = None
                
#             #Med 1 episode dose:
#             Med_1_Episode_4_Dose = None
            
#             #Med 1 dose frequency:
#             Med_1_Episode_4_Dose_Frequency = None
            
#             #Med 1 unit dose:
#             Med_1_Episode_4_Unit_Dose = None
            
#             #Med 1 active capsules:
#             Med_1_Episode_4_Active_Capsules = None
            
#             #Med 1 placebo capsules:
#             Med_1_Episode_4_Placebo_Capsules = None
            
#             #Med 1 total capsules:
#             Med_1_Episode_4_Total_Capsules = None
            
#             pass
    
        
#         #Secondary Med Episode 4:
#         Secondary_Med_Episode_4 = Episode_4['Secondary Opioid Med Episode 4']
        
#         if Secondary_Med_Episode_4 != None:
        
#             #Med 2 name:
#             Med_2_Episode_4 = Secondary_Med_Episode_4['Secondary Med Name']
                
#             #Med 2 episode dose:
#             Med_2_Episode_4_Dose = Secondary_Med_Episode_4['Secondary Med Episode Dose 4']
            
#             #Med 2 dose frequency:
#             Med_2_Episode_4_Dose_Frequency = patient.secondary_opioid_interdose_duration
            
#             #Med 2 unit dose:
#             Med_2_Episode_4_Unit_Dose = Secondary_Med_Episode_4['Secondary Med Episode Unit Dose 4']
            
#             #Med 2 active capsules:
#             Med_2_Episode_4_Active_Capsules = Secondary_Med_Episode_4['Secondary Med Active Capsules Episode 4']
            
#             #Med 2 placebo capsules:
#             Med_2_Episode_4_Placebo_Capsules = Secondary_Med_Episode_4['Secondary Med Placebo Capsules Episode 4']
            
#             #Med 2 total capsules:
#             Med_2_Episode_4_Total_Capsules = Secondary_Med_Episode_4['Secondary Med Total Capsules Episode 4']
            
#             pass
        
#         else:
                
#             #Secondary Med Episode 4:
#             Secondary_Med_Episode_4 = None
            
#             #Med 2 name:
#             Med_2_Episode_4 = None
                
#             #Med 2 episode dose:
#             Med_2_Episode_4_Dose = None
            
#             #Med 2 dose frequency:
#             Med_2_Episode_4_Dose_Frequency = None
            
#             #Med 2 unit dose:
#             Med_2_Episode_4_Unit_Dose = None
            
#             #Med 2 active capsules:
#             Med_2_Episode_4_Active_Capsules = None
            
#             #Med 2 placebo capsules:
#             Med_2_Episode_4_Placebo_Capsules = None
            
#             #Med 2 total capsules:
#             Med_2_Episode_4_Total_Capsules = None
            
#             pass
#         pass
#     else:
#         #Med 1 name:
#         Med_1_Episode_4 = None
            
#         #Med 1 episode dose:
#         Med_1_Episode_4_Dose = None
        
#         #Med 1 dose frequency:
#         Med_1_Episode_4_Dose_Frequency = None
        
#         #Med 1 unit dose:
#         Med_1_Episode_4_Unit_Dose = None
        
#         #Med 1 active capsules:
#         Med_1_Episode_4_Active_Capsules = None
        
#         #Med 1 placebo capsules:
#         Med_1_Episode_4_Placebo_Capsules = None
        
#         #Med 1 total capsules:
#         Med_1_Episode_4_Total_Capsules = None
        
#         #Secondary Med Episode 4:
#         Secondary_Med_Episode_4 = None
        
#         #Med 2 name:
#         Med_2_Episode_4 = None
            
#         #Med 2 episode dose:
#         Med_2_Episode_4_Dose = None
        
#         #Med 2 dose frequency:
#         Med_2_Episode_4_Dose_Frequency = None
        
#         #Med 2 unit dose:
#         Med_2_Episode_4_Unit_Dose = None
        
#         #Med 2 active capsules:
#         Med_2_Episode_4_Active_Capsules = None
        
#         #Med 2 placebo capsules:
#         Med_2_Episode_4_Placebo_Capsules = None
        
#         #Med 2 total capsules:
#         Med_2_Episode_4_Total_Capsules = None
        
#         pass
        
    
#     ######################## AGGREGATE MED 1 ###################################
    
#     #Aggregate Primary Med
    
#         #Total Med 1 24 hr Dose
    
#         #Total Med 1 24 hr MME
        
#         #Total Med 1 24 hr Active Capsule Count
        
#         #Total Med 1 24 hr Placebo Capsule Count
        
#         #Total Med 1 24 hr All Capsule Count
    
#     ######################## AGGREGATE MED 2 ##################################
    
#     #Aggregate Secondary Med
    
#         #Total Med 2 24 hr Dose
    
#         #Total Med 2 24 hr MME
        
#         #Total Med 2 24 hr Active Capsule Count
        
#         #Total Med 2 24 hr Placebo Capsule Count
        
#         #Total Med 2 24 hr All Capsule Count
    
#     ######################## AGGREGATE ALL MED ################################
#     #Aggregate All Med
        
#         #Total All Med Active Capsule Count
#         #Total All Med Placebo Capsule Count
#         #Total All Med All Capsule Count
#         #Pre-taper MME
#         #Post-taper MME (ideal)
#         #Post-taper MME percent decrease (ideal)
#         #Post-taper MME (actual)
#         #Post-taper MME percent decrease (actual)
    
#     ######################## PRE-POST TAPER DATA ##############################
    
#     #Pre/Post Taper Data
    
#     new_row = [patient_ID,
#                month,
#                patient_last_name,
#                patient_first_name,
#                med_1,
#                total_med_1_24_hr_dose,
#                total_med_1_24_hr_MME,
#                med_2,
#                total_med_2_24_hr_dose,
#                total_med_2_24_hr_MME,
#                pre_taper_mme,
#                total_mme,
#                percent_mme_decrease,
# #               number_episodes,
# #               frequency_doses,
#                Med_1_Episode_1,
#                Med_1_Episode_1_Dose,
#                Med_1_Episode_1_Dose_Frequency,
#                Med_1_Episode_1_Unit_Dose,
#                Med_1_Episode_1_Active_Capsules,
#                Med_1_Episode_1_Placebo_Capsules,
#                Med_1_Episode_1_Total_Capsules,
#                Med_2_Episode_1,
#                Med_2_Episode_1_Dose,
#                Med_2_Episode_1_Dose_Frequency,
#                Med_2_Episode_1_Unit_Dose,
#                Med_2_Episode_1_Active_Capsules,
#                Med_2_Episode_1_Placebo_Capsules,
#                Med_2_Episode_1_Total_Capsules,
#                Med_1_Episode_2,
#                Med_1_Episode_2_Dose,
#                Med_1_Episode_2_Dose_Frequency,
#                Med_1_Episode_2_Unit_Dose,
#                Med_1_Episode_2_Active_Capsules,
#                Med_1_Episode_2_Placebo_Capsules,
#                Med_1_Episode_2_Total_Capsules,
#                Med_2_Episode_2,
#                Med_2_Episode_2_Dose,
#                Med_2_Episode_2_Dose_Frequency,
#                Med_2_Episode_2_Unit_Dose,
#                Med_2_Episode_2_Active_Capsules,
#                Med_2_Episode_2_Placebo_Capsules,
#                Med_2_Episode_2_Total_Capsules,
#                Med_1_Episode_3,
#                Med_1_Episode_3_Dose,
#                Med_1_Episode_3_Dose_Frequency,
#                Med_1_Episode_3_Unit_Dose,
#                Med_1_Episode_3_Active_Capsules,
#                Med_1_Episode_3_Placebo_Capsules,
#                Med_1_Episode_3_Total_Capsules,
#                Med_2_Episode_3,
#                Med_2_Episode_3_Dose,
#                Med_2_Episode_3_Dose_Frequency,
#                Med_2_Episode_3_Unit_Dose,
#                Med_2_Episode_3_Active_Capsules,
#                Med_2_Episode_3_Placebo_Capsules,
#                Med_2_Episode_3_Total_Capsules,
#                Med_1_Episode_4,
#                Med_1_Episode_4_Dose,
#                Med_1_Episode_4_Dose_Frequency,
#                Med_1_Episode_4_Unit_Dose,
#                Med_1_Episode_4_Active_Capsules,
#                Med_1_Episode_4_Placebo_Capsules,
#                Med_1_Episode_4_Total_Capsules,
#                Med_2_Episode_4,
#                Med_2_Episode_4_Dose,
#                Med_2_Episode_4_Dose_Frequency,
#                Med_2_Episode_4_Unit_Dose,
#                Med_2_Episode_4_Active_Capsules,
#                Med_2_Episode_4_Placebo_Capsules,
#                Med_2_Episode_4_Total_Capsules
#                ]
  
#     return new_row

# def write_to_csv(df, num_file):
#     '''Convert dataframe to .csv file'''
  
#     #Save file:
#     df.to_csv("/Users/dannywitt/Desktop/Opioid_project/Red_cap_data_input/Practice_output_file{}.csv".format(num_file)) 
#     pass

# def Run_Taper(patient_dictionary):
#     #Initialize main pre-df list:
         
#     main_df_dictionary = {}
    
#     #Initialize column names for df:
    
#     columns = ['patient_ID',
#                'month',
#                'patient_last_name',
#                'patient_first_name',
# #               'number_episodes',
# #               'frequency_doses',
#                'med_1', 
#                'total_med_1_24_hr_dose',
#                'total_med_1_24_hr_MME',
#                'med_2',
#                'total_med_2_24_hr_dose',
#                'total_med_2_24_hr_MME',
#                'pre_taper_MME',
#                'post_taper_MME',
#                'percent_MME_decrease',
#                'Med_1_Episode_1',
#                'Med_1_Episode_1_Dose',
#                'Med_1_Episode_1_Dose_Frequency',
#                'Med_1_Episode_1_Unit_Dose',
#                'Med_1_Episode_1_Active_Capsules',
#                'Med_1_Episode_1_Placebo_Capsules',
#                'Med_1_Episode_1_Total_Capsules',
#                'Med_2_Episode_1',
#                'Med_2_Episode_1_Dose',
#                'Med_2_Episode_1_Dose_Frequency',
#                'Med_2_Episode_1_Unit_Dose',
#                'Med_2_Episode_1_Active_Capsules',
#                'Med_2_Episode_1_Placebo_Capsules',
#                'Med_2_Episode_1_Total_Capsules',
#                'Med_1_Episode_2',
#                'Med_1_Episode_2_Dose',
#                'Med_1_Episode_2_Dose_Frequency',
#                'Med_1_Episode_2_Unit_Dose',
#                'Med_1_Episode_2_Active_Capsules',
#                'Med_1_Episode_2_Placebo_Capsules',
#                'Med_1_Episode_2_Total_Capsules',
#                'Med_2_Episode_2',
#                'Med_2_Episode_2_Dose',
#                'Med_2_Episode_2_Dose_Frequency',
#                'Med_2_Episode_2_Unit_Dose',
#                'Med_2_Episode_2_Active_Capsules',
#                'Med_2_Episode_2_Placebo_Capsules',
#                'Med_2_Episode_2_Total_Capsules',
#                'Med_1_Episode_3',
#                'Med_1_Episode_3_Dose',
#                'Med_1_Episode_3_Dose_Frequency',
#                'Med_1_Episode_3_Unit_Dose',
#                'Med_1_Episode_3_Active_Capsules',
#                'Med_1_Episode_3_Placebo_Capsules',
#                'Med_1_Episode_3_Total_Capsules',
#                'Med_2_Episode_3',
#                'Med_2_Episode_3_Dose',
#                'Med_2_Episode_3_Dose_Frequency',
#                'Med_2_Episode_3_Unit_Dose',
#                'Med_2_Episode_3_Active_Capsules',
#                'Med_2_Episode_3_Placebo_Capsules',
#                'Med_2_Episode_3_Total_Capsules',
#                'Med_1_Episode_4',
#                'Med_1_Episode_4_Dose',
#                'Med_1_Episode_4_Dose_Frequency',
#                'Med_1_Episode_4_Unit_Dose',
#                'Med_1_Episode_4_Active_Capsules',
#                'Med_1_Episode_4_Placebo_Capsules',
#                'Med_1_Episode_4_Total_Capsules',
#                'Med_2_Episode_4',
#                'Med_2_Episode_4_Dose',
#                'Med_2_Episode_4_Dose_Frequency',
#                'Med_2_Episode_4_Unit_Dose',
#                'Med_2_Episode_4_Active_Capsules',
#                'Med_2_Episode_4_Placebo_Capsules',
#                'Med_2_Episode_4_Total_Capsules'
#                ]
#     #Run selected patient in dictionary to generate 13 month taper schedule:
    
#     for patient in patient_dictionary:
#         print_all_reports(patient_dictionary[patient])
#         df_patient = pd.DataFrame(patient_dictionary[patient].main_prescription_list)
#         df_patient.transpose()
#         df_patient.columns = columns
#         main_df_dictionary[patient] = df_patient
#         pass
#     return main_df_dictionary

# main_dictionary = Run_Taper(patient_dictionary)

# patient_1_df = main_dictionary['Patient_1']
# patient_2_df = main_dictionary['Patient_2']
# patient_3_df = main_dictionary['Patient_3']

# write_to_csv(patient_1_df, 1)
# write_to_csv(patient_2_df, 2)
# write_to_csv(patient_3_df, 3)

# #def Input_to_dataframe(self,
# #                       list_of_lists,
# #                       patient,
# #                       month):
# #    '''Function that takes final output dictionaries from Prescription object
# #    and writes prescription data to pandas dataframe in a systematic way for each
# #    patient's data
# #    '''
# #    
# #    pass
# #

