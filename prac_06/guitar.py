"""
Estimated time to complete  : 45  minutes
Actual time to complete     : 60 minutes
"""

YEAR = 2023
VINTAGE_MIN = 50


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance.

        name: string, is simply the name of the guitar
        year: int, is the year that the guitar was made
        cost: float, is the price of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}, ({self.year}) : ${self.cost}"

    def get_age(self):
        """Get the age of the guitar"""
        age = YEAR - self.year
        return age

    def is_vintage(self):
        """Get whether the guitar is classified as 'vintage'"""
        if self.get_age() >= VINTAGE_MIN:
            return True
        else:
            return False

