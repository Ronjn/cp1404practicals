"""
Estimated time to complete  : 45  minutes
Actual time to complete     :  minutes
"""

from prac_06.guitar import Guitar


def main():
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Line 6 JTV-59", 2010, 1512.90)
    guitar3 = Guitar("Fender Stratocaster", 2014, 765.40)

    print(f"Gibson L-5 CES get_age() - Expected 101. Got {guitar1.get_age()}")
    print(f"Line 6 JTV-59 get_age() - Expected 13. Got {guitar2.get_age()}")
    print(f"Fender Stratocaster get_age() - Expected 9. Got {guitar3.get_age()}")

    print()

    print(f"Gibson L-5 CES is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"Line 6 JTV-59 is_vintage() - Expected False. Got {guitar2.is_vintage()}")
    print(f"Fender Stratocaster is_vintage() - Expected False. Got {guitar3.is_vintage()}")


main()

