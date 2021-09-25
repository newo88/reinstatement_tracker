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

    wprn = input("Please enter a WPRN\n") 
    validate_data(wprn)
    print(f"you entered {wprn}")


def validate_data(wprn):
    try:
        int(wprn)
        if len(wprn) != 7:
            raise ValueError(
                    f"exactly 7 digits required you entered {len(wprn)}"
                )    
    except ValueError as e:
        print(f"invalid data {e}") 


get_wprn()

