"""
Estimated time to complete  : 90 minutes
Actual time to complete     : ~4 hours (wow i was close huh)
"""


class Project:

    def __init__(self, name="", date="", priority=0, cost=0, completion=0):
        """Initialise a Guitar instance.

        name: string, is simply the name of the project
        date: string, is start date of the project
        priority: int, is the priority of the project
        cost: float, is the estimated cost of the project
        completion: int, is the percentage completed of the project
        """
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        return f"{self.name}, started on {self.date}, priority:{self.priority}, Estimated cost: ${self.cost}," \
               f" {self.completion}% completed"

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        """Get whether the project is completed"""
        if self.completion == 100:
            return True
        else:
            return False
