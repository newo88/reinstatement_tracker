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

    """
    Request Wprn from user
    """
    while True:
        wprn = input("Please enter your 7 didgit reference number\n")

        user_data = wprn.split(",")
        if validate_data(wprn):
            print("Wprn is Valid\n")
            break

    return user_data


def validate_data(values):

    """
    Validates WPRN to make sure it is a
    seven digit number.
    """
    try:
        [int(value) for value in values]
        while len(values) != 7 or (not values.isdigit()):
            raise ValueError(
                    f"exactly 7 digits required you entered {len(values)}"
                )
    except ValueError as e:
        print(f"invalid data {e}")
        return False

    return True


def measures():

    """
    Requests the dimensions of the hole
    to be reinstated.
    """
    while True:

        print("Please enter length width and dept followed by a comma ,\n")
        print("Example 2.5,2.36,0.5\n ")
        measure = input("Input data here\n")
        user_measure = measure.split(",")
        if validate_measures(user_measure):
            print("Measure is Valid\n")
            break

    return user_measure


def validate_measures(values):
    try:
        [float(value) for value in values]
        if len(values) != 3:
            raise ValueError(
                    f"exactly 3 digits required you entered {len(values)}"
                )
    except ValueError as e:
        print(f"invalid data {e}")
        return False

    return True


def get_area():

    """
    Takes the measure from measures and calculates
    the meter cube required for the hole.
    """
    print("Calculating Area ......")
    result = 1
    for x in user_measure:
        result = result * float(x)
    # https://pythonguides.com/python-print-2-decimal-places/
    result = "{:.2f}".format(result)
    print(f"Area = {result}\n")
    return result


def calculate_cost():
    print("Calculating Cost......")
    price = 2
    area = float(result)
    cost = area * price
    cost = "{:.2f}".format(cost)
    print(f"Cost = {cost}\n")
    return cost


def update_tracker(wprn_data):

    """
    Updates the google sheet with the information entered by the user.
    """

    print("Updating Tracker Sheet.......\n")
    total_row = wprn_data + user_measure
    total_row.append(result)
    total_row.append(f"€ {cost}")
    tracker_worksheet = SHEET.worksheet('project')
    tracker_worksheet.append_row(total_row)
    print("Updated Successfully\n")


print("Welcome to the Reinstatement Tracker Sheet\n")
wprn = get_wprn()
wprn_data = [int(num) for num in wprn]
user_measure = measures()
result = get_area()
cost = calculate_cost()
update_tracker(wprn_data)


