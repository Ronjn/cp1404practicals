from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability attribute."""

    def __init__(self, name, fuel, reliability: float):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car if the reliability is higher than random number generated"""
        random_number = random.randint(0, 100)
        print(random_number)

        if self.reliability > random_number:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self._odometer += distance
        return distance
