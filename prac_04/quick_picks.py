import random
lines = []


def main():
    number_of_quickpicks = int(input("How many quick picks? :"))
    for i in range(0, number_of_quickpicks):
        line = []
        number_of_columns = 6
        range_of_numbers = 45
        for j in range(0, number_of_columns):
            line.append(random.randint(1, range_of_numbers))
        line.sort()
        lines.append(line)
        print("{:2}  {:2}  {:2}  {:2}  {:2}  {:2}".format(lines[i][0], lines[i][1], lines[i][2], lines[i][3],
                                                          lines[i][4], lines[i][5]))


main()

