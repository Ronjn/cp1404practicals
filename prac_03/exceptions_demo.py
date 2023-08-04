"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Answer: When anything other than a number is entered as the numerator.
2. When will a ZeroDivisionError occur?
Answer: When 0 is entered as the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Answer:
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

