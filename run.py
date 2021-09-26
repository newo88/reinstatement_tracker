import gspread
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
    while True:
        
        wprn = input("Please enter a WPRN\n")
        
        user_data = wprn.split(",")
        if validate_data(user_data):
            print("Wprn is Valid")
            break  
        
    return user_data    
   

def validate_data(values):
    try:
        [int(value) for value in values]
        if len(values) != 1:
            raise ValueError(
                    f"exactly 7 digits required you entered {len(wprn)}"
                )    
    except ValueError as e:
        print(f"invalid data {e}") 
        return False

   
    return True
   

def measures():


    print("please enter length width and dept followed by a comma,")
    measure = input("input data here\n")

    user_measure = measure.split(",")
    if validate_data(user_measure):
        print("measure is Valid")
          
        
    return user_measure    

    #total_area_cubed = (length,  int(width),  int(depth))
    print('Total Concrete needed')
    print(total_area_cubed)
    return total_area_cubed


def validate_measures():
    try:
        [int(measure) for measure in measures]
        if len(values) != 3:
            raise ValueError(
                    f"exactly 3 digits required you entered {len(wprn)}"
                )    
    except ValueError as e:
        print(f"invalid data {e}") 
        return False

   
    return True




    
def update_tracker(wprn_data):
    print("updating tracker sheet")
    total_row = wprn_data + total_area_cubed
    tracker_worksheet = SHEET.worksheet('project')
    tracker_worksheet.append_row(total_row)
    print("updated Successfully")

wprn = get_wprn()
wprn_data = [int(num) for num in wprn]
total_area_cubed = measures()
update_tracker(wprn_data)