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

        wprn = input("Please enter a WPRN\n")

        user_data = wprn.split(",")
        if validate_data(wprn):
            print("Wprn is Valid")
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

        print("please enter length width and dept followed by a comma,")
        measure = input("input data here\n")
        user_measure = measure.split(",")
        if validate_measures(user_measure):
            print("measure is Valid")
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

    result = 1
    for x in user_measure:
        result = result * float(x)
    print(result)
    # https://pythonguides.com/python-print-2-decimal-places/
    result = "{:.2f}".format(result)
    return result


def calculate_cost():

    price = 2
    area = float(result)
    cost = area * price
    print(cost)
    cost = "{:.2f}".format(cost)
    return cost


def update_tracker(wprn_data):

    """
    Updates the google sheet with the information entered by the user.
    """

    print("updating tracker sheet")
    total_row = wprn_data + user_measure
    total_row.append(result)
    total_row.append(f"€ {cost}")
    tracker_worksheet = SHEET.worksheet('project')
    tracker_worksheet.append_row(total_row)
    print("updated Successfully")


wprn = get_wprn()
wprn_data = [int(num) for num in wprn]
user_measure = measures()
result = get_area()
cost = calculate_cost()
update_tracker(wprn_data)
