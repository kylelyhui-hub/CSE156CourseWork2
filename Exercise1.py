from datetime import date

  # Function for calculating age
def calculate_age(birth_date):

    today = date.today()

    # Basic year subtraction
    age = today.year - birth_date.year

    # Check if the birthday has occurred yet this year
    # This evaluates to True (1) if the birthday hasn't happened, subtracting 1 from age
    has_not_passed = (today.month, today.day) < (birth_date.month, birth_date.day)

    return age - has_not_passed


def main():
    """
    Main execution function to handle user input and output.
    """
    user_input = input("Please enter your date of birth (mm/dd/yyyy): ")

    # Check basic format length and separators
    if len(user_input) != 10 or user_input[2] != '/' or user_input[5] != '/':
        print("Error: Invalid format. Please use mm/dd/yyyy.")
        return

    try:
        # Split and convert to integers
        parts = user_input.split('/')
        month = int(parts[0])
        day = int(parts[1])
        year = int(parts[2])

        # Create date object (this automatically validates day/month ranges)
        dob = date(year, month, day)
        today = date.today()

        # Check if the date is in the future
        if dob > today:
            print("Error: The date of birth cannot be in the future.")
            return

        # Success - Calculate Age
        age = calculate_age(dob)

        # Format to European style (dd/mm/yyyy) with leading zeros
        # :02d ensures the integer is at least 2 digits wide with leading zeros
        euro_format = f"{dob.day:02d}/{dob.month:02d}/{dob.year}"

        # Final Outputs
        print(f"Date of birth (European format): {euro_format}")
        print(f"Your age is: {age} years")

    except ValueError:
        # This catches invalid months (e.g. 13), invalid days (e.g. Feb 30),
        # or non-numeric characters.
        print("Error: The date provided is invalid.")


if __name__ == "__main__":
    main()
