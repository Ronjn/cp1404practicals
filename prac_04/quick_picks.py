import random
lines = []
string_lines = []

def main():
    quickpick_count = int(input("How many quick picks? :"))

    for i in range(0, quickpick_count):
        line = []
        for j in range(0, 6):
            line.append(random.randint(1, 45))
        lines.append(line)

    convert_int_to_string(quickpick_count)


def convert_int_to_string(quickpick_count):
    for i in range(0, quickpick_count):
        string_line = []
        for j in range(0, 6):
            string_line = [str(number) for number in lines[i]]
        string_lines.append(string_line)
        print(" ".join(sorted(string_lines[i])))


main()

