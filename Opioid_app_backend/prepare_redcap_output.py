#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 10:51:00 2020

@author: dannywitt
"""

def Generate_first_patient_month_list(patient):

    patient_ID_number = patient.ID_number
    redcap_event_name = 'month_1_arm_1'
    patient_last_name = patient.last_name
    patient_first_name = patient.first_name
    med_1 = patient.primary_opioid_med_name
    total_med_1_24_hr_dose = patient.Primary_total_dose_per_24_hr()
    total_med_1_24_hr_MME = patient.Calculate_med_MME_24_hr(patient.primary_opioid_med)
    med_2 = patient.secondary_opioid_med_name
    total_med_2_24_hr_dose = patient.Secondary_total_dose_per_24_hr()
    total_med_2_24_hr_MME = patient.Calculate_med_MME_24_hr(patient.secondary_opioid_med)
    if total_med_2_24_hr_MME == None:
        pre_taper_mme = total_med_1_24_hr_MME
    elif total_med_2_24_hr_MME != None:
        pre_taper_mme = total_med_1_24_hr_MME + total_med_2_24_hr_MME
    total_mme = pre_taper_mme
    percent_mme_decrease = 0

    #PRIMARY MED FIRST:

    if patient.primary_opioid_med != None:

        #Episode 1:

        #Primary Med:
        if patient.different_daily_episode_doses_med_1 == 'Yes':
            Med_1_Episode_1 = patient.primary_opioid_med_name
            Med_1_Episode_1_Dose = patient.primary_opioid_dif_dose_episode_dose_1
            Med_1_Episode_1_Dose_Frequency = patient.primary_opioid_interdose_duration
            Med_1_Episode_1_Unit_Dose = str(patient.primary_opioid_dif_dose_ep_1_unit_dose)
            Med_1_Episode_1_Active_Capsules = patient.primary_opioid_dif_dose_captab_per_episode_dose_1
            Med_1_Episode_1_Placebo_Capsules = 0
            Med_1_Episode_1_Total_Capsules = patient.primary_opioid_dif_dose_captab_per_episode_dose_1
            pass
        elif patient.different_daily_episode_doses_med_1 != 'Yes':
            Med_1_Episode_1 = patient.primary_opioid_med_name
            Med_1_Episode_1_Dose = patient.primary_opioid_episode_dose
            Med_1_Episode_1_Dose_Frequency = patient.primary_opioid_interdose_duration
            Med_1_Episode_1_Unit_Dose = str(patient.primary_opioid_unit_dose)
            Med_1_Episode_1_Active_Capsules = patient.primary_opioid_captab_per_episode_dose
            Med_1_Episode_1_Placebo_Capsules = 0
            Med_1_Episode_1_Total_Capsules = patient.primary_opioid_captab_per_episode_dose
            pass
        else:
            pass

        if patient.primary_opioid_interdose_duration <= 12:
            #Episode 2:

            #Primary Med:
            if patient.different_daily_episode_doses_med_1 == 'Yes':
                  Med_1_Episode_2 = patient.primary_opioid_med_name
                  Med_1_Episode_2_Dose = patient.primary_opioid_dif_dose_episode_dose_2
                  Med_1_Episode_2_Dose_Frequency = patient.primary_opioid_interdose_duration
                  Med_1_Episode_2_Unit_Dose = str(patient.primary_opioid_dif_dose_ep_2_unit_dose)
                  Med_1_Episode_2_Active_Capsules = patient.primary_opioid_dif_dose_captab_per_episode_dose_2
                  Med_1_Episode_2_Placebo_Capsules = 0
                  Med_1_Episode_2_Total_Capsules = patient.primary_opioid_dif_dose_captab_per_episode_dose_2
                  pass
            elif patient.different_daily_episode_doses_med_1 != 'Yes':
                Med_1_Episode_2 = patient.primary_opioid_med_name
                Med_1_Episode_2_Dose = patient.primary_opioid_episode_dose
                Med_1_Episode_2_Dose_Frequency = patient.primary_opioid_interdose_duration
                Med_1_Episode_2_Unit_Dose = str(patient.primary_opioid_unit_dose)
                Med_1_Episode_2_Active_Capsules = patient.primary_opioid_captab_per_episode_dose
                Med_1_Episode_2_Placebo_Capsules = 0
                Med_1_Episode_2_Total_Capsules = patient.primary_opioid_captab_per_episode_dose
                pass
            else:
                pass
            pass
        else:
            Med_1_Episode_2 = None
            Med_1_Episode_2_Dose = None
            Med_1_Episode_2_Dose_Frequency = None
            Med_1_Episode_2_Unit_Dose = None
            Med_1_Episode_2_Active_Capsules = None
            Med_1_Episode_2_Placebo_Capsules = None
            Med_1_Episode_2_Total_Capsules = None
            pass

        if patient.primary_opioid_interdose_duration <= 8:
            #Episode 3:

            #Primary Med:
            if patient.different_daily_episode_doses_med_1 == 'Yes':
                  Med_1_Episode_3 = patient.primary_opioid_med_name
                  Med_1_Episode_3_Dose = patient.primary_opioid_dif_dose_episode_dose_3
                  Med_1_Episode_3_Dose_Frequency = patient.primary_opioid_interdose_duration
                  Med_1_Episode_3_Unit_Dose = str(patient.primary_opioid_dif_dose_ep_3_unit_dose)
                  Med_1_Episode_3_Active_Capsules = patient.primary_opioid_dif_dose_captab_per_episode_dose_3
                  Med_1_Episode_3_Placebo_Capsules = 0
                  Med_1_Episode_3_Total_Capsules = patient.primary_opioid_dif_dose_captab_per_episode_dose_3
                  pass
            elif patient.different_daily_episode_doses_med_1 != 'Yes':
                Med_1_Episode_3 = patient.primary_opioid_med_name
                Med_1_Episode_3_Dose = patient.primary_opioid_episode_dose
                Med_1_Episode_3_Dose_Frequency = patient.primary_opioid_interdose_duration
                Med_1_Episode_3_Unit_Dose = str(patient.primary_opioid_unit_dose)
                Med_1_Episode_3_Active_Capsules = patient.primary_opioid_captab_per_episode_dose
                Med_1_Episode_3_Placebo_Capsules = 0
                Med_1_Episode_3_Total_Capsules = patient.primary_opioid_captab_per_episode_dose
                pass
            else:
                pass
            pass
        else:
            Med_1_Episode_3 = None
            Med_1_Episode_3_Dose = None
            Med_1_Episode_3_Dose_Frequency = None
            Med_1_Episode_3_Unit_Dose = None
            Med_1_Episode_3_Active_Capsules = None
            Med_1_Episode_3_Placebo_Capsules = None
            Med_1_Episode_3_Total_Capsules = None
            pass

        if patient.primary_opioid_interdose_duration <= 6:
            #Episode 4:

            #Primary Med:
            if patient.different_daily_episode_doses_med_1 == 'Yes':
                  Med_1_Episode_4 = patient.primary_opioid_med_name
                  Med_1_Episode_4_Dose = patient.primary_opioid_dif_dose_episode_dose_4
                  Med_1_Episode_4_Dose_Frequency = patient.primary_opioid_interdose_duration
                  Med_1_Episode_4_Unit_Dose = str(patient.primary_opioid_dif_dose_ep_4_unit_dose)
                  Med_1_Episode_4_Active_Capsules = patient.primary_opioid_dif_dose_captab_per_episode_dose_4
                  Med_1_Episode_4_Placebo_Capsules = 0
                  Med_1_Episode_4_Total_Capsules = patient.primary_opioid_dif_dose_captab_per_episode_dose_4
                  pass
            elif patient.different_daily_episode_doses_med_1 != 'Yes':
                Med_1_Episode_4 = patient.primary_opioid_med_name
                Med_1_Episode_4_Dose = patient.primary_opioid_episode_dose
                Med_1_Episode_4_Dose_Frequency = patient.primary_opioid_interdose_duration
                Med_1_Episode_4_Unit_Dose = str(patient.primary_opioid_unit_dose)
                Med_1_Episode_4_Active_Capsules = patient.primary_opioid_captab_per_episode_dose
                Med_1_Episode_4_Placebo_Capsules = 0
                Med_1_Episode_4_Total_Capsules = patient.primary_opioid_captab_per_episode_dose
                pass
            else:
                pass
            pass
        else:
            Med_1_Episode_4 = None
            Med_1_Episode_4_Dose = None
            Med_1_Episode_4_Dose_Frequency = None
            Med_1_Episode_4_Unit_Dose = None
            Med_1_Episode_4_Active_Capsules = None
            Med_1_Episode_4_Placebo_Capsules = None
            Med_1_Episode_4_Total_Capsules = None
            pass
        pass

    else:
          Med_1_Episode_1 = None
          Med_1_Episode_1_Dose = None
          Med_1_Episode_1_Dose_Frequency = None
          Med_1_Episode_1_Unit_Dose = None
          Med_1_Episode_1_Active_Capsules = None
          Med_1_Episode_1_Placebo_Capsules = None
          Med_1_Episode_1_Total_Capsules = None
          Med_1_Episode_2 = None
          Med_1_Episode_2_Dose = None
          Med_1_Episode_2_Dose_Frequency = None
          Med_1_Episode_2_Unit_Dose = None
          Med_1_Episode_2_Active_Capsules = None
          Med_1_Episode_2_Placebo_Capsules = None
          Med_1_Episode_2_Total_Capsules = None
          Med_1_Episode_3 = None
          Med_1_Episode_3_Dose = None
          Med_1_Episode_3_Dose_Frequency = None
          Med_1_Episode_3_Unit_Dose = None
          Med_1_Episode_3_Active_Capsules = None
          Med_1_Episode_3_Placebo_Capsules = None
          Med_1_Episode_3_Total_Capsules = None
          Med_1_Episode_4 = None
          Med_1_Episode_4_Dose = None
          Med_1_Episode_4_Dose_Frequency = None
          Med_1_Episode_4_Unit_Dose = None
          Med_1_Episode_4_Active_Capsules = None
          Med_1_Episode_4_Placebo_Capsules = None
          Med_1_Episode_4_Total_Capsules = None
          pass

    #NEXT, SECONDARY MED:

    if patient.secondary_opioid_med != None:
        #Secondary Med:
        if patient.different_daily_episode_doses_med_2 == 'Yes':
              Med_2_Episode_1 = patient.secondary_opioid_med_name
              Med_2_Episode_1_Dose = patient.secondary_opioid_dif_dose_episode_dose_1
              Med_2_Episode_1_Dose_Frequency = patient.secondary_opioid_interdose_duration
              Med_2_Episode_1_Unit_Dose = str(patient.secondary_opioid_dif_dose_ep_1_unit_dose)
              Med_2_Episode_1_Active_Capsules = patient.secondary_opioid_dif_dose_captab_per_episode_dose_1
              Med_2_Episode_1_Placebo_Capsules = 0
              Med_2_Episode_1_Total_Capsules = patient.secondary_opioid_dif_dose_captab_per_episode_dose_1
              pass
        elif patient.different_daily_episode_doses_med_2 != 'Yes':
            Med_2_Episode_1 = patient.secondary_opioid_med_name
            Med_2_Episode_1_Dose = patient.secondary_opioid_episode_dose
            Med_2_Episode_1_Dose_Frequency = patient.secondary_opioid_interdose_duration
            Med_2_Episode_1_Unit_Dose = str(patient.secondary_opioid_unit_dose)
            Med_2_Episode_1_Active_Capsules = patient.secondary_opioid_captab_per_episode_dose
            Med_2_Episode_1_Placebo_Capsules = 0
            Med_2_Episode_1_Total_Capsules = patient.secondary_opioid_captab_per_episode_dose
            pass
        else:
            pass

        if patient.secondary_opioid_interdose_duration <= 12:
            #Episode 2


            #Secondary Med:
            if patient.different_daily_episode_doses_med_2 == 'Yes':
                  Med_2_Episode_2 = patient.secondary_opioid_med_name
                  Med_2_Episode_2_Dose = patient.secondary_opioid_dif_dose_episode_dose_2
                  Med_2_Episode_2_Dose_Frequency = patient.secondary_opioid_interdose_duration
                  Med_2_Episode_2_Unit_Dose = str(patient.secondary_opioid_dif_dose_ep_2_unit_dose)
                  Med_2_Episode_2_Active_Capsules = patient.secondary_opioid_dif_dose_captab_per_episode_dose_2
                  Med_2_Episode_2_Placebo_Capsules = 0
                  Med_2_Episode_2_Total_Capsules = patient.secondary_opioid_dif_dose_captab_per_episode_dose_2
                  pass
            elif patient.different_daily_episode_doses_med_2 != 'Yes':
                Med_2_Episode_2 = patient.secondary_opioid_med_name
                Med_2_Episode_2_Dose = patient.secondary_opioid_episode_dose
                Med_2_Episode_2_Dose_Frequency = patient.secondary_opioid_interdose_duration
                Med_2_Episode_2_Unit_Dose = str(patient.secondary_opioid_unit_dose)
                Med_2_Episode_2_Active_Capsules = patient.secondary_opioid_captab_per_episode_dose
                Med_2_Episode_2_Placebo_Capsules = 0
                Med_2_Episode_2_Total_Capsules = patient.secondary_opioid_captab_per_episode_dose
                pass
            else:
                pass
            pass
        else:
            Med_2_Episode_2 = None
            Med_2_Episode_2_Dose = None
            Med_2_Episode_2_Dose_Frequency = None
            Med_2_Episode_2_Unit_Dose = None
            Med_2_Episode_2_Active_Capsules = None
            Med_2_Episode_2_Placebo_Capsules = None
            Med_2_Episode_2_Total_Capsules = None
            pass

        if patient.secondary_opioid_interdose_duration <= 8:
            #Episode 3

            #Secondary Med:
            if patient.different_daily_episode_doses_med_2 == 'Yes':
                  Med_2_Episode_3 = patient.secondary_opioid_med_name
                  Med_2_Episode_3_Dose = patient.secondary_opioid_dif_dose_episode_dose_3
                  Med_2_Episode_3_Dose_Frequency = patient.secondary_opioid_interdose_duration
                  Med_2_Episode_3_Unit_Dose = str(patient.secondary_opioid_dif_dose_ep_3_unit_dose)
                  Med_2_Episode_3_Active_Capsules = patient.secondary_opioid_dif_dose_captab_per_episode_dose_3
                  Med_2_Episode_3_Placebo_Capsules = 0
                  Med_2_Episode_3_Total_Capsules = patient.secondary_opioid_dif_dose_captab_per_episode_dose_3
                  pass
            elif patient.different_daily_episode_doses_med_2 != 'Yes':
                Med_2_Episode_3 = patient.secondary_opioid_med_name
                Med_2_Episode_3_Dose = patient.secondary_opioid_episode_dose
                Med_2_Episode_3_Dose_Frequency = patient.secondary_opioid_interdose_duration
                Med_2_Episode_3_Unit_Dose = str(patient.secondary_opioid_unit_dose)
                Med_2_Episode_3_Active_Capsules = patient.secondary_opioid_captab_per_episode_dose
                Med_2_Episode_3_Placebo_Capsules = 0
                Med_2_Episode_3_Total_Capsules = patient.secondary_opioid_captab_per_episode_dose
                pass
            else:
                pass
            pass
        else:
            Med_2_Episode_3 = None
            Med_2_Episode_3_Dose = None
            Med_2_Episode_3_Dose_Frequency = None
            Med_2_Episode_3_Unit_Dose = None
            Med_2_Episode_3_Active_Capsules = None
            Med_2_Episode_3_Placebo_Capsules = None
            Med_2_Episode_3_Total_Capsules = None
            pass

        if patient.secondary_opioid_interdose_duration <= 6:
            #Episode 4

            #Secondary Med:
            if patient.different_daily_episode_doses_med_2 == 'Yes':
                  Med_2_Episode_4 = patient.secondary_opioid_med_name
                  Med_2_Episode_4_Dose = patient.secondary_opioid_dif_dose_episode_dose_4
                  Med_2_Episode_4_Dose_Frequency = patient.secondary_opioid_interdose_duration
                  Med_2_Episode_4_Unit_Dose = str(patient.secondary_opioid_dif_dose_ep_4_unit_dose)
                  Med_2_Episode_4_Active_Capsules = patient.secondary_opioid_dif_dose_captab_per_episode_dose_4
                  Med_2_Episode_4_Placebo_Capsules = 0
                  Med_2_Episode_4_Total_Capsules = patient.secondary_opioid_dif_dose_captab_per_episode_dose_4
                  pass
            elif patient.different_daily_episode_doses_med_2 != 'Yes':
                Med_2_Episode_4 = patient.secondary_opioid_med_name
                Med_2_Episode_4_Dose = patient.secondary_opioid_episode_dose
                Med_2_Episode_4_Dose_Frequency = patient.secondary_opioid_interdose_duration
                Med_2_Episode_4_Unit_Dose = str(patient.secondary_opioid_unit_dose)
                Med_2_Episode_4_Active_Capsules = patient.secondary_opioid_captab_per_episode_dose
                Med_2_Episode_4_Placebo_Capsules = 0
                Med_2_Episode_4_Total_Capsules = patient.secondary_opioid_captab_per_episode_dose
                pass
            else:
                pass
            pass
        else:
            Med_2_Episode_4 = None
            Med_2_Episode_4_Dose = None
            Med_2_Episode_4_Dose_Frequency = None
            Med_2_Episode_4_Unit_Dose = None
            Med_2_Episode_4_Active_Capsules = None
            Med_2_Episode_4_Placebo_Capsules = None
            Med_2_Episode_4_Total_Capsules = None
            pass
        pass

    else:
          Med_2_Episode_1 = None
          Med_2_Episode_1_Dose = None
          Med_2_Episode_1_Dose_Frequency = None
          Med_2_Episode_1_Unit_Dose = None
          Med_2_Episode_1_Active_Capsules = None
          Med_2_Episode_1_Placebo_Capsules = None
          Med_2_Episode_1_Total_Capsules = None
          Med_2_Episode_2 = None
          Med_2_Episode_2_Dose = None
          Med_2_Episode_2_Dose_Frequency = None
          Med_2_Episode_2_Unit_Dose = None
          Med_2_Episode_2_Active_Capsules = None
          Med_2_Episode_2_Placebo_Capsules = None
          Med_2_Episode_2_Total_Capsules = None
          Med_2_Episode_3 = None
          Med_2_Episode_3_Dose = None
          Med_2_Episode_3_Dose_Frequency = None
          Med_2_Episode_3_Unit_Dose = None
          Med_2_Episode_3_Active_Capsules = None
          Med_2_Episode_3_Placebo_Capsules = None
          Med_2_Episode_3_Total_Capsules = None
          Med_2_Episode_4 = None
          Med_2_Episode_4_Dose = None
          Med_2_Episode_4_Dose_Frequency = None
          Med_2_Episode_4_Unit_Dose = None
          Med_2_Episode_4_Active_Capsules = None
          Med_2_Episode_4_Placebo_Capsules = None
          Med_2_Episode_4_Total_Capsules = None
          pass

    new_first_row =[patient_ID_number,
                    redcap_event_name,
                    patient_first_name,
                    patient_last_name,
                    med_1,
                    total_med_1_24_hr_dose,
                    total_med_1_24_hr_MME,
                    med_2,
                    total_med_2_24_hr_dose,
                    total_med_2_24_hr_MME,
                    pre_taper_mme,
                    total_mme,
                    percent_mme_decrease,
                    Med_1_Episode_1,
                    Med_1_Episode_1_Dose,
                    Med_1_Episode_1_Dose_Frequency,
                    Med_1_Episode_1_Unit_Dose,
                    Med_1_Episode_1_Active_Capsules,
                    Med_1_Episode_1_Placebo_Capsules,
                    Med_1_Episode_1_Total_Capsules,
                    Med_2_Episode_1,
                    Med_2_Episode_1_Dose,
                    Med_2_Episode_1_Dose_Frequency,
                    Med_2_Episode_1_Unit_Dose,
                    Med_2_Episode_1_Active_Capsules,
                    Med_2_Episode_1_Placebo_Capsules,
                    Med_2_Episode_1_Total_Capsules,
                    Med_1_Episode_2,
                    Med_1_Episode_2_Dose,
                    Med_1_Episode_2_Dose_Frequency,
                    Med_1_Episode_2_Unit_Dose,
                    Med_1_Episode_2_Active_Capsules,
                    Med_1_Episode_2_Placebo_Capsules,
                    Med_1_Episode_2_Total_Capsules,
                    Med_2_Episode_2,
                    Med_2_Episode_2_Dose,
                    Med_2_Episode_2_Dose_Frequency,
                    Med_2_Episode_2_Unit_Dose,
                    Med_2_Episode_2_Active_Capsules,
                    Med_2_Episode_2_Placebo_Capsules,
                    Med_2_Episode_2_Total_Capsules,
                    Med_1_Episode_3,
                    Med_1_Episode_3_Dose,
                    Med_1_Episode_3_Dose_Frequency,
                    Med_1_Episode_3_Unit_Dose,
                    Med_1_Episode_3_Active_Capsules,
                    Med_1_Episode_3_Placebo_Capsules,
                    Med_1_Episode_3_Total_Capsules,
                    Med_2_Episode_3,
                    Med_2_Episode_3_Dose,
                    Med_2_Episode_3_Dose_Frequency,
                    Med_2_Episode_3_Unit_Dose,
                    Med_2_Episode_3_Active_Capsules,
                    Med_2_Episode_3_Placebo_Capsules,
                    Med_2_Episode_3_Total_Capsules,
                    Med_1_Episode_4,
                    Med_1_Episode_4_Dose,
                    Med_1_Episode_4_Dose_Frequency,
                    Med_1_Episode_4_Unit_Dose,
                    Med_1_Episode_4_Active_Capsules,
                    Med_1_Episode_4_Placebo_Capsules,
                    Med_1_Episode_4_Total_Capsules,
                    Med_2_Episode_4,
                    Med_2_Episode_4_Dose,
                    Med_2_Episode_4_Dose_Frequency,
                    Med_2_Episode_4_Unit_Dose,
                    Med_2_Episode_4_Active_Capsules,
                    Med_2_Episode_4_Placebo_Capsules,
                    Med_2_Episode_4_Total_Capsules
                    ]

    return new_first_row

def Generate_patient_month_list(patient,
                                month,
                                prescription_object):
    #Assign event name:
    redcap_event_name = 'month_{}_arm_1'.format(month)
    
    #Assign variables:
    patient_ID_number = patient.ID_number
    patient_last_name = patient.last_name
    patient_first_name = patient.first_name
    med_1 = patient.primary_opioid_med_name
    total_med_1_24_hr_dose = prescription_object.aggregate_primary_med['Total Primary Med 24hr Dose']
    total_med_1_24_hr_MME = prescription_object.aggregate_primary_med['Total Primary Med 24hr MME']
    med_2 = patient.secondary_opioid_med_name
    total_med_2_24_hr_dose = prescription_object.aggregate_secondary_med['Total Secondary Med 24hr Dose']
    total_med_2_24_hr_MME = prescription_object.aggregate_secondary_med['Total Secondary Med 24hr MME']
    pre_taper_mme = prescription_object.ideal_vs_actual_MME_calculations['Pre-taper total MME']
    #post_taper_ideal_mme = prescription_object.ideal_vs_actual_MME_calculations['Post-taper ideal total MME']
    total_mme = prescription_object.aggregate_all_med['Total All Med 24hr MME']
    percent_mme_decrease = prescription_object.ideal_vs_actual_MME_calculations['Actual percent MME decrease']

    #All episode dictionary:
    all_episode_dictionary = prescription_object.actual_episodes

    #Number of dose episodes in 24 hr:
    #number_episodes = prescription_object.number_episodes

    #Frequency of Dose Episodes:
    #frequency_doses = prescription_object.aggregate_interdose_duration

    ######################## EPISODE 1 ########################################
    #Episode 1:
    Episode_1 = all_episode_dictionary['Episode 1']

    #Primary Med Episode 1:
    Primary_Med_Episode_1 = Episode_1['Primary Opioid Med Episode 1']

    #Med 1 name:
    Med_1_Episode_1 = Primary_Med_Episode_1['Primary Med Name']

    #Med 1 episode dose:
    Med_1_Episode_1_Dose = Primary_Med_Episode_1['Primary Med Episode Dose 1']

    #Med 1 dose frequency:
    Med_1_Episode_1_Dose_Frequency = patient.primary_opioid_interdose_duration

    #Med 1 unit dose:
    Med_1_Episode_1_Unit_Dose = str(Primary_Med_Episode_1['Primary Med Episode Unit Dose 1'])

    #Med 1 active capsules:
    Med_1_Episode_1_Active_Capsules = Primary_Med_Episode_1['Primary Med Active Capsules Episode 1']

    #Med 1 placebo capsules:
    Med_1_Episode_1_Placebo_Capsules = Primary_Med_Episode_1['Primary Med Placebo Capsules Episode 1']

    #Med 1 total capsules:
    Med_1_Episode_1_Total_Capsules = Primary_Med_Episode_1['Primary Med Total Capsules Episode 1']

    #Primary Med Episode 1:
    Secondary_Med_Episode_1 = Episode_1['Secondary Opioid Med Episode 1']

    #Med 2 name:
    Med_2_Episode_1 = Secondary_Med_Episode_1['Secondary Med Name']

    #Med 2 episode dose:
    Med_2_Episode_1_Dose = Secondary_Med_Episode_1['Secondary Med Episode Dose 1']

    #Med 2 dose frequency:
    Med_2_Episode_1_Dose_Frequency = patient.secondary_opioid_interdose_duration

    #Med 2 unit dose:
    Med_2_Episode_1_Unit_Dose = str(Secondary_Med_Episode_1['Secondary Med Episode Unit Dose 1'])

    #Med 2 active capsules:
    Med_2_Episode_1_Active_Capsules = Secondary_Med_Episode_1['Secondary Med Active Capsules Episode 1']

    #Med 2 placebo capsules:
    Med_2_Episode_1_Placebo_Capsules = Secondary_Med_Episode_1['Secondary Med Placebo Capsules Episode 1']

    #Med 2 total capsules:
    Med_2_Episode_1_Total_Capsules = Secondary_Med_Episode_1['Secondary Med Total Capsules Episode 1']

    ######################## EPISODE 2 ########################################

    #Episode 2:
    Episode_2 = all_episode_dictionary['Episode 2']

    #Primary Med Episode 2:
    Primary_Med_Episode_2 = Episode_2['Primary Opioid Med Episode 2']

    #Med 1 name:
    Med_1_Episode_2 = Primary_Med_Episode_2['Primary Med Name']

    #Med 1 episode dose:
    Med_1_Episode_2_Dose = Primary_Med_Episode_2['Primary Med Episode Dose 2']

    #Med 1 dose frequency:
    Med_1_Episode_2_Dose_Frequency = patient.primary_opioid_interdose_duration

    #Med 1 unit dose:
    Med_1_Episode_2_Unit_Dose = str(Primary_Med_Episode_2['Primary Med Episode Unit Dose 2'])

    #Med 1 active capsules:
    Med_1_Episode_2_Active_Capsules = Primary_Med_Episode_2['Primary Med Active Capsules Episode 2']

    #Med 1 placebo capsules:
    Med_1_Episode_2_Placebo_Capsules = Primary_Med_Episode_2['Primary Med Placebo Capsules Episode 2']

    #Med 1 total capsules:
    Med_1_Episode_2_Total_Capsules = Primary_Med_Episode_2['Primary Med Total Capsules Episode 2']
    
    if Episode_2['Secondary Opioid Med Episode 2'] != None:
        
        #Secondary Med Episode 2:
        Secondary_Med_Episode_2 = Episode_2['Secondary Opioid Med Episode 2']
    
        #Med 2 name:
        Med_2_Episode_2 = Secondary_Med_Episode_2['Secondary Med Name']
    
        #Med 2 episode dose:
        Med_2_Episode_2_Dose = Secondary_Med_Episode_2['Secondary Med Episode Dose 2']
    
        #Med 2 dose frequency:
        Med_2_Episode_2_Dose_Frequency = patient.secondary_opioid_interdose_duration
    
        #Med 2 unit dose:
        Med_2_Episode_2_Unit_Dose = str(Secondary_Med_Episode_2['Secondary Med Episode Unit Dose 2'])
    
        #Med 2 active capsules:
        Med_2_Episode_2_Active_Capsules = Secondary_Med_Episode_2['Secondary Med Active Capsules Episode 2']
    
        #Med 2 placebo capsules:
        Med_2_Episode_2_Placebo_Capsules = Secondary_Med_Episode_2['Secondary Med Placebo Capsules Episode 2']
    
        #Med 2 total capsules:
        Med_2_Episode_2_Total_Capsules = Secondary_Med_Episode_2['Secondary Med Total Capsules Episode 2']
    
    else:
        #Secondary Med Episode 2:
        Secondary_Med_Episode_2 = None
    
        #Med 2 name:
        Med_2_Episode_2 = None
    
        #Med 2 episode dose:
        Med_2_Episode_2_Dose = None
    
        #Med 2 dose frequency:
        Med_2_Episode_2_Dose_Frequency = None
    
        #Med 2 unit dose:
        Med_2_Episode_2_Unit_Dose = None
    
        #Med 2 active capsules:
        Med_2_Episode_2_Active_Capsules = None
    
        #Med 2 placebo capsules:
        Med_2_Episode_2_Placebo_Capsules = None
    
        #Med 2 total capsules:
        Med_2_Episode_2_Total_Capsules = None
        
    ######################## EPISODE 3 ########################################

    #Episode 3:
    if 'Episode 3' in all_episode_dictionary.keys():
        Episode_3 = all_episode_dictionary['Episode 3']

        #Primary Med Episode 3:
        Primary_Med_Episode_3 = Episode_3['Primary Opioid Med Episode 3']

        if Primary_Med_Episode_3 != None:

            #Med 1 name:
            Med_1_Episode_3 = Primary_Med_Episode_3['Primary Med Name']

            #Med 1 episode dose:
            Med_1_Episode_3_Dose = Primary_Med_Episode_3['Primary Med Episode Dose 3']

            #Med 1 dose frequency:
            Med_1_Episode_3_Dose_Frequency = patient.primary_opioid_interdose_duration

            #Med 1 unit dose:
            Med_1_Episode_3_Unit_Dose = str(Primary_Med_Episode_3['Primary Med Episode Unit Dose 3'])

            #Med 1 active capsules:
            Med_1_Episode_3_Active_Capsules = Primary_Med_Episode_3['Primary Med Active Capsules Episode 3']

            #Med 1 placebo capsules:
            Med_1_Episode_3_Placebo_Capsules = Primary_Med_Episode_3['Primary Med Placebo Capsules Episode 3']

            #Med 1 total capsules:
            Med_1_Episode_3_Total_Capsules = Primary_Med_Episode_3['Primary Med Total Capsules Episode 3']
            pass
        else:
            #Med 1 name:
            Med_1_Episode_3 = None

            #Med 1 episode dose:
            Med_1_Episode_3_Dose = None

            #Med 1 dose frequency:
            Med_1_Episode_3_Dose_Frequency = None

            #Med 1 unit dose:
            Med_1_Episode_3_Unit_Dose = None

            #Med 1 active capsules:
            Med_1_Episode_3_Active_Capsules = None

            #Med 1 placebo capsules:
            Med_1_Episode_3_Placebo_Capsules = None

            #Med 1 total capsules:
            Med_1_Episode_3_Total_Capsules = None

            pass

        #Secondary Med Episode 3:
        Secondary_Med_Episode_3 = Episode_3['Secondary Opioid Med Episode 3']

        if Secondary_Med_Episode_3 != None:

            #Med 2 name:
            Med_2_Episode_3 = Secondary_Med_Episode_3['Secondary Med Name']

            #Med 2 episode dose:
            Med_2_Episode_3_Dose = Secondary_Med_Episode_3['Secondary Med Episode Dose 3']

            #Med 2 dose frequency:
            Med_2_Episode_3_Dose_Frequency = patient.secondary_opioid_interdose_duration

            #Med 2 unit dose:
            Med_2_Episode_3_Unit_Dose = str(Secondary_Med_Episode_3['Secondary Med Episode Unit Dose 3'])

            #Med 2 active capsules:
            Med_2_Episode_3_Active_Capsules = Secondary_Med_Episode_3['Secondary Med Active Capsules Episode 3']

            #Med 2 placebo capsules:
            Med_2_Episode_3_Placebo_Capsules = Secondary_Med_Episode_3['Secondary Med Placebo Capsules Episode 3']

            #Med 2 total capsules:
            Med_2_Episode_3_Total_Capsules = Secondary_Med_Episode_3['Secondary Med Total Capsules Episode 3']

            pass

        else:
            #Med 2 name:
            Med_2_Episode_3 = None

            #Med 2 episode dose:
            Med_2_Episode_3_Dose = None

            #Med 2 dose frequency:
            Med_2_Episode_3_Dose_Frequency = None

            #Med 2 unit dose:
            Med_2_Episode_3_Unit_Dose = None

            #Med 2 active capsules:
            Med_2_Episode_3_Active_Capsules = None

            #Med 2 placebo capsules:
            Med_2_Episode_3_Placebo_Capsules = None

            #Med 2 total capsules:
            Med_2_Episode_3_Total_Capsules = None

            pass
        pass
    else:
        #Med 1 name:
        Med_1_Episode_3 = None

        #Med 1 episode dose:
        Med_1_Episode_3_Dose = None

        #Med 1 dose frequency:
        Med_1_Episode_3_Dose_Frequency = None

        #Med 1 unit dose:
        Med_1_Episode_3_Unit_Dose = None

        #Med 1 active capsules:
        Med_1_Episode_3_Active_Capsules = None

        #Med 1 placebo capsules:
        Med_1_Episode_3_Placebo_Capsules = None

        #Med 1 total capsules:
        Med_1_Episode_3_Total_Capsules = None

        #Secondary Med Episode 4:
        Secondary_Med_Episode_3 = None

        #Med 2 name:
        Med_2_Episode_3 = None

        #Med 2 episode dose:
        Med_2_Episode_3_Dose = None

        #Med 2 dose frequency:
        Med_2_Episode_3_Dose_Frequency = None

        #Med 2 unit dose:
        Med_2_Episode_3_Unit_Dose = None

        #Med 2 active capsules:
        Med_2_Episode_3_Active_Capsules = None

        #Med 2 placebo capsules:
        Med_2_Episode_3_Placebo_Capsules = None

        #Med 2 total capsules:
        Med_2_Episode_3_Total_Capsules = None

        pass

    ######################## EPISODE 4 ########################################

    #Episode 4:
    if 'Episode 4' in all_episode_dictionary.keys():
        Episode_4 = all_episode_dictionary['Episode 4']

        #Primary Med Episode 4:
        Primary_Med_Episode_4 = Episode_4['Primary Opioid Med Episode 4']

        if Primary_Med_Episode_4 != None:

            #Med 1 name:
            Med_1_Episode_4 = Primary_Med_Episode_4['Primary Med Name']

            #Med 1 episode dose:
            Med_1_Episode_4_Dose = Primary_Med_Episode_4['Primary Med Episode Dose 4']

            #Med 1 dose frequency:
            Med_1_Episode_4_Dose_Frequency = patient.primary_opioid_interdose_duration

            #Med 1 unit dose:
            Med_1_Episode_4_Unit_Dose = str(Primary_Med_Episode_4['Primary Med Episode Unit Dose 4'])

            #Med 1 active capsules:
            Med_1_Episode_4_Active_Capsules = Primary_Med_Episode_4['Primary Med Active Capsules Episode 4']

            #Med 1 placebo capsules:
            Med_1_Episode_4_Placebo_Capsules = Primary_Med_Episode_4['Primary Med Placebo Capsules Episode 4']

            #Med 1 total capsules:
            Med_1_Episode_4_Total_Capsules = Primary_Med_Episode_4['Primary Med Total Capsules Episode 4']

        else:

            #Med 1 name:
            Med_1_Episode_4 = None

            #Med 1 episode dose:
            Med_1_Episode_4_Dose = None

            #Med 1 dose frequency:
            Med_1_Episode_4_Dose_Frequency = None

            #Med 1 unit dose:
            Med_1_Episode_4_Unit_Dose = None

            #Med 1 active capsules:
            Med_1_Episode_4_Active_Capsules = None

            #Med 1 placebo capsules:
            Med_1_Episode_4_Placebo_Capsules = None

            #Med 1 total capsules:
            Med_1_Episode_4_Total_Capsules = None

            pass

        #Secondary Med Episode 4:
        Secondary_Med_Episode_4 = Episode_4['Secondary Opioid Med Episode 4']

        if Secondary_Med_Episode_4 != None:

            #Med 2 name:
            Med_2_Episode_4 = Secondary_Med_Episode_4['Secondary Med Name']

            #Med 2 episode dose:
            Med_2_Episode_4_Dose = Secondary_Med_Episode_4['Secondary Med Episode Dose 4']

            #Med 2 dose frequency:
            Med_2_Episode_4_Dose_Frequency = patient.secondary_opioid_interdose_duration

            #Med 2 unit dose:
            Med_2_Episode_4_Unit_Dose = str(Secondary_Med_Episode_4['Secondary Med Episode Unit Dose 4'])

            #Med 2 active capsules:
            Med_2_Episode_4_Active_Capsules = Secondary_Med_Episode_4['Secondary Med Active Capsules Episode 4']

            #Med 2 placebo capsules:
            Med_2_Episode_4_Placebo_Capsules = Secondary_Med_Episode_4['Secondary Med Placebo Capsules Episode 4']

            #Med 2 total capsules:
            Med_2_Episode_4_Total_Capsules = Secondary_Med_Episode_4['Secondary Med Total Capsules Episode 4']

            pass

        else:

            #Secondary Med Episode 4:
            Secondary_Med_Episode_4 = None

            #Med 2 name:
            Med_2_Episode_4 = None

            #Med 2 episode dose:
            Med_2_Episode_4_Dose = None

            #Med 2 dose frequency:
            Med_2_Episode_4_Dose_Frequency = None

            #Med 2 unit dose:
            Med_2_Episode_4_Unit_Dose = None

            #Med 2 active capsules:
            Med_2_Episode_4_Active_Capsules = None

            #Med 2 placebo capsules:
            Med_2_Episode_4_Placebo_Capsules = None

            #Med 2 total capsules:
            Med_2_Episode_4_Total_Capsules = None

            pass
        pass
    else:
        #Med 1 name:
        Med_1_Episode_4 = None

        #Med 1 episode dose:
        Med_1_Episode_4_Dose = None

        #Med 1 dose frequency:
        Med_1_Episode_4_Dose_Frequency = None

        #Med 1 unit dose:
        Med_1_Episode_4_Unit_Dose = None

        #Med 1 active capsules:
        Med_1_Episode_4_Active_Capsules = None

        #Med 1 placebo capsules:
        Med_1_Episode_4_Placebo_Capsules = None

        #Med 1 total capsules:
        Med_1_Episode_4_Total_Capsules = None

        #Secondary Med Episode 4:
        Secondary_Med_Episode_4 = None

        #Med 2 name:
        Med_2_Episode_4 = None

        #Med 2 episode dose:
        Med_2_Episode_4_Dose = None

        #Med 2 dose frequency:
        Med_2_Episode_4_Dose_Frequency = None

        #Med 2 unit dose:
        Med_2_Episode_4_Unit_Dose = None

        #Med 2 active capsules:
        Med_2_Episode_4_Active_Capsules = None

        #Med 2 placebo capsules:
        Med_2_Episode_4_Placebo_Capsules = None

        #Med 2 total capsules:
        Med_2_Episode_4_Total_Capsules = None

        pass


    ######################## PRE-POST TAPER DATA ##############################

    #Pre/Post Taper Data
    
    new_row = [patient_ID_number,
                redcap_event_name,
                patient_first_name,
                patient_last_name,
                med_1,
                total_med_1_24_hr_dose,
                total_med_1_24_hr_MME,
                med_2,
                total_med_2_24_hr_dose,
                total_med_2_24_hr_MME,
                pre_taper_mme,
                total_mme,
                percent_mme_decrease,
                Med_1_Episode_1,
                Med_1_Episode_1_Dose,
                Med_1_Episode_1_Dose_Frequency,
                Med_1_Episode_1_Unit_Dose,
                Med_1_Episode_1_Active_Capsules,
                Med_1_Episode_1_Placebo_Capsules,
                Med_1_Episode_1_Total_Capsules, 
                Med_2_Episode_1,
                Med_2_Episode_1_Dose,
                Med_2_Episode_1_Dose_Frequency,
                Med_2_Episode_1_Unit_Dose,
                Med_2_Episode_1_Active_Capsules,
                Med_2_Episode_1_Placebo_Capsules,
                Med_2_Episode_1_Total_Capsules,
                Med_1_Episode_2,
                Med_1_Episode_2_Dose,
                Med_1_Episode_2_Dose_Frequency,
                Med_1_Episode_2_Unit_Dose,
                Med_1_Episode_2_Active_Capsules,
                Med_1_Episode_2_Placebo_Capsules,
                Med_1_Episode_2_Total_Capsules,
                Med_2_Episode_2,
                Med_2_Episode_2_Dose,
                Med_2_Episode_2_Dose_Frequency,
                Med_2_Episode_2_Unit_Dose,
                Med_2_Episode_2_Active_Capsules,
                Med_2_Episode_2_Placebo_Capsules,
                Med_2_Episode_2_Total_Capsules,
                Med_1_Episode_3,
                Med_1_Episode_3_Dose,
                Med_1_Episode_3_Dose_Frequency,
                Med_1_Episode_3_Unit_Dose,
                Med_1_Episode_3_Active_Capsules,
                Med_1_Episode_3_Placebo_Capsules,
                Med_1_Episode_3_Total_Capsules,
                Med_2_Episode_3,
                Med_2_Episode_3_Dose,
                Med_2_Episode_3_Dose_Frequency,
                Med_2_Episode_3_Unit_Dose,
                Med_2_Episode_3_Active_Capsules,
                Med_2_Episode_3_Placebo_Capsules,
                Med_2_Episode_3_Total_Capsules,
                Med_1_Episode_4,
                Med_1_Episode_4_Dose,
                Med_1_Episode_4_Dose_Frequency,
                Med_1_Episode_4_Unit_Dose,
                Med_1_Episode_4_Active_Capsules,
                Med_1_Episode_4_Placebo_Capsules,
                Med_1_Episode_4_Total_Capsules,
                Med_2_Episode_4,
                Med_2_Episode_4_Dose,
                Med_2_Episode_4_Dose_Frequency,
                Med_2_Episode_4_Unit_Dose,
                Med_2_Episode_4_Active_Capsules,
                Med_2_Episode_4_Placebo_Capsules,
                Med_2_Episode_4_Total_Capsules
                ]
    return new_row
