"""
Estimated time to complete  : 40 minutes
Actual time to complete     : 30 minutes
"""


class ProgrammingLanguage:

    def __init__(self, name="", typing="", reflection="", year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflections={self.reflection}, First appeared in {self.year}"
