#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 11:02:48 2019

@author: dannywitt
"""

#Will use Patient Information and Medication

from Opioid_app_backend.patient_information import Patient

from Opioid_app_backend.medication import (Hydrocodone_Acetaminophen,
                                            Hydromorphone_Immediate_Release,
                                            Hydromorphone_Extended_Release,
                                            Morphine_Immediate_Release,
                                            Morphine_Extended_Release,
                                            Oxycodone_Immediate_Release,
                                            Oxycodone_Extended_Release,
                                            Oxycodone_Acetaminophen,
                                            Tramadol_Immediate_Release)

class Prescription(Patient):
    '''
    Need class to generate number of pills per episode from starting information;
    Class is designed to take medication inputs (medication types, doses, frequencies,
    MMEs) and patient prescription information (number of tablets/capsules, etc.) and
    output --> actual med doses and capsules (active vs. placebo)

    '''

    def __init__(self,
                 a_unique_patient,
                 primary_opioid_starting_capsules_per_episode,
                 secondary_opioid_starting_capsules_per_episode,
                 tertiary_opioid_starting_capsules_per_episode):
        #Import medications of patient

        self.primary_opioid_med = a_unique_patient.primary_opioid_med
        self.secondary_opioid_med = a_unique_patient.secondary_opioid_med
        self.tertiary_opioid_med = a_unique_patient.tertiary_opioid_med

        #Update starting episode capsule counts per medication:

        self.primary_opioid_total_capsules_per_episode = primary_opioid_starting_capsules_per_episode
        self.secondary_opioid_total_capsules_per_episode = secondary_opioid_starting_capsules_per_episode
        self.tertiary_opioid_total_capsules_per_episode = tertiary_opioid_starting_capsules_per_episode

        #Import only medication information that exists for given patient:

        if a_unique_patient.primary_opioid_med != None:
           self.primary_opioid_med = a_unique_patient.primary_opioid_med
           self.prim_opioid_episode_dose = a_unique_patient.prim_opioid_episode_dose
           self.prim_opioid_interdose_duration = a_unique_patient.prim_opioid_interdose_duration
           self.prim_opioid_episode_count_24_hr = a_unique_patient.Primary_med_episodes_24_hr()

           #generate below attributes:
           #a_unique_patient.Primary_med_capsule_count()
           #self.prim_opioid_unit_dose = a_unique_patient.prim_opioid_unit_dose
           #self.primary_med_total_capsules_per_episode = a_unique_patient.primary_med_total_capsules_per_episode
           #self.primary_med_total_capsules_24 = a_unique_patient.primary_med_total_capsules_24
           pass

        else:
            pass

        if a_unique_patient.secondary_opioid_med != None:
            self.secondary_opioid_med = a_unique_patient.secondary_opioid_med
            self.secondary_opioid_episode_dose = a_unique_patient.secondary_opioid_episode_dose
            self.secondary_opioid_interdose_duration = a_unique_patient.secondary_opioid_interdose_duration
            self.secondary_opioid_episode_count_24_hr = a_unique_patient.secondary_opioid_episode_count_24_hr
            #secondary med total capsule count
            pass
        else:
            pass

        if a_unique_patient.tertiary_opioid_med != None:
            self.tertiary_opioid_med = a_unique_patient.tertiary_opioid_med
            self.tertiary_opioid_episode_dose = a_unique_patient.tertiary_opioid_episode_dose
            self.tertiary_opioid_interdose_duration = a_unique_patient.tertiary_opioid_interdose_duration
            self.tertiary_opioid_episode_count_24_hr = a_unique_patient.tertiary_opioid_episode_count_24_hr
            #tertiary med total capsule count
        else:
            pass

        pass

    def number_episodes_per_day(self):
        #Will control whether we can use episode 1, 2, 3, or 4
        #Deal with different inputs of daily episodes per medication
        #(e.g., primary med episodes 24 hr = 4, secondary med episodes = 2)
        #and reconcile actual number of episodes:
        pass

   def Primary_med_active_placebo_capsule_count(self, total_primary_capsules_per_episode):
    #Generate count of active and placebo capsules for primary medication

    if self.primary_opioid_med != None:
        possible_prim_unit_doses = []
        for possible_opioid_unit_dose in self.primary_opioid_med.available_opioid_unit_doses:
            if self.prim_opioid_episode_dose % possible_opioid_unit_dose == 0:
                possible_prim_unit_doses.append(possible_opioid_unit_dose)
            elif :
                pass
            else:
                continue
        self.prim_opioid_unit_dose = max(possible_prim_unit_doses)
        self.primary_med_total_capsules_per_episode = self.prim_opioid_episode_dose / self.prim_opioid_unit_dose
        self.primary_med_total_capsules_24 = self.primary_med_total_capsules_per_episode * self.Primary_med_episodes_24_hr()

        #self.active_capsules =
        #placebo_capsules =
    else:
        pass
    pass

    def constrained_episode_dose(self):
        #take in medication type, ideal episode dose, and number capsules of med,
        #and convert this to constrained episode dose (total for med), unit size,
        #number of units, in episode dose, number of active capsules, number placebo

        #Update patient object's actual prescribed med-specific episode dose
        #(rather than previous ideal taper amount)
        pass

    def episode_1(self):
        #Think of this as all the information needed by pharmacy to create
        #blister pack of pills for patient for episode #1 of day, using
        #different medications, their episode dose, and converting ideal episode
        #dose into constrained episode dose
        pass

    def episode_2(self):
        #Think of this as all the information needed by pharmacy to create
        #blister pack of pills for patient for episode #2 of day:
        pass

    def episode_3(self):
        #Think of this as all the information needed by pharmacy to create
        #blister pack of pills for patient for episode #3 of day:
        pass

    def episode_4(self):
        #Think of this as all the information needed by pharmacy to create
        #blister pack of pills for patient for episode #4 (if necessary) of day:
        pass

    def generate_total_pills(self):
        #What inputs are needed to calculate this:
        #each med, episode dose,
        pass

    def primary_med_prescription(self):
        #take new dose information, number of caps/tabs, dosing frequency and
        #generate (1) number active pill per consumption episode,
        #(2) dose of opioid per active pill,
        #(3) total opioid dose for consumption episode, (4) total dose per 24 hour,
        #(5) number of placebo pills, (6) dosing frequency, and (7) check total
        #number of active + placebo pills are accurate and constant
        pass

    def secondary_med_prescription(self):
        pass

    def tertiary_med_prescription(self):
        pass



#Test script:

#Convert ideal dose --> prescription dose (unit dose available and
# maintaining <= starting number capsules):
primary_opioid_med = 'kush'
secondary_opioid_med = 'k2'

dose_episodes_per_day_1 = 3
dose_episodes_per_day_2 = 2

unique_dose_episodes = max([dose_episodes_per_day_1, dose_episodes_per_day_2])

daily_dose_information = {'number_active_meds': [],
                          'unique_dose_episodes': [],
                          'total_capsules_episode_1' : [],
                          'total_capsules_episode_2' : [],
                          'total_capsules_episode_3' : [],
                          'total_capsules_episode_4' : [],
                          'total_daily_capsules' : [],
                          'dose_interval' : []}

dose_episode_1 = {'primary_opioid_med' : ['med_name',
                                          'unit_dose',
                                          'total_episode_dose',
                                          'number_unit_doses',
                                          'active_dose_per_capsule',
                                          'number_active_capsules',
                                          'episode_MME'],
                  'secondary_opioid_med' : [2],
                  'number_placebo': []}

dose_episode_2 : {'primary_opioid_med' : [3],
                  'secondary_opioid_med' : [4],
                  'number_placebo': []}

dose_episode_3 : {'primary_opioid_med' : (5),
                  'secondary_opioid_med' : [6],
                  'number_placebo': []}

dose_episode_4 : {'primary_opioid_med' : (7),
                  'secondary_opioid_med' : [8],
                  'number_placebo': []}

avail_doses = [(5, 325), (7.5, 325), (10, 325)]

dose = 20

opioid_options = [i[0] for i in avail_doses]
num_options = len(opioid_options)
closeness = [dose - i for i in opioid_options]
print(opioid_options)
print(closeness)
print(dose_episode_1['primary_opioid_med'])
