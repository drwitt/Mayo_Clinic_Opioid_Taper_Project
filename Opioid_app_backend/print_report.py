#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:29:40 2019

@author: dannywitt
"""
import numpy as np
import pandas as pd

class Print_monthly_report:
    
    def __init__(self, a_unique_patient):
        #Trial Month (0-12 mo.)
        print(a_unique_patient.research_study_timer)
        print('Study ID: {}'.format(a_unique_patient.ID_number))
        #patient first name:
        print('First Name: {}'.format(a_unique_patient.first_name))
        #patient last name:
        print('Last Name: {}'.format(a_unique_patient.last_name))
        
        print(' ')
        
        print('Med 1:')
        print(' ')
        
        if a_unique_patient.primary_opioid_med != None:
            #Med 1:
            print(a_unique_patient.primary_opioid_med.full_drug_name())
            
            #If constant episode dose:
            if a_unique_patient.primary_opioid_episode_dose != None:
                #Dose Med 1:
                print('Dosing: Equal Daily Episode Doses')
                print('Dose: {}mg'.format(a_unique_patient.primary_opioid_episode_dose))
            else:
                pass
            
            #If non-constant episode dose:
            
            if a_unique_patient.different_daily_episode_doses_med_1 == 'Yes':
                #Dose Med 1, Daily Episode 1:
                print('Dosing: Non-constant Daily Episode Doses')
                if a_unique_patient.primary_opioid_dif_dose_episode_dose_1 != None:
                    print('Daily Dose 1: {}mg'.format(a_unique_patient.primary_opioid_dif_dose_episode_dose_1))
                    pass
                else:
                    print('Daily Dose 1 Completely Tapered')
                    pass
                #Dose Med 1, Daiy Episode 2:
                if a_unique_patient.primary_opioid_dif_dose_episode_dose_2 != None:
                    print('Daily Dose 2: {}mg'.format(a_unique_patient.primary_opioid_dif_dose_episode_dose_2))
                    pass
                else:
                    print('Daily Dose 2 Completely Tapered')
                    pass
                #Dose Med 1, Daiy Episode 3:
                if a_unique_patient.primary_opioid_dif_dose_episode_dose_3 != None:
                    print('Daily Dose 3: {}mg'.format(a_unique_patient.primary_opioid_dif_dose_episode_dose_3))
                    pass
                else:
                    print('Daily Dose 3 Completely Tapered')
                    pass
                #Dose Med 1, Daiy Episode 4:
                if a_unique_patient.primary_opioid_dif_dose_episode_dose_3 != None:
                    print('Daily Dose 4: {}mg'.format(a_unique_patient.primary_opioid_dif_dose_episode_dose_4))
                    pass
                else:
                    print('Daily Dose 4 Completely Tapered')
                    pass
                
            #Interdose Time 1:
            print('Dose Freq: Q{}hr'.format(a_unique_patient.primary_opioid_interdose_duration))
            pass
        else:
            print('Either no Primary Med or Completely Tapered')
            print('Total Placebo per Episode: {}'.format(a_unique_patient.primary_opioid_captab_per_episode_dose))
            print('Frequency: {}'.format(a_unique_patient.primary_opioid_interdose_duration))
        
        print(' ')
        
        print('Med 2:')
        print(' ')
        
        #Med 2:
        if a_unique_patient.secondary_opioid_med != None:
            
            print(a_unique_patient.secondary_opioid_med.full_drug_name())
        
            #If constant episode dose:
            if a_unique_patient.secondary_opioid_episode_dose != None:
                print('Dosing: Equal Daily Episode Doses')
                print('Dose: {}mg'.format(a_unique_patient.secondary_opioid_episode_dose))
            
            else:
                pass
            
            #If non-constant episode dose:
            
            if a_unique_patient.different_daily_episode_doses_med_2 == 'Yes':
                print('Dosing: Non-constant Daily Episode Doses')
                #Dose Med 1, Daiy Episode 1:
                if a_unique_patient.secondary_opioid_dif_dose_episode_dose_1 != None:
                    print('Daily Dose 1: {}mg'.format(a_unique_patient.secondary_opioid_dif_dose_episode_dose_1))
                    pass
                else:
                    print('Daily Dose 1 Completely Tapered')
                    pass
                #Dose Med 1, Daiy Episode 2:
                if a_unique_patient.secondary_opioid_dif_dose_episode_dose_2 != None:
                    print('Daily Dose 2: {}mg'.format(a_unique_patient.secondary_opioid_dif_dose_episode_dose_2))
                    pass
                else:
                    print('Daily Dose 2 Completely Tapered')
                    pass
                #Dose Med 1, Daiy Episode 3:
                if a_unique_patient.secondary_opioid_dif_dose_episode_dose_3 != None:
                    print('Daily Dose 3: {}mg'.format(a_unique_patient.secondary_opioid_dif_dose_episode_dose_3))
                    pass
                else:
                    print('Daily Dose 3 Completely Tapered')
                    pass
                #Dose Med 1, Daiy Episode 4:
                if a_unique_patient.secondary_opioid_dif_dose_episode_dose_3 != None:
                    print('Daily Dose 4: {}mg'.format(a_unique_patient.secondary_opioid_dif_dose_episode_dose_4))
                    pass
                else:
                    print('Daily Dose 4 Completely Tapered')
                    pass
                
            #Interdose Time 2:
            print('Dose Freq: Q{}hr'.format(a_unique_patient.secondary_opioid_interdose_duration))
            pass
        else:
            print('Either no Secondary Med or Completely Tapered')
        
        print(' ')
        
#        print('Med 3:')
#        
#        print(' ')
#        if a_unique_patient.tertiary_opioid_med != None:
#            #Med 3:
#            print(a_unique_patient.tertiary_opioid_med.full_drug_name())
#            
#            #If constant episode dose:
#            if a_unique_patient.tertiary_opioid_episode_dose != None:
#                print('Dose: {}mg'.format(a_unique_patient.tertiary_opioid_episode_dose))
#            
#            else:
#                pass
#            
#            #If non-constant episode dose:
#            
#            if a_unique_patient.different_daily_episode_doses_med_3 == 'Yes':
#                #Dose Med 3, Daiy Episode 1:
#                if a_unique_patient.tertiary_opioid_dif_dose_episode_dose_1 != None:
#                    print('Daily Dose 1: {}mg'.format(a_unique_patient.tertiary_opioid_dif_dose_episode_dose_1))
#                    pass
#                else:
#                    print('Daily Dose 1 Completely Tapered')
#                    pass
#                #Dose Med 3, Daiy Episode 2:
#                if a_unique_patient.tertiary_opioid_dif_dose_episode_dose_2 != None:
#                    print('Daily Dose 2: {}mg'.format(a_unique_patient.tertiary_opioid_dif_dose_episode_dose_2))
#                    pass
#                else:
#                    print('Daily Dose 2 Completely Tapered')
#                    pass
#                #Dose Med 3, Daiy Episode 3:
#                if a_unique_patient.tertiary_opioid_dif_dose_episode_dose_3 != None:
#                    print('Daily Dose 3: {}mg'.format(a_unique_patient.tertiary_opioid_dif_dose_episode_dose_3))
#                    pass
#                else:
#                    print('Daily Dose 3 Completely Tapered')
#                    pass
#                #Dose Med 3, Daiy Episode 4:
#                if a_unique_patient.tertiary_opioid_dif_dose_episode_dose_3 != None:
#                    print('Daily Dose 4: {}mg'.format(a_unique_patient.tertiary_opioid_dif_dose_episode_dose_4))
#                    pass
#                else:
#                    print('Daily Dose 4 Completely Tapered')
#                    pass 
#            
#            #Interdose Time 3:
#            print('Dose Freq: Q{}hr'.format(a_unique_patient.tertiary_opioid_interdose_duration))
#            pass
#        else:
#            print('Either No Tertiary or Completely Tapered')
#        
#        print(' ')
        
        print('Total MME = {}'.format(a_unique_patient.Calculate_total_MME_24_hr()))