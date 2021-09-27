import gspread
import numpy as np
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('reinstatement_measure_sheet')

def get_wprn():
    """
    Request Wprn from user 
    """
    while True:
        
        wprn = input("Please enter a WPRN\n")
        
        
        if validate_data(wprn):
            print("Wprn is Valid")
            break  
        
    return wprn    
   

def validate_data(values):
    try:
        [int(value) for value in values]
        if len(values) != 7:
            raise ValueError(
                    f"exactly 7 digits required you entered {len(values)}"
                )    
    except ValueError as e:
        print(f"invalid data {e}") 
        return False

   
    return True
   

def measures():
    while True:

        print("please enter length width and dept followed by a comma,")
        measure = input("input data here\n")
         
        user_measure = measure.split(",")
        if validate_measures(user_measure):
            print("measure is Valid")
            break
      
    return user_measure 
    

def validate_measures(values):
    try:
        [int(value) for value in values]
        if len(values) != 3:
            raise ValueError(
                    f"exactly 3 digits required you entered {len(values)}"
                )    
    except ValueError as e:
        print(f"invalid data {e}") 
        return False

   
    return True

    
def update_tracker(wprn_data):
    print("updating tracker sheet")
    total_row = wprn_data + user_measure
    tracker_worksheet = SHEET.worksheet('project')
    tracker_worksheet.append_row(total_row)
    print("updated Successfully")
    print(type(user_measure))
    print('Total Concrete needed')
    #total_area_cubed = np.prod(user_measure)
    #print(total_area_cubed)
   

    

wprn = get_wprn()
wprn_data = [int(num) for num in wprn]
user_measure = measures()
update_tracker(wprn_data)