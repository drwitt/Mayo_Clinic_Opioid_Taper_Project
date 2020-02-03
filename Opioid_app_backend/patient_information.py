#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 19:35:11 2019

@author: dannywitt
"""
import numpy as np
import pandas as pd

from Opioid_app_backend.medication import (Hydrocodone_Acetaminophen,
                        Hydromorphone_Immediate_Release,
                        Morphine_Immediate_Release,
                        Morphine_Extended_Release,
                        Oxycodone_Immediate_Release,
                        Oxycodone_Extended_Release,
                        Oxycodone_Acetaminophen,
                        Tramadol_Immediate_Release
                        )

from Opioid_app_backend.research_time_counter import Research_month
#from opioid_dose_taper import Taper

#Import all meds, available to any patient:

class Patient(Hydrocodone_Acetaminophen,
                Hydromorphone_Immediate_Release,
                Morphine_Immediate_Release,
                Morphine_Extended_Release,
                Oxycodone_Immediate_Release,
                Oxycodone_Extended_Release,
                Oxycodone_Acetaminophen,
                Tramadol_Immediate_Release,
                Research_month):

    '''Goal: initialize a patient class which takes information about a patient
    with the following possible arguments (seen in init method); can use to
    instantiate a patient object for each real-world patient which contains
    personal identifiers, drug information, and dosing information'''


    def __init__(self,
                 ID_number,
                 first_name,
                 last_name):

        self.ID_number = ID_number
        self.first_name = first_name
        self.last_name = last_name

        #Primary opioid medication:
        self.primary_opioid_med = None
        self.primary_opioid_med_name = None
        self.primary_opioid_episode_dose = None
        self.primary_opioid_unit_dose = None
        self.primary_opioid_captab_per_episode_dose = None
        self.primary_opioid_interdose_duration = None
        self.different_daily_episode_doses_med_1 = None

        if self.different_daily_episode_doses_med_1 == 'Yes':
            self.primary_opioid_dif_dose_episode_dose_1 = None
            self.primary_opioid_dif_dose_ep_1_unit_dose = None
            self.primary_opioid_dif_dose_captab_per_episode_dose_1 = None
            self.primary_opioid_dif_dose_episode_dose_2 = None
            self.primary_opioid_dif_dose_ep_2_unit_dose = None
            self.primary_opioid_dif_dose_captab_per_episode_dose_2 = None
            self.primary_opioid_dif_dose_episode_dose_3 = None
            self.primary_opioid_dif_dose_ep_3_unit_dose = None
            self.primary_opioid_dif_dose_captab_per_episode_dose_3 = None
            self.primary_opioid_dif_dose_episode_dose_4 = None
            self.primary_opioid_dif_dose_ep_4_unit_dose = None
            self.primary_opioid_dif_dose_captab_per_episode_dose_4 = None
        else:
            pass

        #Secondary opioid medication:
        self.secondary_opioid_med = None
        self.secondary_opioid_med_name = None
        self.secondary_opioid_episode_dose = None
        self.secondary_opioid_unit_dose = None
        self.secondary_opioid_captab_per_episode_dose = None
        self.secondary_opioid_interdose_duration = None
        self.different_daily_episode_doses_med_2 = None

        if self.different_daily_episode_doses_med_2 == 'Yes':
            self.secondary_opioid_dif_dose_episode_dose_1 = None
            self.secondary_opioid_dif_dose_ep_1_unit_dose = None
            self.secondary_opioid_dif_dose_captab_per_episode_dose_1 = None
            self.secondary_opioid_dif_dose_episode_dose_2 = None
            self.secondary_opioid_dif_dose_ep_2_unit_dose = None
            self.secondary_opioid_dif_dose_captab_per_episode_dose_2 = None
            self.secondary_opioid_dif_dose_episode_dose_3 = None
            self.secondary_opioid_dif_dose_ep_3_unit_dose = None
            self.secondary_opioid_dif_dose_captab_per_episode_dose_3 = None
            self.secondary_opioid_dif_dose_episode_dose_4 = None
            self.secondary_opioid_dif_dose_ep_4_unit_dose = None
            self.secondary_opioid_dif_dose_captab_per_episode_dose_4 = None
        else:
            pass

        #Tertiary opioid medication:
        self.tertiary_opioid_med = None
        self.tertiary_opioid_episode_dose = None
        self.tertiary_opioid_unit_dose = None
        self.tertiary_opioid_captab_per_episode_dose = None
        self.tertiary_opioid_interdose_duration = None
        self.different_daily_episode_doses_med_3 = None

        if self.different_daily_episode_doses_med_3 == 'Yes':
            self.tertiary_opioid_dif_dose_episode_dose_1 = None
            self.tertiary_opioid_dif_dose_ep_1_unit_dose = None
            self.tertiary_opioid_dif_dose_captab_per_episode_dose_1 = None

            self.tertiary_opioid_dif_dose_episode_dose_2 = None
            self.tertiary_opioid_dif_dose_ep_2_unit_dose = None
            self.tertiary_opioid_dif_dose_captab_per_episode_dose_2 = None

            self.tertiary_opioid_dif_dose_episode_dose_3 = None
            self.tertiary_opioid_dif_dose_ep_3_unit_dose = None
            self.tertiary_opioid_dif_dose_captab_per_episode_dose_3 = None

            self.tertiary_opioid_dif_dose_episode_dose_4 = None
            self.tertiary_opioid_dif_dose_ep_4_unit_dose = None
            self.tertiary_opioid_dif_dose_captab_per_episode_dose_4 = None
            self.tertiary_opioid_interdose_duration = None
        else:
            pass

        self.research_study_timer = Research_month()
        self.main_prescription_list = None

#        else:
#            self.primary_opioid_med = None
#            self.prim_opiod_episode_dose = None
#            self.prim_opioid_interdose_duration = None
#            self.total_primary_opioid_dose_per_24_hr = None
#            self.prim_opioid_MME_24_hr = None
#
#        if self.secondary_opioid_med != None:
#            self.secondary_opioid_med = self.Assign_med_class(self.secondary_opioid_med)
#            #Raise error if not available medication or handle case when there is
#            #no secondary medication (i.e., patient only on one med)
#            #self.secondary_opioid_episode_dose = secondary_opioid_episode_dose
#            #Have a conditional statement that only assigns secondary dose IF there
#            #is a second medication; else assign None
#            #self.secondary_opioid_interdose_duration = secondary_opioid_interdose_duration
#            #Same as above
#            self.total_secondary_opioid_dose_per_24_hr = self.Secondary_total_dose_per_24_hr()
#            #Same as above
#            self.secondary_opioid_MME_24_hr = self.Calculate_MME_24_hr(self.secondary_opioid_episode_dose,
#                                                                      self.secondary_opioid_interdose_duration,
#                                                                      self.secondary_opioid_med.MME_conversion_factor)
#        else:
#            self.secondary_opioid_med = None
#            self.secondary_opiod_episode_dose = None
#            self.secondary_opioid_interdose_duration = None
#            self.total_secondary_opioid_dose_per_24_hr = None
#            self.secondary_opioid_MME_24_hr = None
#
#        if self.tertiary_opioid_med != None:
#            self.tertiary_opioid_med = self.Assign_med_class(self.tertiary_opioid_med)
#            #Same (as above) for all parts of tertiary medication!
#            #self.tertiary_opioid_episode_dose = tertiary_opioid_episode_dose
#            #self.tertiary_opioid_interdose_duration = tertiary_opioid_interdose_duration
#            self.total_tertiary_opioid_dose_per_24_hr = self.Tertiary_total_dose_per_24_hr()
#            self.tertiary_opioid_MME_24_hr = self.Calculate_MME_24_hr(self.tertiary_opioid_episode_dose,
#                                                              self.tertiary_opioid_interdose_duration,
#                                                              self.tertiary_opioid_med.MME_conversion_factor)
#        else:
#            self.tertiary_opioid_med = None
#            self.tertiary_opiod_episode_dose = None
#            self.tertiary_opioid_interdose_duration = None
#            self.total_tertiary_opioid_dose_per_24_hr = None
#            self.tertiary_opioid_MME_24_hr = None
#
#
#
#        if self.primary_opioid_med != None or self.secondary_opioid_med != None or self.tertiary_opioid_med != None:
#            self.total_MME_24_hr = sum(filter(None,
#                                          [self.prim_opioid_MME_24_hr,
#                                           self.secondary_opioid_MME_24_hr,
#                                           self.tertiary_opioid_MME_24_hr]
#                                          ))
#
#        elif self.primary_opioid_med != None and self.secondary_opioid_med != None:
#            self.total_MME_24_hr = (self.prim_opioid_MME_24_hr
#                                    + self.secondary_opioid_MME_24_hr)
#        elif self.primary_opioid_med != None:
#            self.total_MME_24_hr = self.prim_opioid_MME_24_hr
#        else:
#            self.total_MME_24_hr = 0

        return

    def Patient_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def Current_medication_list(self):
        return [self.primary_opioid_med,
                self.secondary_opioid_med,
                self.tertiary_opioid_med]

    def Total_number_meds(self):
        med_list = list([self.primary_opioid_med, self.secondary_opioid_med, self.tertiary_opioid_med])
        available_meds = [x for x in med_list if x is not None]
        number_meds = len(available_meds)
        return number_meds

    def Number_episodes_per_24_hr(self, interdose_duration):
        if interdose_duration == None:
            return None
        else:
            number_episodes_24_hr = (24 / interdose_duration)
            return number_episodes_24_hr

    def Primary_med_episodes_24_hr(self):
        #Input interdose durations and count number episodes of each medication
        #for future prescription parameters:
        if self.primary_opioid_interdose_duration != None:
            self.primary_opioid_episode_count_24_hr = self.Number_episodes_per_24_hr(self.primary_opioid_interdose_duration)
        else:
            pass
        return self.primary_opioid_episode_count_24_hr

    def Secondary_med_episodes_24_hr(self):
        #Input interdose durations and count number episodes of each medication
        #for future prescription parameters:
        if self.secondary_opioid_interdose_duration != None:
            self.secondary_opioid_episode_count_24_hr = self.Number_episodes_per_24_hr(self.secondary_opioid_interdose_duration)
        else:
            pass
        return self.secondary_opioid_episode_count_24_hr

    def Tertiary_med_episodes_24_hr(self):
        #Input interdose durations and count number episodes of each medication
        #for future prescription parameters:
        if self.tertiary_opioid_interdose_duration != None:
            self.tertiary_opioid_episode_count_24_hr = self.Number_episodes_per_24_hr(self.tertiary_opioid_interdose_duration)
        else:
            pass
        return self.tertiary_opioid_episode_count_24_hr

    def Primary_med_initial_capsule_count(self):
        #Generate total capsule counts per medication (total will be same
        #throughout entirety of study, however active vs. placebo will change);
        #create episode count of capsules and total 24 hour count for primary
        #medication:

        if self.primary_opioid_med != None:
            possible_primary_unit_doses = []
            for possible_opioid_unit_dose in self.primary_opioid_med.available_opioid_unit_doses:
                if self.primary_opioid_episode_dose % possible_opioid_unit_dose == 0:
                    possible_primary_unit_doses.append(possible_opioid_unit_dose)
                else:
                    continue
            self.primary_opioid_unit_dose = max(possible_primary_unit_doses)
            self.primary_med_total_capsules_per_episode = self.primary_opioid_episode_dose / self.primary_opioid_unit_dose
           #In case we need per 24 hours, calculate total capsules per 24 hours, too:
            self.primary_med_total_capsules_24 = self.primary_med_total_capsules_per_episode * self.Primary_med_episodes_24_hr()

        else:
            pass
        return self.primary_med_total_capsules_per_episode

    def Secondary_med_initial_capsule_count(self):
        #Generate total capsule counts per medication (total will be same
        #throughout entirety of study, however active vs. placebo will change);
        #create episode count of capsules and total 24 hour count for primary
        #medication:
        if self.secondary_opioid_med != None:
            possible_secondary_unit_doses = []
            for possible_opioid_unit_dose in self.secondary_opioid_med.available_opioid_unit_doses:
                if self.secondary_opioid_episode_dose % possible_opioid_unit_dose == 0:
                    possible_secondary_unit_doses.append(possible_opioid_unit_dose)
                else:
                    continue
            self.secondary_opioid_unit_dose = max(possible_secondary_unit_doses)
            self.secondary_med_total_capsules_per_episode = self.secondary_opioid_episode_dose / self.secondary_opioid_unit_dose
            self.secondary_med_total_capsules_24 = self.secondary_med_total_capsules_per_episode * self.Secondary_med_episodes_24_hr()

        else:
            pass
        pass

    def Tertiary_med_initial_capsule_count(self):
        if self.tertiary_opioid_med != None:
            possible_tertiary_unit_doses = []
            for possible_opioid_unit_dose in self.tertiary_opioid_med.available_opioid_unit_doses:
                if self.tertiary_opioid_episode_dose % possible_opioid_unit_dose == 0:
                    possible_tertiary_unit_doses.append(possible_opioid_unit_dose)
                else:
                    continue
            self.tertiary_opioid_unit_dose = max(possible_tertiary_unit_doses)
            self.tertiary_med_total_capsules_per_episode = self.tertiary_opioid_episode_dose / self.tertiary_opioid_unit_dose
            self.tertiary_med_total_capsules_24 = self.tertiary_med_total_capsules_per_episode * self.Tertiary_med_episodes_24_hr()

        else:
            pass
        pass

    def Primary_total_dose_per_24_hr(self):
        if self.primary_opioid_med != None:
            if self.different_daily_episode_doses_med_1 != 'Yes':
                primary_total_dose_per_24_hr = self.primary_opioid_episode_dose * (24/self.primary_opioid_interdose_duration)
                pass
            elif self.different_daily_episode_doses_med_1 == 'Yes':
                primary_med_dose_list = [self.primary_opioid_dif_dose_episode_dose_1,
                                         self.primary_opioid_dif_dose_episode_dose_2,
                                         self.primary_opioid_dif_dose_episode_dose_3,
                                         self.primary_opioid_dif_dose_episode_dose_4]
                list_to_remove = ['nan', 'NA', 'Nan', None]
                primary_med_dose_list_remove_Nonetype = [ep_exists for ep_exists in primary_med_dose_list if ep_exists not in list_to_remove and not np.isnan(ep_exists)]
                primary_total_dose_per_24_hr = sum(primary_med_dose_list_remove_Nonetype)
            else:
                pass
            return primary_total_dose_per_24_hr
        else:
            pass

    def Secondary_total_dose_per_24_hr(self):
        if self.secondary_opioid_med != None:
            if self.different_daily_episode_doses_med_2 != 'Yes':
                secondary_total_dose_per_24_hr = self.secondary_opioid_episode_dose * (24/self.secondary_opioid_interdose_duration)
                pass
            elif self.different_daily_episode_doses_med_2 == 'Yes':
                secondary_med_dose_list = [self.secondary_opioid_dif_dose_episode_dose_1,
                                           self.secondary_opioid_dif_dose_episode_dose_2,
                                           self.secondary_opioid_dif_dose_episode_dose_3,
                                           self.secondary_opioid_dif_dose_episode_dose_4]
                list_to_remove = ['nan', 'NA', 'Nan', None]
                secondary_med_dose_list_remove_Nonetype = [ep_exists for ep_exists in secondary_med_dose_list if ep_exists not in list_to_remove and not np.isnan(ep_exists)]
                secondary_total_dose_per_24_hr = sum(secondary_med_dose_list_remove_Nonetype)
                pass
            else:
                pass

            return secondary_total_dose_per_24_hr
        else:
            pass

    def Tertiary_total_dose_per_24_hr(self):
        if self.tertiary_opioid_med != None:
            if self.different_daily_episode_doses_med_3 != 'Yes':
                tert_total_dose_per_24_hr = self.tertiary_opioid_episode_dose * (24/self.tertiary_opioid_interdose_duration)
                pass
            elif self.different_daily_episode_doses_med_3 == 'Yes':
                tertiary_med_dose_list = [self.tertiary_opioid_dif_dose_episode_dose_1,
                                         self.tertiary_opioid_dif_dose_episode_dose_2,
                                         self.tertiary_opioid_dif_dose_episode_dose_3,
                                         self.tertiary_opioid_dif_dose_episode_dose_4]
                list_to_remove = ['nan', 'NA', 'Nan', None]
                tertiary_med_dose_list_remove_Nonetype = [ep_exists for ep_exists in tertiary_med_dose_list if ep_exists not in list_to_remove and not np.isnan(ep_exists)]
                tert_total_dose_per_24_hr = sum(tertiary_med_dose_list_remove_Nonetype)
            else:
                pass
            return tert_total_dose_per_24_hr
        else:
            pass

    def Calculate_med_MME_24_hr(self, medication_object):
        if self.primary_opioid_med != None:
            if medication_object is self.primary_opioid_med:
                total_MME = self.Primary_total_dose_per_24_hr() * medication_object.MME_conversion_factor
                return total_MME
            else:
                pass
            pass
        else:
            pass

        if self.secondary_opioid_med != None:
            if medication_object is self.secondary_opioid_med:
                total_MME= self.Secondary_total_dose_per_24_hr() * medication_object.MME_conversion_factor
                return total_MME
            else:
                pass
            pass
        else:
            pass

        if self.tertiary_opioid_med != None:
            if medication_object is self.tertiary_opioid_med:
                total_MME = self.Tertiary_total_dose_per_24_hr() * medication_object.MME_conversion_factor
                return total_MME
            else:
                pass
            pass
        else:
            pass

        pass

    def Calculate_total_MME_24_hr(self):
        if self.primary_opioid_med != None:
            med_1 = self.Calculate_med_MME_24_hr(self.primary_opioid_med)
            pass
        else:
            med_1 = None
            pass
        if self.secondary_opioid_med != None:
            med_2 = self.Calculate_med_MME_24_hr(self.secondary_opioid_med)
            pass
        else:
            med_2 = None
            pass
        if self.tertiary_opioid_med != None:
            med_3 = self.Calculate_med_MME_24_hr(self.tertiary_opioid_med)
            pass
        else:
            med_3 = None
            pass
        list_MME = [med_1, med_2, med_3]
        list_to_remove = ['nan', 'NA', 'Nan', None]
        no_None_list_MME = [x for x in list_MME if x not in list_to_remove and not np.isnan(x)]
        return sum(no_None_list_MME)
