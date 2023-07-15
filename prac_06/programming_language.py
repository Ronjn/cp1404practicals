"""
Estimated time to complete  : 40 minutes
Actual time to complete     : 30 minutes
"""


class ProgrammingLanguage:

    def __init__(self, name="", typing="", reflection="", year=0):
        """Initialise a Language instance.

        name: string, is simply the name of the language
        typing: string, the typing mode of the language
        reflection: bool, true or false if the language has reflection
        year: int, is the year that the language was released
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Get whether the language is dynamic typing"""
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflections={self.reflection}, First appeared in {self.year}"
