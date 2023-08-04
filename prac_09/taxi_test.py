from prac_09.taxi import Taxi

my_taxi = Taxi(100, "Prius 1", 1.23)

my_taxi.drive(40)

print(f"Details: {my_taxi}, Current fare: {my_taxi.get_fare()}")

my_taxi.start_fare()
my_taxi.drive(100)

print(f"Details: {my_taxi}, Current fare: {my_taxi.get_fare()}")
