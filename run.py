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
    wprn = input("Please enter a WPRN ")
    try:
        val = int(wprn)
        print("Wprn number is: ", val)
        break;
    except ValueError:
            print("This is not a valid wprn. Please enter a valid wprn")
    

get_wprn()
