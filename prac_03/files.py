# Program 1, writes name to name.txt
out_file = open('name.txt', 'w')
print("Enter name: ")
name = input()
print(f"{name}", file=out_file)
out_file.close()

# Program 2, opens and prints name.txt
out_file = open('name.txt', 'r')
nameinfile: str = out_file.readline()
print(f"Your name is {nameinfile}")
out_file.close()

# Program 3, opens number.txt and adds first two numbers together
with open("numbers.txt") as out_file:
    numbers = out_file.read().splitlines()
    no1 = int(numbers[0])
    no2 = int(numbers[1])
    SUM = no1 + no2
print(f"Result is {SUM}")
out_file.close()

# Program 4, prints sum total for all numbers in numbers.txt
with open("numbers.txt") as out_file:
    numbers = out_file.read().splitlines()
    j = len(numbers)
    TSUM = 0
    for i in range(0, j, 1):
        TSUM = TSUM + (int(numbers[i]))
print(f"Total is {TSUM}")
out_file.close()

