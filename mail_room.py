# -*- coding: utf-8 -*-
from builtins import input


MENU_DICT = {

    "main_menu_prompt": """\nPlease select from the following menu options:\n
S) Send Thank You\nC) Create Report\n""",
    "donation_prompt": "\nEnter 'Q' for menu or enter donation amount: ",
    "name_prompt": "\nL) List of Names\nQ) Quit\nOr enter a name: ",
}

NAMES = {}


def main():
    """Call functions."""
    menu(MENU_DICT["main_menu_prompt"], validate_main_menu)


def validate_main_menu(string):
    """Validate user input."""
    if string in ['C', 'S']:
        return string
    else:
        return False


def validate_name(name):
    """Check if input is type(str)."""
    try:
        int(name)
        return False
    except ValueError:
        return name


def validate_donation(amount):
    """Check if input is an instance of an integer."""
    try:
        int_amount = int(amount)
        if isinstance(int_amount, int):
            return int_amount
    except ValueError:
        return False


def get_name():
    """Prompt for name."""
    while True:
        name = input(MENU_DICT["name_prompt"])
        check_name = validate_name(name)
        if check_name == 'L':
            print("\nDonors\n")
            for keys in NAMES:
                print(keys)
        elif check_name == 'Q':
            menu(MENU_DICT["main_menu_prompt"], validate_main_menu)
        elif check_name is False:
            continue
        else:
            break
    print(name)
    return get_donation(name)


def get_donation(name):
    """Get donation amount."""
    while True:
        amount = input(MENU_DICT["donation_prompt"])
        if amount == 'Q':
            menu(MENU_DICT["main_menu_prompt"], validate_main_menu)
        else:
            check_num = validate_donation(amount)
            if check_num is False:
                continue
            else:
                break
    return append_to_dict(name, amount)


def append_to_dict(name, donation):
    """Check if name is in NAMES. If not append with donation."""
    NAMES.setdefault(name, []).append(int(donation))
    return print_email(name, donation)


def print_email(name, donation):
    """Print email to the console."""
    print("\nThank you {} for your generous donation of: ${}\n"
          .format(name, donation))
    return menu(MENU_DICT["main_menu_prompt"], validate_main_menu)


def report_math(key, donations):
    """Calculate total, number and avg. donations of each user in NAMES."""
    number_of = 0
    avg = 0
    total = sum(donations)
    number_of = len(donations)
    avg = int(total / number_of)
    print("{:<20}{:<20}{:<20}{:<20}".format(key, total, number_of, avg))
    return "ran"


def create_report():
    """Print a report and return to main_menu."""
    print("\n{:<20}{:<20}{:<20}{:<20}\n"
          .format("Name", "Total", "Quantity", "Avg"))
    for key, value in NAMES.items():
        report_math(key, value)
    return menu(MENU_DICT["main_menu_prompt"], validate_main_menu)


def router(user_input):
    """Return function call to a menu."""
    if user_input == 'S':
        get_name()
    elif user_input == 'C':
        create_report()


def menu(prompt, validator):
    """Present menu options and get user response."""
    while True:
        user_input = input(MENU_DICT["main_menu_prompt"])
        check_input = validate_main_menu(user_input)
        if check_input is False:
            continue
        else:
            break
    return router(user_input)
