import random


def main():
    number_of_rows = int(input("How many quick picks? :"))
    for i in range(0, number_of_rows):
        selections = []
        number_of_selections = 6
        candidate_min = 1
        candidate_max = 45
        candidates = list(range(candidate_min, candidate_max + 1))  # Creates a list of candidates from 1,
        for j in range(0, number_of_selections):
            random_choice = random.choice(candidates)      # Selects a random number from candidates
            candidates.remove(random_choice)               # Removes that number from candidates
            selections.append(random_choice)        # Adds that number to the selections
        selections.sort()
        print("{:2}  {:2}  {:2}  {:2}  {:2}  {:2}".format(selections[0], selections[1], selections[2],
                                                          selections[3], selections[4], selections[5]))


main()

