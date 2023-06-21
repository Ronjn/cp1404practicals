import random
lines = []


def main():
    quickpick_count = int(input("How many quick picks? :"))
    for i in range(0, quickpick_count):
        line = []
        for j in range(0, 6):
            line.append(random.randint(1, 45))
        line.sort()
        lines.append(line)
        print("{:2}  {:2}  {:2}  {:2}  {:2}  {:2}".format(lines[i][0], lines[i][1], lines[i][2], lines[i][3],
                                                          lines[i][4], lines[i][5]))


main()

