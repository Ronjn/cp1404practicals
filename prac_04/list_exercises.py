

numbers = []
number_count = 5
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

def main():
    for number in range(1, number_count + 1):
        number = float(input(f"Enter number {number} : "))
        numbers.append(number)
    calculations()

    user = input("Enter username: ")
    if user in usernames:
        print("Access Granted")
    else:
        print("Access Denied")






def calculations():
    small_num = min(numbers)
    big_num = max(numbers)
    avg_num = sum(numbers) / len(numbers)
    first_num = numbers[0]
    last_num = numbers[-1]
    print(f"The first number is {first_num}, The last number is {last_num}, The smallest number is {small_num}, The "
          f"largest number is {big_num}, The average number is {avg_num}")


main()

