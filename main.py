"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module 'tui'
        any processing should be done using the appropriate functions in the module 'process'
        any visualisation should be done using the appropriate functions in the module 'visual'
"""


# Task 10: Import required modules
# TODO: Your code here
import csv
import enum
import json
import matplotlib.pyplot as plt
import os
import random
import typing
import math
import unittest
import tui
import process
import visual

# Task 11: Create an empty list named 'covid_records'.
# This will be used to store the data read from the source data file.
# TODO: Your code here
covid_records = []


def run():
    # Task 12: Call the function welcome of the module 'tui'.
    # This will display our welcome message when the program is executed.
    # TODO: Your code here
    tui.welcome()

    # Task 13: Load the data.
    # - Use the appropriate function in the module 'tui' to display a message to indicate that the data loading
    # operation has started.
    # - Load the data. Each line in the file should be a record in the list 'covid_records'.
    # You should appropriately handle the case where the file cannot be found or loaded.
    # - Use the appropriate functions in the module 'tui' to display a message to indicate how many records have
    # been loaded and that the data loading operation has completed.
    # TODO: Your code here
    tui.progress('Data loading', 0)
    
    filename = "./data/covid_19_data.csv"

    fields = []
    
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        for row in csvreader:
            covid_records.append(row)
    
    tui.total_records(len(covid_records))
    
    tui.progress('Data loading', 100)



    while True:
        # Task 14: Using the appropriate function in the module 'tui', display a menu of options
        # for the different operations that can be performed on the data (menu variant 0).
        # Assign the selected option to a suitable local variable
        # TODO: Your code here
        
        user_choice = tui.menu(variant=0)

        # Task 15: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, do the following:
        # - Use the appropriate function in the module 'tui' to display a menu of options for processing the data
        # (menu variant 1).
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve an individual record by serial number then
        #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process
        #       has started.
        #       - Use the appropriate function in the module 'process' to retrieve the record and then appropriately
        #       display it.
        #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve (multiple) records by observation dates then
        #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
        #       process has started.
        #       - Use the appropriate function in the module 'process' to retrieve records with
        #       - Use the appropriate function in the module 'tui' to display the retrieved records.
        #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
        #       process has completed.
        #
        #   - If the user selected the option to group records by country/region then
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has started.
        #       - Use the appropriate function in the module 'process' to group the records
        #       - Use the appropriate function in the module 'tui' to display the groupings.
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has completed.
        #
        #   - If the user selected the option to summarise the records then
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has started.
        #       - Use the appropriate function in the module 'process' to summarise the records.
        #       - Use the appropriate function in the module 'tui' to display the summary
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has completed.
        # TODO: Your code here
        
        
        if user_choice == 1:
            tui.progress('Data processing', 0)
            
            data_process_choice = tui.menu(variant=1)
            
            
            
            if data_process_choice == 1:
                
                tui.progress('Record retrieval', 0)
                retrieved_record = process.retrieve_record(covid_records)
                if retrieved_record == []:
                    print('No such record found.')
                else:
                    print('The following record has been found:')
                    print(retrieved_record) 
                tui.progress('Record retrieval', 100)
            
            
            
            elif data_process_choice == 2:
                
                tui.progress('Record retrieval', 0)
                retrieved_records = process.retrieve_observation_dates(covid_records)  
                if retrieved_records == []:
                    print('No records found.')
                else:
                    print('The following records have been found:')
                    tui.display_records(retrieved_records, cols=None) 
                tui.progress('Record retrieval', 100)
            
            
            
            elif data_process_choice == 3:
                
                tui.progress('Grouping', 0)
                groups = process.group_by_region(covid_records)
                
                for group in groups:
                    print(f'Region: {group}')
                    tui.display_records(groups[group], cols=None) 
                    print('-'*45)
                tui.progress('Grouping', 100)
            
            
            
            elif data_process_choice == 4:
                
                tui.progress('Summary process', 0)
                summary = process.retrieve_summary(covid_records)
                tui.display_summary(summary)
                tui.progress('Summary process', 100)
                
                
                
            
            tui.progress('Data processing', 100)
            

        # Task 21: Check if the user selected the option for visualising data.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to indicate that the data visualisation operation
        # has started.
        # - Visualise the data by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what visualisation is to be done.
        #   - call the appropriate function in the module 'visual'
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # data visualisation operation has completed.
        # TODO: Your code here
        elif user_choice == 2:
            tui.progress('Data visualisation', 0)
            
            visualisation_choice = tui.menu(variant=2)
            
            if visualisation_choice == 1:
                summary = process.retrieve_summary(covid_records)
                visual.confirmed_cases_pichart(summary)
            
            elif visualisation_choice == 2:
                summary = process.retrieve_summary(covid_records)
                visual.deaths_barchart(summary)
            
            
            elif visualisation_choice == 3:
                groups = process.group_by_region(covid_records)
                visual.display_animation(groups, country='Mainland China')
                
            
            tui.progress('Data visualisation', 100)
            
            
        
        # Task 25: Check if the user selected the option for exporting data.  If so, then do the following:
        # - Use the appropriate function in the module 'tui' to retrieve the type of data to be exported.
        # - Check what option has been selected
        #
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has started.
        # - Export the data (see below)
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has completed.
        #
        # To export the data, you should demonstrate the application of OOP principles including the concepts of
        # abstraction and inheritance.  You should create suitable classes with appropriate methods.
        # You should use these to write the records (either all or only those for a specific country/region) to a JSON file.
        # TODO: Your code here
        
        elif user_choice == 3:
            
            tui.progress('Data exportation', 0)
            export_choice = tui.menu(variant=3)
            
            if export_choice == 1:
                obj = process.DataExport()
                obj.export_all_data(covid_records)
            
            elif export_choice == 2:
                country='Mainland China'
                groups = process.group_by_region(covid_records)
                country_data = groups[country]
                obj = process.DataExport()
                obj.export_country_data(country_data)
                
            
            tui.progress('Data exportation', 100)

        # Task 26: Check if the user selected the option for exiting the program.
        # If so, then break out of the loop
        # TODO: Your code here
        elif user_choice == 4:
            break

        # Task 27: If the user selected an invalid option then use the appropriate function of the
        # module tui to display an error message
        # TODO: Your code here
        else:
            tui.error(msg='Invalid choice entered')
            
        


if __name__ == "__main__":
    run()
