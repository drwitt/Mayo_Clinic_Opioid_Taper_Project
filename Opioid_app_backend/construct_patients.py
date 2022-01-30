#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Opioid_app_backend.patient_information import Patient

from Opioid_app_backend.medication import (Hydrocodone_Acetaminophen,
                                            Hydromorphone_Immediate_Release,
                                            Morphine_Immediate_Release,
                                            Morphine_Extended_Release,
                                            Oxycodone_Immediate_Release,
                                            Oxycodone_Extended_Release,
                                            Oxycodone_Acetaminophen,
                                            Tramadol_Immediate_Release)
class Patient_Builder():
    """

    Payload object information:

    ['study_id',
    'redcap_event_name',
    'name_first',
    'name_last',
    'id_num',
    'opioid_med_count',
    'prim_opioid_name',
    'prim_opioid_cnt_daily_dose',
    'prim_opioid_const_ep_dose',
    'prim_opioid_dose_freq',
    'prim_opioid_episode_dose',
    'prim_opioid_const_ep_unit_dose',
    'prim_opioid_const_ep_capsule_cnt',
    'prim_opioid_episode_dose_1',
    'prim_opioid_ep_1_unit_dose',
    'prim_opioid_ep_1_capsule_cnt',
    'prim_opioid_episode_dose_2',
    'prim_opioid_ep_2_unit_dose',
    'prim_opioid_ep_2_capsule_cnt',
    'prim_opioid_episode_dose_3',
    'prim_opioid_ep_3_unit_dose',
    'prim_opioid_ep_3_capsule_cnt',
    'prim_opioid_episode_dose_4',
    'prim_opioid_ep_4_unit_dose',
    'prim_opioid_ep_4_capsule_cnt',
    'sec_opioid_name',
    'sec_opioid_cnt_daily_dose',
    'sec_opioid_const_ep_dose',
    'sec_opioid_dose_freq',
    'sec_opioid_episode_dose',
    'sec_opioid_const_ep_unit_dose',
    'sec_opioid_const_ep_capsule_cnt',
    'sec_opioid_episode_dose_1',
    'sec_opioid_ep_1_unit_dose',
    'sec_opioid_ep_1_capsule_cnt',
    'sec_opioid_episode_dose_2',
    'sec_opioid_ep_2_unit_dose',
    'sec_opioid_ep_2_capsule_cnt',
    'sec_opioid_episode_dose_3',
    'sec_opioid_ep_3_unit_dose',
    'sec_opioid_ep_3_capsule_cnt',
    'sec_opioid_episode_dose_4',
    'sec_opioid_ep_4_unit_dose',
    'sec_opioid_ep_4_capsule_cnt'
    ]

    """
    def __init__(self, payload):
        self.payload = payload
        return

    def assign_patient_instance(self, patient_info_blob):
        """
        Parse "list of dictionaries" payload to build a patient class instance
        object.
        """
        #Assign string('') values from API call to None ojects, that way we change
        #assign the value of key directly to the patient instance/object.
        for k, v in patient_info_blob.items():
            if patient_info_blob[k] == '':
                patient_info_blob[k] = None
                pass
            else:
                pass

        #Assign patient attributes:

        #First name:
        first_name = patient_info_blob['name_first']

        #Last name:
        last_name = patient_info_blob['name_last']

        #Id number:
        id_num = patient_info_blob['id_num']

        #Make patient class instance:
        patient = Patient(id_num, first_name, last_name)

        #Assign opioid medication count (i.e., how many unique opioid meds
        #does patient take?):
        opioid_count = int(patient_info_blob['opioid_med_count'])
        patient.opioid_med_count = opioid_count

        #Assign opioid med objects:

        #Assign patient primary opioid medication class:
        primary_med = patient_info_blob['prim_opioid_name']
        patient.primary_opioid_med = self.assign_med_class(primary_med)
        
        if patient.primary_opioid_med != None:
            patient.primary_opioid_med_name = patient.primary_opioid_med.med_name
        else:
            patient.primary_opioid_med_name = None

        #Assign patient secondary opioid medication class:
        secondary_med = patient_info_blob['sec_opioid_name']
        patient.secondary_opioid_med = self.assign_med_class(secondary_med)
        
        if patient.secondary_opioid_med != None:
            patient.secondary_opioid_med_name = patient.secondary_opioid_med.med_name
        else:
            patient.secondary_opioid_med_name = None
        
        #Assign all patient primary and secondary medication attributes to temporary local
        #variables (note, if the patient did not have an entry in REDCap, then
        #corresponding variable object is None):

        #Primary opioid medication:
        if patient_info_blob['prim_opioid_dose_freq'] == None:
            prim_opioid_dose_freq = patient_info_blob['prim_opioid_dose_freq']
        else:
            prim_opioid_dose_freq = float(patient_info_blob['prim_opioid_dose_freq'])

        if patient_info_blob['prim_opioid_episode_dose'] == None:
            prim_opioid_episode_dose = patient_info_blob['prim_opioid_episode_dose']
        else:
            prim_opioid_episode_dose = float(patient_info_blob['prim_opioid_episode_dose'])

        if patient_info_blob['prim_opioid_const_ep_unit_dose'] == None:
            prim_opioid_const_ep_unit_dose = patient_info_blob['prim_opioid_const_ep_unit_dose']
        else:
            prim_opioid_const_ep_unit_dose = float(patient_info_blob['prim_opioid_const_ep_unit_dose'])

        if patient_info_blob['prim_opioid_const_ep_capsule_cnt'] == None:
            prim_opioid_const_ep_capsule_cnt = patient_info_blob['prim_opioid_const_ep_capsule_cnt']
        else:
            prim_opioid_const_ep_capsule_cnt = float(patient_info_blob['prim_opioid_const_ep_capsule_cnt'])

        if patient_info_blob['prim_opioid_episode_dose_1'] == None:
            prim_opioid_ep_dose_1 = patient_info_blob['prim_opioid_episode_dose_1']
        else:
            prim_opioid_ep_dose_1 = float(patient_info_blob['prim_opioid_episode_dose_1'])

        if patient_info_blob['prim_opioid_ep_1_unit_dose'] == None:
            prim_opioid_ep_1_unit_dose = patient_info_blob['prim_opioid_ep_1_unit_dose']
        else:
            prim_opioid_ep_1_unit_dose = float(patient_info_blob['prim_opioid_ep_1_unit_dose'])

        if patient_info_blob['prim_opioid_ep_1_capsule_cnt'] == None:
            prim_opioid_ep_1_capsule_cnt = patient_info_blob['prim_opioid_ep_1_capsule_cnt']
        else:
            prim_opioid_ep_1_capsule_cnt = float(patient_info_blob['prim_opioid_ep_1_capsule_cnt'])

        if patient_info_blob['prim_opioid_episode_dose_2'] == None:
            prim_opioid_ep_dose_2 = patient_info_blob['prim_opioid_episode_dose_2']
        else:
            prim_opioid_ep_dose_2 = float(patient_info_blob['prim_opioid_episode_dose_2'])

        if patient_info_blob['prim_opioid_ep_2_unit_dose'] == None:
            prim_opioid_ep_2_unit_dose = patient_info_blob['prim_opioid_ep_2_unit_dose']
        else:
            prim_opioid_ep_2_unit_dose = float(patient_info_blob['prim_opioid_ep_2_unit_dose'])

        if patient_info_blob['prim_opioid_ep_2_capsule_cnt'] == None:
            prim_opioid_ep_2_capsule_cnt = patient_info_blob['prim_opioid_ep_2_capsule_cnt']
        else:
            prim_opioid_ep_2_capsule_cnt = float(patient_info_blob['prim_opioid_ep_2_capsule_cnt'])

        if patient_info_blob['prim_opioid_episode_dose_3'] == None:
            prim_opioid_ep_dose_3 = patient_info_blob['prim_opioid_episode_dose_3']
        else:
            prim_opioid_ep_dose_3 = float(patient_info_blob['prim_opioid_episode_dose_3'])

        if patient_info_blob['prim_opioid_ep_3_unit_dose'] == None:
            prim_opioid_ep_3_unit_dose = patient_info_blob['prim_opioid_ep_3_unit_dose']
        else:
            prim_opioid_ep_3_unit_dose = float(patient_info_blob['prim_opioid_ep_3_unit_dose'])

        if patient_info_blob['prim_opioid_ep_3_capsule_cnt'] == None:
            prim_opioid_ep_3_capsule_cnt = patient_info_blob['prim_opioid_ep_3_capsule_cnt']
        else:
            prim_opioid_ep_3_capsule_cnt = float(patient_info_blob['prim_opioid_ep_3_capsule_cnt'])

        if patient_info_blob['prim_opioid_episode_dose_4'] == None:
            prim_opioid_ep_dose_4 = patient_info_blob['prim_opioid_episode_dose_4']
        else:
            prim_opioid_ep_dose_4 = float(patient_info_blob['prim_opioid_episode_dose_4'])

        if patient_info_blob['prim_opioid_ep_4_unit_dose'] == None:
            prim_opioid_ep_4_unit_dose = patient_info_blob['prim_opioid_ep_4_unit_dose']
        else:
            prim_opioid_ep_4_unit_dose = float(patient_info_blob['prim_opioid_ep_4_unit_dose'])

        if patient_info_blob['prim_opioid_ep_4_capsule_cnt'] == None:
            prim_opioid_ep_4_capsule_cnt = patient_info_blob['prim_opioid_ep_4_capsule_cnt']
        else:
            prim_opioid_ep_4_capsule_cnt = float(patient_info_blob['prim_opioid_ep_4_capsule_cnt'])

        #Secondary opioid medication:
        if patient_info_blob['sec_opioid_dose_freq'] == None:
            sec_opioid_dose_freq = patient_info_blob['sec_opioid_dose_freq']
        else:
            sec_opioid_dose_freq = float(patient_info_blob['sec_opioid_dose_freq'])

        if patient_info_blob['sec_opioid_episode_dose'] == None:
            sec_opioid_episode_dose = patient_info_blob['sec_opioid_episode_dose']
        else:
            sec_opioid_episode_dose = float(patient_info_blob['sec_opioid_episode_dose'])

        if patient_info_blob['sec_opioid_const_ep_unit_dose'] == None:
            sec_opioid_const_ep_unit_dose = patient_info_blob['sec_opioid_const_ep_unit_dose']
        else:
            sec_opioid_const_ep_unit_dose = float(patient_info_blob['sec_opioid_const_ep_unit_dose'])

        if patient_info_blob['sec_opioid_const_ep_capsule_cnt'] == None:
            sec_opioid_const_ep_capsule_cnt = patient_info_blob['sec_opioid_const_ep_capsule_cnt']
        else:
            sec_opioid_const_ep_capsule_cnt = float(patient_info_blob['sec_opioid_const_ep_capsule_cnt'])

        if patient_info_blob['sec_opioid_episode_dose_1'] == None:
            sec_opioid_ep_dose_1 = patient_info_blob['sec_opioid_episode_dose_1']
        else:
            sec_opioid_ep_dose_1 = float(patient_info_blob['sec_opioid_episode_dose_1'])

        if patient_info_blob['sec_opioid_ep_1_unit_dose'] == None:
            sec_opioid_ep_1_unit_dose = patient_info_blob['sec_opioid_ep_1_unit_dose']
        else:
            sec_opioid_ep_1_unit_dose = float(patient_info_blob['sec_opioid_ep_1_unit_dose'])

        if patient_info_blob['sec_opioid_ep_1_capsule_cnt'] == None:
            sec_opioid_ep_1_capsule_cnt = patient_info_blob['sec_opioid_ep_1_capsule_cnt']
        else:
            sec_opioid_ep_1_capsule_cnt = float(patient_info_blob['sec_opioid_ep_1_capsule_cnt'])

        if patient_info_blob['sec_opioid_episode_dose_2'] == None:
            sec_opioid_ep_dose_2 = patient_info_blob['sec_opioid_episode_dose_2']
        else:
            sec_opioid_ep_dose_2 = float(patient_info_blob['sec_opioid_episode_dose_2'])

        if patient_info_blob['sec_opioid_ep_2_unit_dose'] == None:
            sec_opioid_ep_2_unit_dose = patient_info_blob['sec_opioid_ep_2_unit_dose']
        else:
            sec_opioid_ep_2_unit_dose = float(patient_info_blob['sec_opioid_ep_2_unit_dose'])

        if patient_info_blob['sec_opioid_ep_2_capsule_cnt'] == None:
            sec_opioid_ep_2_capsule_cnt = patient_info_blob['sec_opioid_ep_2_capsule_cnt']
        else:
            sec_opioid_ep_2_capsule_cnt = float(patient_info_blob['sec_opioid_ep_2_capsule_cnt'])

        if patient_info_blob['sec_opioid_episode_dose_3'] == None:
            sec_opioid_ep_dose_3 = patient_info_blob['sec_opioid_episode_dose_3']
        else:
            sec_opioid_ep_dose_3 = float(patient_info_blob['sec_opioid_episode_dose_3'])

        if patient_info_blob['sec_opioid_ep_3_unit_dose'] == None:
            sec_opioid_ep_3_unit_dose = patient_info_blob['sec_opioid_ep_3_unit_dose']
        else:
            sec_opioid_ep_3_unit_dose = float(patient_info_blob['sec_opioid_ep_3_unit_dose'])

        if patient_info_blob['sec_opioid_ep_3_capsule_cnt'] == None:
            sec_opioid_ep_3_capsule_cnt = patient_info_blob['sec_opioid_ep_3_capsule_cnt']
        else:
            sec_opioid_ep_3_capsule_cnt = float(patient_info_blob['sec_opioid_ep_3_capsule_cnt'])

        if patient_info_blob['sec_opioid_episode_dose_4'] == None:
            sec_opioid_ep_dose_4 = patient_info_blob['sec_opioid_episode_dose_4']
        else:
            sec_opioid_ep_dose_4 = float(patient_info_blob['sec_opioid_episode_dose_4'])

        if patient_info_blob['sec_opioid_ep_4_unit_dose'] == None:
            sec_opioid_ep_4_unit_dose = patient_info_blob['sec_opioid_ep_4_unit_dose']
        else:
            sec_opioid_ep_4_unit_dose = float(patient_info_blob['sec_opioid_ep_4_unit_dose'])

        if patient_info_blob['sec_opioid_ep_4_capsule_cnt'] == None:
            sec_opioid_ep_4_capsule_cnt = patient_info_blob['sec_opioid_ep_4_capsule_cnt']
        else:
            sec_opioid_ep_4_capsule_cnt = float(patient_info_blob['sec_opioid_ep_4_capsule_cnt'])

        #Generate primary medication attributes for patient instance:

        #Identify number of episode doses per 24 hr for primary opioid med and
        #convert to an int object for numeric logical comparison:
        prim_op_ep_per_day = int(patient_info_blob['prim_opioid_cnt_daily_dose'])

        #Identify dose frequency per 24 hr (i.e., interdose duration):
        patient.prim_opioid_interdose_duration = prim_opioid_dose_freq

        #Case 1--patient only has 1 episode dose per day for primary opioid_df
        #medication:
        patient.primary_opioid_episode_dose = prim_opioid_episode_dose
        patient.primary_opioid_unit_dose = prim_opioid_const_ep_unit_dose
        patient.primary_opioid_captab_per_episode_dose = prim_opioid_const_ep_capsule_cnt
        patient.primary_opioid_interdose_duration = prim_opioid_dose_freq

        if prim_op_ep_per_day > 1:
            #If patient has >1 episode doses for primary med, then identify if
            #episodes for primary med are all equivalent; will be either 'Yes' or
            #'No' string value:
            prim_op_ep_const_dose = int(patient_info_blob['prim_opioid_const_ep_dose'])
            if prim_op_ep_const_dose == 0:
                patient.different_daily_episode_doses_med_1 = 'Yes'
                pass
            elif prim_op_ep_const_dose == 1:
                patient.different_daily_episode_doses_med_1 = 'No'
                pass
            else:
                pass

            #Case 2--patient has >1 episode dose per day, but each episode dose is
            #an EQUIVALENT episode dose (in this case, we can use number of episodes
            #and episode dose to assign the correct patient primary med attributes):
            if patient.different_daily_episode_doses_med_1 == 'No':
                #Each equivalent episode dose (self.primary_opioid_episode_dose)
                #is already represented by Case 1 attributes
                #for each episode dose attribute:
                pass

            #Case 3--patient has >1 episode dose per day, and episode doses are
            #NOT ALL equivalent:
            if patient.different_daily_episode_doses_med_1 == 'Yes':
                patient.primary_opioid_dif_dose_episode_dose_1 = prim_opioid_ep_dose_1
                patient.primary_opioid_dif_dose_ep_1_unit_dose = prim_opioid_ep_1_unit_dose
                patient.primary_opioid_dif_dose_captab_per_episode_dose_1 = prim_opioid_ep_1_capsule_cnt
                patient.primary_opioid_dif_dose_episode_dose_2 = prim_opioid_ep_dose_2
                patient.primary_opioid_dif_dose_ep_2_unit_dose = prim_opioid_ep_2_unit_dose
                patient.primary_opioid_dif_dose_captab_per_episode_dose_2 =  prim_opioid_ep_2_capsule_cnt
                patient.primary_opioid_dif_dose_episode_dose_3 = prim_opioid_ep_dose_3
                patient.primary_opioid_dif_dose_ep_3_unit_dose = prim_opioid_ep_3_unit_dose
                patient.primary_opioid_dif_dose_captab_per_episode_dose_3 = prim_opioid_ep_3_capsule_cnt
                patient.primary_opioid_dif_dose_episode_dose_4 = prim_opioid_ep_dose_4
                patient.primary_opioid_dif_dose_ep_4_unit_dose = prim_opioid_ep_4_unit_dose
                patient.primary_opioid_dif_dose_captab_per_episode_dose_4 = prim_opioid_ep_4_capsule_cnt

        #Generate primary medication attributes for patient instance:

        #Check if there are 2 different opioid medications; if yes, then
        #proceed to define attributes for secondary medication:
        if patient.opioid_med_count == 2:
            #Identify number of episode doses per 24 hr for secondary opioid med and
            #convert to an int object for numeric logical comparison:
            sec_op_ep_per_day = int(patient_info_blob['sec_opioid_cnt_daily_dose'])

            #Identify dose frequency per 24 hr (i.e., interdose duration):
            patient.secondary_opioid_interdose_duration = sec_opioid_dose_freq

            #Case 1--patient only has 1 episode dose per day for secondary opioid_df
            #medication:
            patient.secondary_opioid_episode_dose = sec_opioid_episode_dose
            patient.secondary_opioid_unit_dose = sec_opioid_const_ep_unit_dose
            patient.secondary_opioid_captab_per_episode_dose = sec_opioid_const_ep_capsule_cnt
            patient.secondary_opioid_interdose_duration = sec_opioid_dose_freq

            if sec_op_ep_per_day > 1:
                #If patient has >1 episode doses for secondary med, then identify if
                #episodes for secondary med are all equivalent; will be either 'Yes' or
                #'No' string value:
                sec_op_ep_const_dose = int(patient_info_blob['sec_opioid_const_ep_dose'])
                if sec_op_ep_const_dose == 0:
                    patient.different_daily_episode_doses_med_2 = 'Yes'
                    pass
                elif sec_op_ep_const_dose == 1:
                    patient.different_daily_episode_doses_med_2 = 'No'
                    pass
                else:
                    pass

                #Case 2--patient has >1 episode dose per day, but each episode dose is
                #an EQUIVALENT episode dose (in this case, we can use number of episodes
                #and episode dose to assign the correct patient secondary med attributes):
                if patient.different_daily_episode_doses_med_2 == 'No':
                    #Each equivalent episode dose (self.secondary_opioid_episode_dose)
                    #is already represented by Case 1 attributes
                    #for each episode dose attribute:
                    pass

                #Case 3--patient has >1 episode dose per day, and episode doses are
                #NOT ALL equivalent:
                if patient.different_daily_episode_doses_med_2 == 'Yes':
                    patient.secondary_opioid_dif_dose_episode_dose_1 = sec_opioid_ep_dose_1
                    patient.secondary_opioid_dif_dose_ep_1_unit_dose = sec_opioid_ep_1_unit_dose
                    patient.secondary_opioid_dif_dose_captab_per_episode_dose_1 = sec_opioid_ep_1_capsule_cnt
                    patient.secondary_opioid_dif_dose_episode_dose_2 = sec_opioid_ep_dose_2
                    patient.secondary_opioid_dif_dose_ep_2_unit_dose = sec_opioid_ep_2_unit_dose
                    patient.secondary_opioid_dif_dose_captab_per_episode_dose_2 =  sec_opioid_ep_2_capsule_cnt
                    patient.secondary_opioid_dif_dose_episode_dose_3 = sec_opioid_ep_dose_3
                    patient.secondary_opioid_dif_dose_ep_3_unit_dose = sec_opioid_ep_3_unit_dose
                    patient.secondary_opioid_dif_dose_captab_per_episode_dose_3 = sec_opioid_ep_3_capsule_cnt
                    patient.secondary_opioid_dif_dose_episode_dose_4 = sec_opioid_ep_dose_4
                    patient.secondary_opioid_dif_dose_ep_4_unit_dose = sec_opioid_ep_4_unit_dose
                    patient.secondary_opioid_dif_dose_captab_per_episode_dose_4 = sec_opioid_ep_4_capsule_cnt

        print('Assigning patient instance.')

        return patient

    def assign_med_class(self, opioid_med_value):
        """Convert opioid medication value into medication class instance.

        Args:
          opioid_med_string: an int variable corresponding to available opioid
          medication (mapped from RedCap entry)

        Returns:
          A medication class object corresponding to the value arg.

        Raises:
          ValueError: If no available medication value passed as arg.

        """
        drug_value_map = {'1': Hydrocodone_Acetaminophen(),\
                          '2': Hydromorphone_Immediate_Release(),\
                          '3': Morphine_Immediate_Release(),\
                          '4': Morphine_Extended_Release(),\
                          '5': Oxycodone_Immediate_Release(),\
                          '6': Oxycodone_Extended_Release(),\
                          '7': Oxycodone_Acetaminophen(),\
                          '8': Tramadol_Immediate_Release()
                           }
        if opioid_med_value in list(drug_value_map.keys()):
            return drug_value_map[opioid_med_value]
        else:
            return None

    def build_patients(self):
        patient_obj_list = []
        for payload_obj in self.payload:
            #Make sure to restrict use of only dictionary objects with data
            #from patient's initial baseline state (i.e., dictionary objects
            #in which key ('redcap_event_name') has value of 
            #'baseline_data_arm_1')) 
            if payload_obj['redcap_event_name'] == 'baseline_data_arm_1':
                new_patient = self.assign_patient_instance(payload_obj)
                patient_obj_list.append(new_patient)
                pass
            else:
                #Objects that do not represent baseline patient data;
                #do not use these to build patient objects.
                pass
            pass
        pass

        #Generate med class objects:
        print('\nAll patients constructed.\n')

        return patient_obj_list

    def data_check(self):
        #Check ingested data:
        # med_string = input('Enter med name:')
        # print(type(med_string))
        #
        # #Assert opioid_med_string is a string object type:
        # while True:
        #     try:
        #         assert isinstance(med_string, str)
        #         break
        #     except TypeError:
        #         print("Oops!  That was not a valid string.  Try again...")
        #
        #
        # #Assign patient and med class instances:
        # med_obj = Assign_med_class(med_string)
        #
        # print(med_obj)
        return
