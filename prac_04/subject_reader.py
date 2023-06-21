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
    input_file.close()


def display_subject_details():
    for i in range(0, len(subjects)):
        subject_code = (subjects[i])[0]
        subject_teacher = (subjects[i])[1]
        student_count = (subjects[i])[2]
        print(f"{subject_code} is taught by {subject_teacher} and has {student_count} students")


main()

