#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 17:12:47 2019

@author: dannywitt
"""

#Test script:
i = '(10, 10)'
i = i.strip('(').strip(')').replace(' ', '').split(',')
print(i)
i = list(map(float, i))
print(i)
#from medication import (Hydrocodone_Acetaminophen, 
#                        Hydromorphone_Immediate_Release,
#                        Morphine_Immediate_Release,
#                        Morphine_Extended_Release,
#                        Oxycodone_Immediate_Release,
#                        Oxycodone_Extended_Release, 
#                        Oxycodone_Acetaminophen, 
#                        Tramadol_Immediate_Release
#                        )
#
#from patient_information import Patient
#from opioid_dose_taper import Taper
#from prescription import Prescription
#
#a = Patient('101',
#            'Howard',
#            'Schultz')
#
#a.primary_opioid_med = Oxycodone_Acetaminophen()
#a.different_daily_episode_doses_med_1 = 'No'
#a.primary_opioid_interdose_duration = 6

#a.primary_opioid_dif_dose_episode_dose_1 = 5
#a.primary_opioid_dif_dose_episode_dose_2 = 25
#a.primary_opioid_dif_dose_episode_dose_3 = 25
#a.primary_opioid_dif_dose_episode_dose_4 = 5
#a.primary_opioid_dif_dose_captab_per_episode_dose_1 = 1
#a.primary_opioid_dif_dose_captab_per_episode_dose_2 = 3
#a.primary_opioid_dif_dose_captab_per_episode_dose_3 = 3
#a.primary_opioid_dif_dose_captab_per_episode_dose_4 = 1
#a.primary_opioid_dif_dose_ep_1_unit_dose = (5)
#a.primary_opioid_dif_dose_ep_2_unit_dose = (10, 10, 5)
#a.primary_opioid_dif_dose_ep_3_unit_dose = (10, 10, 5)
#a.primary_opioid_dif_dose_ep_4_unit_dose = (5)

#a.primary_opioid_episode_dose = 32.5
#a.primary_opioid_unit_dose = [10, 10, 10, 2.5]
#a.primary_opioid_captab_per_episode_dose = 4
#
#
#
#a.secondary_opioid_med = Hydrocodone_Acetaminophen()
#a.different_daily_episode_doses_med_2 = 'Yes'
#a.secondary_opioid_interdose_duration = 8
#
#a.secondary_opioid_dif_dose_episode_dose_1 = 2.5
#a.secondary_opioid_dif_dose_episode_dose_2 = 0
#a.secondary_opioid_dif_dose_episode_dose_3 = 0
#a.secondary_opioid_dif_dose_episode_dose_4 = 0
#a.secondary_opioid_dif_dose_captab_per_episode_dose_1 = 1
#a.secondary_opioid_dif_dose_captab_per_episode_dose_2 = 1
#a.secondary_opioid_dif_dose_captab_per_episode_dose_3 = 1
#a.secondary_opioid_dif_dose_captab_per_episode_dose_4 = 1
#a.secondary_opioid_dif_dose_ep_1_unit_dose = (2.5)
#a.secondary_opioid_dif_dose_ep_2_unit_dose = None
#a.secondary_opioid_dif_dose_ep_3_unit_dose = None
#a.secondary_opioid_dif_dose_ep_4_unit_dose = None

#a.secondary_opioid_episode_dose = 27.5
#a.secondary_opioid_unit_dose = [10, 10, 5, 2.5]
#a.secondary_opioid_captab_per_episode_dose = 4

##Total MME:
#print('Total MME: {}'.format(a.Calculate_total_MME_24_hr()))
#
##Primary med:
#print('Primary MME: {}'.format(a.Calculate_med_MME_24_hr(a.primary_opioid_med)))
#
##Secondary med:
#print('Secondary MME: {}'.format(a.Calculate_med_MME_24_hr(a.secondary_opioid_med)))
#
##Tertiary med:
#print('Tertiary MME: {}'.format(a.Calculate_med_MME_24_hr(a.tertiary_opioid_med)))
#
##Generate initial Taper object:
#
#taper = Taper(a)
#print('')
#print('Execute taper!')
#print('')
#
##Pre-taper states:
#
################Primary Med:
#print('Primary med in taper object: {}'.format(taper.taper_primary_med.med_name))
#print('Primary med taper dose 24hr: {}'.format(taper.taper_primary_med_dose_24))
#print('Primary med taper MME 24 hr: {}'.format(taper.taper_primary_med_MME_24))
#
#if a.different_daily_episode_doses_med_1 == 'Yes':
#    print('Primary med episode dose 1: {}'.format(taper.taper_primary_med_episode_dose_diff_1))
#    print('Primary med episode dose 2: {}'.format(taper.taper_primary_med_episode_dose_diff_2))
#    print('Primary med episode dose 3: {}'.format(taper.taper_primary_med_episode_dose_diff_3))
#    print('Primary med episode dose 4: {}'.format(taper.taper_primary_med_episode_dose_diff_4))
#    pass
#else:
#    print('Primary med episode dose: {}'.format(taper.taper_primary_med_episode_dose))
#    pass
#
#print('')
##################Secondary Med:
#print('Secondary med in taper object: {}'.format(taper.taper_secondary_med.med_name))
#print('Secondary med taper dose 24hr: {}'.format(taper.taper_secondary_med_dose_24))
#print('Secondary med taper MME 24 hr: {}'.format(taper.taper_secondary_med_MME_24))
#
#if a.different_daily_episode_doses_med_2 == 'Yes':
#    print('Secondary med episode dose 1: {}'.format(taper.taper_secondary_med_episode_dose_diff_1))
#    print('Secondary med episode dose 2: {}'.format(taper.taper_secondary_med_episode_dose_diff_2))
#    print('Secondary med episode dose 3: {}'.format(taper.taper_secondary_med_episode_dose_diff_3))
#    print('Secondary med episode dose 4: {}'.format(taper.taper_secondary_med_episode_dose_diff_4))
#    pass
#else:
#    print('Secondary med episode dose: {}'.format(taper.taper_secondary_med_episode_dose))
#    pass
#
#print('')
##################Tertiary Med:
#print('Tertiary med in taper object: {}'.format(taper.taper_tertiary_med))
#print('Tertiary med taper dose 24hr: {}'.format(taper.taper_tertiary_med_dose_24))
#print('Tertiary med taper MME 24 hr: {}'.format(taper.taper_tertiary_med_MME_24))
#
#if a.different_daily_episode_doses_med_3 == 'Yes':
#    print('Tertiary med episode dose 1: {}'.format(taper.taper_tertiary_med_episode_dose_diff_1))
#    print('Tertiary med episode dose 2: {}'.format(taper.taper_tertiary_med_episode_dose_diff_2))
#    print('Tertiary med episode dose 3: {}'.format(taper.taper_tertiary_med_episode_dose_diff_3))
#    print('Tertiary med episode dose 4: {}'.format(taper.taper_tertiary_med_episode_dose_diff_4))
#    pass
#else:
#    print('Tertiary med episode dose: {}'.format(taper.taper_tertiary_med_episode_dose))
#    pass
#
#print('')
###################Taper Med:
#print('Pre-taper selected taper med: {}'.format(taper.current_taper_med.med_name))
#print('Pre-taper taper med 24 hr dose: {}'.format(taper.current_taper_med_dose_24))
#print('Pre-taper taper med 24 hr MME: {}'.format(taper.current_taper_med_MME_24))
#
##Post-taper states:
#
##If one medication tapered:
#print('')
#if taper.yes_2_meds is True:
#    print('Number of medications involved in taper = 2')
#    pass
#elif taper.yes_2_meds is False:
#    print('Number of medications involved in taper = 1')
#print('')
#
##Current taper med specific
#print('Post-taper selected med: {}'.format(taper.current_taper_med.med_name))
#if taper.yes_2_meds is False:
#    print('Post taper ideal 24 hr dose: {}'.format(taper.post_taper_dose_24))
#    print('Post taper ideal 24 hr dose reduction: {}'.format(taper.post_taper_dose_reduction_over_24))
#    print('Post taper ideal 24 hr MME: {}'.format(taper.post_taper_med_MME_24))
#    pass
#elif taper.yes_2_meds is True:
#    print('Pre taper 24 hr dose Tmed 1: {}'.format(taper.pre_taper_dose_24_med_1))
#    print('Pre taper 24 hr dose Tmed 2: {}'.format(taper.pre_taper_dose_24_med_2))
#    print('Post taper 24 hr dose Tmed 1: {}'.format(taper.post_taper_dose_24_med_1))
#    print('Post taper 24 hr dose Tmed 2: {}'.format(taper.post_taper_dose_24_med_2))
#    pass
#else:
#    pass
#
#
#print('Post taper ideal total MME difference: {}'.format(taper.total_taper_MME_difference))
#
##Other relevant post-taper variables/information:
#print('Two meds tapered?: {}'.format(taper.yes_2_meds))
#print('Non-taper drugs: {}'.format(taper.non_taper_med_list))
#
#
###############################################################################
##Prescription Object:
#
#prescript = Prescription(a, taper)
#prescript
#
#if a.primary_opioid_med != None:
#    #Primary med information:
#    print(a.primary_opioid_med.med_name)
#    print(a.Primary_total_dose_per_24_hr())
#    print('Primary MME: {}'.format(a.Calculate_med_MME_24_hr(a.primary_opioid_med)))
#    print(a.primary_opioid_interdose_duration)
#    
#    #Constant episode dose:
#    
#    if a.different_daily_episode_doses_med_1 != 'Yes':
#        print(a.primary_opioid_episode_dose)
#        print(a.primary_opioid_unit_dose)
#        print(a.primary_opioid_captab_per_episode_dose)
#    
#        pass
#    else:
#        pass
#    #Nonconstant episode dose:
#        
#    if a.different_daily_episode_doses_med_1 == 'Yes':
#        print(a.primary_opioid_dif_dose_episode_dose_1)
#        print(a.primary_opioid_dif_dose_ep_1_unit_dose)
#        print(a.primary_opioid_dif_dose_captab_per_episode_dose_1)
#        print(a.primary_opioid_dif_dose_episode_dose_2)
#        print(a.primary_opioid_dif_dose_ep_2_unit_dose)
#        print(a.primary_opioid_dif_dose_captab_per_episode_dose_2)
#        print(a.primary_opioid_dif_dose_episode_dose_3)
#        print(a.primary_opioid_dif_dose_ep_3_unit_dose)
#        print(a.primary_opioid_dif_dose_captab_per_episode_dose_3)
#        print(a.primary_opioid_dif_dose_episode_dose_4)
#        print(a.primary_opioid_dif_dose_ep_4_unit_dose)
#        print(a.primary_opioid_dif_dose_captab_per_episode_dose_4)
#        pass
#    else:
#        pass
#    pass
#else:
#    pass
###############################################################################
##Secondary med information:
# 
#if a.secondary_opioid_med != None:
#    print(a.secondary_opioid_med.med_name)
#    print(a.Secondary_total_dose_per_24_hr())
#    print('Secondary MME: {}'.format(a.Calculate_med_MME_24_hr(a.secondary_opioid_med)))
#    
#    #Constant episode dose:
#    
#    if a.different_daily_episode_doses_med_2 != 'Yes':
#        print('Secondary med (constant) episode dose: {}'.format(a.secondary_opioid_episode_dose))
#        print('Secondary med (constant) unit dose: {}'.format(a.secondary_opioid_unit_dose))
#        print('Secondary med (constant) captab per episode dose: {}'.format(a.secondary_opioid_captab_per_episode_dose))
#    
#        pass
#    else:
#        pass
#    #Nonconstant episode dose:
#        
#    if a.different_daily_episode_doses_med_2 == 'Yes':
#        print('Secondary med (nonconstant) episode dose 1: {}'.format(a.secondary_opioid_dif_dose_episode_dose_1))
#        print('Secondary med (nonconstant) episode 1 unit dose: {}'.format(a.secondary_opioid_dif_dose_ep_1_unit_dose))
#        print('Secondary med (nonconstant) episode 1 captabs: {}'.format(a.secondary_opioid_dif_dose_captab_per_episode_dose_1))
#        print('Secondary med (nonconstant) episode dose 2: {}'.format(a.secondary_opioid_dif_dose_episode_dose_2))
#        print('Secondary med (nonconstant) episode 2 unit dose: {}'.format(a.secondary_opioid_dif_dose_ep_2_unit_dose))
#        print('Secondary med (nonconstant) episode 2 captabs: {}'.format(a.secondary_opioid_dif_dose_captab_per_episode_dose_2))
#        print('Secondary med (nonconstant) episode dose 3: {}'.format(a.secondary_opioid_dif_dose_episode_dose_3))
#        print('Secondary med (nonconstant) episode 3 unit dose: {}'.format(a.secondary_opioid_dif_dose_ep_3_unit_dose))
#        print('Secondary med (nonconstant) episode 3 captabs: {}'.format(a.secondary_opioid_dif_dose_captab_per_episode_dose_3))
#        print('Secondary med (nonconstant) episode dose 4: {}'.format(a.secondary_opioid_dif_dose_episode_dose_4))
#        print('Secondary med (nonconstant) episode 4 unit dose: {}'.format(a.secondary_opioid_dif_dose_ep_4_unit_dose))
#        print('Secondary med (nonconstant) episode 4 captabs: {}'.format(a.secondary_opioid_dif_dose_captab_per_episode_dose_4))
#        pass
#    else:
#        pass
#    pass
#else:
#    pass
#
#
###############################################################################
##Tertiary med information:
#
#if a.tertiary_opioid_med != None:
#    print('Tertiary med name:'.format(a.tertiary_opioid_med.med_name))
#    print('Tertiary med dose 24 hr: {}'.format(a.tertiary_total_dose_per_24_hr()))
#    print('Tertiary MME: {}'.format(a.Calculate_med_MME_24_hr(a.tertiary_opioid_med)))
#
#    #Constant episode dose:
#    
#    if a.different_daily_episode_doses_med_3 != 'Yes':
#        print('Tertiary med (constant) episode dose: {}'.format(a.tertiary_opioid_episode_dose))
#        print('Tertiary med (constant) unit dose: {}'.format(a.tertiary_opioid_unit_dose))
#        print('Tertiary med (constant) captabs: {}'.format(a.tertiary_opioid_captab_per_episode_dose))
#    
#        pass
#    else:
#        pass
#    #Nonconstant episode dose:
#        
#    if a.different_daily_episode_doses_med_3 == 'Yes':
#        print(a.tertiary_opioid_dif_dose_episode_dose_1)
#        print(a.tertiary_opioid_dif_dose_ep_1_unit_dose)
#        print(a.tertiary_opioid_dif_dose_captab_per_episode_dose_1)
#        print(a.tertiary_opioid_dif_dose_episode_dose_2)
#        print(a.tertiary_opioid_dif_dose_ep_2_unit_dose)
#        print(a.tertiary_opioid_dif_dose_captab_per_episode_dose_2)
#        print(a.tertiary_opioid_dif_dose_episode_dose_3)
#        print(a.tertiary_opioid_dif_dose_ep_3_unit_dose)
#        print(a.tertiary_opioid_dif_dose_captab_per_episode_dose_3)
#        print(a.tertiary_opioid_dif_dose_episode_dose_4)
#        print(a.tertiary_opioid_dif_dose_ep_4_unit_dose)
#        print(a.tertiary_opioid_dif_dose_captab_per_episode_dose_4)
#        pass
#    else:
#        pass
#    pass
#else:
#    pass