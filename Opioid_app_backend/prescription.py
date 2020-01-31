#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 11:20:18 2019

@author: dannywitt
"""

#Will use Patient Information and Medication
import numpy as np
import pandas as pd
import numbers

from itertools import chain, combinations_with_replacement

from patient_information import Patient

from opioid_dose_taper import Taper

from print_report import Print_monthly_report

from medication import (Hydrocodone_Acetaminophen, 
                        Hydromorphone_Immediate_Release,
                        Morphine_Immediate_Release,
                        Morphine_Extended_Release,
                        Oxycodone_Immediate_Release,
                        Oxycodone_Extended_Release, 
                        Oxycodone_Acetaminophen, 
                        Tramadol_Immediate_Release)

class Prescription(Taper):
    '''
    Need class to generate number of pills per episode from starting information;
    Class is designed to take medication inputs (medication types, doses, frequencies,
    MMEs) and patient prescription information (number of tablets/capsules, etc.) and 
    output --> actual med doses and capsules (active vs. placebo)
    
    '''
    
    def __init__(self,
                 a_unique_patient,
                 taper_object
                 ):
        
        #Instantiate flag variables:
        self.primary_med_current_taper = False
        self.secondary_med_current_taper = False
        self.tertiary_med_current_taper = False
        self.is_constant_epdose = False
        
        #Initialize these variables:
        self.final_actual_updated_episode_dose = None
        self.opioid_unit_dose = None
        self.current_taper_ideal_episode_dose_single_med_constant_dose = None
        self.current_taper_ideal_total_24_hr_dose_nonconstant_doses = None
        self.pre_taper_nonconstant_episode_1 = None
        self.pre_taper_nonconstant_episode_2 = None
        self.pre_taper_nonconstant_episode_3 = None
        self.pre_taper_nonconstant_episode_4 = None
        self.actual_episodes = None
        
        #Generate starting variables for constant-dosed medications:
        self.ideal_primary_opioid_episode_dose = None
        self.ideal_secondary_opioid_episode_dose = None
        self.ideal_tertiary_opioid_episode_dose = None
        
        #Generate starting variables for non-constant-dosed medications:
        self.ideal_primary_opioid_total_24_hr_dose = None
        self.ideal_secondary_total_24_hr_dose = None
        self.ideal_tertiary_total_24_hr_dose = None
        
        #Import medications of patient
        
        self.primary_opioid_med = a_unique_patient.primary_opioid_med
        self.secondary_opioid_med = a_unique_patient.secondary_opioid_med
        self.tertiary_opioid_med = a_unique_patient.tertiary_opioid_med
        
        #Update starting episode capsule counts per medication:
        
        self.primary_opioid_total_capsules_per_episode = a_unique_patient.primary_opioid_captab_per_episode_dose
        self.secondary_opioid_total_capsules_per_episode = a_unique_patient.secondary_opioid_captab_per_episode_dose
        self.tertiary_opioid_total_capsules_per_episode = a_unique_patient.tertiary_opioid_captab_per_episode_dose
        
        #Import only medication information that exists for given patient:
        
        #Check if all medications have been tapered to 0mg:
        
        
        #Check if primary med is current taper med:
        if a_unique_patient.primary_opioid_med != None:
            self.primary_opioid_interdose_duration = a_unique_patient.primary_opioid_interdose_duration
            self.primary_opioid_episode_count_24_hr = a_unique_patient.Primary_med_episodes_24_hr()
            #Generate relevant post-taper information and processing:
            #If taper med = primary med:
            if a_unique_patient.primary_opioid_med == taper_object.current_taper_med:
                self.primary_med_current_taper = True
                #If constant, set returned ideal episode variable to that:
                if a_unique_patient.different_daily_episode_doses_med_1 != 'Yes':
                    self.is_constant_epdose = True
                    self.ideal_primary_opioid_episode_dose = self.Taper_to_Prescription_Inputs(a_unique_patient, taper_object)
                    self.current_taper_ideal_episode_dose_single_med_constant_dose = self.ideal_primary_opioid_episode_dose
                    pass
                elif a_unique_patient.different_daily_episode_doses_med_1 == 'Yes':
                    self.is_constant_epdose = False 
                    
                    self.pre_taper_nonconstant_episode_1 = a_unique_patient.primary_opioid_dif_dose_episode_dose_1
                    self.pre_taper_nonconstant_episode_2 = a_unique_patient.primary_opioid_dif_dose_episode_dose_2
                    self.pre_taper_nonconstant_episode_3 = a_unique_patient.primary_opioid_dif_dose_episode_dose_3
                    self.pre_taper_nonconstant_episode_4 = a_unique_patient.primary_opioid_dif_dose_episode_dose_4
                    
                    self.ideal_primary_opioid_total_24_hr_dose = self.Taper_to_Prescription_Inputs(a_unique_patient, taper_object)
                    self.current_taper_ideal_total_24_hr_dose_nonconstant_doses = self.ideal_primary_total_24_hr_dose
                    pass
                else:
                    pass
                pass
            else:
                self.ideal_primary_opioid_episode_dose = 0
                self.ideal_primary_opioid_total_24_hr_dose = 0
                pass
            pass
        else:
            pass
        
        #Check if secondary med is current taper med:
        if a_unique_patient.secondary_opioid_med != None:
            self.secondary_opioid_interdose_duration = a_unique_patient.secondary_opioid_interdose_duration
            self.secondary_opioid_episode_count_24_hr = a_unique_patient.Secondary_med_episodes_24_hr()
            #Generate relevant post-taper information and processing:
            #If taper med = primary med:
            if a_unique_patient.secondary_opioid_med == taper_object.current_taper_med:
                self.secondary_med_current_taper = True
                #If constant, set returned ideal episode variable to that:
                if a_unique_patient.different_daily_episode_doses_med_2 != 'Yes':
                    self.is_constant_epdose = True
                    self.ideal_secondary_opioid_episode_dose = self.Taper_to_Prescription_Inputs(a_unique_patient, taper_object)
                    self.current_taper_ideal_episode_dose_single_med_constant_dose = self.ideal_secondary_opioid_episode_dose
                    pass
                elif a_unique_patient.different_daily_episode_doses_med_2 == 'Yes':
                    self.is_constant_epdose = False
                    
                    self.pre_taper_nonconstant_episode_1 = a_unique_patient.secondary_opioid_dif_dose_episode_dose_1
                    self.pre_taper_nonconstant_episode_2 = a_unique_patient.secondary_opioid_dif_dose_episode_dose_2
                    self.pre_taper_nonconstant_episode_3 = a_unique_patient.secondary_opioid_dif_dose_episode_dose_3
                    self.pre_taper_nonconstant_episode_4 = a_unique_patient.secondary_opioid_dif_dose_episode_dose_4
                    
                    self.ideal_secondary_total_24_hr_dose = self.Taper_to_Prescription_Inputs(a_unique_patient, taper_object)
                    self.current_taper_ideal_total_24_hr_dose_nonconstant_doses = self.ideal_secondary_total_24_hr_dose
                    pass
                else:
                    pass
                pass
            else:
                self.ideal_secondary_opioid_episode_dose = 0
                self.ideal_secondary_opioid_total_24_hr_dose = 0
                pass
            pass
        else:
            pass
        
        if a_unique_patient.tertiary_opioid_med != None:
            self.tertiary_opioid_interdose_duration = a_unique_patient.tertiary_opioid_interdose_duration
            self.tertiary_opioid_episode_count_24_hr = a_unique_patient.Tertiary_med_episodes_24_hr()
             #Generate relevant post-taper information and processing:
            #If taper med = primary med:
            if a_unique_patient.tertiary_opioid_med == taper_object.current_taper_med:
                self.tertiary_med_current_taper = True
                #If constant, set returned ideal episode variable to that:
                if a_unique_patient.different_daily_episode_doses_med_3 != 'Yes':
                    self.is_constant_epdose = True
                    self.ideal_tertiary_opioid_episode_dose = self.Taper_to_Prescription_Inputs(a_unique_patient, taper_object)
                    self.current_taper_ideal_episode_dose_single_med_constant_dose = self.ideal_tertiary_opioid_episode_dose
                    pass
                #If non-constant, set returned ideal episode variable to 24 hr sum:
                elif a_unique_patient.different_daily_episode_doses_med_3 == 'Yes':
                    self.is_constant_epdose = False
                    
                    self.pre_taper_nonconstant_episode_1 = a_unique_patient.tertiary_opioid_dif_dose_episode_dose_1
                    self.pre_taper_nonconstant_episode_2 = a_unique_patient.tertiary_opioid_dif_dose_episode_dose_2
                    self.pre_taper_nonconstant_episode_3 = a_unique_patient.tertiary_opioid_dif_dose_episode_dose_3
                    self.pre_taper_nonconstant_episode_4 = a_unique_patient.tertiary_opioid_dif_dose_episode_dose_4
                    
                    self.ideal_tertiary_total_24_hr_dose = self.Taper_to_Prescription_Inputs(a_unique_patient, taper_object)
                    self.current_taper_ideal_total_24_hr_dose_nonconstant_doses = self.ideal_tertiary_total_24_hr_dose
                    pass
                else:
                    pass
                pass
            else:
                self.ideal_tertiary_opioid_episode_dose = 0
                self.ideal_tertiary_opioid_total_24_hr_dose = 0
            pass
        else:
            pass
            
        #Insert other relevant taper-specific information here:
        ######################################################################
        
        #Current taper medication (either only med that was tapered, or second
        #medication in a taper episode that exhausted medication 1 and then
        #subsequently started tapering a new medication, making it the new 
        #"current taper medication":
        
        #One or medication tapered:
        self.yes_2_meds = taper_object.yes_2_meds
        
        if taper_object.all_done is True:
            self.current_taper_ideal_episode_dose_single_med_constant_dose = 0
            self.current_taper_ideal_total_24_hr_dose_nonconstant_doses = 0
            self.pre_taper_nonconstant_episode_1 = 0
            self.pre_taper_nonconstant_episode_2 = 0
            self.pre_taper_nonconstant_episode_3 = 0
            self.pre_taper_nonconstant_episode_4 = 0
            
            #Set all medications to 0:
            a_unique_patient.primary_opioid_episode_dose = 0
            a_unique_patient.primary_opioid_unit_dose = [None]
            a_unique_patient.primary_opioid_dif_dose_episode_dose_1 = 0
            a_unique_patient.primary_opioid_dif_dose_ep_1_unit_dose = [None]
            a_unique_patient.primary_opioid_dif_dose_episode_dose_2 = 0
            a_unique_patient.primary_opioid_dif_dose_ep_2_unit_dose = [None]
            a_unique_patient.primary_opioid_dif_dose_episode_dose_3 = 0
            a_unique_patient.primary_opioid_dif_dose_ep_3_unit_dose = [None]
            a_unique_patient.primary_opioid_dif_dose_episode_dose_4 = 0
            a_unique_patient.primary_opioid_dif_dose_ep_4_unit_dose = [None]
            
            a_unique_patient.secondary_opioid_episode_dose = 0
            a_unique_patient.secondary_opioid_unit_dose = [None]
            a_unique_patient.secondary_opioid_dif_dose_episode_dose_1 = 0
            a_unique_patient.secondary_opioid_dif_dose_ep_1_unit_dose = [None]
            a_unique_patient.secondary_opioid_dif_dose_episode_dose_2 = 0
            a_unique_patient.secondary_opioid_dif_dose_ep_2_unit_dose = [None]
            a_unique_patient.secondary_opioid_dif_dose_episode_dose_3 = 0
            a_unique_patient.secondary_opioid_dif_dose_ep_3_unit_dose = [None]
            a_unique_patient.secondary_opioid_dif_dose_episode_dose_4 = 0
            a_unique_patient.secondary_opioid_dif_dose_ep_4_unit_dose = [None]
            
#            a_unique_patient.tertiary_opioid_episode_dose = 0
#            a_unique_patient.tertiary_opioid_unit_dose = 
#            a_unique_patient.tertiary_opioid_dif_dose_episode_dose_1 = 0
#            a_unique_patient.tertiary_opioid_dif_dose_ep_1_unit_dose = 0
#            a_unique_patient.tertiary_opioid_dif_dose_episode_dose_2 = 0
#            a_unique_patient.tertiary_opioid_dif_dose_ep_2_unit_dose = 0
#            a_unique_patient.tertiary_opioid_dif_dose_episode_dose_3 = 0
#            a_unique_patient.tertiary_opioid_dif_dose_ep_3_unit_dose = 0
#            a_unique_patient.tertiary_opioid_dif_dose_episode_dose_4 = 0
#            a_unique_patient.tertiary_opioid_dif_dose_ep_4_unit_dose = 0
            pass
        
        else:
            pass
        
        #If current taper medication is constant-dosed, apply function to
        #generate updated episode dose and unit dose(s):
        if self.is_constant_epdose is True:
            self.Constant_ideal2actual_conversion(a_unique_patient,
                                                  taper_object.current_taper_med,
                                                  self.current_taper_ideal_episode_dose_single_med_constant_dose)
            pass
        elif self.is_constant_epdose is False:
            self.Non_constant_ideal2actual_conversion(a_unique_patient,
                                                      taper_object.current_taper_med,
                                                      self.current_taper_ideal_total_24_hr_dose_nonconstant_doses,
                                                      self.pre_taper_nonconstant_episode_1,
                                                      self.pre_taper_nonconstant_episode_2,
                                                      self.pre_taper_nonconstant_episode_3,
                                                      self.pre_taper_nonconstant_episode_4)
            pass
        else:
            pass
        pass
    
        #Execute final prescription generator:
        self.Final_prescription_generator(a_unique_patient,
                                          taper_object)
            
        pass
    
    def Calculate_post_taper_episode_dose(self,
                                          patient,
                                          tapered_medication,
                                          post_taper_med_dose_24):
        '''Takes returned taper medication and post-taper 24 hr dose of that med
        and converts that reduced dose over 24 hours to an episode dose of that 
        medication and updates that episode dose in the patient's object
        '''
        #If primary medication is tapered:
        if tapered_medication == patient.primary_opioid_med:
            self.most_recent_tapered_med = tapered_medication
            self.most_recent_pre_taper_dose_24 = patient.Primary_total_dose_per_24_hr()
            
            #Update calculated tapered dose of current taper med for 24 hr.
            self.total_primary_opioid_dose_per_24_hr = post_taper_med_dose_24
            self.most_recent_post_taper_dose_24 = post_taper_med_dose_24

            #Identify whether medication is constant episode dose or non-constant
            #episode dose; update episode doses accordingly:
            if patient.different_daily_episode_doses_med_1 != 'Yes':
                self.most_recent_pre_taper_episode_dose = patient.primary_opioid_episode_dose
                #Calculate updated episode dose based on post-taper 24 hr. dose:
                self.ideal_primary_opioid_episode_dose_constant = self.total_primary_opioid_dose_per_24_hr / (24 / patient.primary_opioid_interdose_duration)
                self.most_recent_post_taper_episode_dose = post_taper_med_dose_24 / patient.primary_opioid_interdose_duration
                return self.ideal_primary_opioid_episode_dose_constant
            
            #If non-constant, proceed as follows:
            elif patient.different_daily_episode_doses_med_1 == 'Yes':
                self.most_recent_pre_taper_nonconstant_dose_episode_1 = patient.primary_opioid_dif_dose_episode_dose_1
                self.most_recent_pre_taper_nonconstant_dose_episode_2 = patient.primary_opioid_dif_dose_episode_dose_2
                self.most_recent_pre_taper_nonconstant_dose_episode_3 = patient.primary_opioid_dif_dose_episode_dose_3
                self.most_recent_pre_taper_nonconstant_dose_episode_4 = patient.primary_opioid_dif_dose_episode_dose_4
                
                self.primary_opioid_episode_nonconstant_dose_post_taper_total_24_sum = self.total_primary_opioid_dose_per_24_hr
                return self.primary_opioid_episode_nonconstant_dose_post_taper_total_24_sum
 
            else:
                pass
            pass
        
        #If secondary medication is tapered:
        elif tapered_medication == patient.secondary_opioid_med:
            self.most_recent_tapered_med = tapered_medication
            self.most_recent_pre_taper_dose_24 = patient.Secondary_total_dose_per_24_hr()
            
            #Update calculated tapered dose of current taper med for 24 hr.
            self.total_secondary_opioid_dose_per_24_hr = post_taper_med_dose_24
            self.most_recent_post_taper_dose_24 = post_taper_med_dose_24
            
            #Identify whether medication is constant episode dose or non-constant
            #episode dose; update episode doses accordingly:
            if patient.different_daily_episode_doses_med_2 != 'Yes':
                self.most_recent_pre_taper_episode_dose = patient.secondary_opioid_episode_dose
                #Calculate updated episode dose based on post-taper 24 hr. dose:
                self.ideal_secondary_opioid_episode_dose_constant = self.total_secondary_opioid_dose_per_24_hr / (24 / patient.secondary_opioid_interdose_duration)
                self.most_recent_post_taper_episode_dose = post_taper_med_dose_24 / patient.secondary_opioid_interdose_duration
                return self.ideal_secondary_opioid_episode_dose_constant
            
            #If non-constant, proceed as follows:
            elif patient.different_daily_episode_doses_med_2 == 'Yes':
                self.most_recent_pre_taper_diff_dose_episode_1 = patient.secondary_opioid_dif_dose_episode_dose_1
                self.most_recent_pre_taper_diff_dose_episode_2 = patient.secondary_opioid_dif_dose_episode_dose_2
                self.most_recent_pre_taper_diff_dose_episode_3 = patient.secondary_opioid_dif_dose_episode_dose_3
                self.most_recent_pre_taper_diff_dose_episode_4 = patient.secondary_opioid_dif_dose_episode_dose_4
                
                self.secondary_opioid_episode_nonconstant_dose_post_taper_total_24_sum = self.total_secondary_opioid_dose_per_24_hr
                return self.secondary_opioid_episode_nonconstant_dose_post_taper_total_24_sum
                pass
 
            else:
                pass
            pass
        
#        #If tertiary medication is tapered:
#        elif tapered_medication == self.tertiary_opioid_med:
#            self.most_recent_tapered_med = tapered_medication
#            self.most_recent_pre_taper_dose_24 = self.Tertiary_total_dose_per_24_hr()
#            self.most_recent_pre_taper_episode_dose = self.tertiary_opioid_episode_dose
#            
#            #Update calculated tapered dose of current taper med for 24 hr.
#            self.total_tertiary_opioid_dose_per_24_hr = post_taper_med_dose_24
#            self.most_recent_post_taper_dose_24 = post_taper_med_dose_24
#
#            #Calculate updated episode dose based on post-taper 24 hr. dose:
#            self.tertiary_opioid_episode_dose = self.total_tertiary_opioid_dose_per_24_hr / (24 / self.tertiary_opioid_interdose_duration)
#            self.most_recent_post_taper_episode_dose = post_taper_med_dose_24 / self.tertiary_opioid_interdose_duration
#            return self.tertiary_opioid_episode_dose
       
        else:
            pass
    
    def Taper_to_Prescription_Inputs(self, patient, taper_object):
        '''
        Identifies if most recent taper involved 1 or 2 medications; if single 
        medication, determines if that single medication was primary, secondary,
        or tertiary opioid medication and updates ideal episode dose (if constant
        dose med) or ideal total 24 hr dose (if non-constant); if multiple
        medications involved in taper, first medication (which has been tapered
        to 0mg--exhausted) is converted to NoneType with dose = 0mg in the patient
        object AND second medication which is subsequently tapered in same
        taper episode is handled identically to the above pathway, such that
        either ideal episode dose (constant dosing) or ideal total 24 hr dose
        (non-constant dosing) is returned.
        '''
        
        #Check to see if all medications have been exhausted; if so, break from
        #current iteration of for loop and end script, and print ALL DONE:
        if taper_object.all_done is True:
             patient.primary_opioid_med = None
             patient.secondary_opioid_med = None
             patient.tertiary_opioid_med = None
             Print_monthly_report(patient)
             print('\nAll medications are placebo.\n')
        else:
             pass
         
        #Check to see if most recent taper involved only a single medication, or
        #involved tapering one medication to 0mg/0 MME then also tapering a second
        #medication (or third medication, within same taper episode);
        #Then, generate post_taper_episode_dose for tapered medications:
         
        #Case 1: Only one medication actually tapered 
        if taper_object.yes_2_meds is False:
            #Update only current tapered medication:
            for medication in enumerate(patient.Current_medication_list()):
                #Primary med identification:
                if medication[1] == taper_object.current_taper_med:
                    #Primary med:
                    if medication[0] == 0:
                        #Update med as
                        tapered_med = taper_object.current_taper_med
                        updated_taper_dose_24_hr = taper_object.post_taper_dose_24
                        
                        #####Need to differentiate if constant or nonconstant and
                        #return appropriate variable:
                        if patient.different_daily_episode_doses_med_1 != 'Yes':
                            self.ideal_primary_opioid_episode_dose = self.Calculate_post_taper_episode_dose(patient, 
                                                                                                            tapered_med, 
                                                                                                            updated_taper_dose_24_hr)
                            return self.ideal_primary_opioid_episode_dose
                        elif patient.different_daily_episode_doses_med_1 == 'Yes':
                            self.ideal_primary_total_24_hr_dose = self.Calculate_post_taper_episode_dose(patient, 
                                                                                                         tapered_med, 
                                                                                                         updated_taper_dose_24_hr)
                            return self.ideal_primary_total_24_hr_dose
                        else:
                            pass
                        pass
                    
                    #Secondary med identification:
                    elif medication[0] == 1:
                        #Update med as
                        tapered_med = taper_object.current_taper_med
                        updated_taper_dose_24_hr = taper_object.post_taper_dose_24
                        #####Need to differentiate if constant or nonconstant and
                        #return appropriate variable:
                        if patient.different_daily_episode_doses_med_2 != 'Yes':
                            self.ideal_secondary_opioid_episode_dose = self.Calculate_post_taper_episode_dose(patient,
                                                                                                              tapered_med, 
                                                                                                              updated_taper_dose_24_hr)
                            return self.ideal_secondary_opioid_episode_dose
                        elif patient.different_daily_episode_doses_med_2 == 'Yes':
                            self.ideal_secondary_total_24_hr_dose = self.Calculate_post_taper_episode_dose(patient,
                                                                                                           tapered_med, 
                                                                                                           updated_taper_dose_24_hr)
                            return self.ideal_secondary_total_24_hr_dose
                        else:
                            pass
                        pass
                    #Tertiary med identification:
                    elif medication[0] == 2:
                        #Update med as
                        tapered_med = taper_object.current_taper_med
                        updated_taper_dose_24_hr = taper_object.post_taper_dose_24
                        #####Need to differentiate if constant or nonconstant and
                        #return appropriate variable:
                        if patient.different_daily_episode_doses_med_3 != 'Yes':
                            self.ideal_tertiary_opioid_episode_dose = self.Calculate_post_taper_episode_dose(tapered_med, updated_taper_dose_24_hr)
                            return self.ideal_tertiary_opioid_episode_dose
            
                        elif patient.different_daily_episode_doses_med_3 == 'Yes':
                            self.ideal_tertiary_total_24_hr_dose = self.Calculate_post_taper_episode_dose(tapered_med, updated_taper_dose_24_hr)
                            return self.ideal_tertiary_total_24_hr_dose
                        else:
                            pass
                        pass
                    else:
                        pass
                    pass
                else:
                    pass
                pass
            pass
     
        #Case 2: Two medications involved in taper, so update :
        elif taper_object.yes_2_meds is True:
            #Case 2.1: Identify and update exhuasted med as "None":
            for medication in enumerate(patient.Current_medication_list()):
                if medication[1] == taper_object.previous_tapered_med_now_exhausted:
                    #Primary med identification:
                    if medication[0] == 0:
                        #Update med as "None":
                        patient.primary_opioid_med = None
                        patient.primary_opioid_episode_dose = 0
                        pass
                    #Secondary med identification:
                    elif medication[0] == 1:
                        #Update med as "None"
                        patient.secondary_opioid_med = None
                        patient.secondary_opioid_episode_dose = 0
                        pass
                    #Tertiary med identification
                    elif medication[0] == 2:
                        #Update med as "None"
                        patient.tertiary_opioid_med = None
                        patient.tertiary_opioid_episode_dose = 0
                        pass
                    else:
                        pass
                    pass
                else:
                    pass
                pass
         
            #Case 2.2: Identify and update second (i.e., current) tapered medication
            for medication in enumerate(patient.Current_medication_list()):
                if medication[1] == taper_object.current_taper_med:
                    #Primary med:
                    if medication[0] == 0:
                        #Update med as
                        if taper_object.post_taper_dose_24_med_2 > 0:
                            tapered_med = taper_object.current_taper_med
                            updated_taper_dose_24_hr = taper_object.post_taper_dose_24_med_2
                            #####Need to differentiate if constant or nonconstant and
                            #return appropriate variable:
                            if patient.different_daily_episode_doses_med_1 != 'Yes':
                                self.ideal_primary_opioid_episode_dose = self.Calculate_post_taper_episode_dose(patient, 
                                                                                                             tapered_med, 
                                                                                                             updated_taper_dose_24_hr)
                                return self.ideal_primary_opioid_episode_dose
                            elif patient.different_daily_episode_doses_med_1 == 'Yes':
                                self.ideal_primary_total_24_hr_dose = self.Calculate_post_taper_episode_dose(patient, 
                                                                                                          tapered_med, 
                                                                                                          updated_taper_dose_24_hr)
                                return self.ideal_primary_total_24_hr_dose
                            else:
                                pass
                            pass
                        else:
                            patient.primary_opioid_med = None
                            pass
                        pass
                    
                    #Secondary med identification:
                    elif medication[0] == 1:
                        #Update med as
                        if taper_object.post_taper_dose_24_med_2 > 0:
                            tapered_med = taper_object.current_taper_med
                            updated_taper_dose_24_hr = taper_object.post_taper_dose_24_med_2
                            #####Need to differentiate if constant or nonconstant and
                            #return appropriate variable:
                            if patient.different_daily_episode_doses_med_2 != 'Yes':
                                self.ideal_secondary_opioid_episode_dose = self.Calculate_post_taper_episode_dose(patient, 
                                                                                                                  tapered_med, 
                                                                                                                  updated_taper_dose_24_hr)
                                return self.ideal_secondary_opioid_episode_dose
                            elif patient.different_daily_episode_doses_med_2 == 'Yes':
                                self.ideal_secondary_total_24_hr_dose = self.Calculate_post_taper_episode_dose(patient,
                                                                                                               tapered_med, 
                                                                                                               updated_taper_dose_24_hr)
                                return self.ideal_secondary_total_24_hr_dose
                            pass
                        else:
                            patient.secondary_opioid_med = None
                            pass
                        pass

                    #Tertiary med identification:
                    elif medication[0] == 2:
                        #Update med as
                        if taper_object.post_taper_dose_24_med_2 > 0:
                            tapered_med = taper_object.current_taper_med
                            updated_taper_dose_24_hr = taper_object.post_taper_dose_24_med_2
                            #####Need to differentiate if constant or nonconstant and
                            #return appropriate variable:
                            if patient.different_daily_episode_doses_med_3 != 'Yes':
                                self.ideal_tertiary_opioid_episode_dose = self.Calculate_post_taper_episode_dose(tapered_med, 
                                                                                                                 updated_taper_dose_24_hr)
                                return self.ideal_tertiary_opioid_episode_dose
                            elif patient.different_daily_episode_doses_med_3 == 'Yes':
                                self.ideal_tertiary_total_24_hr_dose = self.Calculate_post_taper_episode_dose(tapered_med, 
                                                                                                              updated_taper_dose_24_hr)
                                return self.ideal_tertiary_total_24_hr_dose
                            else:
                                pass
                            pass
                        
                        else:
                            patient.tertiary_opioid_med = None
                            pass
                        pass
                    else:
                        pass
                    pass
                else:
                    pass
                pass
            pass
        else:
            pass
        pass
    pass
    
    def Number_episodes_per_day(self,
                                patient):
        #Will control whether we can use episode 1, 2, 3, or 4
        #Deal with different inputs of daily episodes per medication
        #(e.g., primary med episodes 24 hr = 4, secondary med episodes = 2)
        #and reconcile actual number of episodes:
        #unique_dose_episodes = max([dose_episodes_per_day_1, dose_episodes_per_day_2])
        
        primary_med_number_episodes = patient.Number_episodes_per_24_hr(patient.primary_opioid_interdose_duration)
        secondary_med_number_episodes = patient.Number_episodes_per_24_hr(patient.secondary_opioid_interdose_duration)
        self.total_episodes = max(primary_med_number_episodes,
                             secondary_med_number_episodes)
        
        primary_med_interdose_duration = patient.primary_opioid_interdose_duration
        secondary_med_interdose_duration = patient.secondary_opioid_interdose_duration
        episode_frequency_combinations = [(primary_med_number_episodes, primary_med_interdose_duration),
                                          (secondary_med_number_episodes, secondary_med_interdose_duration)]
        self.total_interdose_duration = (sorted(episode_frequency_combinations[0]))[1]
        pass
    
    def Non_constant_equal_epdose_pathway(self,
                                          patient,
                                          current_tap_med_object,
                                          count_smallest_unit,
                                          smallest_unit_dose,
                                          count_existing_episodes,
                                          existing_episodes):
        
        #Reduce each episode dose from ep 1 > ep 2 > ep 3 > ep 4 order by 
        #smallest unit dose:
        #Set up adjusted episode doses to track reduction of units from
        #pre-taper episode doses:
        
        #Set max index to number of meds - 1 (maximum can be index=3, which
        #permits lists of length <= 4 max:
        
        index_max = (count_existing_episodes - 1)
        episode_index = 0
        for unit_count in range(int(count_smallest_unit)):
            existing_episodes[episode_index][1] -= smallest_unit_dose
            self.smallest_units_left_in_taper_episode -= 1
            if episode_index < index_max:
                episode_index += 1
                pass
            elif episode_index >= index_max:
                episode_index = 0
                pass
            else:
                pass
            pass
        #Generates a list of sublists with sublist[0] = episode dose and
        #sublist[1] = unit dose(s); sublists in order of episodes,
        #since list generated from existing_episodes which is 
        #itself generated by episodes: 1, 2, 3, 4 order
        self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list = []
        for ideal_episode in existing_episodes:
            ideal_episode = ideal_episode[1]
            actual_episode_and_unit_doses = self.Constant_ideal2actual_conversion(patient,
                                                  current_tap_med_object, 
                                                  ideal_episode)
            self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list.append(actual_episode_and_unit_doses)
            pass
        return self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list
    
    
    def Non_constant_ideal2actual_conversion(self, 
                                             patient,
                                             current_tap_med_object,
                                             ideal_nonconstant_24_hr_dose, 
                                             episode_1_dose,
                                             episode_2_dose,
                                             episode_3_dose,
                                             episode_4_dose):
        '''
        Input constant dosed (1) medication object which was most recently tapered 
        and also input the (2) current tapered med ideal episode dose.
        
        Use the medication object's available unit doses and the ideal episode 
        dose (given constant dosing) to generate the actual final episode dose
        for that given medication.
        
        Use three pathways to return three different values, depending on whether
        taper medication is primary, secondary, or tertiary medication.
        
        
        ################
        Goal: input total post-taper 24hr dose of a medication and up to
        4 existing episode doses for a patient's day; some of these episode
        doses can be Nonetype if there are not >2 episodes; goal is to:
            (1) Assess current episode doses that exists and count of active
            episode doses (assign var)
            (2) Identify actual decrease in pre- to post-taper dose of given med
            (3) Identify number of episodes and choose how many episodes to
            spread decreased 24 hr dose across:
                (3a) use smallest unit dose available for given medication (an
                attribute of that medication object)
                (3b) count how many unit doses make up decreased total 24hr dose
                (this will be the number to iterate over for existing episode
                doses and decreasing by smallest unit dose with each iteration)
            (4) Establish Count_small_unit as iterator (e.g., for i in range(count)); 
            identify if all episode doses (1) all equal or (2) not all equal:
                (4.1) If equal, apply rank of taper ep1 > ep2 > ep3 > ep4, continue
                (4.2) If different episode doses exist, then identify largest 
                episode dose in list
                    (4.2a) Identify episodes that have largest episode dose (i.e., 
                    pick out all equal, largest episodes)
                        4.2a.1: Choose ep1 > ep2 > ep3 > ep4 to taper by smallest 
                        unit dose, continue
                (4c) update each episode dose through each step and regenerate
                dose list through each iteration to compare
            (5) At end of iteration (up to count of smallest unit doses), return
            updated episode doses as dictionary: {(ep 1: updated dose), (ep 2: 
            updated dose), etc...)}
        '''
        #Initialize collection list of final episode doses and unit dose[s]:
        self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list = []
        
        #Identify patient starting number episodes for given taper medication
        #(will stay constant throughout study):
        
       
        for medication in enumerate(patient.Current_medication_list()):
            if medication[1] == current_tap_med_object:
                #Primary med is taper med:
                if medication[0] == 0:
                    self.total_med_nonconstant_episodes_daily = patient.Number_episodes_per_24_hr(patient.primary_opioid_interdose_duration)
                    pass
                #Seconday med is taper med:
                elif medication[0] == 1:
                    self.total_med_nonconstant_episodes_daily = patient.Number_episodes_per_24_hr(patient.secondary_opioid_interdose_duration)
                    pass
                elif medication[0] == 2:
                    self.total_med_nonconstant_episodes_daily = patient.Number_episodes_per_24_hr(patient.tertiary_opioid_interdose_duration)
                    pass
                else:
                    pass
                pass
            else:
                pass
            pass
        
        #count active daily episodes:
        list_episode_doses = [episode_1_dose,
                              episode_2_dose,
                              episode_3_dose,
                              episode_4_dose]
        
        #isolate existing (non- None) episodes; ie, remove NoneType episodes:
        list_to_remove = ['nan', 'NA', 'Nan', None]
        self.existing_episodes = [episode for episode in list_episode_doses if episode not in list_to_remove and not np.isnan(episode)] 
        #Count number of existing episodes:
        self.count_existing_episodes = len(self.existing_episodes)
       
        #Check if ideal_nonconstant_24_hr_dose if None; if not None, then
        #medication is non-zero dose and proceed to generate ideal episode
        #doses for taper medication:
        
        if ideal_nonconstant_24_hr_dose > 0:
            self.ideal_pre_post_taper_decrease_nonconstant_total_24_hr_dose = (sum(self.existing_episodes) - ideal_nonconstant_24_hr_dose)
            #Logical pathway: determine whether the pre-taper episode doses that
            #exist are all equal doses at the pre-taper state; approach is to compare
            #all episode doses that exist for given tapered medication by iterating
            #through existing list and comparing each episode dose to each other
            #episode dose; this will return a list of boolean objects saying if the 
            #episode doses are all within +/- 1 mg of one another. 
            
            check_episodes_same = [np.isclose(i, j, atol = 1) for i in self.existing_episodes for j in self.existing_episodes]
            
            #Determine smallest unit dose available for current taper medication
            self.smallest_unit_taper_med = min(current_tap_med_object.available_opioid_unit_doses)
            #Determine number of smallest unit doses that sum to total ideal
            #decrease/difference between pre- and post-taper 24 hr. dose:
            self.count_smallest_units_in_decrease_ideal_pre_post_taper_24_hr_dose = round(self.ideal_pre_post_taper_decrease_nonconstant_total_24_hr_dose / self.smallest_unit_taper_med)
            self.smallest_units_left_in_taper_episode = self.count_smallest_units_in_decrease_ideal_pre_post_taper_24_hr_dose
            
            listed_enumerated_existing_episodes = []
            for ep,dose in enumerate(self.existing_episodes):
                epdose = [ep, dose]
                listed_enumerated_existing_episodes.append(epdose)
                pass
            
            self.enumerated_existing_episodes = listed_enumerated_existing_episodes
            #State Option I: All episode are approximately the same dose:
            
            if all(check_episodes_same):
                self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list = self.Non_constant_equal_epdose_pathway(patient,
                                                                                               current_tap_med_object,
                                                                                               self.smallest_units_left_in_taper_episode,
                                                                                               self.smallest_unit_taper_med,
                                                                                               self.count_existing_episodes,
                                                                                               self.enumerated_existing_episodes)
                                                       
            #State Option II: At least 1 episode dose is not approximately equal to
            #another episode dose
            
            elif not all(check_episodes_same):
                #Goal: generate enumerated list of episode doses; rank list from
                #maximum to minimum subtuple[1] dose; iterate through subtracting
                #smallest unit from largest dose at each iteration, while re-ranking
                #largest to smallest after each subtraction episode; if at any time
                #approximately equal doses are achieved across episode doses, then
                #break out of iteration and use self.Non_constant_equal_epdose_pathway:
                
                #Also, keep track of how many small unit doses are left in given
                #dose taper event (so that if the doses become equal and break out
                #of "for" loop, there is an accurate counter of how many more
                #smallest units to remove from across all episode doses):
                
                self.enumerated_sorted_existing_episodes = sorted(self.enumerated_existing_episodes, key=lambda x: x[1], reverse=True)
                for unit in range(int(self.count_smallest_units_in_decrease_ideal_pre_post_taper_24_hr_dose)):
                    #Generate updated dose for largest episode dose:
                    updated_dose = self.enumerated_sorted_existing_episodes[0][1] - self.smallest_unit_taper_med
                    #Update new reduced dose:
                    self.enumerated_sorted_existing_episodes[0][1] = updated_dose
                    #Generate temporary episode dose only list for comparison:
                    temp_existing_epdose_list = [x[1] for x in self.enumerated_sorted_existing_episodes]
                    #Reduce number of units for dose reduction for given taper
                    #episode:
                    self.smallest_units_left_in_taper_episode -= 1
                    #Check if all doses approximately equal (as done above):
                    check_episodes_same = [np.isclose(i, j, atol = 1) for i in temp_existing_epdose_list for j in temp_existing_epdose_list]
                    if all(check_episodes_same):
                        self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list = self.Non_constant_equal_epdose_pathway(patient,
                                                                                               current_tap_med_object,
                                                                                               self.smallest_units_left_in_taper_episode,
                                                                                               self.smallest_unit_taper_med,
                                                                                               self.count_existing_episodes,
                                                                                               self.enumerated_sorted_existing_episodes)
                        break
                    elif not all(check_episodes_same):
                        #Re-sort from largest to smallest episode doses to have 
                        #largest dose for new iteration of for loop:
                        self.enumerated_sorted_existing_episodes = sorted(self.enumerated_sorted_existing_episodes, key=lambda x: x[1], reverse=True)
                        continue
                    else:
                        pass
                    pass
                
                #If episode doses had all available smallest unit doses decreased,
                #then convert enumerated list of tuples back to ordered
                #ep 1, ep 2, ep 3, ep 4, etc. list of existing doses:
                if not all(check_episodes_same):
                    updated_epdoses_original_episode_order = sorted(self.enumerated_sorted_existing_episodes, key=lambda x: x[0])
                    #Use constant dose function to derive final actual episode doses:
                    self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list = []
                    for ideal_episode in updated_epdoses_original_episode_order:
                        ideal_episode = ideal_episode[1]
                        actual_episode_and_unit_doses = self.Constant_ideal2actual_conversion(patient,
                                                                                              current_tap_med_object, 
                                                                                              ideal_episode)
                        self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list.append(actual_episode_and_unit_doses)
                        pass
                    pass
                elif all(check_episodes_same):
                    pass
                pass
            else:
                pass
            pass
        #Now, assign (1) final episode doses to patient object and (2) 
        #assign final per episode unit doses to patient object:
            
        #Check length of episode list (if it is less than 4, add "None" to
        #remaining episode spots):
        while len(self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list) < 4:
            self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list.append((None, None))
            pass
        
        #Primary medication:
        if self.primary_med_current_taper is True:
            if self.is_constant_epdose is False:
                patient.primary_opioid_dif_dose_episode_dose_1 = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[0][0]
                patient.primary_opioid_dif_dose_ep_1_unit_dose = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[0][1]
                patient.primary_opioid_dif_dose_episode_dose_2 = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[1][0]
                patient.primary_opioid_dif_dose_ep_2_unit_dose = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[1][1]
                patient.primary_opioid_dif_dose_episode_dose_3 = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[2][0]
                patient.primary_opioid_dif_dose_ep_3_unit_dose = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[2][1]
                patient.primary_opioid_dif_dose_episode_dose_4 = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[3][0]
                patient.primary_opioid_dif_dose_ep_4_unit_dose = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[3][1]
                pass
            else:
                pass
            pass
        #Secondary Medication:
        elif self.secondary_med_current_taper is True:
            if self.is_constant_epdose is False:
                patient.secondary_opioid_dif_dose_episode_dose_1 = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[0][0]
                patient.secondary_opioid_dif_dose_ep_1_unit_dose = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[0][1]
                patient.secondary_opioid_dif_dose_episode_dose_2 = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[1][0]
                patient.secondary_opioid_dif_dose_ep_2_unit_dose = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[1][1]
                patient.secondary_opioid_dif_dose_episode_dose_3 = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[2][0]
                patient.secondary_opioid_dif_dose_ep_3_unit_dose = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[2][1]
                patient.secondary_opioid_dif_dose_episode_dose_4 = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[3][0]
                patient.secondary_opioid_dif_dose_ep_4_unit_dose = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[3][1]
                pass
            else:
                pass
            pass
#        #Tertiary Medication:
#        elif self.tertiary_med_current_taper is True:
#            if self.is_constant_epdose is False:
#                patient.tertiary_opioid_dif_dose_episode_dose_1 = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[0][0]
#                patient.tertiary_opioid_dif_dose_ep_1_unit_dose = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[0][1]
#                patient.tertiary_opioid_dif_dose_episode_dose_2 = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[1][0]
#                patient.tertiary_opioid_dif_dose_ep_2_unit_dose = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[1][1]
#                patient.tertiary_opioid_dif_dose_episode_dose_3 = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[2][0]
#                patient.tertiary_opioid_dif_dose_ep_3_unit_dose = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[2][1]
#                patient.tertiary_opioid_dif_dose_episode_dose_4 = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[3][0]
#                patient.tertiary_opioid_dif_dose_ep_4_unit_dose = self.final_actual_post_taper_nonconstant_episode_and_unit_dose_list[3][1]
#                pass
#            else:
#                pass
#            pass
        else:
            pass
        pass
    
    def Constant_ideal2actual_conversion(self,
                                         patient,
                                         current_tap_med_object,
                                         ideal_constant_episode_dose
                                         ):  
        '''
        Input constant dosed (1) medication object which was most recently tapered 
        and also input the (2) current tapered med ideal episode dose.
        
        Use the medication object's available unit doses and the ideal episode 
        dose (given constant dosing) to generate the actual final episode dose
        for that given medication.
        
        Use three pathways to return three different values, depending on whether
        taper medication is primary, secondary, or tertiary medication.
        
        '''
        
        #Part I: Take current taper med object and ideal constant episode dose
        #and examine medication's available single or combined unit doses; if
        #unit or combined unit doses do not evenly divide the initial ideal
        #post-taper constant episode dose, then iterate down through possible
        #adjusted 24 hr doses of tapered med and identify the largest
        #available adjusted 24 dose that evenly divides single/combined unit
        #dose; then return either single or combined unit dose(s) as a list
        #to serve as input for the final prescription generator function
        print(ideal_constant_episode_dose)
        #Check if episode dose is 0mg:
        if ideal_constant_episode_dose == int(0) or ideal_constant_episode_dose == float(0):
            self.final_actual_updated_episode_dose = 0
            self.opioid_unit_dose = None
            pass
        elif ideal_constant_episode_dose != int(0) or ideal_constant_episode_dose != float(0):
        
            first_pass_possible_unit_doses = []
            rounded_episode_dose = int(np.ceil(ideal_constant_episode_dose))
            
            #Generate single and combined units of medication from existing
            #available unit doses:
            combo_list = []
            def all_subsets(ss):
                return chain(*map(lambda x: combinations_with_replacement(ss, x), range(0, len(ss)+1)))
            
            for subset in all_subsets(current_tap_med_object.available_opioid_unit_doses):
                combo_list.append(subset)
                
            #These will be combined sums of unit doses:
            possible_opioid_unit_dose_combinations = [sum(tup) for tup in combo_list]
            possible_opioid_unit_dose_combinations = [float(i) for i in possible_opioid_unit_dose_combinations]
            
            #Construct dictionary with keys (list of unique combo tuples) and
            #values (sums of unit doses) available:
            
            dictionary_opioid_unit_doses = dict(zip(combo_list, possible_opioid_unit_dose_combinations))
            
            #Remove sum of 0 from dictionary (artifact):
            dictionary_opioid_unit_doses = {k:v for k,v in dictionary_opioid_unit_doses.items() if v != 0.0}
            unit_dose_list = list(dictionary_opioid_unit_doses.values())
            #Identify if any of the combined unit doses evenly divide into the 
            #rounded ideal episode dose:
            for possible_opioid_unit_dose in unit_dose_list:
                if rounded_episode_dose % possible_opioid_unit_dose == 0:
                    first_pass_possible_unit_doses.append(possible_opioid_unit_dose)
                else:
                    continue
                pass
            
            if len(first_pass_possible_unit_doses) > 0:
                print(first_pass_possible_unit_doses)
                first_pass_possible_unit_doses = list(set(first_pass_possible_unit_doses))
                potential_opioid_unit_dose = max(first_pass_possible_unit_doses)
                if potential_opioid_unit_dose in current_tap_med_object.available_opioid_unit_doses:
                    self.opioid_unit_dose = potential_opioid_unit_dose
                    pass
                elif potential_opioid_unit_dose not in current_tap_med_object.available_opioid_unit_doses:
                    #Use the known potential_prim_opioid_unit_dose (which is a 
                    #value in our dictionary) to identify all possible 
                    #combinations of base unit doses, with goal of minimizing 
                    #number of base unit doses required:
                    
                    possible_combination_list = []
                    for k,v in dictionary_opioid_unit_doses.items():
                        if v == potential_opioid_unit_dose:
                            possible_combination_list.append(k)
                            pass
                        else:
                            pass
                        pass
                    
                    #Now, identify the "shortest" tuple (i.e., the tuple which
                    #represents the minimum number of base unit doses):
                    tup_size = []
                    for index,tup in enumerate(possible_combination_list):
                        tup_size.append((index, len(tup)))
                        pass
                    
                   
                    shortest_tup_length = min([i[1] for i in tup_size])
                    
                    index_at_shortest_tup = [i[0] for i in tup_size if i[1] == shortest_tup_length]
                    #Use this index of shortest tuple for identifying the 
                    #correct combination of base unit doses to assign as
                    #primary opioid unit dose:
                    self.opioid_unit_dose = possible_combination_list[index_at_shortest_tup[0]]
                    pass
                else:
                    pass
    
                self.final_actual_updated_episode_dose = rounded_episode_dose
                
            else:
                #No perfectly divisible units of primary med for current
                #ideal episode dose; so create range from 0 to current ideal
                #episode dose and iterate down by 1mg until reach episode dose
                #that is perfectly divisible by available unit doses:
                first_pass_possible_unit_doses = []
                #Adjust rate of decreasing adjusted episode doses:
                dose_decrement_adjuster = 0.75
                index_multiplier = 0
                
                for adjusted_episode_dose in range((int(rounded_episode_dose)-1),0,-1):
                    index_multiplier += 1
                    adjusted_episode_dose += (dose_decrement_adjuster * index_multiplier)
                    #Same as previously done (try to abstract into a function):
                    for possible_opioid_unit_dose in unit_dose_list:
                        if np.isclose((adjusted_episode_dose % possible_opioid_unit_dose), 0):
                            first_pass_possible_unit_doses.append(possible_opioid_unit_dose)
                            pass
                        else:
                            continue
                        pass
            
                    if len(first_pass_possible_unit_doses) > 0:
                        first_pass_possible_unit_doses = list(set(first_pass_possible_unit_doses))
                        potential_opioid_unit_dose = max(first_pass_possible_unit_doses)
                        if potential_opioid_unit_dose in current_tap_med_object.available_opioid_unit_doses:
                            self.opioid_unit_dose = potential_opioid_unit_dose
                            pass
                        elif potential_opioid_unit_dose not in current_tap_med_object.available_opioid_unit_doses:
                            #Use the known potential_prim_opioid_unit_dose (which is a 
                            #value in our dictionary) to identify all possible 
                            #combinations of base unit doses, with goal of minimizing 
                            #number of base unit doses required:
                            
                            possible_combination_list = []
                            for k,v in dictionary_opioid_unit_doses.items():
                                if v == potential_opioid_unit_dose:
                                    possible_combination_list.append(k)
                                    pass
                                else:
                                    pass
                                pass
                            
                            #Now, identify the "shortest" tuple (i.e., the tuple which
                            #represents the minimum number of base unit doses):
                            tup_size = []
                            for index,tup in enumerate(possible_combination_list):
                                tup_size.append((index, len(tup)))
                                pass
                            
                            shortest_tup_length = min([i[1] for i in tup_size])
                            index_at_shortest_tup = [i[0] for i in tup_size if i[1] == shortest_tup_length]
                            #Use this index of shortest tuple for identifying the 
                            #correct combination of base unit doses to assign as
                            #primary opioid unit dose:
                            self.opioid_unit_dose = possible_combination_list[index_at_shortest_tup[0]]
                            pass
                        else:
                            pass
            
                        self.final_actual_updated_episode_dose = adjusted_episode_dose
                        break
                    
                    else:
                        continue
                    pass
                
                if not first_pass_possible_unit_doses:
                    #If no episode dose or unit assigned, then check to see if between
                    #available unit doses:
                    if min(current_tap_med_object.available_opioid_unit_doses) <= rounded_episode_dose <= max(current_tap_med_object.available_opioid_unit_doses):
                       closest_unit_dose = min(current_tap_med_object.available_opioid_unit_doses)
                       self.final_actual_updated_episode_dose = closest_unit_dose
                       self.opioid_unit_dose = closest_unit_dose
                       pass
                    else:
                       self.final_actual_updated_episode_dose = 0
                       self.opioid_unit_dose = None
                       pass
                    pass
                elif first_pass_possible_unit_doses:
                    pass
                pass
            pass
        else:
            pass
        
        #Part II: Take final updated episode dose and current taper medication
        #and identify current taper med as primary, secondary, or tertiary medication
        #and return 3 possible values to serve as input:
        if self.primary_med_current_taper is True:
            if self.is_constant_epdose is True:
                patient.primary_opioid_episode_dose = self.final_actual_updated_episode_dose
                patient.primary_opioid_unit_dose = [self.opioid_unit_dose]
                pass
            elif self.is_constant_epdose is False:
                #This returns list of episode dose and unit dose to the 
                #original non-constant function which is using the 
                #constant function to generate the appropriate episode dose
                #and unit dose based on equal episode dose state:
                episode_dose = self.final_actual_updated_episode_dose
                episode_unit_dose = self.opioid_unit_dose
                return [episode_dose, episode_unit_dose]
            pass
        else:
            pass
        
        if self.secondary_med_current_taper is True:
            if self.is_constant_epdose is True:
                patient.secondary_opioid_episode_dose = self.final_actual_updated_episode_dose
                patient.secondary_opioid_unit_dose = [self.opioid_unit_dose]
                pass
            elif self.is_constant_epdose is False:
                #This returns list of episode dose and unit dose to the 
                #original non-constant function which is using the 
                #constant function to generate the appropriate episode dose
                #and unit dose based on equal episode dose state:
                episode_dose = self.final_actual_updated_episode_dose
                episode_unit_dose = self.opioid_unit_dose
                return [episode_dose, episode_unit_dose]
            pass
        else:
            pass
        
#        if self.tertiary_med_current_taper is True:
#            if self.is_constant_epdose is True:
#                patient.tertiary_opioid_episode_dose = self.final_actual_updated_episode_dose
#                patient.tertiary_opioid_unit_dose = [self.opioid_unit_dose]
#                pass
#            elif self.is_constant_epdose is False:
#                #This returns list of episode dose and unit dose to the 
#                #original non-constant function which is using the 
#                #constant function to generate the appropriate episode dose
#                #and unit dose based on equal episode dose state:
#                episode_dose = self.final_actual_updated_episode_dose
#                episode_unit_dose = self.opioid_unit_dose
#                return [episode_dose, episode_unit_dose]
#            pass
#        else:
#            pass
        pass
        
    def Active_Placebo_Capsule_Constant_Dose_Generator(self,
                                         patient,
                                         med_object):
        
        #Primary Med, constant dosing:
        if patient.primary_opioid_med != None:
            if patient.primary_opioid_med == med_object:
                if patient.different_daily_episode_doses_med_1 != 'Yes':
                    total_capsules_per_episode = patient.primary_opioid_captab_per_episode_dose
                    if isinstance(patient.primary_opioid_unit_dose, float) or isinstance(patient.primary_opioid_unit_dose, int):
                        number_active_capsules_per_episode = 1
                        pass
                    elif isinstance(patient.primary_opioid_unit_dose, tuple) or isinstance(patient.primary_opioid_unit_dose, list):
                        if None in patient.primary_opioid_unit_dose:
                            number_active_capsules_per_episode = 0
                            pass
                        else:
                            number_active_capsules_per_episode = len(patient.primary_opioid_unit_dose)
                            pass
                        pass
                    else:
                        number_active_capsules_per_episode = 0
                        pass
                    
                    number_placebo_capsules_per_episode = (total_capsules_per_episode - number_active_capsules_per_episode)
                    total_aggregate_24_hr_active_capsules = (patient.Number_episodes_per_24_hr(patient.primary_opioid_interdose_duration) * number_active_capsules_per_episode)
                    total_aggregate_24_hr_placebo_capsules = (patient.Number_episodes_per_24_hr(patient.primary_opioid_interdose_duration) * number_placebo_capsules_per_episode)
                    total_aggregate_24_hr_all_capsules = (total_aggregate_24_hr_active_capsules + total_aggregate_24_hr_placebo_capsules)
                    pass
                else:
                    pass
                pass
            else:
                pass
            pass
        elif patient.primary_opioid_med == None:
            if patient.primary_opioid_med == med_object:
                total_capsules_per_episode = patient.primary_opioid_captab_per_episode_dose
                number_active_capsules_per_episode = 0
                total_aggregate_24_hr_active_capsules = 0
                number_placebo_capsules_per_episode = total_capsules_per_episode - number_active_capsules_per_episode
                total_aggregate_24_hr_placebo_capsules = patient.Number_episodes_per_24_hr(patient.primary_opioid_interdose_duration) * number_placebo_capsules_per_episode
                total_aggregate_24_hr_all_capsules = total_aggregate_24_hr_active_capsules + total_aggregate_24_hr_placebo_capsules
        else:
            pass
        
        #Secondary Med, constant dosing:
        if patient.secondary_opioid_med != None:
            if patient.secondary_opioid_med == med_object:
                if patient.different_daily_episode_doses_med_2 != 'Yes':
                    total_capsules_per_episode = patient.secondary_opioid_captab_per_episode_dose
                    if isinstance(patient.secondary_opioid_unit_dose, float) or isinstance(patient.secondary_opioid_unit_dose, int):
                        number_active_capsules_per_episode = 1
                        pass
                    elif isinstance(patient.secondary_opioid_unit_dose, tuple) or isinstance(patient.secondary_opioid_unit_dose, list):
                        if None in patient.secondary_opioid_unit_dose:
                            number_active_capsules_per_episode = 0
                            pass
                        else:
                            number_active_capsules_per_episode = len(patient.secondary_opioid_unit_dose)
                            pass
                        pass
                    else:
                        number_active_capsules_per_episode = 0
                    
                    number_placebo_capsules_per_episode = (total_capsules_per_episode - number_active_capsules_per_episode)
                    total_aggregate_24_hr_active_capsules = (patient.Number_episodes_per_24_hr(patient.secondary_opioid_interdose_duration) * number_active_capsules_per_episode)
                    total_aggregate_24_hr_placebo_capsules = (patient.Number_episodes_per_24_hr(patient.secondary_opioid_interdose_duration) * number_placebo_capsules_per_episode)
                    total_aggregate_24_hr_all_capsules = (total_aggregate_24_hr_active_capsules + total_aggregate_24_hr_placebo_capsules)
                    pass
                else:
                    pass
                pass
            else:
                pass
            pass
        elif patient.secondary_opioid_med == None:
            if patient.secondary_opioid_med == med_object:
                total_capsules_per_episode = patient.secondary_opioid_captab_per_episode_dose
                number_active_capsules_per_episode = 0
                total_aggregate_24_hr_active_capsules = 0
                number_placebo_capsules_per_episode = total_capsules_per_episode - number_active_capsules_per_episode
                total_aggregate_24_hr_placebo_capsules = patient.Number_episodes_per_24_hr(patient.secondary_opioid_interdose_duration) * number_placebo_capsules_per_episode
                total_aggregate_24_hr_all_capsules = total_aggregate_24_hr_active_capsules + total_aggregate_24_hr_placebo_capsules
                
                
            pass
        else:
            pass
        
#        #Tertiary Med, constant dosing:
#        if patient.tertiary_opioid_med != None:
#            if patient.tertiary_opioid_med == med_object:
#                if patient.different_daily_episode_doses_med_3 != 'Yes':
#                    total_capsules_per_episode = patient.tertiary_opioid_captab_per_episode_dose
#                    number_active_capsules_per_episode = len(patient.tertiary_opioid_unit_dose)
#                    number_placebo_capsules_per_episode = (total_capsules_per_episode - number_active_capsules_per_episode)
#                    total_aggregate_24_hr_active_capsules = (patient.Number_episodes_per_24_hr(patient.tertiary_opioid_interdose_duration) * number_active_capsules_per_episode)
#                    total_aggregate_24_hr_placebo_capsules = (patient.Number_episodes_per_24_hr(patient.tertiary_opioid_interdose_duration) * number_placebo_capsules_per_episode)
#                    total_aggregate_24_hr_all_capsules = (total_aggregate_24_hr_active_capsules + total_aggregate_24_hr_placebo_capsules)
#                    pass
#                else:
#                    pass
#                pass
#            else:
#                pass
#            pass
#        elif patient.tertiary_opioid_med == None:
#            if patient.tertiary_opioid_med == med_object:
#                total_capsules_per_episode = patient.tertiary_opioid_captab_per_episode_dose
#                number_active_capsules_per_episode = 0
#                total_aggregate_24_hr_active_capsules = 0
#                number_placebo_capsules_per_episode = total_capsules_per_episode - number_active_capsules_per_episode
#                total_aggregate_24_hr_placebo_capsules = patient.Number_episodes_per_24_hr(patient.tertiary_opioid_interdose_duration) * number_placebo_capsules_per_episode
#                total_aggregate_24_hr_all_capsules = total_aggregate_24_hr_active_capsules + total_aggregate_24_hr_placebo_capsules
#            pass
#        else:
#            pass
        
        total_active_placebo_dict = {'Total Episode Capsules': total_capsules_per_episode,
                                     'Active Capsules': number_active_capsules_per_episode,
                                     'Placebo Capsules': number_placebo_capsules_per_episode,
                                     'Aggregate 24 hr Active Capsules': total_aggregate_24_hr_active_capsules,
                                     'Aggregate 24 hr Placebo Capsules': total_aggregate_24_hr_placebo_capsules,
                                     'Aggregate 24 hr All Capsules': total_aggregate_24_hr_all_capsules
                                     }
        
        return total_active_placebo_dict
       
    def Active_Placebo_Capsule_Nonconstant_Dose_Generator(self,
                                                          patient,
                                                          med_object):
        #Primary Med, non-constant dosing:
        if patient.primary_opioid_med != None:
            if patient.primary_opioid_med == med_object:
                if patient.different_daily_episode_doses_med_1 == 'Yes':
                    
                    #Episode 1:
                    total_capsules_per_episode_1 = patient.primary_opioid_dif_dose_captab_per_episode_dose_1
                    if total_capsules_per_episode_1 != None:
                        
                        if isinstance(patient.primary_opioid_dif_dose_ep_1_unit_dose, float) or isinstance(patient.primary_opioid_dif_dose_ep_1_unit_dose, int):
                            number_active_capsules_per_episode_1 = 1
                            pass
                        elif isinstance(patient.primary_opioid_dif_dose_ep_1_unit_dose, tuple) or isinstance(patient.primary_opioid_dif_dose_ep_1_unit_dose, list):
                            if None in patient.primary_opioid_dif_dose_ep_1_unit_dose:
                                number_active_capsules_per_episode_1 = 0
                                pass
                            else:
                                number_active_capsules_per_episode_1 = len(patient.primary_opioid_dif_dose_ep_1_unit_dose)
                            pass
                        else:
                            number_active_capsules_per_episode_1 = 0
                            pass
                        
                        number_placebo_capsules_per_episode_1 = (total_capsules_per_episode_1 - number_active_capsules_per_episode_1)
                        pass
                    else:
                        number_active_capsules_per_episode_1 = 0
                        number_placebo_capsules_per_episode_1 = 0
                        pass
                    
                    #Episode 2:
                    total_capsules_per_episode_2 = patient.primary_opioid_dif_dose_captab_per_episode_dose_2
                    if total_capsules_per_episode_2 != None:
                        if isinstance(patient.primary_opioid_dif_dose_ep_2_unit_dose, float) or isinstance(patient.primary_opioid_dif_dose_ep_2_unit_dose, int):
                            number_active_capsules_per_episode_2 = 1
                            pass
                        elif isinstance(patient.primary_opioid_dif_dose_ep_2_unit_dose, tuple) or isinstance(patient.primary_opioid_dif_dose_ep_2_unit_dose, list):
                            if None in patient.primary_opioid_dif_dose_ep_2_unit_dose:
                                number_active_capsules_per_episode_2 = 0
                                pass
                            else:
                                number_active_capsules_per_episode_2 = len(patient.primary_opioid_dif_dose_ep_2_unit_dose)
                                pass
                            pass
                        else:
                            number_active_capsules_per_episode_2 = 0
                            pass
                        
                        number_placebo_capsules_per_episode_2 = (total_capsules_per_episode_2 - number_active_capsules_per_episode_2)
                        pass
                    else:
                         number_active_capsules_per_episode_2 = 0
                         number_placebo_capsules_per_episode_2 = 0
                         pass
                     
                    #Episode 3:
                    total_capsules_per_episode_3 = patient.primary_opioid_dif_dose_captab_per_episode_dose_3
                    if total_capsules_per_episode_3 != None:
                        if isinstance(patient.primary_opioid_dif_dose_ep_3_unit_dose, float) or isinstance(patient.primary_opioid_dif_dose_ep_3_unit_dose, int):
                            number_active_capsules_per_episode_3 = 1
                            pass
                        elif isinstance(patient.primary_opioid_dif_dose_ep_3_unit_dose, tuple) or isinstance(patient.primary_opioid_dif_dose_ep_3_unit_dose, list):
                            if None in patient.primary_opioid_dif_dose_ep_3_unit_dose:
                                number_active_capsules_per_episode_3 = 0
                                pass
                            else:
                                number_active_capsules_per_episode_3 = len(patient.primary_opioid_dif_dose_ep_3_unit_dose)
                                pass
                            pass
                        else:
                            number_active_capsules_per_episode_3 = 0
                            pass
                        
                        number_placebo_capsules_per_episode_3 = (total_capsules_per_episode_3 - number_active_capsules_per_episode_3)
                        pass
                    else:
                        number_active_capsules_per_episode_3 = 0
                        number_placebo_capsules_per_episode_3 = 0
                        pass
                    
                    #Episode 4:
                    total_capsules_per_episode_4 = patient.primary_opioid_dif_dose_captab_per_episode_dose_4
                    if total_capsules_per_episode_4 != None:
                        if isinstance(patient.primary_opioid_dif_dose_ep_4_unit_dose, float) or isinstance(patient.primary_opioid_dif_dose_ep_4_unit_dose, int):
                            number_active_capsules_per_episode_4 = 1
                            pass
                        elif isinstance(patient.primary_opioid_dif_dose_ep_4_unit_dose, tuple) or isinstance(patient.primary_opioid_dif_dose_ep_4_unit_dose, list):
                            if None in patient.primary_opioid_dif_dose_ep_4_unit_dose:
                                number_active_capsules_per_episode_4 = 0
                                pass
                            else:
                                number_active_capsules_per_episode_4 = len(patient.primary_opioid_dif_dose_ep_4_unit_dose)
                                pass
                            pass
                        else:
                            number_active_capsules_per_episode_4 = 0
                            
                        number_placebo_capsules_per_episode_4 = (total_capsules_per_episode_4 - number_active_capsules_per_episode_4)
                        pass
                    else:
                        number_active_capsules_per_episode_4 = 0
                        number_placebo_capsules_per_episode_4 = 0
                        pass
                    
                    #Aggregate Measures:
                    list_to_remove = ['nan', 'NA', 'Nan', None]
                    
                    active_list = [number_active_capsules_per_episode_1,
                                   number_active_capsules_per_episode_2,
                                   number_active_capsules_per_episode_3,
                                   number_active_capsules_per_episode_4]
                    active_list = [epdose for epdose in active_list if epdose not in list_to_remove and not np.isnan(epdose)]
    
                    placebo_list = [number_placebo_capsules_per_episode_1,
                                    number_placebo_capsules_per_episode_2,
                                    number_placebo_capsules_per_episode_3,
                                    number_placebo_capsules_per_episode_4]
                    placebo_list = [epdose for epdose in placebo_list if epdose not in list_to_remove and not np.isnan(epdose)]
                    
                    total_aggregate_24_hr_active_capsules = sum(active_list)
                    
                    total_aggregate_24_hr_placebo_capsules = sum(placebo_list)
                    
                    total_aggregate_24_hr_all_capsules = (total_aggregate_24_hr_active_capsules + total_aggregate_24_hr_placebo_capsules)
                    pass
                else:
                    pass
                pass
            else:
                pass
            pass
        
        elif patient.primary_opioid_med == None:
            if patient.primary_opioid_med == med_object:
                
                total_capsules_per_episode_1= patient.primary_opioid_dif_dose_captab_per_episode_dose_1
                total_capsules_per_episode_2= patient.primary_opioid_dif_dose_captab_per_episode_dose_2
                total_capsules_per_episode_3= patient.primary_opioid_dif_dose_captab_per_episode_dose_3
                total_capsules_per_episode_4= patient.primary_opioid_dif_dose_captab_per_episode_dose_4
                
                number_active_capsules_per_episode_1 = 0
                number_active_capsules_per_episode_2 = 0
                number_active_capsules_per_episode_3 = 0
                number_active_capsules_per_episode_4 = 0
                
                if total_capsules_per_episode_1 != None:
                    number_placebo_capsules_per_episode_1 = total_capsules_per_episode_1 - number_active_capsules_per_episode_1
                    pass
                else: number_placebo_capsules_per_episode_1 = None
                if total_capsules_per_episode_2 != None:
                    number_placebo_capsules_per_episode_2 = total_capsules_per_episode_2 - number_active_capsules_per_episode_2
                    pass
                else: number_placebo_capsules_per_episode_2 = None
                if total_capsules_per_episode_3 != None:
                    number_placebo_capsules_per_episode_3 = total_capsules_per_episode_3 - number_active_capsules_per_episode_3
                    pass
                else:
                    number_placebo_capsules_per_episode_3 = None
                if total_capsules_per_episode_4 != None:
                    number_placebo_capsules_per_episode_4 = total_capsules_per_episode_4 - number_active_capsules_per_episode_4
                    pass
                else:
                    number_placebo_capsules_per_episode_4 = None
                
                total_aggregate_24_hr_active_capsules = 0
                total_aggregate_24_hr_all_capsules = sum(filter(None,[total_capsules_per_episode_1,
                                                          total_capsules_per_episode_2,
                                                          total_capsules_per_episode_3,
                                                          total_capsules_per_episode_4
                                                          ]))
                        
                
                total_aggregate_24_hr_placebo_capsules = total_aggregate_24_hr_all_capsules - total_aggregate_24_hr_active_capsules
                pass
            else:
                pass
            pass
        else:
            pass
        
        #Secondary Med, non-constant dosing:
        if patient.secondary_opioid_med != None:
            if patient.secondary_opioid_med == med_object:
                if patient.different_daily_episode_doses_med_2 == 'Yes':
                    
                    #Assign no dose reference to check against:
                    list_of_no_dose = [0, 0.0, None]
                    
                    #Episode 1:
                    total_capsules_per_episode_1 = patient.secondary_opioid_dif_dose_captab_per_episode_dose_1
                    if total_capsules_per_episode_1 != None:
                        if isinstance(patient.secondary_opioid_dif_dose_ep_1_unit_dose, numbers.Number):
                            if patient.secondary_opioid_dif_dose_ep_1_unit_dose > 0:
                                number_active_capsules_per_episode_1 = 1
                                pass
                            else:
                                number_active_capsules_per_episode_1 = 0
                                pass
                            pass
                        
                        elif pd.isnull(patient.secondary_opioid_dif_dose_ep_1_unit_dose):
                            number_active_capsules_per_episode_1 = 0
                            pass
                        
                        elif patient.secondary_opioid_dif_dose_ep_1_unit_dose in list_of_no_dose:
                            number_active_capsules_per_episode_1 = 0
                            pass
                        
                        elif isinstance(patient.secondary_opioid_dif_dose_ep_1_unit_dose, tuple) or isinstance(patient.secondary_opioid_dif_dose_ep_1_unit_dose, list):
                            if None in patient.secondary_opioid_dif_dose_ep_1_unit_dose:
                                number_active_capsules_per_episode_1 = 0
                                pass
                            else:
                                number_active_capsules_per_episode_1 = len(patient.secondary_opioid_dif_dose_ep_1_unit_dose)
                                pass
                            pass
                        else:
                            number_active_capsules_per_episode_1 = 0
                            pass
                        
                        number_placebo_capsules_per_episode_1 = (total_capsules_per_episode_1 - number_active_capsules_per_episode_1)
                        pass
                    else:
                        number_active_capsules_per_episode_1 = 0
                        number_placebo_capsules_per_episode_1 = 0
                        pass
                    
                    #Episode 2:
                    total_capsules_per_episode_2 = patient.secondary_opioid_dif_dose_captab_per_episode_dose_2
                    if total_capsules_per_episode_2 != None:
                        if isinstance(patient.secondary_opioid_dif_dose_ep_2_unit_dose, numbers.Number):
                            if patient.secondary_opioid_dif_dose_ep_2_unit_dose > 0:
                                number_active_capsules_per_episode_2 = 1
                                pass
                            else:
                                number_active_capsules_per_episode_2 = 0
                                pass
                            pass
                        
                        elif pd.isnull(patient.secondary_opioid_dif_dose_ep_2_unit_dose):
                            number_active_capsules_per_episode_2 = 0
                            pass
                        
                        elif patient.secondary_opioid_dif_dose_ep_2_unit_dose in list_of_no_dose:
                            number_active_capsules_per_episode_2 = 0
                            pass
                        
                        elif isinstance(patient.secondary_opioid_dif_dose_ep_2_unit_dose, tuple) or isinstance(patient.secondary_opioid_dif_dose_ep_2_unit_dose, list):
                            if None in patient.secondary_opioid_dif_dose_ep_2_unit_dose:
                                number_active_capsules_per_episode_2 = 0
                                pass
                            else:
                                number_active_capsules_per_episode_2 = len(patient.secondary_opioid_dif_dose_ep_2_unit_dose)
                                pass
                            pass
                        else:
                            number_active_capsules_per_episode_2 = 0
                            pass
                        
                        number_placebo_capsules_per_episode_2 = (total_capsules_per_episode_2 - number_active_capsules_per_episode_2)
                        pass
                    else:
                        number_active_capsules_per_episode_2 = 0
                        number_placebo_capsules_per_episode_2 = 0
                        pass
                    
                    #Episode 3:
                    total_capsules_per_episode_3 = patient.secondary_opioid_dif_dose_captab_per_episode_dose_3
                    if total_capsules_per_episode_3 != None:
                        if isinstance(patient.secondary_opioid_dif_dose_ep_3_unit_dose, numbers.Number):
                            if patient.secondary_opioid_dif_dose_ep_3_unit_dose > 0:
                                number_active_capsules_per_episode_3 = 1
                                pass
                            else:
                                number_active_capsules_per_episode_3 = 0
                                pass
                            pass
                        
                        elif pd.isnull(patient.secondary_opioid_dif_dose_ep_3_unit_dose):
                            number_active_capsules_per_episode_3 = 0
                            pass
                        
                        elif patient.secondary_opioid_dif_dose_ep_3_unit_dose in list_of_no_dose:
                            number_active_capsules_per_episode_3 = 0
                            pass
                        
                        elif isinstance(patient.secondary_opioid_dif_dose_ep_3_unit_dose, tuple) or isinstance(patient.secondary_opioid_dif_dose_ep_3_unit_dose, list):
                            if None in patient.secondary_opioid_dif_dose_ep_3_unit_dose:
                                number_active_capsules_per_episode_3 = 0
                                pass
                            else:
                                number_active_capsules_per_episode_3 = len(patient.secondary_opioid_dif_dose_ep_3_unit_dose)
                                pass
                            pass
                        
                        else:
                            number_active_capsules_per_episode_3 = 0
                            pass
                        
                        number_placebo_capsules_per_episode_3 = (total_capsules_per_episode_3 - number_active_capsules_per_episode_3)
                        pass
                    else:
                        number_active_capsules_per_episode_3 = 0
                        number_placebo_capsules_per_episode_3 = 0
                        pass
                    
                    #Episode 4:
                    total_capsules_per_episode_4 = patient.secondary_opioid_dif_dose_captab_per_episode_dose_4
                    if total_capsules_per_episode_4 != None:
                        if isinstance(patient.secondary_opioid_dif_dose_ep_4_unit_dose, numbers.Number):
                            if patient.secondary_opioid_dif_dose_ep_4_unit_dose > 0:
                                number_active_capsules_per_episode_4 = 1
                                pass
                            else:
                                number_active_capsules_per_episode_4 = 0
                                pass
                            pass
                        
                        elif pd.isnull(patient.secondary_opioid_dif_dose_ep_4_unit_dose):
                            number_active_capsules_per_episode_4 = 0
                            pass
                        
                        elif patient.secondary_opioid_dif_dose_ep_4_unit_dose in list_of_no_dose:
                            number_active_capsules_per_episode_4 = 0
                            pass
                        
                        elif isinstance(patient.secondary_opioid_dif_dose_ep_4_unit_dose, tuple) or isinstance(patient.secondary_opioid_dif_dose_ep_4_unit_dose, list):
                           if None in patient.secondary_opioid_dif_dose_ep_4_unit_dose:
                                number_active_capsules_per_episode_4 = 0
                                pass
                           else:
                               number_active_capsules_per_episode_4 = len(patient.secondary_opioid_dif_dose_ep_4_unit_dose)
                               pass
                           pass
                        else:
                            number_active_capsules_per_episode_4 = 0
                            pass
                        
                        number_placebo_capsules_per_episode_4 = (total_capsules_per_episode_4 - number_active_capsules_per_episode_4)
                        pass
                    else:
                        number_active_capsules_per_episode_4 = 0
                        number_placebo_capsules_per_episode_4 = 0
                        pass
                    
                    #Aggregate Measures:
                    list_to_remove = ['nan', 'NA', 'Nan', None]
                    active_list = [number_active_capsules_per_episode_1,
                                   number_active_capsules_per_episode_2,
                                   number_active_capsules_per_episode_3,
                                   number_active_capsules_per_episode_4]
                    active_list = [epdose for epdose in active_list if epdose not in list_to_remove and not np.isnan(epdose)]
                    placebo_list = [number_placebo_capsules_per_episode_1,
                                    number_placebo_capsules_per_episode_2,
                                    number_placebo_capsules_per_episode_3,
                                    number_placebo_capsules_per_episode_4]
                    placebo_list = [epdose for epdose in placebo_list if epdose not in list_to_remove and not np.isnan(epdose)]
                    
                    total_aggregate_24_hr_active_capsules = sum(active_list)
                    
                    total_aggregate_24_hr_placebo_capsules = sum(placebo_list)
                    
                    total_aggregate_24_hr_all_capsules = (total_aggregate_24_hr_active_capsules + total_aggregate_24_hr_placebo_capsules)
                    pass
                else:
                    pass
                pass
            else:
                pass
            pass
        elif patient.secondary_opioid_med == None:
            if patient.secondary_opioid_med == med_object:
                
                total_capsules_per_episode_1= patient.secondary_opioid_dif_dose_captab_per_episode_dose_1
                total_capsules_per_episode_2= patient.secondary_opioid_dif_dose_captab_per_episode_dose_2
                total_capsules_per_episode_3= patient.secondary_opioid_dif_dose_captab_per_episode_dose_3
                total_capsules_per_episode_4= patient.secondary_opioid_dif_dose_captab_per_episode_dose_4
                
                number_active_capsules_per_episode_1 = 0
                number_active_capsules_per_episode_2 = 0
                number_active_capsules_per_episode_3 = 0
                number_active_capsules_per_episode_4 = 0
                
                number_placebo_capsules_per_episode_1 = total_capsules_per_episode_1 - number_active_capsules_per_episode_1
                number_placebo_capsules_per_episode_2 = total_capsules_per_episode_2 - number_active_capsules_per_episode_2
                number_placebo_capsules_per_episode_3 = total_capsules_per_episode_3 - number_active_capsules_per_episode_3
                number_placebo_capsules_per_episode_4 = total_capsules_per_episode_4 - number_active_capsules_per_episode_4
                
                total_aggregate_24_hr_active_capsules = 0
                total_aggregate_24_hr_all_capsules = sum([total_capsules_per_episode_1,
                                                          total_capsules_per_episode_2,
                                                          total_capsules_per_episode_3,
                                                          total_capsules_per_episode_4
                                                          ])
                pass
            else:
                pass
            pass
        else:
            pass
        
#        #Tertiary Med, non-constant dosing:
#        if patient.tertiary_opioid_med != None:
#            if patient.tertiary_opioid_med == med_object:
#                if patient.different_daily_episode_doses_med_3 == 'Yes':
#                    
#                    #Episode 1:
#                    total_capsules_per_episode_1 = patient.tertiary_opioid_dif_dose_captab_per_episode_dose_1
#                    if type(patient.tertiary_opioid_dif_dose_ep_1_unit_dose) is int:
#                        number_active_capsules_per_episode_1 = 1
#                        pass
#                    else:
#                        number_active_capsules_per_episode_1 = len(patient.tertiary_opioid_dif_dose_ep_1_unit_dose)
#                        pass
#                    
#                    number_placebo_capsules_per_episode_1 = (total_capsules_per_episode_1 - number_active_capsules_per_episode_1)
#                    
#                    #Episode 2:
#                    total_capsules_per_episode_2 = patient.tertiary_opioid_dif_dose_captab_per_episode_dose_2
#                    if type(patient.tertiary_opioid_dif_dose_ep_2_unit_dose) is int:
#                        number_active_capsules_per_episode_2 = 1
#                        pass
#                    else:
#                        number_active_capsules_per_episode_2 = len(patient.tertiary_opioid_dif_dose_ep_2_unit_dose)
#                        pass
#                    
#                    number_placebo_capsules_per_episode_2 = (total_capsules_per_episode_2 - number_active_capsules_per_episode_2)
#                    
#                    #Episode 3:
#                    total_capsules_per_episode_3 = patient.tertiary_opioid_dif_dose_captab_per_episode_dose_3
#                    if type(patient.tertiary_opioid_dif_dose_ep_3_unit_dose) is int:
#                        number_active_capsules_per_episode_3 = 1
#                        pass
#                    else:
#                        number_active_capsules_per_episode_3 = len(patient.tertiary_opioid_dif_dose_ep_3_unit_dose)
#                        pass
#                    
#                    number_placebo_capsules_per_episode_3 = (total_capsules_per_episode_3 - number_active_capsules_per_episode_3)
#                    
#                    #Episode 4:
#                    total_capsules_per_episode_4 = patient.tertiary_opioid_dif_dose_captab_per_episode_dose_4
#                    if type(patient.tertiary_opioid_dif_dose_ep_4_unit_dose) is int:
#                        number_active_capsules_per_episode_4 = 1
#                        pass
#                    else:
#                        number_active_capsules_per_episode_4 = len(patient.tertiary_opioid_dif_dose_ep_4_unit_dose)
#                        pass
#                    
#                    number_placebo_capsules_per_episode_4 = (total_capsules_per_episode_4 - number_active_capsules_per_episode_4)
#                    
#                    #Aggregate Measures:
#                    list_to_remove = ['nan', 'NA', 'Nan', None]
#                    
#                    active_list = [number_active_capsules_per_episode_1,
#                                   number_active_capsules_per_episode_2,
#                                   number_active_capsules_per_episode_3,
#                                   number_active_capsules_per_episode_4]
#                    active_list = [epdose for epdose in active_list if epdose not in list_to_remove and not np.isnan(epdose)]
#    
#                    placebo_list = [number_placebo_capsules_per_episode_1,
#                                    number_placebo_capsules_per_episode_2,
#                                    number_placebo_capsules_per_episode_3,
#                                    number_placebo_capsules_per_episode_4]
#                    placebo_list = [epdose for epdose in placebo_list if epdose not in list_to_remove and not np.isnan(epdose)]
#                    
#                    total_aggregate_24_hr_active_capsules = sum(active_list)
#                    
#                    total_aggregate_24_hr_placebo_capsules = sum(placebo_list)
#                    
#                    total_aggregate_24_hr_all_capsules = (total_aggregate_24_hr_active_capsules + total_aggregate_24_hr_placebo_capsules)
#                    pass
#                   
#                else:
#                    pass
#                pass
#            else:
#                pass
#            pass
#        elif patient.tertiary_opioid_med == None:
#            if patient.tertiary_opioid_med == med_object:
#                
#                total_capsules_per_episode_1= patient.tertiary_opioid_dif_dose_captab_per_episode_dose_1
#                total_capsules_per_episode_2= patient.tertiary_opioid_dif_dose_captab_per_episode_dose_2
#                total_capsules_per_episode_3= patient.tertiary_opioid_dif_dose_captab_per_episode_dose_3
#                total_capsules_per_episode_4= patient.tertiary_opioid_dif_dose_captab_per_episode_dose_4
#                
#                number_active_capsules_per_episode_1 = 0
#                number_active_capsules_per_episode_2 = 0
#                number_active_capsules_per_episode_3 = 0
#                number_active_capsules_per_episode_4 = 0
#                
#                number_placebo_capsules_per_episode_1 = total_capsules_per_episode_1 - number_active_capsules_per_episode_1
#                number_placebo_capsules_per_episode_2 = total_capsules_per_episode_2 - number_active_capsules_per_episode_2
#                number_placebo_capsules_per_episode_3 = total_capsules_per_episode_3 - number_active_capsules_per_episode_3
#                number_placebo_capsules_per_episode_4 = total_capsules_per_episode_4 - number_active_capsules_per_episode_4
#                
#                total_aggregate_24_hr_active_capsules = 0
#                total_aggregate_24_hr_all_capsules = sum([total_capsules_per_episode_1,
#                                                          total_capsules_per_episode_2,
#                                                          total_capsules_per_episode_3,
#                                                          total_capsules_per_episode_4
#                                                          ])
#                pass
#            else:
#                pass
#            pass
#        else:
#            pass
        
        total_active_placebo_dict = {'Total Episode 1 Capsules': total_capsules_per_episode_1,
                                     'Total Episode 2 Capsules': total_capsules_per_episode_2,
                                     'Total Episode 3 Capsules': total_capsules_per_episode_3,
                                     'Total Episode 4 Capsules': total_capsules_per_episode_4,
                                     'Active Capsules Episode 1': number_active_capsules_per_episode_1,
                                     'Active Capsules Episode 2': number_active_capsules_per_episode_2,
                                     'Active Capsules Episode 3': number_active_capsules_per_episode_3,
                                     'Active Capsules Episode 4': number_active_capsules_per_episode_4,
                                     'Placebo Capsules Episode 1': number_placebo_capsules_per_episode_1,
                                     'Placebo Capsules Episode 2': number_placebo_capsules_per_episode_2,
                                     'Placebo Capsules Episode 3': number_placebo_capsules_per_episode_3,
                                     'Placebo Capsules Episode 4': number_placebo_capsules_per_episode_4,
                                     'Aggregate 24 hr Active Capsules': total_aggregate_24_hr_active_capsules,
                                     'Aggregate 24 hr Placebo Capsules': total_aggregate_24_hr_placebo_capsules,
                                     'Aggregate 24 hr All Capsules': total_aggregate_24_hr_all_capsules
                                     }
        
        return total_active_placebo_dict
    
    def Constant_episode_med_prescription(self,
                                 patient,
                                 med_object):
        
        #Goal of this class is to generate final prescription for pharmacy and 
        #patient. This includes:
        #Drug types/names
        #A = Dose of each drug (mg)
        #B = Number of tablets/capsules per dose
        #C = Frequency of dose
        #D =Total drug dose in 24 hr
        #E = Total tablets/capsules per 24 hr
        #X = Number of tablets/capsules with active opioid medication 
        #per dose = B 
        #Y = Number of capsules with placebo/control substance per
        #dose = starting number capsules - B
        
        #Constant or nonconstant episodes:
        
        #Constant dose episodes for given med:
        #Same number total capsules per episode, same episode dose, same unit doses
    
        #Non-constant dose episodes for given med:
        #Same or different number total capsules per episode (depending on initial
        #capsule counts per episode) 
        
        
        #Same or different episode doses/unit doses per episode
        #Primary constant-dose medication:
        if patient.primary_opioid_med == med_object:
            if patient.different_daily_episode_doses_med_1 != 'Yes': 
                capsule_dictionary = self.Active_Placebo_Capsule_Constant_Dose_Generator(patient, med_object)
                med_prescription_information = {'Primary Med Object': patient.primary_opioid_med,
                                                    'Primary Med Name': patient.primary_opioid_med_name,
                                                    'Primary Med Non-Constant Episode Dosing': patient.different_daily_episode_doses_med_1,
                                                    'Primary Med Episode Dose': patient.primary_opioid_episode_dose,
                                                    'Primary Med Episode Unit Dose': patient.primary_opioid_unit_dose,
                                                    'Primary Med Interdose Duration': patient.primary_opioid_interdose_duration,
                                                    'Primary Med Total CapTab per Episode Dose': patient.primary_opioid_captab_per_episode_dose
                                                    }
                merged_medication_information = {**med_prescription_information, **capsule_dictionary}
                return merged_medication_information
            elif patient.different_daily_episode_doses_med_1 == 'Yes':
                pass
            pass
        else:
            pass
                
        
        #Secondary constant-dose medication:
        if patient.secondary_opioid_med == med_object:
            if patient.different_daily_episode_doses_med_2 != 'Yes': 
                capsule_dictionary = self.Active_Placebo_Capsule_Constant_Dose_Generator(patient, med_object)
                med_prescription_information = {'Secondary Med Object': patient.secondary_opioid_med,
                                                    'Secondary Med Name': patient.secondary_opioid_med_name,
                                                    'Secondary Med Non-Constant Episode Dosing': patient.different_daily_episode_doses_med_2,
                                                    'Secondary Med Episode Dose': patient.secondary_opioid_episode_dose,
                                                    'Secondary Med Episode Unit Dose': patient.secondary_opioid_unit_dose,
                                                    'Secondary Med Interdose Duration': patient.secondary_opioid_interdose_duration,
                                                    'Secondary Med Total CapTab per Episode Dose': patient.secondary_opioid_captab_per_episode_dose
                                                    }
                merged_medication_information = {**med_prescription_information, **capsule_dictionary}     
                return merged_medication_information                    
            elif patient.different_daily_episode_doses_med_2 == 'Yes':
                pass
            pass
        else:
            pass
        
#        #Tertiary constant-dose medication:
#        if patient.tertiary_opioid_med == med_object:
#            if patient.different_daily_episode_doses_med_3 != 'Yes': 
#                capsule_dictionary = self.Active_Placebo_Capsule_Constant_Dose_Generator(patient, med_object)
#                med_prescription_information = {'Tertiary Med Object': patient.tertiary_opioid_med,
#                                            'Tertiary Med Name': patient.tertiary_opioid_med.med_name,
#                                            'Tertiary Med Non-Constant Episode Dosing': patient.different_daily_episode_doses_med_3,
#                                            'Tertiary Med Episode Dose': patient.tertiary_opioid_episode_dose,
#                                            'Tertiary Med Episode Unit Dose': patient.tertiary_opioid_unit_dose,
#                                            'Tertiary Med Interdose Duration': patient.tertiary_opioid_interdose_duration,
#                                            'Tertiary Med Total CapTab per Episode Dose': patient.tertiary_opioid_captab_per_episode_dose
#                                            }
#                merged_medication_information = {**med_prescription_information, **capsule_dictionary}
#                return merged_medication_information
#            elif patient.different_daily_episode_doses_med_3 == 'Yes':
#                pass
#            pass
#        else:
#            pass
    
    def Nonconstant_episode_med_prescription(self,
                                             patient,
                                             med_object):
        
        #Primary non-constant episode dose medication:
        if patient.primary_opioid_med == med_object:
            if patient.different_daily_episode_doses_med_1 == 'Yes':
                self.capsule_dictionary = self.Active_Placebo_Capsule_Nonconstant_Dose_Generator(patient, med_object)
                self.med_prescription_information = {'Primary Med Object': patient.primary_opioid_med,
                                                     'Primary Med Name': patient.primary_opioid_med_name,
                                                     'Primary Med Non-Constant Episode Dosing': patient.different_daily_episode_doses_med_1,
                                                     'Primary Med Episode Dose 1': patient.primary_opioid_dif_dose_episode_dose_1,
                                                     'Primary Med Episode Dose 2': patient.primary_opioid_dif_dose_episode_dose_2,
                                                     'Primary Med Episode Dose 3': patient.primary_opioid_dif_dose_episode_dose_3,
                                                     'Primary Med Episode Dose 4': patient.primary_opioid_dif_dose_episode_dose_4,
                                                     'Primary Med Episode Unit Dose 1': patient.primary_opioid_dif_dose_ep_1_unit_dose,
                                                     'Primary Med Episode Unit Dose 2': patient.primary_opioid_dif_dose_ep_2_unit_dose,
                                                     'Primary Med Episode Unit Dose 3': patient.primary_opioid_dif_dose_ep_3_unit_dose,
                                                     'Primary Med Episode Unit Dose 4': patient.primary_opioid_dif_dose_ep_4_unit_dose,
                                                     'Primary Med Total CapTab per Episode Dose 1': patient.primary_opioid_dif_dose_captab_per_episode_dose_1,
                                                     'Primary Med Total CapTab per Episode Dose 2': patient.primary_opioid_dif_dose_captab_per_episode_dose_2,
                                                     'Primary Med Total CapTab per Episode Dose 3': patient.primary_opioid_dif_dose_captab_per_episode_dose_3,
                                                     'Primary Med Total CapTab per Episode Dose 4': patient.primary_opioid_dif_dose_captab_per_episode_dose_4,
                                                     'Primary Med Interdose Duration': patient.primary_opioid_interdose_duration
                                                     }
            elif patient.different_daily_episode_doses_med_1 != 'Yes':
                pass
            pass
        else:
            pass
        
        #Secondary non-constant episode dose medication:
        if patient.secondary_opioid_med == med_object:
            if patient.different_daily_episode_doses_med_2 == 'Yes': 
                self.capsule_dictionary = self.Active_Placebo_Capsule_Nonconstant_Dose_Generator(patient, med_object)
                self.med_prescription_information = {'Secondary Med Object': patient.secondary_opioid_med,
                                                     'Secondary Med Name': patient.secondary_opioid_med_name,
                                                     'Secondary Med Non-Constant Episode Dosing': patient.different_daily_episode_doses_med_2,
                                                     'Secondary Med Episode Dose 1': patient.secondary_opioid_dif_dose_episode_dose_1,
                                                     'Secondary Med Episode Dose 2': patient.secondary_opioid_dif_dose_episode_dose_2,
                                                     'Secondary Med Episode Dose 3': patient.secondary_opioid_dif_dose_episode_dose_3,
                                                     'Secondary Med Episode Dose 4': patient.secondary_opioid_dif_dose_episode_dose_4,
                                                     'Secondary Med Episode Unit Dose 1': patient.secondary_opioid_dif_dose_ep_1_unit_dose,
                                                     'Secondary Med Episode Unit Dose 2': patient.secondary_opioid_dif_dose_ep_2_unit_dose,
                                                     'Secondary Med Episode Unit Dose 3': patient.secondary_opioid_dif_dose_ep_3_unit_dose,
                                                     'Secondary Med Episode Unit Dose 4': patient.secondary_opioid_dif_dose_ep_4_unit_dose,
                                                     'Secondary Med Total CapTab per Episode Dose 1': patient.secondary_opioid_dif_dose_captab_per_episode_dose_1,
                                                     'Secondary Med Total CapTab per Episode Dose 2': patient.secondary_opioid_dif_dose_captab_per_episode_dose_2,
                                                     'Secondary Med Total CapTab per Episode Dose 3': patient.secondary_opioid_dif_dose_captab_per_episode_dose_3,
                                                     'Secondary Med Total CapTab per Episode Dose 4': patient.secondary_opioid_dif_dose_captab_per_episode_dose_4,
                                                     'Secondary Med Interdose Duration': patient.secondary_opioid_interdose_duration
                                                     }
            elif patient.different_daily_episode_doses_med_2 != 'Yes':
                pass
            pass
        else:
            pass
        
#        #Tertiary non-constant episode dose medication:
#        if patient.tertiary_opioid_med == med_object:
#            if patient.different_daily_episode_doses_med_3 == 'Yes': 
#                self.capsule_dictionary = self.Active_Placebo_Capsule_Nonconstant_Dose_Generator(patient, med_object)
#                self.med_prescription_information = {'Tertiary Med Object': patient.tertiary_opioid_med,
#                                                     'Tertiary Med Name': patient.tertiary_opioid_med.med_name,
#                                                     'Tertiary Med Non-Constant Episode Dosing': patient.different_daily_episode_doses_med_3,
#                                                     'Tertiary Med Episode Dose 1': patient.tertiary_opioid_dif_dose_episode_dose_1,
#                                                     'Tertiary Med Episode Dose 2': patient.tertiary_opioid_dif_dose_episode_dose_2,
#                                                     'Tertiary Med Episode Dose 3': patient.tertiary_opioid_dif_dose_episode_dose_3,
#                                                     'Tertiary Med Episode Dose 4': patient.tertiary_opioid_dif_dose_episode_dose_4,
#                                                     'Tertiary Med Episode Unit Dose 1': patient.tertiary_opioid_dif_dose_ep_1_unit_dose,
#                                                     'Tertiary Med Episode Unit Dose 2': patient.tertiary_opioid_dif_dose_ep_2_unit_dose,
#                                                     'Tertiary Med Episode Unit Dose 3': patient.tertiary_opioid_dif_dose_ep_3_unit_dose,
#                                                     'Tertiary Med Episode Unit Dose 4': patient.tertiary_opioid_dif_dose_ep_4_unit_dose,
#                                                     'Tertiary Med Total CapTab per Episode Dose 1': patient.tertiary_opioid_dif_dose_captab_per_episode_dose_1,
#                                                     'Tertiary Med Total CapTab per Episode Dose 2': patient.tertiary_opioid_dif_dose_captab_per_episode_dose_2,
#                                                     'Tertiary Med Total CapTab per Episode Dose 3': patient.tertiary_opioid_dif_dose_captab_per_episode_dose_3,
#                                                     'Tertiary Med Total CapTab per Episode Dose 4': patient.tertiary_opioid_dif_dose_captab_per_episode_dose_4,
#                                                     'Tertiary Med Interdose Duration': patient.tertiary_opioid_interdose_duration
#                                                     }
#            elif patient.different_daily_episode_doses_med_3 != 'Yes':
#                pass
#            pass
#        else:
#            pass
        
        merged_medication_information = {**self.med_prescription_information, **self.capsule_dictionary}
        return merged_medication_information
    
    
    def Episode_1(self,
                  patient,
                  all_meds_dictionary):
        #Think of this as all the information needed by pharmacy to create
        #blister pack of pills for patient for episode #1 of day, using 
        #different medications, their adjusted episode doses, unit episode
        #dose per medication in active capsules, total active capsules per 
        #medication, total placebo capusules per medication
        
        #Primary Medication Episode 1:
        primary_med_dictionary = all_meds_dictionary['Primary_med']
        
        if primary_med_dictionary['Primary Med Non-Constant Episode Dosing'] == 'Yes':
            Primary_Med_Episode_1 = {'Primary Med Name': primary_med_dictionary['Primary Med Name'],
                                     'Primary Med Episode Dose 1': primary_med_dictionary['Primary Med Episode Dose 1'],
                                     'Primary Med Episode Unit Dose 1': primary_med_dictionary['Primary Med Episode Unit Dose 1'],
                                     'Primary Med Total Capsules Episode 1': primary_med_dictionary['Primary Med Total CapTab per Episode Dose 1'],
                                     'Primary Med Active Capsules Episode 1': primary_med_dictionary['Active Capsules Episode 1'],
                                     'Primary Med Placebo Capsules Episode 1': primary_med_dictionary['Placebo Capsules Episode 1'],
                                     'Primary Med Interdose Duration': primary_med_dictionary['Primary Med Interdose Duration']}
            pass
        elif primary_med_dictionary['Primary Med Non-Constant Episode Dosing'] != 'Yes':
            Primary_Med_Episode_1 = {'Primary Med Name': primary_med_dictionary['Primary Med Name'],
                                     'Primary Med Episode Dose 1': primary_med_dictionary['Primary Med Episode Dose'],
                                     'Primary Med Episode Unit Dose 1': primary_med_dictionary['Primary Med Episode Unit Dose'],
                                     'Primary Med Total Capsules Episode 1': primary_med_dictionary['Primary Med Total CapTab per Episode Dose'],
                                     'Primary Med Active Capsules Episode 1': primary_med_dictionary['Active Capsules'],
                                     'Primary Med Placebo Capsules Episode 1': primary_med_dictionary['Placebo Capsules'],
                                     'Primary Med Interdose Duration': primary_med_dictionary['Primary Med Interdose Duration']}
            pass
        else:
            pass
        
        #Secondary Medication Episode 1:
        secondary_med_dictionary = all_meds_dictionary['Secondary_med']
        
        if secondary_med_dictionary['Secondary Med Non-Constant Episode Dosing'] == 'Yes':
            Secondary_Med_Episode_1 = {'Secondary Med Name': secondary_med_dictionary['Secondary Med Name'],
                                     'Secondary Med Episode Dose 1': secondary_med_dictionary['Secondary Med Episode Dose 1'],
                                     'Secondary Med Episode Unit Dose 1': secondary_med_dictionary['Secondary Med Episode Unit Dose 1'],
                                     'Secondary Med Total Capsules Episode 1': secondary_med_dictionary['Secondary Med Total CapTab per Episode Dose 1'],
                                     'Secondary Med Active Capsules Episode 1': secondary_med_dictionary['Active Capsules Episode 1'],
                                     'Secondary Med Placebo Capsules Episode 1': secondary_med_dictionary['Placebo Capsules Episode 1'],
                                     'Secondary Med Interdose Duration': secondary_med_dictionary['Secondary Med Interdose Duration']}
            pass
        elif secondary_med_dictionary['Secondary Med Non-Constant Episode Dosing'] != 'Yes':
            Secondary_Med_Episode_1 = {'Secondary Med Name': secondary_med_dictionary['Secondary Med Name'],
                                     'Secondary Med Episode Dose 1': secondary_med_dictionary['Secondary Med Episode Dose'],
                                     'Secondary Med Episode Unit Dose 1': secondary_med_dictionary['Secondary Med Episode Unit Dose'],
                                     'Secondary Med Total Capsules Episode 1': secondary_med_dictionary['Secondary Med Total CapTab per Episode Dose'],
                                     'Secondary Med Active Capsules Episode 1': secondary_med_dictionary['Active Capsules'],
                                     'Secondary Med Placebo Capsules Episode 1': secondary_med_dictionary['Placebo Capsules'],
                                     'Secondary Med Interdose Duration': secondary_med_dictionary['Secondary Med Interdose Duration']}
            pass
        else:
            pass
        
#        #Tertiary Medication Episode 1:
#        tertiary_med_dictionary = all_meds_dictionary['Tertiary_med']
#        
#        if patient.tertiary_opioid_med != None:
#            if  tertiary_med_dictionary['Tertiary Med Non-Constant Episode Dosing'] == 'Yes':
#                tertiary_med_episode_1 = {'Tertiary Med Name':  tertiary_med_dictionary['Tertiary Med Name'],
#                                         'Tertiary Med Episode Dose 1':  tertiary_med_dictionary['Tertiary Med Episode Dose 1'],
#                                         'Tertiary Med Episode Unit Dose 1':  tertiary_med_dictionary['Tertiary Med Episode Unit Dose 1'],
#                                         'Tertiary Med Total Capsules Episode 1':  tertiary_med_dictionary['Tertiary Med Total CapTab per Episode Dose 1'],
#                                         'Tertiary Med Active Capsules Episode 1':  tertiary_med_dictionary['Tertiary Capsules Episode 1'],
#                                         'Tertiary Med Placebo Capsules Episode 1':  tertiary_med_dictionary['Tertiary Capsules Episode 1'],
#                                         'Tertiary Med Interdose Duration':  tertiary_med_dictionary['Tertiary Med Interdose Duration']}
#                pass
#            elif  tertiary_med_dictionary['Tertiary Med Non-Constant Episode Dosing'] != 'Yes':
#                tertiary_med_episode_1 = {'Tertiary Med Name':  tertiary_med_dictionary['Tertiary Med Name'],
#                                         'Tertiary Med Episode Dose 1':  tertiary_med_dictionary['Tertiary Med Episode Dose'],
#                                         'Tertiary Med Episode Unit Dose 1':  tertiary_med_dictionary['Tertiary Med Episode Unit Dose'],
#                                         'Tertiary Med Total Capsules Episode 1':  tertiary_med_dictionary['Tertiary Med Total CapTab per Episode Dose'],
#                                         'Tertiary Med Active Capsules Episode 1':  tertiary_med_dictionary['Active Capsules'],
#                                         'Tertiary Med Placebo Capsules Episode 1':  tertiary_med_dictionary['Placebo Capsules'],
#                                         'Tertiary Med Interdose Duration':  tertiary_med_dictionary['Tertiary Med Interdose Duration']}
#                pass
#            else:
#                pass
#            pass
#        elif patient.tertiary_opioid_med == None:
#            tertiary_med_episode_1 = None
#            pass
#        else:
#            pass
        
        episode_1_prescription = {'Primary Opioid Med Episode 1' : Primary_Med_Episode_1,
                                  'Secondary Opioid Med Episode 1' : Secondary_Med_Episode_1}
#                                  'tertiary_opioid_med_ep_1': tertiary_med_episode_1}
        
        return episode_1_prescription
    
    def Episode_2(self,
                  patient,
                  all_meds_dictionary):
        #Think of this as all the information needed by pharmacy to create
        #blister pack of pills for patient for episode #2 of day:
        
        #Primary Medication Episode 2:
        
        #Identify whether the primary medication has a second episode:
        if patient.primary_opioid_interdose_duration != None:
            if patient.primary_opioid_interdose_duration < 24:
                
                primary_med_dictionary = all_meds_dictionary['Primary_med']
                
                if primary_med_dictionary['Primary Med Non-Constant Episode Dosing'] == 'Yes':
                    primary_med_episode_2 = {'Primary Med Name': primary_med_dictionary['Primary Med Name'],
                                             'Primary Med Episode Dose 2': primary_med_dictionary['Primary Med Episode Dose 2'],
                                             'Primary Med Episode Unit Dose 2': primary_med_dictionary['Primary Med Episode Unit Dose 2'],
                                             'Primary Med Total Capsules Episode 2': primary_med_dictionary['Primary Med Total CapTab per Episode Dose 2'],
                                             'Primary Med Active Capsules Episode 2': primary_med_dictionary['Active Capsules Episode 2'],
                                             'Primary Med Placebo Capsules Episode 2': primary_med_dictionary['Placebo Capsules Episode 2'],
                                             'Primary Med Interdose Duration': primary_med_dictionary['Primary Med Interdose Duration']}
                    pass
                elif primary_med_dictionary['Primary Med Non-Constant Episode Dosing'] != 'Yes':
                    primary_med_episode_2 = {'Primary Med Name': primary_med_dictionary['Primary Med Name'],
                                             'Primary Med Episode Dose 2': primary_med_dictionary['Primary Med Episode Dose'],
                                             'Primary Med Episode Unit Dose 2': primary_med_dictionary['Primary Med Episode Unit Dose'],
                                             'Primary Med Total Capsules Episode 2': primary_med_dictionary['Primary Med Total CapTab per Episode Dose'],
                                             'Primary Med Active Capsules Episode 2': primary_med_dictionary['Active Capsules'],
                                             'Primary Med Placebo Capsules Episode 2': primary_med_dictionary['Placebo Capsules'],
                                             'Primary Med Interdose Duration': primary_med_dictionary['Primary Med Interdose Duration']}
                    pass
                else:
                    pass
                pass
            else:
                primary_med_episode_2 = None
                pass
            pass
        elif patient.primary_opioid_interdose_duration == None:
            primary_med_episode_2 = None
            pass
        else:
            pass
        
        #Secondary Medication Episode 2:
        if patient.secondary_opioid_interdose_duration != None:
            if patient.secondary_opioid_interdose_duration <= 24:
                secondary_med_dictionary = all_meds_dictionary['Secondary_med']
                
                if secondary_med_dictionary['Secondary Med Non-Constant Episode Dosing'] == 'Yes':
                    secondary_med_episode_2 = {'Secondary Med Name': secondary_med_dictionary['Secondary Med Name'],
                                             'Secondary Med Episode Dose 2': secondary_med_dictionary['Secondary Med Episode Dose 2'],
                                             'Secondary Med Episode Unit Dose 2': secondary_med_dictionary['Secondary Med Episode Unit Dose 2'],
                                             'Secondary Med Total Capsules Episode 2': secondary_med_dictionary['Secondary Med Total CapTab per Episode Dose 2'],
                                             'Secondary Med Active Capsules Episode 2': secondary_med_dictionary['Active Capsules Episode 2'],
                                             'Secondary Med Placebo Capsules Episode 2': secondary_med_dictionary['Placebo Capsules Episode 2'],
                                             'Secondary Med Interdose Duration': secondary_med_dictionary['Secondary Med Interdose Duration']}
                    pass
                elif secondary_med_dictionary['Secondary Med Non-Constant Episode Dosing'] != 'Yes':
                    secondary_med_episode_2 = {'Secondary Med Name': secondary_med_dictionary['Secondary Med Name'],
                                             'Secondary Med Episode Dose 2': secondary_med_dictionary['Secondary Med Episode Dose'],
                                             'Secondary Med Episode Unit Dose 2': secondary_med_dictionary['Secondary Med Episode Unit Dose'],
                                             'Secondary Med Total Capsules Episode 2': secondary_med_dictionary['Secondary Med Total CapTab per Episode Dose'],
                                             'Secondary Med Active Capsules Episode 2': secondary_med_dictionary['Active Capsules'],
                                             'Secondary Med Placebo Capsules Episode 2': secondary_med_dictionary['Placebo Capsules'],
                                             'Secondary Med Interdose Duration': secondary_med_dictionary['Secondary Med Interdose Duration']}
                    pass
                else:
                    secondary_med_episode_2 = None
                    pass
                pass
            else:
                secondary_med_episode_2 = None
                pass
            pass
        elif patient.secondary_opioid_interdose_duration == None:
            secondary_med_episode_2 = None
            pass
        else:
            pass
    
#        #Tertiary Medication Episode 1:
#        if patient.tertiary_opioid_med != None:
#            tertiary_med_dictionary = all_meds_dictionary['Tertiary_med']
#            if  tertiary_med_dictionary['Tertiary Med Non-Constant Episode Dosing'] == 'Yes':
#                tertiary_med_episode_2 = {'Tertiary Med Name':  tertiary_med_dictionary['Tertiary Med Name'],
#                                         'Tertiary Med Episode Dose 2':  tertiary_med_dictionary['Tertiary Med Episode Dose 2'],
#                                         'Tertiary Med Episode Unit Dose 2':  tertiary_med_dictionary['Tertiary Med Episode Unit Dose 2'],
#                                         'Tertiary Med Total Capsules Episode 2':  tertiary_med_dictionary['Tertiary Med Total CapTab per Episode Dose 2'],
#                                         'Tertiary Med Active Capsules Episode 2':  tertiary_med_dictionary['Tertiary Capsules Episode 2'],
#                                         'Tertiary Med Placebo Capsules Episode 2':  tertiary_med_dictionary['Tertiary Capsules Episode 2'],
#                                         'Tertiary Med Interdose Duration':  tertiary_med_dictionary['Tertiary Med Interdose Duration']}
#                pass
#            elif  tertiary_med_dictionary['Tertiary Med Non-Constant Episode Dosing'] != 'Yes':
#                tertiary_med_episode_2 = {'Tertiary Med Name':  tertiary_med_dictionary['Tertiary Med Name'],
#                                         'Tertiary Med Episode Dose 2':  tertiary_med_dictionary['Tertiary Med Episode Dose'],
#                                         'Tertiary Med Episode Unit Dose 2':  tertiary_med_dictionary['Tertiary Med Episode Unit Dose'],
#                                         'Tertiary Med Total Capsules Episode 2':  tertiary_med_dictionary['Tertiary Med Total CapTab per Episode Dose'],
#                                         'Tertiary Med Active Capsules Episode 2':  tertiary_med_dictionary['Active Capsules'],
#                                         'Tertiary Med Placebo Capsules Episode 2':  tertiary_med_dictionary['Placebo Capsules'],
#                                         'Tertiary Med Interdose Duration':  tertiary_med_dictionary['Tertiary Med Interdose Duration']}
#                pass
#            else:
#                pass
#            pass
#        elif patient.tertiary_opioid_med == None:
#            tertiary_med_episode_2 = None
#            pass
#        else:
#            pass
        
        episode_2_prescription = {'Primary Opioid Med Episode 2' : primary_med_episode_2,
                                  'Secondary Opioid Med Episode 2' : secondary_med_episode_2}
#                                  'tertiary_opioid_med_ep_2': tertiary_med_episode_2}

        return episode_2_prescription
    
    def Episode_3(self,
                  patient,
                  all_meds_dictionary):
        #Think of this as all the information needed by pharmacy to create
        #blister pack of pills for patient for episode #3 of day:
    
        
        #Primary Medication Episode 3:
        if patient.primary_opioid_interdose_duration != None:
            if patient.primary_opioid_interdose_duration <= 8:
                primary_med_dictionary = all_meds_dictionary['Primary_med']
                   
                if primary_med_dictionary['Primary Med Non-Constant Episode Dosing'] == 'Yes':
                    primary_med_episode_3 = {'Primary Med Name': primary_med_dictionary['Primary Med Name'],
                                             'Primary Med Episode Dose 3': primary_med_dictionary['Primary Med Episode Dose 3'],
                                             'Primary Med Episode Unit Dose 3': primary_med_dictionary['Primary Med Episode Unit Dose 3'],
                                             'Primary Med Total Capsules Episode 3': primary_med_dictionary['Primary Med Total CapTab per Episode Dose 3'],
                                             'Primary Med Active Capsules Episode 3': primary_med_dictionary['Active Capsules Episode 3'],
                                             'Primary Med Placebo Capsules Episode 3': primary_med_dictionary['Placebo Capsules Episode 3'],
                                             'Primary Med Interdose Duration': primary_med_dictionary['Primary Med Interdose Duration']}
                    pass
                elif primary_med_dictionary['Primary Med Non-Constant Episode Dosing'] != 'Yes':
                    primary_med_episode_3 = {'Primary Med Name': primary_med_dictionary['Primary Med Name'],
                                             'Primary Med Episode Dose 3': primary_med_dictionary['Primary Med Episode Dose'],
                                             'Primary Med Episode Unit Dose 3': primary_med_dictionary['Primary Med Episode Unit Dose'],
                                             'Primary Med Total Capsules Episode 3': primary_med_dictionary['Primary Med Total CapTab per Episode Dose'],
                                             'Primary Med Active Capsules Episode 3': primary_med_dictionary['Active Capsules'],
                                             'Primary Med Placebo Capsules Episode 3': primary_med_dictionary['Placebo Capsules'],
                                             'Primary Med Interdose Duration': primary_med_dictionary['Primary Med Interdose Duration']}
                    pass
                else:
                    primary_med_episode_3 = None
                    pass
                pass
            else:
                primary_med_episode_3 = None
                pass
            pass
        elif patient.primary_episode_interdose_duration == None:
            primary_med_episode_3 = None
            pass
        else:
            pass
        
        #Secondary Medication Episode 3:
        if patient.secondary_opioid_interdose_duration != None:
            if patient.secondary_opioid_interdose_duration <= 8:
                secondary_med_dictionary = all_meds_dictionary['Secondary_med']
        
                if secondary_med_dictionary['Secondary Med Non-Constant Episode Dosing'] == 'Yes':
                    secondary_med_episode_3 = {'Secondary Med Name': secondary_med_dictionary['Secondary Med Name'],
                                             'Secondary Med Episode Dose 3': secondary_med_dictionary['Secondary Med Episode Dose 3'],
                                             'Secondary Med Episode Unit Dose 3': secondary_med_dictionary['Secondary Med Episode Unit Dose 3'],
                                             'Secondary Med Total Capsules Episode 3': secondary_med_dictionary['Secondary Med Total CapTab per Episode Dose 3'],
                                             'Secondary Med Active Capsules Episode 3': secondary_med_dictionary['Active Capsules Episode 3'],
                                             'Secondary Med Placebo Capsules Episode 3': secondary_med_dictionary['Placebo Capsules Episode 3'],
                                             'Secondary Med Interdose Duration': secondary_med_dictionary['Secondary Med Interdose Duration']}
                    pass
                elif secondary_med_dictionary['Secondary Med Non-Constant Episode Dosing'] != 'Yes':
                    secondary_med_episode_3 = {'Secondary Med Name': secondary_med_dictionary['Secondary Med Name'],
                                             'Secondary Med Episode Dose 3': secondary_med_dictionary['Secondary Med Episode Dose'],
                                             'Secondary Med Episode Unit Dose 3': secondary_med_dictionary['Secondary Med Episode Unit Dose'],
                                             'Secondary Med Total Capsules Episode 3': secondary_med_dictionary['Secondary Med Total CapTab per Episode Dose'],
                                             'Secondary Med Active Capsules Episode 3': secondary_med_dictionary['Active Capsules'],
                                             'Secondary Med Placebo Capsules Episode 3': secondary_med_dictionary['Placebo Capsules'],
                                             'Secondary Med Interdose Duration': secondary_med_dictionary['Secondary Med Interdose Duration']}
                    pass
                else:
                    secondary_med_episode_3 = None
                    pass
                pass
            else:
                secondary_med_episode_3 = None
                pass
            pass
        elif patient.secondary_episode_interdose_duration == None:
            secondary_med_episode_3 = None
            pass
        else:
            pass
        
#        #Tertiary Medication Episode 3:
#        if patient.tertiary_opioid_med != None:
#            tertiary_med_dictionary = all_meds_dictionary['Tertiary_med']
#            if  tertiary_med_dictionary['Tertiary Med Non-Constant Episode Dosing'] == 'Yes':
#                tertiary_med_episode_3 = {'Tertiary Med Name':  tertiary_med_dictionary['Tertiary Med Name'],
#                                         'Tertiary Med Episode Dose 3':  tertiary_med_dictionary['Tertiary Med Episode Dose 3'],
#                                         'Tertiary Med Episode Unit Dose 3':  tertiary_med_dictionary['Tertiary Med Episode Unit Dose 3'],
#                                         'Tertiary Med Total Capsules Episode 3':  tertiary_med_dictionary['Tertiary Med Total CapTab per Episode Dose 3'],
#                                         'Tertiary Med Active Capsules Episode 3':  tertiary_med_dictionary['Tertiary Capsules Episode 3'],
#                                         'Tertiary Med Placebo Capsules Episode 3':  tertiary_med_dictionary['Tertiary Capsules Episode 3'],
#                                         'Tertiary Med Interdose Duration':  tertiary_med_dictionary['Tertiary Med Interdose Duration']}
#                pass
#            elif  tertiary_med_dictionary['Tertiary Med Non-Constant Episode Dosing'] != 'Yes':
#                tertiary_med_episode_3 = {'Tertiary Med Name':  tertiary_med_dictionary['Tertiary Med Name'],
#                                         'Tertiary Med Episode Dose 3':  tertiary_med_dictionary['Tertiary Med Episode Dose'],
#                                         'Tertiary Med Episode Unit Dose 3':  tertiary_med_dictionary['Tertiary Med Episode Unit Dose'],
#                                         'Tertiary Med Total Capsules Episode 3':  tertiary_med_dictionary['Tertiary Med Total CapTab per Episode Dose'],
#                                         'Tertiary Med Active Capsules Episode 3':  tertiary_med_dictionary['Active Capsules'],
#                                         'Tertiary Med Placebo Capsules Episode 3':  tertiary_med_dictionary['Placebo Capsules'],
#                                         'Tertiary Med Interdose Duration':  tertiary_med_dictionary['Tertiary Med Interdose Duration']}
#                pass
#            else:
#                pass
#            pass
#        elif patient.tertiary_opioid_med == None:
#            tertiary_med_episode_3 = None
#            pass
#        else:
#            pass
        
        episode_3_prescription = {'Primary Opioid Med Episode 3' : primary_med_episode_3,
                                  'Secondary Opioid Med Episode 3' : secondary_med_episode_3}
#                                  'tertiary_opioid_med_ep_3': tertiary_med_episode_3}

        return episode_3_prescription
    
    def Episode_4(self,
                  patient,
                  all_meds_dictionary):
        #Think of this as all the information needed by pharmacy to create
        #blister pack of pills for patient for episode #4 of day:
        
        #Primary Medication Episode 4:
        if patient.primary_opioid_interdose_duration != None:
            if patient.primary_opioid_interdose_duration <= 6:
                if patient.primary_opioid_med != None:
                    primary_med_dictionary = all_meds_dictionary['Primary_med']
                    if primary_med_dictionary['Primary Med Non-Constant Episode Dosing'] == 'Yes':
                        primary_med_episode_4 = {'Primary Med Name': primary_med_dictionary['Primary Med Name'],
                                         'Primary Med Episode Dose 4': primary_med_dictionary['Primary Med Episode Dose 4'],
                                         'Primary Med Episode Unit Dose 4': primary_med_dictionary['Primary Med Episode Unit Dose 4'],
                                         'Primary Med Total Capsules Episode 4': primary_med_dictionary['Primary Med Total CapTab per Episode Dose 4'],
                                         'Primary Med Active Capsules Episode 4': primary_med_dictionary['Active Capsules Episode 4'],
                                         'Primary Med Placebo Capsules Episode 4': primary_med_dictionary['Placebo Capsules Episode 4'],
                                         'Primary Med Interdose Duration': primary_med_dictionary['Primary Med Interdose Duration']}
                        pass
                    elif primary_med_dictionary['Primary Med Non-Constant Episode Dosing'] != 'Yes':
                        primary_med_episode_4 = {'Primary Med Name': primary_med_dictionary['Primary Med Name'],
                                                 'Primary Med Episode Dose 4': primary_med_dictionary['Primary Med Episode Dose'],
                                                 'Primary Med Episode Unit Dose 4': primary_med_dictionary['Primary Med Episode Unit Dose'],
                                                 'Primary Med Total Capsules Episode 4': primary_med_dictionary['Primary Med Total CapTab per Episode Dose'],
                                                 'Primary Med Active Capsules Episode 4': primary_med_dictionary['Active Capsules'],
                                                 'Primary Med Placebo Capsules Episode 4': primary_med_dictionary['Placebo Capsules'],
                                                 'Primary Med Interdose Duration': primary_med_dictionary['Primary Med Interdose Duration']}
                        pass
                    else:
                        primary_med_episode_4 = None
                        pass
                    pass
                else:
                    pass
                pass
            else:
                primary_med_episode_4 = None
                pass
            pass

        elif patient.primary_opioid_med == None:
            primary_med_episode_4 = None
            pass
        else:
            pass
        
        #Secondary Medication Episode 4:
        if patient.secondary_opioid_interdose_duration != None:
            if patient.secondary_opioid_interdose_duration <= 6:
                if patient.secondary_opioid_med != None:
                    secondary_med_dictionary = all_meds_dictionary['Secondary_med']
                    if secondary_med_dictionary['Secondary Med Non-Constant Episode Dosing'] == 'Yes':
                        secondary_med_episode_4 = {'Secondary Med Name': secondary_med_dictionary['Secondary Med Name'],
                                                 'Secondary Med Episode Dose 4': secondary_med_dictionary['Secondary Med Episode Dose 4'],
                                                 'Secondary Med Episode Unit Dose 4': secondary_med_dictionary['Secondary Med Episode Unit Dose 4'],
                                                 'Secondary Med Total Capsules Episode 4': secondary_med_dictionary['Secondary Med Total CapTab per Episode Dose 4'],
                                                 'Secondary Med Active Capsules Episode 4': secondary_med_dictionary['Active Capsules Episode 4'],
                                                 'Secondary Med Placebo Capsules Episode 4': secondary_med_dictionary['Placebo Capsules Episode 4'],
                                                 'Secondary Med Interdose Duration': secondary_med_dictionary['Secondary Med Interdose Duration']}
                        pass
                    elif secondary_med_dictionary['Secondary Med Non-Constant Episode Dosing'] != 'Yes':
                        secondary_med_episode_4 = {'Secondary Med Name': secondary_med_dictionary['Secondary Med Name'],
                                                 'Secondary Med Episode Dose 4': secondary_med_dictionary['Secondary Med Episode Dose'],
                                                 'Secondary Med Episode Unit Dose 4': secondary_med_dictionary['Secondary Med Episode Unit Dose'],
                                                 'Secondary Med Total Capsules Episode 4': secondary_med_dictionary['Secondary Med Total CapTab per Episode Dose'],
                                                 'Secondary Med Active Capsules Episode 4': secondary_med_dictionary['Active Capsules'],
                                                 'Secondary Med Placebo Capsules Episode 4': secondary_med_dictionary['Placebo Capsules'],
                                                 'Secondary Med Interdose Duration': secondary_med_dictionary['Secondary Med Interdose Duration']}
                        pass
                    else:
                        secondary_med_episode_4 = None
                        pass
                    pass
                else:
                    secondary_med_episode_4 = None
                    pass
                pass
            else:
                secondary_med_episode_4 = None
                pass
            pass
        elif patient.secondary_opioid_med == None:
           secondary_med_episode_4 = None
           pass
        else:
            pass
        
#        #Tertiary Medication Episode 4:
#        if patient.tertiary_opioid_med != None:
#            tertiary_med_dictionary = all_meds_dictionary['Tertiary_med']
#            if  tertiary_med_dictionary['Tertiary Med Non-Constant Episode Dosing'] == 'Yes':
#                tertiary_med_episode_4 = {'Tertiary Med Name':  tertiary_med_dictionary['Tertiary Med Name'],
#                                         'Tertiary Med Episode Dose 4':  tertiary_med_dictionary['Tertiary Med Episode Dose 4'],
#                                         'Tertiary Med Episode Unit Dose 4':  tertiary_med_dictionary['Tertiary Med Episode Unit Dose 4'],
#                                         'Tertiary Med Total Capsules Episode 4':  tertiary_med_dictionary['Tertiary Med Total CapTab per Episode Dose 4'],
#                                         'Tertiary Med Active Capsules Episode 4':  tertiary_med_dictionary['Tertiary Capsules Episode 4'],
#                                         'Tertiary Med Placebo Capsules Episode 4':  tertiary_med_dictionary['Tertiary Capsules Episode 4'],
#                                         'Tertiary Med Interdose Duration':  tertiary_med_dictionary['Tertiary Med Interdose Duration']}
#                pass
#            elif  tertiary_med_dictionary['Tertiary Med Non-Constant Episode Dosing'] != 'Yes':
#                tertiary_med_episode_4 = {'Tertiary Med Name':  tertiary_med_dictionary['Tertiary Med Name'],
#                                         'Tertiary Med Episode Dose 4':  tertiary_med_dictionary['Tertiary Med Episode Dose'],
#                                         'Tertiary Med Episode Unit Dose 4':  tertiary_med_dictionary['Tertiary Med Episode Unit Dose'],
#                                         'Tertiary Med Total Capsules Episode 4':  tertiary_med_dictionary['Tertiary Med Total CapTab per Episode Dose'],
#                                         'Tertiary Med Active Capsules Episode 4':  tertiary_med_dictionary['Active Capsules'],
#                                         'Tertiary Med Placebo Capsules Episode 4':  tertiary_med_dictionary['Placebo Capsules'],
#                                         'Tertiary Med Interdose Duration':  tertiary_med_dictionary['Tertiary Med Interdose Duration']}
#                pass
#            else:
#                pass
#            pass
#        elif patient.tertiary_opioid_med == None:
#            tertiary_med_episode_4 = None
#            pass
#        else:
#            pass
        
        episode_4_prescription = {'Primary Opioid Med Episode 4' : primary_med_episode_4,
                                  'Secondary Opioid Med Episode 4' : secondary_med_episode_4}
#                                  'tertiary_opioid_med_ep_4': tertiary_med_episode_4}

        return episode_4_prescription
    
    def Aggregate_primary_med_24_hr(self,
                                    patient,
                                    all_meds_dictionary):
        
        primary_med_dictionary = all_meds_dictionary['Primary_med']
        if patient.primary_opioid_med != None:
            #24-hr dose:
            total_primary_med_24hr_dose = patient.Primary_total_dose_per_24_hr()
            #24-hr MME:
            total_primary_med_24hr_MME = patient.Calculate_med_MME_24_hr(patient.primary_opioid_med)
            #Number active capsules 24-hr:
            total_primary_med_24hr_active_capsule_count = primary_med_dictionary['Aggregate 24 hr Active Capsules']
            #Number placebo capsules 24-hr:
            total_primary_med_24hr_placebo_capsule_count = primary_med_dictionary['Aggregate 24 hr Placebo Capsules']
            #Number total capsules 24-hr:
            total_primary_med_24hr_all_type_capsule_count = primary_med_dictionary['Aggregate 24 hr All Capsules']
            pass

        else:
            #24-hr dose:
            total_primary_med_24hr_dose = 0
            #24-hr MME:
            total_primary_med_24hr_MME = 0
            #Number active capsules 24-hr:
            total_primary_med_24hr_active_capsule_count = primary_med_dictionary['Aggregate 24 hr Active Capsules']

            #Number placebo capsules 24-hr:
            total_primary_med_24hr_placebo_capsule_count = primary_med_dictionary['Aggregate 24 hr Placebo Capsules']
            
            #Number total capsules 24-hr:
            total_primary_med_24hr_all_type_capsule_count = primary_med_dictionary['Aggregate 24 hr All Capsules']
            pass
        
        agg_primary_24_hr_information = {'Total Primary Med 24hr Dose': total_primary_med_24hr_dose,
                                         'Total Primary Med 24hr MME': total_primary_med_24hr_MME,
                                         'Total Primary Med 24hr Active Capsule Count': total_primary_med_24hr_active_capsule_count,
                                         'Total Primary Med 24hr Placebo Capsule Count': total_primary_med_24hr_placebo_capsule_count,
                                         'Total Primary Med 24hr All Med Capsule Count': total_primary_med_24hr_all_type_capsule_count}
        return agg_primary_24_hr_information
    
    def Aggregate_secondary_med_24_hr(self,
                                    patient,
                                    all_meds_dictionary):
        
        secondary_med_dictionary = all_meds_dictionary['Secondary_med']
        if patient.secondary_opioid_med != None:
            #24-hr dose:
            total_secondary_med_24hr_dose = patient.Secondary_total_dose_per_24_hr()
            #24-hr MME:
            total_secondary_med_24hr_MME = patient.Calculate_med_MME_24_hr(patient.secondary_opioid_med)
            #Number active capsules 24-hr:
            total_secondary_med_24hr_active_capsule_count = secondary_med_dictionary['Aggregate 24 hr Active Capsules']
            #Number placebo capsules 24-hr:
            total_secondary_med_24hr_placebo_capsule_count = secondary_med_dictionary['Aggregate 24 hr Placebo Capsules']
            #Number total capsules 24-hr:
            total_secondary_med_24hr_all_type_capsule_count = secondary_med_dictionary['Aggregate 24 hr All Capsules']
            pass

        else:
            #24-hr dose:
            total_secondary_med_24hr_dose = 0
            #24-hr MME:
            total_secondary_med_24hr_MME = 0
            #Number active capsules 24-hr:
            total_secondary_med_24hr_active_capsule_count = secondary_med_dictionary['Aggregate 24 hr Active Capsules']
            #Number placebo capsules 24-hr:
            total_secondary_med_24hr_placebo_capsule_count = secondary_med_dictionary['Aggregate 24 hr Placebo Capsules']
            #Number total capsules 24-hr:
            total_secondary_med_24hr_all_type_capsule_count = secondary_med_dictionary['Aggregate 24 hr All Capsules']
            pass
        
        agg_secondary_24_hr_information = {'Total Secondary Med 24hr Dose': total_secondary_med_24hr_dose,
                                         'Total Secondary Med 24hr MME': total_secondary_med_24hr_MME,
                                         'Total Secondary Med 24hr Active Capsule Count': total_secondary_med_24hr_active_capsule_count,
                                         'Total Secondary Med 24hr Placebo Capsule Count': total_secondary_med_24hr_placebo_capsule_count,
                                         'Total Secondary Med 24hr All Med Capsule Count': total_secondary_med_24hr_all_type_capsule_count}
        return agg_secondary_24_hr_information
    
#    def Aggregate_tertiary_med_24_hr(self,
#                                    patient,
#                                    all_meds_dictionary):
#        
#        if patient.tertiary_opioid_med != None:
#            tertiary_med_dictionary = all_meds_dictionary['Tertiary_med']
#            #24-hr dose:
#            total_tertiary_med_24hr_dose = patient.Tertiary_total_dose_per_24_hr()
#            #24-hr MME:
#            total_tertiary_med_24hr_MME = patient.Calculate_med_MME_24_hr(patient.tertiary_opioid_med)
#            #Number active capsules 24-hr:
#            total_tertiary_med_24hr_active_capsule_count = tertiary_med_dictionary['Aggregate 24 hr Active Capsules']
#            #Number placebo capsules 24-hr:
#            total_tertiary_med_24hr_placebo_capsule_count = tertiary_med_dictionary['Aggregate 24 hr Placebo Capsules']
#            #Number total capsules 24-hr:
#            total_tertiary_med_24hr_all_type_capsule_count = tertiary_med_dictionary['Aggregate 24 hr All Capsules']
#            pass
#
#        else:
#            #24-hr dose:
#            total_tertiary_med_24hr_dose = 0
#            #24-hr MME:
#            total_tertiary_med_24hr_MME = 0
#            #Number active capsules 24-hr:
#            total_tertiary_med_24hr_active_capsule_count = 0
#            #Number placebo capsules 24-hr:
#            total_tertiary_med_24hr_placebo_capsule_count = 0
#            #Number total capsules 24-hr:
#            total_tertiary_med_24hr_all_type_capsule_count = 0
#            pass
#        
#        agg_tertiary_24_hr_information = {'Total Tertiary Med 24hr Dose': total_tertiary_med_24hr_dose,
#                                         'Total Tertiary Med 24hr MME': total_tertiary_med_24hr_MME,
#                                         'Total Tertiary Med 24hr Active Capsule Count': total_tertiary_med_24hr_active_capsule_count,
#                                         'Total Tertiary Med 24hr Placebo Capsule Count': total_tertiary_med_24hr_placebo_capsule_count,
#                                         'Total Tertiary Med 24hr All Med Capsule Count': total_tertiary_med_24hr_all_type_capsule_count}
#        return agg_tertiary_24_hr_information
    
    def Aggregate_all_med_24_hr(self,
                                patient,
                                all_meds_dictionary):
        primary_med_agg_dictionary = self.Aggregate_primary_med_24_hr(patient,
                                                                      all_meds_dictionary)
    
        secondary_med_agg_dictionary = self.Aggregate_secondary_med_24_hr(patient,
                                                                          all_meds_dictionary)
    
#        tertiary_med_agg_dictionary = self.Aggregate_tertiary_med_24_hr(patient,
#                                                                            all_meds_dictionary)
           
        #24-hr MME:
        total_med_24hr_MME = patient.Calculate_total_MME_24_hr()
       
        #Number active capsules 24-hr:
        total_med_24hr_active_capsule_count = sum([primary_med_agg_dictionary['Total Primary Med 24hr Active Capsule Count'],
                                                   secondary_med_agg_dictionary['Total Secondary Med 24hr Active Capsule Count']])
#                                                   tertiary_med_agg_dictionary['Total Tertiary Med 24hr Active Capsule Count']])
        
        #Number placebo capsules 24-hr:
        total_med_24hr_placebo_capsule_count = sum([primary_med_agg_dictionary['Total Primary Med 24hr Placebo Capsule Count'],
                                                           secondary_med_agg_dictionary['Total Secondary Med 24hr Placebo Capsule Count']])
#                                                           tertiary_med_agg_dictionary['Total Tertiary Med 24hr Placebo Capsule Count']])
        
        #Number total capsules 24-hr:
        total_med_24hr_all_type_capsule_count = sum([primary_med_agg_dictionary['Total Primary Med 24hr All Med Capsule Count'],
                                                           secondary_med_agg_dictionary['Total Secondary Med 24hr All Med Capsule Count']])
#                                                           tertiary_med_agg_dictionary['Total Tertiary Med 24hr All Med Capsule Count']])
    
        
        agg_all_med_24_hr_information = {'Total All Med 24hr MME': total_med_24hr_MME,
                                         'Total All Med 24hr Active Capsule Count': total_med_24hr_active_capsule_count,
                                         'Total All Med 24hr Placebo Capsule Count': total_med_24hr_placebo_capsule_count,
                                         'Total All Med 24hr All Type Capsule Count': total_med_24hr_all_type_capsule_count}
        return agg_all_med_24_hr_information
    
    def Calculate_difference_actual_vs_ideal_taper_24hr_MME(self,
                                                            patient,
                                                            taper_object,
                                                            all_meds_dictionary):
        #State ideal MME all med 24 hr.
        
        #Pre-taper total MME:
        pre_taper_total_MME = taper_object.pre_taper_total_all_med_MME_24
        
        #Post-taper total MME:
        post_taper_ideal_total_MME = taper_object.post_taper_total_MME_24
        
        #Ideal percent MME decrease:
        if pre_taper_total_MME < 1:
            ideal_percent_MME_decrease_across_taper = 0
            pass
        elif pre_taper_total_MME > 1:
            ideal_percent_MME_decrease_across_taper = (1 - (post_taper_ideal_total_MME / pre_taper_total_MME))*100
            pass
        else:
            pass
        
        #State actual MME all med 24 hr.
        actual_all_meds_dictionary = self.Aggregate_all_med_24_hr(patient,
                                                                  all_meds_dictionary)
        
        actual_total_MME = actual_all_meds_dictionary['Total All Med 24hr MME']
        
        #Actual percent MME decrease:
        if pre_taper_total_MME < 1:
            actual_percent_MME_decrease_across_taper = 0
            pass
        elif pre_taper_total_MME > 1:
            actual_percent_MME_decrease_across_taper = (1 - (actual_total_MME / pre_taper_total_MME))*100
            pass
        else:
            pass
        
        #Calculate difference in percent of previous MME (between actual-ideal):
        relative_difference_ideal_vs_actual_total_MME = (ideal_percent_MME_decrease_across_taper - actual_percent_MME_decrease_across_taper)
        
        ideal_to_actual_MME_comparison_dictionary = {'Pre-taper total MME': pre_taper_total_MME,
                                                     'Post-taper ideal total MME': post_taper_ideal_total_MME,
                                                     'Ideal percent MME decrease': ideal_percent_MME_decrease_across_taper,
                                                     'Actual total MME': actual_total_MME,
                                                     'Actual percent MME decrease': actual_percent_MME_decrease_across_taper,
                                                     'Relative Percent Difference Actual-Ideal MME Change (Relative to Pre-Taper MME)': relative_difference_ideal_vs_actual_total_MME}
        return ideal_to_actual_MME_comparison_dictionary
    
    def Final_prescription_generator(self,
                                     patient,
                                     taper_object):
    
        #Generate count of active and placebo capsules for all existing 
        #medications:
        
        #Per medication:
        
        #Primary:
        
        #Constant dose:
        if patient.different_daily_episode_doses_med_1 != 'Yes':
            self.primary_med_prescription_information = self.Constant_episode_med_prescription(patient,
                                                                      patient.primary_opioid_med)
            pass
        
        #Nonconstant dose:
        elif patient.different_daily_episode_doses_med_1 == 'Yes':
            self.primary_med_prescription_information = self.Nonconstant_episode_med_prescription(patient,
                                                                         patient.primary_opioid_med)
            pass
        else:
            pass
        
        #Secondary:
        
        #Constant dose:
        if patient.different_daily_episode_doses_med_2 != 'Yes':
            self.secondary_med_prescription_information = self.Constant_episode_med_prescription(patient,
                                                                        patient.secondary_opioid_med)
            pass
        
        #Nonconstant dose:
        elif patient.different_daily_episode_doses_med_2 == 'Yes':
            self.secondary_med_prescription_information = self.Nonconstant_episode_med_prescription(patient,
                                                                           patient.secondary_opioid_med)
            pass
        else:
            pass
        
#        #Tertiary:
#        
#        #Constant dose:
#        if patient.different_daily_episode_doses_med_3 != 'Yes':
#            self.tertiary_med_prescription_information = self.Constant_episode_med_prescription(patient,
#                                                                       patient.tertiary_opioid_med)
#            pass
#        
#        #Nonconstant dose:
#        elif patient.different_daily_episode_doses_med_3 == 'Yes':
#            self.tertiary_med_prescription_information = self.Nonconstant_episode_med_prescription(patient,
#                                                                          patient.tertiary_opioid_med)
#            pass
#        else:
#            pass
        
        #Generate final all medication information dictionary:
        self.all_medication_prescription_information = [self.primary_med_prescription_information,
                                                        self.secondary_med_prescription_information]
                                                        #self.tertiary_med_prescription_information]
        medications = ['Primary_med', 'Secondary_med']#, 'Tertiary_med']
        
        self.final_medication_prescription_information_dictionary = dict(zip(medications, self.all_medication_prescription_information))
        
        #Generate number episodes and frequency of doses: 
        self.Number_episodes_per_day(patient)
        self.number_episodes = self.total_episodes
        self.aggregate_interdose_duration = self.total_interdose_duration
        
        #returns these variables: self.total_episodes and self.total_interdose_duration 
        
        #Hypothetical Episodes:
        
        #Episode 1:
        hypothetical_episode_1 = self.Episode_1(patient,
                                   self.final_medication_prescription_information_dictionary)
        print('Hypothetical Episode 1: {}'.format(hypothetical_episode_1))
        print('')
        #Episode 2:
        hypothetical_episode_2 = self.Episode_2(patient,
                                   self.final_medication_prescription_information_dictionary)
        print('Hypothetical Episode 2: {}'.format(hypothetical_episode_2))
        print('')
        #Episode 3:
        hypothetical_episode_3 = self.Episode_3(patient,
                                   self.final_medication_prescription_information_dictionary)
        print('Hypothetical Episode 3: {}'.format(hypothetical_episode_3))
        print('')
        #Episode 4:
        hypothetical_episode_4 = self.Episode_4(patient,
                                   self.final_medication_prescription_information_dictionary)
        
        print('Hypothetical Episode 4: {}'.format(hypothetical_episode_4))
        print('')
        
        #Actual Episodes (according to starting episode count per day):
        if self.number_episodes == 1:
            actual_episode_list = ['Episode 1']
            actual_episode_dict = [hypothetical_episode_1]
            self.actual_episodes = dict(zip(actual_episode_list, actual_episode_dict))
            pass
        elif self.number_episodes == 2:
            actual_episode_list = ['Episode 1', 'Episode 2']
            actual_episode_dict = [hypothetical_episode_1, hypothetical_episode_2]
            self.actual_episodes = dict(zip(actual_episode_list, actual_episode_dict))
            pass
        elif self.number_episodes == 3:
            actual_episode_list = ['Episode 1', 'Episode 2', 'Episode 3']
            actual_episode_dict = [hypothetical_episode_1, hypothetical_episode_2, hypothetical_episode_3]
            self.actual_episodes = dict(zip(actual_episode_list, actual_episode_dict))
            pass
        elif self.number_episodes == 4:
            actual_episode_list = ['Episode 1', 'Episode 2', 'Episode 3', 'Episode 4']
            actual_episode_dict = [hypothetical_episode_1, hypothetical_episode_2, hypothetical_episode_3, hypothetical_episode_4]
            self.actual_episodes = dict(zip(actual_episode_list, actual_episode_dict))
            pass
        else:
            pass
#        actual_episode_list = ['Episode 1', 'Episode 2', 'Episode 3', 'Episode 4']
#        actual_episode_dict = [hypothetical_episode_1, hypothetical_episode_2, hypothetical_episode_3, hypothetical_episode_4]
#        self.actual_episodes = dict(zip(actual_episode_list, actual_episode_dict))
        
        print('Actual Total Episodes: {}'.format(self.actual_episodes))
        print('')
        #Total (Dose and MME) Metrics:
        
        #24-hr aggregate primary med:
        
        self.aggregate_primary_med = self.Aggregate_primary_med_24_hr(patient,
                                                                 self.final_medication_prescription_information_dictionary)
        print(self.aggregate_primary_med)
        print('')
        #24-hr aggregate secondary med:
        self.aggregate_secondary_med = self.Aggregate_secondary_med_24_hr(patient,
                                                                 self.final_medication_prescription_information_dictionary)
        print(self.aggregate_secondary_med)
        print('')
        #24-hr aggregate tertiary med:
#        aggregate_tertiary_med = self.Aggregate_tertiary_med_24_hr(patient,
#                                                                 self.final_medication_prescription_information_dictionary)
#        print(aggregate_tertiary_med)
#        print('')
        #24-hr all medications:
        
        self.aggregate_all_med = self.Aggregate_all_med_24_hr(patient,
                                                                 self.final_medication_prescription_information_dictionary)
        print(self.aggregate_all_med)
        print('')
        self.ideal_vs_actual_MME_calculations = self.Calculate_difference_actual_vs_ideal_taper_24hr_MME(patient,
                                                                                                    taper_object,
                                                                                                    self.final_medication_prescription_information_dictionary)
        print(self.ideal_vs_actual_MME_calculations)
        pass
