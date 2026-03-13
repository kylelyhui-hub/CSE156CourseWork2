"""
CE156 Assignment 2 - Exercise 2
Author: [Your Name]
Date: March 2026
Description: This script reads student data from a file, stores them as tuples,
and allows the user to search for students by department in a formatted table.
"""


def display_students_by_dept(student_list, target_dept):
    """
    Filters students by department and prints a sorted table of results.

    Args:
        student_list (list): List of tuples (reg_num, name, department).
        target_dept (str): The department name to filter by.
    """
    # Filter the list based on the department (case-insensitive for robustness)
    matches = [s for s in student_list if s[2].strip().upper() == target_dept.strip().upper()]

    if not matches:
        print(f"\nNo students found in the '{target_dept}' department.")
        return

    # Sort by registration number (index 0 of our tuple)
    matches.sort()

    # Output formatted table
    print(f"\nStudents in {target_dept.upper()}:")
    print(f"{'Reg No.':<15} | {'Name':<20}")
    print("-" * 38)

    for reg_num, name, dept in matches:
        print(f"{reg_num:<15} | {name:<20}")
    print()


def main():
    """
    Main program logic: File reading and the interactive search loop.
    """
    file_name = input("Enter the name of the student data file: ")
    students = []

    try:
        with open(file_name, 'r') as file:
            for line in file:
                # Expecting: Name, RegNum, Dept
                parts = line.strip().split(',')
                if len(parts) == 3:
                    name = parts[0].strip()
                    reg_num = parts[1].strip()
                    dept = parts[2].strip()

                    # Store as (Name, Dept, RegNum) for easy sorting
                    students.append((name, dept, reg_num))

    except FileNotFoundError:
        print(f"Error: The file '{file_name}' could not be found. Terminating.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    # Requirement: Output the list of tuples (no formatting required)
    print("\nData loaded successfully. List of tuples:")
    print(students)

    # Search Loop
    while True:
        dept_query = input("\nEnter department name to search (or press Enter to skip): ")

        if dept_query:
            display_students_by_dept(students, dept_query)

        quit_choice = input("Enter 'q' to quit or any other key to search again: ").lower()
        if quit_choice == 'q':
            print("Exiting program.")
            break


if __name__ == "__main__":
    main()