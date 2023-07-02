"""
Emails
Estimate: 45 minutes
Actual:   50 minutes
"""


def main():
    email = input("Enter your email: ")
    name = extract_name(email)
    email_to_name = {}

    # Keep asking user for more emails until "" is inputted
    while email != "":
        name_confirmation = input(f"Is your name {name}? (Y/n) ").upper()

        # If name from email is correct, move on to next email, otherwise record correct name
        if name_confirmation == "" or name_confirmation == "Y":
            email_to_name[email] = name
            email = input("Enter your email: ")
            name = extract_name(email)
        else:
            name = input("Enter your name: ")
            email_to_name[email] = name

    print_names_and_emails(email_to_name)


def print_names_and_emails(email_to_name):
    """Prints the email and corresponding name from dictionary"""
    for key in email_to_name:
        name, email = email_to_name[key], key
        print(f"{name} ({email})")


def extract_name(email):
    """Gets and formats name from user's inputted email"""
    raw_name = (email.split("@"))[0]          # Retrieves everything before the @ as a string
    names = raw_name.split(".")               # Splits up the raw_name into a list incase email has firstname.lastname
    names = [name.title() for name in names]  # Capitalises first letter for each name
    name = " ".join(names)                    # Joins the names back together, with a space between them
    return name


main()
