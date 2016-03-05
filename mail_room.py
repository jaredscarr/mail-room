# -*- coding: utf-8 -*-
from decimal import Decimal
from builtins import input
import pdb


MENU_DICT = {

    "main_menu_prompt": """Please select from the following menu options:\nS) Send Thank You
                C) Create Report\nQ) Quit""",
    "donation_prompt": "Donation amount? ",
    "name_prompt": "Type 'L' for a list of names or enter a name: ",
}

NAMES = {
    'jared': [323, 333, 3236],
    'alex': [45, 3345, 343, 234],
    'larry': [5, 5, 5, 5, 5, 5, 5],
}


def call_all():
    """Call functions."""
    menu(MENU_DICT["main_menu_prompt"], validate_main_menu)


def validate_main_menu(string):
    """Validate user input."""
    if string in ['C', 'S', 'Q']:
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

    # if isinstance(name, str):
    #     return name
    # else:
    #     return False


def validate_donation(dollars):
    """Check if input is type(float)."""
    twoplaces = Decimal(10) ** -2
    try:
        # int(dollars)
        # if isinstance(dollars, float) or isinstance(dollars, int):
        float(Decimal(dollars).quantize(twoplaces))
        return dollars
    except ValueError:
        return False

    # if isinstance(dollars, float):
    #     return dollars
    # else:
    #     return False


def get_name():
    """Prompt for name."""
    while True:
        name = input(MENU_DICT["name_prompt"])
        check_name = validate_name(name)
        if check_name == 'L':
            for keys in NAMES:
                print(keys)
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
        check_num = validate_donation(amount)
        if check_num is False:
            continue
        else:
            break
    return append_to_dict(name, amount)


# This is our best function
def append_to_dict(name, donation):
    """Check if name is in NAMES. If not append with donation."""
    NAMES.setdefault(name, []).append(donation)
    return print_email(name, donation)


def print_email(name, donation):
    """Print email to the console."""
    print("Thank you {} for your generous donation of: ${}"
          .format(name, donation))
    return menu(MENU_DICT["main_menu_prompt"], validate_main_menu)


def create_report():
    """Print a report and return to main_menu."""
    print(NAMES)
    return menu(MENU_DICT["main_menu_prompt"], validate_main_menu)


def router(user_input):
    """Return function call to a menu."""
    if user_input == 'Q':
        menu(MENU_DICT["main_menu_prompt"], validate_main_menu)
    elif user_input == 'S':
        get_name()
    elif user_input == 'C':
        create_report()
    print('router ran')


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


call_all()
