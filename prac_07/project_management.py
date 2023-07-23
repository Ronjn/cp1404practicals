"""
Estimated time to complete  : 90 minutes
Actual time to complete     :  minutes
"""

from prac_07.project import Project
import datetime

MIN_COMPLETION = 0
MAX_COMPLETION = 100

MIN_PRIORITY = 1
MAX_PRIORITY = 25

MENU = "\nMenu: \n" \
       "L - Load projects\n" \
       "S - Save projects\n" \
       "D - Display projects\n" \
       "F - Filter projects by date\n" \
       "A - Add new project\n" \
       "U - Update project\n" \
       "Q - Quit\n"


def main():
    """Prints menu to the user and gets the user's choice"""
    print("Project Manager 1.0 - by Bryn Baird")

    file_name = "projects.txt"
    projects = load_projects(file_name)

    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            candidate_file_name = get_user_input("file name")
            loaded_projects = load_projects(candidate_file_name)
            if loaded_projects is not None:  # Checks the projects were loaded successfully before updating the list
                file_name = candidate_file_name
                projects = loaded_projects
        elif choice == "S":
            file_name = get_user_input("file name")
            save_projects(projects, file_name)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects(projects)
        elif choice == "A":
            projects = add_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid menu selection")
        print(MENU)
        choice = input(">>> ").upper()

    print("Thank you for using custom-built project management software.")
    save_projects(projects, file_name)


def display_projects(projects):
    """Displays list of incomplete and complete projects to user, sorted by priority"""

    complete_projects = []
    incomplete_projects = []

    projects.sort()

    # Appends projects to either completed project list or uncompleted by using is_complete method
    for project in projects:
        if project.is_complete():
            complete_projects.append(project)
        else:
            incomplete_projects.append(project)

    # Prints all the incomplete projects
    print("Incomplete projects:")
    for incomplete_project in incomplete_projects:
        print(f"\t{incomplete_project}")

    # Prints all the completed projects
    print("\nComplete projects:")
    for complete_project in complete_projects:
        print(f"\t{complete_project}")


def get_user_input(required_input):
    """Asks the user for their input, and ensures the input is not blank
    Mainly used for getting user input that should be a string
    """

    user_input = input(f"{required_input}: ")
    while user_input == "":
        print("Input cannot be blank")
        user_input = input(f"{required_input}: ")
    return user_input


def add_project(projects):
    """Adds a new project to memory based on user's input"""

    print(f"\nLets add a new project")

    # Uses the get_user_input function to get input for name, date, priority, cost, and completion
    new_project_name = get_user_input("Project name")
    new_project_date = get_date_input("Start date (dd/mm/yy)")
    new_project_priority = get_int_input("Priority", MIN_PRIORITY, MAX_PRIORITY)
    new_project_cost = get_float_input("Cost estimate")
    new_project_completion = get_int_input("Percent complete", MIN_COMPLETION, MAX_COMPLETION)

    # Creates the new project
    new_project = Project(new_project_name, new_project_date, (int(new_project_priority)), (float(new_project_cost)),
                          (int(new_project_completion)))

    projects.append(new_project)  # Adds the new project to the primary list of projects

    # Prints a confirmation to the user that new project has been added
    print(f"{projects[-1]} added to Project Manager\n")
    return projects


def get_date_input(field_name):
    """Gets user input when expecting a date"""

    need_input = True
    user_date = None

    # Will ask the user for their input until it satisfies all conditions
    while need_input:
        user_input = input(f"{field_name}: ")
        if user_input == "":
            print("Input cannot be blank")
        else:
            try:
                user_date = datetime.datetime.strptime(user_input, "%d/%m/%Y").date()
                need_input = False
            except ValueError:
                print(f"Invalid date format")

    return user_date


