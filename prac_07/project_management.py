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
    print("Project Manager 1.0 - by Bryn Baird")

    file_name = "projects.txt"
    projects = load_projects(file_name)

    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            candidate_file_name = get_user_input("file name")
            loaded_projects = load_projects(candidate_file_name)
            if loaded_projects is not None:
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
    """Displays list of incomplete and complete projects to user"""

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
    """Asks the user for their input, and ensures the input is not blank"""

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
    new_project_date = get_user_input("Start date (dd/mm/yy)")
    new_project_priority = get_user_input("Priority")
    new_project_cost = get_user_input("Cost estimate")
    new_project_completion = get_user_input("Percent complete")

    # Creates the new project
    new_project = Project(new_project_name, new_project_date, (int(new_project_priority)), (float(new_project_cost)),
                          (int(new_project_completion)))

    projects.append(new_project)  # Adds the new project to the primary list of projects

    # Prints a confirmation to the user that new project has been added
    print(f"{projects[-1]} added to Project Manager\n")
    return projects


def get_int_input(field_name, min_int, max_int):
    need_input = True

    user_int = None
    while need_input:
        user_input = input(f"New {field_name} (range {min_int} - {max_int}): ")
        if user_input == "":
            print("")
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
    for project_index, project in enumerate(projects, 1):
        print(f"({project_index}) {project}")

    project_choice = int(input("Project choice: ")) - 1
    print(projects[project_choice])

    new_percentage = get_int_input("percentage", MIN_COMPLETION, MAX_COMPLETION)
    if new_percentage is not None:
        projects[project_choice].completion = new_percentage

    new_priority = get_int_input("priority", MIN_PRIORITY, MAX_PRIORITY)
    if new_priority is not None:
        projects[project_choice].priority = new_priority


def filter_projects(projects):
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    #date_string = "30/12/2021"  # Placeholder for testing
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

    for project in projects:
        project_date = datetime.datetime.strptime(project.date, "%d/%m/%Y").date()
        if project_date > date:
            print(project)


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
            # year should be an int
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

    print(f"Projects have been successfully saved to {file_name}")


main()
