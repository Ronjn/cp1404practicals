import random

NUMBER_OF_SELECTIONS = 6    # How many numbers per quick pick
CANDIDATE_MIN = 1           # lowest number for selection
CANDIDATE_MAX = 45          # highest number for selection


def main():
    # Ask the user how many quick picks to generate
    number_of_picks = int(input("How many quick picks? :"))

    # Generates and outputs each pick
    for pick in range(0, number_of_picks):
        selections = []
        candidates = list(range(CANDIDATE_MIN, CANDIDATE_MAX + 1))  # Creates a list of all possible candidates

        # Select as many candidates as required
        for selection_index in range(0, NUMBER_OF_SELECTIONS):
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