def get_float_input(field_name):
    """Gets user input when expecting a float"""

    need_input = True
    user_float = None

    # Will ask the user for their input until it satisfies all conditions
    while need_input:
        user_input = input(f"{field_name}: ")
        if user_input == "":
            print("Input cannot be blank")
        else:
            try:
                user_float = float(user_input)
                need_input = False
            except ValueError:
                print(f"{field_name} must be a valid number")

    return user_float


def get_int_input(field_name, min_int, max_int):
    """Gets user input when expecting an int, within a certain range"""

    need_input = True
    user_int = None

    # Will ask the user for their input until it satisfies all conditions
    while need_input:
        user_input = input(f"{field_name} (range {min_int} - {max_int}): ")
        if user_input == "":
            print("Original value kept")
            need_input = False
        else:
            try:
                user_int = int(user_input)
                if min_int <= user_int <= max_int:
                    need_input = False
                else:
                    print(f"{field_name} must be within {min_int} - {max_int}")
            except ValueError:
                print(f"{field_name} must be a valid number")

    return user_int


def update_project(projects):
    """Updates a projects priority and or completion percent based on user's choice"""

    # Prints all projects with an index
    for project_index, project in enumerate(projects, 1):
        print(f"({project_index}) {project}")

    # Gets the user's choice and prints the project they selected
    project_choice = int(input("Project choice: ")) - 1
    print(projects[project_choice])

    # Calls the get_int_input function to get the user's input, and updates the project based on their input
    new_percentage = get_int_input("New percentage", MIN_COMPLETION, MAX_COMPLETION)
    if new_percentage is not None:
        projects[project_choice].completion = new_percentage

    # Calls the get_int_input function to get the user's input, and updates the project based on their input
    new_priority = get_int_input("New priority", MIN_PRIORITY, MAX_PRIORITY)
    if new_priority is not None:
        projects[project_choice].priority = new_priority


def filter_projects(projects):
    """Displays projects started after the user's chosen date"""

    need_input = True

    # Repeatedly asks user for input until a valid date is inputted
    while need_input:
        try:
            # Gets the user's date input and converts it to a date using datetime module
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

            # Creates a list sorted by date of the projects
            date_sorted_projects = sorted(projects, key=lambda p: datetime.datetime.strptime(p.date, "%d/%m/%Y").date())

            # Prints the projects to the user
            for project in date_sorted_projects:
                project_date = datetime.datetime.strptime(project.date, "%d/%m/%Y").date()
                if project_date > date:
                    print(project)

            need_input = False

        except ValueError:
            print("Invalid date format, try again")


def load_projects(file_name):
    """Read file of projects, save as objects."""

    projects = []

    try:
        # Open the file for reading
        in_file = open(file_name, 'r')
        # File format is like: Name    Start Date  Priority    Cost Estimate   Completion Percentage
        # 'Consume' the first line (header) - we don't need its contents
        in_file.readline()
        # All other lines are project data
        for line in in_file:
            # print(repr(line))  # debugging
            # Strip newline from end and split it into parts (CSV)
            parts = line.strip().split('\t')
            # Construct a Project object using the elements
            project = Project(parts[0], (parts[1]), int(parts[2]), float(parts[3]), int(parts[4]))
            # Add the project we've just constructed to the list
            projects.append(project)
        # Close the file as soon as we've finished reading it
        in_file.close()

        print(f"{len(projects)} projects successfully loaded from {file_name}")

    except FileNotFoundError:
        print(f"{file_name} could not be found in current directory, try again.")
        return None  # This return is only used if file was not found

    return projects


def save_projects(projects, file_name):
    """Saves data to file"""

    output_file = open(file_name, 'w+')  # Opens the file and truncates

    output_file.write(f"Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")  # Writes the header

    # For each project in projects, adds the project to the file
    for project in projects:
        line = f"{project.name}\t{project.date}\t{project.priority}\t{project.cost}\t{project.completion}\n"
        output_file.write(line)
    output_file.close()

    # Confirmation printed to the user
    print(f"Projects have been successfully saved to {file_name}")


main()
