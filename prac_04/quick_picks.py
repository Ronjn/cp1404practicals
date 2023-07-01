import random


def main():
    number_of_selections = 6    # How many numbers per quick pick
    candidate_min = 1           # lowest number for selection
    candidate_max = 45          # highest number for selection

    # Ask the user how many quick picks to generate
    number_of_picks = int(input("How many quick picks? :"))

    # Generates and outputs each pick
    for pick in range(0, number_of_picks):
        selections = []
        candidates = list(range(candidate_min, candidate_max + 1))  # Creates a list of all possible candidates

        # Select as many candidates as required
        for selection_index in range(0, number_of_selections):
            selection = random.choice(candidates)   # Selects a random number from candidates
            selections.append(selection)            # Adds that number to the selections
            candidates.remove(selection)            # Removes that number from candidates
        selections.sort()   # Puts selections in ascending order

        print_quickpick(selections)  # Print the quickpick that was just created


def print_quickpick(selections):
    """Print a row of selections"""
    for selection in selections:
        print("{:4}".format(selection), end='')  # No newline until row is finished printing
    print()


main()

