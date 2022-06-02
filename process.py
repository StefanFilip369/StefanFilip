"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of records that have been loaded.
- Retrieve a record with the serial number as specified by the user.
- Retrieve the records for the observation dates as specified by the user.
- Retrieve all of the records grouped by the country/region.
- Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries

 
"""

# TODO: Your code here
import tui
import json


def total_loaded(records_list):
    return len(records_list)


def retrieve_record(records_list):
    sr_no = tui.serial_number()
    for record in records_list:
        if int(record[0]) == sr_no:
            return record
    
    return []



def retrieve_observation_dates(records_list):
    dates = tui.observation_dates()
    result = []
    
    for record in records_list:
        if record[1] in dates:
            result.append(record)
    
    return result






def group_by_region(records_list):
    
    groups = {}
    
    for record in records_list:
        if record[3] not in groups.keys():
            groups[record[3]] = [record]
        
        else:
            groups[record[3]].append(record)
    
    return groups





def retrieve_summary(records_list):
    groups = group_by_region(records_list)
    
    summary = {}
    
    for group in groups:
        summary[group] = {'confirmed': 0,
                          'deaths': 0,
                          'recoveries': 0}
        

        for record in groups[group]:
            summary[group]['confirmed'] += int(record[5])
            summary[group]['deaths'] += int(record[6])
            summary[group]['recoveries'] += int(record[7])
    
    return summary
    
    
    
    
class DataExport:
    def __init__(self):
        print('Constructor')
        
        
    def export_all_data(self, records_list):
        json_object = json.dumps(records_list, indent = 4)

        # Writing to sample.json
        with open("all_data_exported.json", "w") as outfile:
            outfile.write(json_object)
            
            
    def export_country_data(self, country_data):
        json_object = json.dumps(country_data, indent = 4)

        # Writing to sample.json
        with open("country_data_exported.json", "w") as outfile:
            outfile.write(json_object)
        
    
    
    
    
    
    
    
    
    
    
    
    
