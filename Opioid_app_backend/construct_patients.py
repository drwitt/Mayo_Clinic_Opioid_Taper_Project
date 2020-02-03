#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#from Opioid_app_backend.patient_information import Patient

# class Patient_Builder(self, json_payload):
#     """
#     """
#     def __init__(self):
#         self.payload = json_payload
#         self.build_patients()
#         return
#
#     def assign_patient_instance(self, patient_id, json_block):
#         """
#         Harvest data from json payload to build a patient class instance object.
#         """
#         #Make patient class instance:
#         patient = Patient()
#
#         #Assign patient attributes:
#
#         #Assign patient medication class:
#         patient.primary_opioid_med = self.assign_med_class()
#
#         #etc.
#         print('assigning patient instance')
#
#         return
#
#     def assign_med_class(self, opioid_med_string):
#         """Convert opioid medication string name into medication class instance.
#
#         Args:
#           opioid_med_string: a string variable with name of available opioid
#           medication.
#
#         Returns:
#           A medication class object corresponding to the string arg.
#
#         Raises:
#           ValueError: If no available medication string passed as arg.
#
#         """
#         drug_name_to_object_dictionary = {'Hydrocodone Acetaminophen':\
#                                                 Hydrocodone_Acetaminophen(),\
#                                           'Hydromorphone Immediate Release':\
#                                                 Hydromorphone_Immediate_Release(),\
#                                           'Morphine Immediate Release':\
#                                                 Morphine_Immediate_Release(),\
#                                           'Morphine Extended Release':\
#                                                 Morphine_Extended_Release(),\
#                                           'Oxycodone Immediate Release':\
#                                                 Oxycodone_Immediate_Release(),\
#                                           'Oxycodone Extended Release':\
#                                                 Oxycodone_Extended_Release(),\
#                                           'Oxycodone Acetaminophen':\
#                                                 Oxycodone_Acetaminophen(),\
#                                           'Tramadol Immediate Release':\
#                                                 Tramadol_Immediate_Release()
#                                           }
#
#         #Check string is in dictionary keys; if yes, assign string to return class
#         #instance of corresponding medication; if no, assign None value
#
#         if opioid_med_string in list(drug_name_to_object_dictionary.keys()):
#             return drug_name_to_object_dictionary[opioid_med_string]
#         else:
#             return None
#
#     def build_patients(self):
#         patient_list = []
#         for patient_id, info_block in self.payload:
#             patient_obj = self.assign_patient_instance(patient_id, info_block)
#             patient_list.append(patient_obj)
#         print('patients constructed.')
#         return patient_list
#
#     def data_check(self):
#         #Check ingested data:
#         # med_string = input('Enter med name:')
#         # print(type(med_string))
#         #
#         # #Assert opioid_med_string is a string object type:
#         # while True:
#         #     try:
#         #         assert isinstance(med_string, str)
#         #         break
#         #     except TypeError:
#         #         print("Oops!  That was not a valid string.  Try again...")
#         #
#         #
#         # #Assign patient and med class instances:
#         # med_obj = Assign_med_class(med_string)
#         #
#         # print(med_obj)
#         return

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
