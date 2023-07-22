"""
Estimated time to complete  : 90 minutes
Actual time to complete     :  minutes
"""


class Project:

    def __init__(self, name="", date="", priority=0, cost=0, completion=0):
        """Initialise a Guitar instance.

        name: string, is simply the name of the guitar
        year: int, is the year that the guitar was made
        cost: float, is the price of the guitar
        """
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        return f"{self.name}, started on {self.date}, priority:{self.priority}, Estimated cost: ${self.cost}," \
               f"{self.completion}% completed"

    def is_complete(self):
        """Get whether the project is completed"""
        if self.completion == 100:
            return True
        else:
            return False
