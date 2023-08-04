"""Band class for CP1404"""


class Band:
    """Band class"""

    def __init__(self, name=""):
        """Construct a Band with a name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.name} ({self.musicians})"

    def __repr__(self):
        """Return a string representation of a Band, showing the variables."""
        return str(vars(self))

    def add(self, musician):
        """Add a musician to the bands list."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the musician playing their first (or no) musician."""
        for musician in self.musicians:
            if not musician.instruments:
                print(f"{musician.name} needs an instrument!")
            else:
                print(f"{musician.name} is playing: {musician.instruments}")
