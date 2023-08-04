from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "(Q) - Quit\n" \
       "(C) - Choose Taxi\n" \
       "(D) - Drive\n"


def main():
    """Print menu to the user and handle taxi selection and drive functionality"""
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0

    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":

        if choice == "C":
            print("Taxis available:")

            # Print all taxis to the user with an index
            for taxi_index, taxi in enumerate(taxis, 0):
                print(f"{taxi_index} - {taxi}")

            # Assign taxi choice to the user's selection
            taxi_choice = get_int_input("Choose taxi: ", 0, len(taxis)-1)
            current_taxi = taxis[taxi_choice]
            print(f"You have chosen the {current_taxi.name}")

        elif choice == "D":
            # Check if user has selected taxi before driving
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                # Create new fare and drive the taxi the user's specified distance
                current_taxi.start_fare()
                distance = get_int_input("Drive how far? ", 0, 10000)
                current_taxi.drive(distance)

                # Print trip cost and add it to the bill
                print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare()}")
                bill += current_taxi.get_fare()

        else:
            print("Invalid option")

        print(f"Bill to date: ${bill}")
        print(MENU)
        choice = input(">>> ").upper()


def get_int_input(field_name, min_int, max_int):
    """Get user input when expecting an int, within a certain range"""

    need_input = True
    user_int = None

    # Ask the user for their input until it satisfies all conditions
    while need_input:
        user_input = input(f"{field_name} (range {min_int} - {max_int}): ")
        if user_input == "":
            print("Input cannot be blank")
        else:
            try:
                user_int = int(user_input)
                if min_int <= user_int <= max_int:
                    need_input = False
                else:
                    print(f"{field_name} must be within {min_int} - {max_int}")
            except ValueError:
                print(f"{field_name} must be a valid number")

    return user_int


main()
