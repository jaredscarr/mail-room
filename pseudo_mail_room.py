def main_menu():
    """Wecome user and present with menu options for next step."""

    if choice is send_thank_you:
        send_thank_you(prompt_for_name)
    if create_report:
        create_report()


def send_thank_you(prompt_for_name):
    """Prompt for name and take input."""
    if input == 'q':
        main_menu()
    elif list:
        show_list()
    elif name:
        name_search(name)


def create_report(name, donation):
    """Print donor name, total number, sum,  avg. of donations."""
    print("Name: {} Number of Donations: {} Sum: {} Avg.").format()
    # present options for returning to main menu
    if input == 'y':
        main_menu()


def name_search(name):
    """Search if name is in the list."""
    if input == 'q':
        main_menu()
    elif name in name_list:
        donation(name)
    else:
        add_name(name)


def donation(name):
    """Prompt for donation amount and verifiy it's number."""
    if input == 'q':
        main_menu()
    elif not a number:
        donation(name)
    else:
        add_donation(name, donation)


def add_name(name):
    """Add name to list of donors."""
    # append name to donor list
    donation(name)


def add_donation(name, donation):
    """Append donation to selected donor."""
    print_email(name, donation)


def print_email(name, donation):
    """Print an email to the console. Return to main."""
    print("Dear {}, \nThank you for your generous donation of ${}.").format(
        name, donation)
    # prompt user if they want to return to main menu
    if input == 'y':
        main_menu()
