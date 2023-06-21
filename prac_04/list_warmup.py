numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0]            prediction: 3               output: 3
# numbers[-1]           prediction: 2               output: 2
# numbers[3]            prediction: 1               output: 1
# numbers[:-1]          prediction: unknown         output: [3, 1, 4, 1, 5, 9]
# numbers[3:4]          prediction: 1, 2, 3, 4, 5   output: 1
# 5 in numbers          prediction: 4               output: True
# 7 in numbers          prediction: unknown         output: False
# "3" in numbers        prediction: unknown         output: False
# numbers + [6, 5, 3]   prediction: error           output: [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]


# 1. Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"

# 2. Change the last element of numbers to 1
numbers[-1] = 1

# 3. Print all the elements from numbers except the first two (slice)
print(numbers[2:])

# 4. Print whether 9 is an element of numbers
print(9 in numbers)
