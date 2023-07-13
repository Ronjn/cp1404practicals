"""
Estimated time to complete  : 45  minutes
Actual time to complete     : 60 minutes
"""


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}, ({self.year}) : ${self.cost}"

    def get_age(self):
        age = 2023 - self.year
        return age

    def is_vintage(self):
        if self.get_age() > 49:
            return True
        else:
            return False

