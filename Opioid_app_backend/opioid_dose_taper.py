#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 12:10:30 2019

@author: dannywitt
"""

from Opioid_app_backend.patient_information import Patient

class Taper(Patient):
    '''Class designed to
    '''

    def __init__(self,
                 a_unique_patient):

        #Set marker for when all medications exhausted:
        self.all_done = False

        #Instantiate attribute:
        self.yes_2_meds = False
        self.post_taper_dose_24 = None

        #Prior to taper, what is most up to date medication list:
        self.pre_taper_med_list = a_unique_patient.Current_medication_list()

        #Identify correct medication to be tapered:
        self.current_taper_med = self.Sort_and_choose_medications(self.pre_taper_med_list)
        #Generate total MME for all medications and doses prior to taper:
        self.pre_taper_total_all_med_MME_24 = a_unique_patient.Calculate_total_MME_24_hr()

        #Generate each medication's dose and MME from patient object:

        #Drug 1: primary med
        if a_unique_patient.primary_opioid_med != None:
            self.taper_primary_med = a_unique_patient.primary_opioid_med
            if a_unique_patient.different_daily_episode_doses_med_1 != 'Yes':
                self.taper_primary_med_episode_dose = a_unique_patient.primary_opioid_episode_dose
                pass
            elif a_unique_patient.different_daily_episode_doses_med_1 == 'Yes':
                self.taper_primary_med_episode_dose_diff_1 = a_unique_patient.primary_opioid_dif_dose_episode_dose_1
                self.taper_primary_med_episode_dose_diff_2 = a_unique_patient.primary_opioid_dif_dose_episode_dose_2
                self.taper_primary_med_episode_dose_diff_3 = a_unique_patient.primary_opioid_dif_dose_episode_dose_3
                self.taper_primary_med_episode_dose_diff_4 = a_unique_patient.primary_opioid_dif_dose_episode_dose_4
                pass
            else:
                pass
            self.taper_primary_med_dose_24 = a_unique_patient.Primary_total_dose_per_24_hr()
            self.taper_primary_med_MME_24 = a_unique_patient.Calculate_med_MME_24_hr(a_unique_patient.primary_opioid_med)

            #Taper med is patient's primary med:
            if self.current_taper_med == self.taper_primary_med:
                self.current_taper_med = self.taper_primary_med
                self.current_taper_med_dose_24 = self.taper_primary_med_dose_24
                self.current_taper_med_MME_24 = self.taper_primary_med_MME_24
            else:
                pass

            #Update previous dose (pre-taper) as current "previous dose" (post-taper)
            #self.previous_primary_med_dose = self.taper_primary_med_dose_24

        else:
            self.taper_primary_med = None

        #Drug 2: secondary med
        if a_unique_patient.secondary_opioid_med != None:
            self.taper_secondary_med = a_unique_patient.secondary_opioid_med
            if a_unique_patient.different_daily_episode_doses_med_2 != 'Yes':
                self.taper_secondary_med_episode_dose = a_unique_patient.secondary_opioid_episode_dose
                pass
            elif a_unique_patient.different_daily_episode_doses_med_2 == 'Yes':
                self.taper_secondary_med_episode_dose_diff_1 = a_unique_patient.secondary_opioid_dif_dose_episode_dose_1
                self.taper_secondary_med_episode_dose_diff_2 = a_unique_patient.secondary_opioid_dif_dose_episode_dose_2
                self.taper_secondary_med_episode_dose_diff_3 = a_unique_patient.secondary_opioid_dif_dose_episode_dose_3
                self.taper_secondary_med_episode_dose_diff_4 = a_unique_patient.secondary_opioid_dif_dose_episode_dose_4
                pass
            else:
                pass
            self.taper_secondary_med_dose_24 = a_unique_patient.Secondary_total_dose_per_24_hr()
            self.taper_secondary_med_MME_24 = a_unique_patient.Calculate_med_MME_24_hr(a_unique_patient.secondary_opioid_med)

            #Taper med is patient's secondary med:
            if self.current_taper_med == self.taper_secondary_med:
                self.current_taper_med = self.taper_secondary_med
                self.current_taper_med_dose_24 = self.taper_secondary_med_dose_24
                self.current_taper_med_MME_24 = self.taper_secondary_med_MME_24
            else:
                pass
            #Update previous dose (pre-taper) as current "previous dose" (post-taper)
            #self.previous_secondary_med_dose = self.taper_sec_med_dose_24

        else:
            self.taper_secondary_med = None

        #Execute actual taper if there are medications in patient's list:
        if self.taper_primary_med != None or self.taper_secondary_med != None:
            self.Apply_taper(a_unique_patient, self.current_taper_med)
            pass
        #Otherwise, if no medications in patient's med list, then return all
        #Taper object attributes as "None":
        else:
            self.non_taper_med_list = None
            self.total_taper_MME_difference = None
            self.post_taper_med_MME_24 = None
            self.pre_taper_dose_24 = None
            self.post_taper_dose_24 = None

        return

    def Sort_and_choose_medications(self, list_of_meds):
        '''Input list of medications and sort through medications to choose
        correct taper medication; highest priority given to medications that
        are extended release, followed by immediate release, and finally lowest
        priority given to tramadol (i.e., tramadol is last medication to taper).
        '''

        #Part 1: Identify if Tramadol is in medication list
        available_meds = [x for x in list_of_meds if x is not None]
        number_of_meds = len(available_meds)
        #If there are at least 1 medication in the available meds list,
        #then proceed with sorting the appropriate medication to taper:

        if number_of_meds > 0:
            # NO TRAMADOL CASES: proceed with identifying extended and immediate
            #release medications:
            #Step 1: Check to see if Tramadol present-- not present
            if self.Tramadol_filter(available_meds) is False:
                self.Extended_vs_immediate_filter(available_meds)
                non_tram_pre_taper_extended_release = self.extended_release_drugs
                non_tram_pre_taper_immediate_release = self.immediate_release_drugs

                #Case 1.0: No tramadol, but extended release is present
                if non_tram_pre_taper_extended_release:
                    current_taper_med = self.Apply_potency_ranking(non_tram_pre_taper_extended_release)

                    #Case 1.1: only one extended release medication in total;
                    #return only current_taper_med
                    if number_of_meds == 1:
                        self.non_taper_med_list = []
                        return current_taper_med

                    #Case 1.2: at least one extended release (current taper med)
                    #and one additional medication in list; return
                    #current_taper_med and update self.non_taper_med_list with
                    #other single med
                    elif number_of_meds == 2:
                        self.non_taper_med_list = []
                        for medication in available_meds:
                            if medication != current_taper_med:
                                self.non_taper_med_list.append(medication)
                                pass
                            pass
                        return current_taper_med

                    #Case 1.3: at least one extended release (current taper med)
                    #and two additional medications in list; return
                    #current_taper_med and update self.non_taper_med_list with
                    #other two medications
                    elif number_of_meds == 3:
                        self.non_taper_med_list = []
                        for medication in available_meds:
                            if medication != current_taper_med:
                                self.non_taper_med_list.append(medication)
                                pass
                            pass
                        return current_taper_med

                #Case 2.0: No tramadol, no extended release, so at least one
                #immediate release medication present in medication list
                elif not non_tram_pre_taper_extended_release:
                    current_taper_med = self.Apply_potency_ranking(non_tram_pre_taper_immediate_release)

                    #Case 2.1: No tramadol, and only one immediate release
                    #medication in total; return only current_taper_med
                    if number_of_meds == 1:
                        self.non_taper_med_list = []
                        return current_taper_med

                    #Case 2.2: No tramadol; two immediate release medications
                    #in total; return current_taper_med and update
                    #self.non_taper_med_list with other medication
                    elif number_of_meds == 2:
                        self.non_taper_med_list = []
                        for medication in available_meds:
                            if medication != current_taper_med:
                                self.non_taper_med_list.append(medication)
                                pass
                            pass
                        return current_taper_med

                    #Case 2.3: No tramadol; three immediate release medications
                    #in total; return current_taper_med and return other two
                    #medications in updated self.non_taper_med_list
                    elif number_of_meds == 3:
                        self.non_taper_med_list = []
                        for medication in available_meds:
                            if medication != current_taper_med:
                                self.non_taper_med_list.append(medication)
                                pass
                            pass
                        return current_taper_med
                    pass
                pass
            else:
                pass

            #TRAMADOL IS PRESENT CASES:

            #Case 3.0: Check to see if Tramadol in list and whether it is ONLY medication;
            #if only Tramadol left in medication list, choose Tramadol as
            #current taper medication:

            if self.Tramadol_filter(available_meds) is True and number_of_meds == 1:
                current_taper_med = available_meds[0]
                return current_taper_med
            else:
                pass

            #Case 4.0: Else, if Tramadol in medication list with other medications, then
            #temporarily remove Tramadol from local list of available medications:
            if self.Tramadol_filter(available_meds) is True and number_of_meds != 1:
                #Collect non-Tramadol meds for filtering; but, maintain available_meds
                #list as original non-None medications (including Tramadol)
                non_tram_meds = available_meds[:]
                for medication in available_meds:
                    if medication.med_name == 'Tramadol' or medication.med_name == 'Tramadol Acetaminophen':
                        non_tram_meds.remove(medication)
                        pass
                    else:
                        pass
                    pass
                #Case 4.1: Check extended vs. non-extended release types and sort into
                #two lists:

                #Update number of available non-Tramadol medications:
                number_of_meds = len(non_tram_meds)

                #Using available meds w/ removed Tramadol (from step in Case 4.0)
                self.Extended_vs_immediate_filter(non_tram_meds)
                non_tram_pre_taper_extended_release = self.extended_release_drugs
                non_tram_pre_taper_immediate_release = self.immediate_release_drugs

                #Case 4.2: If extended release medications exist, then choose any random
                #medication from list (not including Tramadol) and update that med
                #to current taper medication:

                if non_tram_pre_taper_extended_release:
                    current_taper_med = self.Apply_potency_ranking(non_tram_pre_taper_extended_release)

                    #Case 4.2.1: one extended release medication in addition to
                    #Tramadol; return only current_taper_med:

                    if number_of_meds == 1:
                        self.non_taper_med_list = []
                        for medication in available_meds:
                            if medication != current_taper_med:
                                self.non_taper_med_list.append(medication)
                                pass
                        return current_taper_med

                    #Case 4.2.2: at least one extended release (current taper med)
                    #and one additional medication in list; return
                    #current_taper_med and update self.non_taper_med_list with
                    #other single med
                    elif number_of_meds == 2:
                        self.non_taper_med_list = []
                        for medication in available_meds:
                            if medication != current_taper_med:
                                self.non_taper_med_list.append(medication)
                                pass
                            pass
                        return current_taper_med

                #Case 4.3: If no extended release medications remain in list, then apply
                #decision rules for immediate release medications and update that
                #med to current taper medication:

                elif not non_tram_pre_taper_extended_release:
                    current_taper_med = self.Apply_potency_ranking(non_tram_pre_taper_immediate_release)

                    #Case 4.3.1: one immediate release medication in addition
                    #to Tramadol; return only current_taper_med

                    if number_of_meds == 1:
                        self.non_taper_med_list = []
                        for medication in available_meds:
                            if medication != current_taper_med:
                                self.non_taper_med_list.append(medication)
                                pass
                        return current_taper_med

                    #Case 4.3.2: at least one immediate release (current taper med)
                    #and one additional medication in list; return
                    #current_taper_med and update self.non_taper_med_list with
                    #other single med
                    elif number_of_meds == 2:
                        self.non_taper_med_list = []
                        for medication in available_meds:
                            if medication != current_taper_med:
                                self.non_taper_med_list.append(medication)
                                pass
                            pass
                        return current_taper_med
                    else:
                        pass
                    pass
                else:
                    pass
                pass
            else:
                pass
            pass
        else:
            self.all_done = True
            pass

    def Extended_vs_immediate_filter(self, list_of_meds):
        '''A method for determining which medications in a pre-taper list of
        medications are extended or immediate release, then returning a list of
        extended release and list of immediate release meds'''
        self.immediate_release_drugs = []
        self.extended_release_drugs = []
        for medication in list_of_meds:
            if medication != None:
                if medication.delivery_rate == 'Extended Release':
                    self.extended_release_drugs.append(medication)
                    pass
                elif medication.delivery_rate == 'Immediate Release':
                    self.immediate_release_drugs.append(medication)
                    pass
                pass
            else:
                pass
        return

    def Apply_potency_ranking(self, list_of_meds):
        '''Input list of either all immediate release or all extended release
        medications; sort list from index = 0 to n with following medication
        taper priority:

            oxycodone > hydromorphone > morphine > hydrocodone > tramadol
        e.g., if oxycodone IR and morphine IR both in patient list, then taper
        oxycodone to 0mg before starting subsequent taper of morphine
        '''

        for medication in list_of_meds:
            if 'Oxycodone' in medication.med_name.split():
                priority_taper = medication
                pass
            else:
                pass
            if 'Hydromorphone' in medication.med_name.split():
                priority_taper = medication
                pass
            else:
                pass
            if 'Morphine' in medication.med_name.split():
                priority_taper = medication
                pass
            else:
                pass
            if 'Hydrocodone' in medication.med_name.split():
                priority_taper = medication
                pass
            else:
                pass

        return priority_taper

    def Tramadol_filter(self, list_of_meds):
        '''A method for determining if a list of medications in a pre-taper
        list of medications includes Tramadol, outputs True or False'''
        tramadol_list = []
        for medication in list_of_meds:
            if medication.med_name == 'Tramadol' or medication.med_name == 'Tramadol Acetaminophen':
                tramadol_list.append(1)
            else:
                tramadol_list.append(0)

        if sum(tramadol_list) > 0:
            return True
        else:
            return False

    def Apply_taper(self, patient, medication):
        '''Apply actual taper to chosen taper medication, return updated post-
        taper medication dose (over 24 hours) and episode dose at stable inter-
        dose frequency
        '''
        #Part 1: Calculate total MME taper reduction amount

        #First Decision: is the total MME > 60 MME?
        #If total MME (24 hrs) is > 60 MME, then the taper should be a
        #reduction in MME by 10% of total pre-taper MME (i.e., multiply by
        # 0.9*pre-taper MME):
        pre_taper_total_MME_24 = self.pre_taper_total_all_med_MME_24
        if pre_taper_total_MME_24 > 60:
            #Calculate taper in MME over 24 hours:
            self.post_taper_total_MME_24 = (pre_taper_total_MME_24 * 0.9)

            #Calculate taper in dose of taper medication over 24 hours:
            #First, calculate total taper change in MME over 24 hours:
            self.total_taper_MME_difference = pre_taper_total_MME_24 - self.post_taper_total_MME_24

        #Else, taper is minus 5 MME:
        elif 0 < pre_taper_total_MME_24 <=60:
            self.post_taper_total_MME_24 = pre_taper_total_MME_24 - 5
            self.total_taper_MME_difference = pre_taper_total_MME_24 - self.post_taper_total_MME_24
            pass
        elif pre_taper_total_MME_24 <= 0:
            self.post_taper_total_MME_24 = 0
            self.total_taper_MME_difference = 0
            pass
        else:
            pass


        #Part 2: Now, assess whether taper reduction will be (1) applied to only
        #a single medication but will not exhaust that medication's dose/MME,
        #(2) applied to only a single medication but will exhaust that medication
        #dose/MME to exactly 0, or (3) spread across two medications (by
        #exhausting the initial taper medication #1 and then reducing the
        #dose/MME of a second taper medication #2)

        #Case 2.1: only one medication tapered and not exhausted to 0mg or O MME
        #If current MME of taper drug > post-taper MME of given taper drug, then
        #proceed and update 24-hour dose of given drug, and keep same drug list
        #and primary/secondary meds

        if self.current_taper_med_MME_24 > self.total_taper_MME_difference:
            self.yes_2_meds = False
            #Calculate MME for medication:
            self.post_taper_med_MME_24 = self.current_taper_med_MME_24 - self.total_taper_MME_difference
            #Next, use this to calculate total decrease in dose over 24 hr:
            self.pre_taper_dose_24 = self.current_taper_med_dose_24
            self.post_taper_dose_reduction_over_24 = self.total_taper_MME_difference / self.current_taper_med.MME_conversion_factor
            #Return post_taper_dose_24
            self.post_taper_dose_24 = self.pre_taper_dose_24 - self.post_taper_dose_reduction_over_24
            pass

        #Case 2.2: If current MME of taper drug = post-taper MME of given taper
        #drug, then proceed and move tapered drug to be 'None', and update
        #medication status as such
        elif self.current_taper_med_MME_24 == self.total_taper_MME_difference:
            self.yes_2_meds = False
            #Calculate MME for medication:
            self.post_taper_med_MME_24 = self.current_taper_med_MME_24 - self.total_taper_MME_difference
            #Next, use this to calculate total decrease in dose over 24 hr:
            self.pre_taper_dose_24 = self.current_taper_med_dose_24
            self.post_taper_dose_reduction_over_24 = self.total_taper_MME_difference / self.current_taper_med.MME_conversion_factor
            #Return post_taper_dose_24
            self.post_taper_dose_24 = self.pre_taper_dose_24 - self.post_taper_dose_reduction_over_24
            future_med_list = [med for med in patient.Current_medication_list() if med != self.current_taper_med and med != None]
            self.current_taper_med = None

            #Check if last medication in list, and ending perfectly at 0mg; if
            #this is the case, then set self.all_done flag to equal True:
            if len(future_med_list) == 0:
                self.all_done = True
            pass

        #Case 2.3: #If current MME of taper drug < post-taper MME of given
        #taper drug, then proceed to move taper drug 1 to be 'None',
        #calculate remaining "MME needed to still taper in episode", by
        #subtracting post-taper MME minus previously current MME of taper
        #drug, then select new taper drug (i.e., taper drug 2) using
        #Sort_and_choose_medications() method, apply taper to new drug

        elif self.current_taper_med_MME_24 < self.total_taper_MME_difference:
            self.yes_2_meds = True
            #Calculate residual taper MME left over after initial current
            #taper med exhausted:
            self.residual_taper_MME = self.total_taper_MME_difference - self.current_taper_med_MME_24
            self.pre_taper_dose_24_med_1 = self.current_taper_med_dose_24
            self.post_taper_dose_24_med_1 = 0

            #Update medication list with exhausted medication as "None":
            self.pre_taper_med_list = [x if x != self.current_taper_med else None for x in self.pre_taper_med_list]
            #Before changing to next taper medication, save record of first
            #tapered medication which was exhausted to 0mg dose/ MME:
            self.previous_tapered_med_now_exhausted = self.current_taper_med

            #Identify correct second medication to be tapered:
            self.current_taper_med = self.Sort_and_choose_medications(self.pre_taper_med_list)
            if self.all_done is True:
                self.post_taper_dose_24_med_2 = 0
#                import sys
#                sys.exit('All medications have been tapered to 0mg/0 MME for this patient. \
#            Proceed with all placebo treatment.')
#                pass
            else:
                for medication in enumerate(self.pre_taper_med_list):
                    if medication[1] == self.current_taper_med:
                        if medication[0] == 0:
                            self.current_taper_med_dose_24 = self.taper_primary_med_dose_24
                            pass
                        elif medication[0] == 1:
                            self.current_taper_med_dose_24 = self.taper_secondary_med_dose_24
                            pass
                        else:
                            pass
                        pass
                    else:
                        pass

                self.pre_taper_dose_24_med_2 = self.current_taper_med_dose_24
                #Convert residual MME into reduction of second taper medication's
                #dosage:
                self.second_taper_dose_reduction_24 = self.residual_taper_MME / self.current_taper_med.MME_conversion_factor
                self.post_taper_dose_24_med_2 = self.pre_taper_dose_24_med_2 - self.second_taper_dose_reduction_24
                if self.post_taper_dose_24_med_2 < 0:
                    #Set that medication to 0mg/O MME:
                    self.post_taper_dose_24_med_2 = 0

                #Check to see if 2nd tapered med (in given taper cycle) has also been exhausted; if this is
                #the case, then proceed to taper the 3rd medication (if one exists)

                ############################PROCEED HERE, NOT FINISHED FOR SPECIAL CASES WITH
                #EXHAUSTING 2nd tapered med (choosing 3rd current taper med)within same taper
                #episode (use above logic used to choose next taper med from above):

                    #Choose new current taper medication:
                    #self.current_taper_med

                #############################Are there cases when all 3 drugs exhausted in same
                #taper episode? Should account for these cases too.
                pass
