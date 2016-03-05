# -*- coding: utf-8 -*-


MENU_DICT = {

    "main_menu_prompt": """Please select from the following menu options:\nS) Send Thank You
                C) Create Report\nQ) Quit""",
    "donation_prompt": "Donation amount? ",
    "name_prompt": "Type 'L' for a list of names or enter a name: ",
}

NAMES = {}


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
    if isinstance(name, str):
        return name
    else:
        return False


def validate_donation(dollars):
    """Check if input is type(float)."""
    if isinstance(dollars, float):
        return dollars
    else:
        return False


def get_name():
    """Prompt for name."""
    while True:
        name = input(MENU_DICT["name_prompt"])
        check_name = validate_name(name)
        if check_name == 'L':
            print(NAMES.keys())
        elif check_name is False:
            continue
        else:
            break
    print(name)
    return name


# def get_donation(name):
#     """Get donation amount."""
#     while True:
#         amount = input(MENU_DICT["donation"])
#         validate_donation(amount)

#     return


# def append_to_dict(name, donation):
#     """Check if name is in NAMES. If not append with donation."""


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
