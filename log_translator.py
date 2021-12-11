# -*- coding: utf-8 -*-
"""
This script allows to select log files to translate.
It also allows to select the output directory.
Matevz, B1 IDS 2021
"""
import os
import easygui
from multiprocessing.dummy import Pool as ThreadPool
import time
from google_trans_new import google_translator
import pandas as pd

translator = google_translator(url_suffix="ee", timeout=5)

def request(text):
    #t = google_translator(timeout=5)
    translate_text = translator.translate(text, lang_src='et', lang_tgt='en')
    return translate_text

def main():
    start_time = time.time()
    print("\n\t\tSelect files and output path.\n")
    defaultdir = "C:/Users/Farnaz Baksh/Documents/UT - MSc Studies/Semester 1/Introduction to Data Science (LTAT.02.002)/Project files/B01 - Student Profiling/logs*.xlsx"
    logfiles = easygui.fileopenbox(msg='select log file to translate', title='log file input selector', default=defaultdir, filetypes=["*.xlsx"], multiple=True)

    save_to_path = easygui.diropenbox(msg='Select dir to store translated dataset.', title='output dataset path selector', default=defaultdir)
    
    number_of_files = len(logfiles)
    
    print(f"\n\tProcessing of {number_of_files} files started...")
    file_iterand=1
    for logbookpath in logfiles:
        print(f"\t#####Processing file {file_iterand} of {number_of_files}#####")
        file_iterand+=1
        
        total_tasks = 10
        progress = 0
        print(f"\n##### {round((progress/total_tasks)*100)}% done #####")
        progress +=1
        
        total_time = time.time()
        basename_without_ext = os.path.splitext(os.path.basename(logbookpath))[0]
        print(f"\n\t\tNow processing {basename_without_ext}...\n")
        start_time = time.time()
        print("\nNow reading excel logbook file...")
        df = pd.read_excel(logbookpath) # read in logbook
        read_time = time.time()
        print(f"reading in {basename_without_ext} took {round(read_time - start_time)}s")
        
        progress +=1
        print(f"\n##### {round((progress/total_tasks)*100)}% done #####")
        
        start_time = time.time()
        print("\nNow translating column names...")
        # translate columns' name using rename function
        df.rename(columns=lambda x: translator.translate(x, lang_src='et', lang_tgt='en'), inplace=True)    

        translation_time = time.time()

        print(f"\ntranslating {len(df.columns)} column names took this long {round(translation_time - start_time)}s")
        progress +=1
        print(f"\n##### {round((progress/total_tasks)*100)}% done #####")
        
        ##########################################################################################################################
        pool = ThreadPool(4) # nm of threads possible
        ##########################################################################################################################
        print("\nNow translating values...")
        start = time.time()

        progress +=1
        print(f"\n##### {round((progress/total_tasks)*100)}% done #####")
        try:
            values_event_context = df['Event context '].value_counts().index.tolist() # selects values in each column and returns value counts
            values_name_of_event = df['Name of event '].value_counts().index.tolist() # selects values in each column and returns value counts
            values_component = df['Component '].value_counts().index.tolist() # selects values in each column and returns value counts
        
            print("\nNow translating Component column values...")
            results_component = pool.map(request, values_component)
            progress +=1
            print(f"\n##### {round((progress/total_tasks)*100)}% done #####")
            
            print("\nNow translating Name of Event column values...")
            results_name_of_event = pool.map(request, values_name_of_event)
            progress +=1
            print(f"\n##### {round((progress/total_tasks)*100)}% done #####")
            
            print("\nNow translating Event Context column values...")
            results_event_context = pool.map(request, values_event_context)
            progress +=1
            print(f"\n##### {round((progress/total_tasks)*100)}% done #####")

        except Exception as e:
            print("\nAn error occurred! Shutting down...")
            raise e

        finally:
            len_translated = len(values_event_context) + len(values_name_of_event) + len(values_component)
            print(f"translating {len_translated} values took: {round(time.time() - start)}s")
            pool.close()
            pool.join()
        
        progress +=1
        print(f"\n##### {round((progress/total_tasks)*100)}% done #####")
        
        df_cp = df.copy()
        start_time = time.time()
        print("\nNow processing translated values...")
        for i in range(0, len(df_cp)):

            ###############################################################
            value_component = df_cp['Component '].loc[i]
            x=0
            for val in values_component:
                if value_component == val:
                    df_cp['Component '].loc[i] = results_component[x]
                x+=1

            ###############################################################
            value_name_of_event = df_cp['Name of event '].loc[i]
            y=0
            for val in values_name_of_event:
                if value_name_of_event == val:
                    df_cp['Name of event '].loc[i] = results_name_of_event[y]
                y+=1    

            ###############################################################
            value_event_context = df_cp['Event context '].loc[i]
            z=0
            for val in values_event_context:
                if value_event_context == val:
                    df_cp['Event context '].loc[i] = results_event_context[z]
                z+=1

        end_time = time.time()
        print(f"\nprocessing all {len_translated} translated values took {round(end_time - start_time)}s")
        
        progress +=1
        print(f"\n##### {round((progress/total_tasks)*100)}% done #####")
        
        basename_without_ext = os.path.splitext(os.path.basename(logbookpath))[0]
        filename = 'EN' + basename_without_ext + 'EN' + '.csv'
        df_cp.to_csv(os.path.join(save_to_path, filename))
        print(f"\n\tSaved translated log to: {save_to_path}\n")
        print(f"\n\n\tProcessing {basename_without_ext} overall took {round(time.time() - total_time)/60}min\n")
        
        progress +=1
        print(f"\n##### {round((progress/total_tasks)*100)}% done #####")
        print(f"\t#####{round(((file_iterand-1)/number_of_files)*100)}% of files translated#####")

if __name__=="__main__":
    main()