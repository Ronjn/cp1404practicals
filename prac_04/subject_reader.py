"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"
subjects = []


def main():
    data = get_data()
    display_subject_details()
    print(data)
    print(subjects)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        subjects.append(parts)
    return subjects


def display_subject_details():
    for subject in subjects:
        subject_code = subject[0]
        subject_teacher = subject[1]
        student_count = subject[2]
        print(f"{subject_code} is taught by {subject_teacher} and has {student_count} students")


main()

