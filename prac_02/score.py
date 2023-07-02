"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = get_result(score)
    print(result)
    score = random.randint(0, 100)
    result = get_result(score)
    print("Random score result: " + result)


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



