#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 17:32:25 2019

@author: dannywitt
"""

#Test

from Opioid_app_backend.medication import Medication
from Opioid_app_backend.opioid_dose_taper import Opioid_taper_calculator
from Opioid_app_backend.prescription import Prescription
from Opioid_app_backend.Dosing_specifications import Dosing_specifications
from Opioid_app_backend.Patient_information import Patient

#test_dosage_specs = Dosing_specifications(10, 2)
#
#print('This is the episode dosage: {}mg'.format(test_dosage_specs.total_dose_per_consumption_episode))
#
#print('This is the dosing frequency: Q{} hours'.format(test_dosage_specs.interdose_duration))
#
#print('This is the time between doses: every {} hours'.format(test_dosage_specs.time_between_doses))
#
#print('This is the total 24 hr dose: {}mg/day'.format(test_dosage_specs.total_dose_per_day))
#
#med_acetaminophen = Medication('Codeine Acetaminophen', 'Immediate Release', 15, 'Tablet', [60, 30, 15], 15)
#
##Print entire namespace:
#print(med_acetaminophen.__dict__)
#
#print(med_acetaminophen.Full_drug_name())
#print(med_acetaminophen.med_name)
#print(med_acetaminophen.delivery_rate)
#print(med_acetaminophen.unit_dose)
#print(med_acetaminophen.drug_delivery_form)
#print(med_acetaminophen.minimum_dose_available)
#print(med_acetaminophen.available_opioid_doses)

#patient_1 = Patient(1000101,
#                    'Harry',
#                    'Winkler',
#                    'Codeine',
#                    15,
#                    2,
#                    'Morphine',
#                    10,
#                    4,
#                    'Hydromorphone',
#                    5,
#                    2)
#
#patient_2 = Patient(10002001,
#                    'Gretchen',
#                    'Fildemeister',
#                    'Hydrocodone',
#                    10,
#                    4,
#                    'None',
#                    'NA',
#                    'NA',
#                    'None',
#                    'NA',
#                    'NA')
#
#patient_3 = Patient(100123,
#                    'Janice',
#                    'Tubersky',
#                    'Hydromorphone',
#                    5,
#                    3,
#                    'Morphine',
#                    15,
#                    2,
#                    'None',
#                    'NA',
#                    'NA')
#
#print(patient_1.Patient_name())
#print(patient_1.Medication_list())
#print(patient_1.total_number_opioid_meds)
#
#print(patient_2.Patient_name())
#print(patient_2.Medication_list())
#print(patient_2.total_number_opioid_meds)
#
#print(patient_3.Patient_name())
#print(patient_3.Medication_list())
#print(patient_3.total_number_opioid_meds)
#print(patient_3.prim_opioid_dose)
#print(patient_3.secondary_opioid_dose)

from medication import Medication
from medication import Codeine_Acetaminophen
from medication import Codeine_Sulfate
from medication import Hydrocodone_Acetaminophen
from medication import Hydrocodone_Ibuprofen

pt_1_med = Codeine_Sulfate()

print(pt_1_med.combination_state)
print(pt_1_med.combined_drug_name)
print(pt_1_med.full_drug_name())
print(pt_1_med.available_opioid_unit_doses)
print(pt_1_med.minimum_dose_available)

pt_2_med = Codeine_Acetaminophen()
pt_3_med = Hydrocodone_Acetaminophen()
pt_4_med = Hydrocodone_Ibuprofen()
print('_______________________________________')
print(pt_4_med.med_name)
print(pt_4_med.combined_drug_name)
print(pt_4_med.available_opioid_unit_doses)
print(pt_4_med.combination_drug_unit_doses)
print(pt_4_med.available_combination_doses)
print(pt_4_med.MME_conversion_factor)
