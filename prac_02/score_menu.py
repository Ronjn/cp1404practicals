import random


def main():
    menu = """        (G)et a valid score
        (P)rint result
        (S)how stars
        (Q)uit"""
    print(menu)
    choice = input(">>> ").upper()
    score = -1
    while choice != "Q":
        if choice == "G":
            score = random.randint(0, 100)
            print("Score generated as: " + str(score))
        elif choice == "P":
            if score == -1:
                print("First you must use G to generate a score")
            result = get_result(score)
            print(result)
        elif choice == "S":
            for j in range(0, score, 1):
                print("*", end='')
            print()
        print(menu)
        choice = input(">>> ").upper()
    print("Thank you and goodbye!")


def get_result(score):
    if score < 0:
        result = "Invalid score"
    elif score > 100:
        result = "Invalid score"
    elif score >= 50:
        if score >= 90:
            result = "Excellent"
        else:
            result = "Passable"
    else:
        result = "Bad"
    return result


main()

