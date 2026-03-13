"""
CE156 Assignment 2 - Exercise 3
Author: [Your Name]
Date: March 2026
Description: Processes university marks using NumPy arrays.
Calculates weighted totals, applies hurdle rules, and exports sorted results.
"""

import numpy as np
import sys


def get_grade(r_exam, r_cw, r_total):
    """
    Applies the grading rules based on rounded marks.

    Rules:
    - Fail if rounded Exam or CW Average < 35.
    - 1st: Total >= 70
    - 2nd: Total 50-69
    - 3rd: Total 40-49
    - Fail: Total < 40
    """
    if r_exam < 35 or r_cw < 35:
        return "Fail"

    if r_total >= 70:
        return "1st"
    elif 50 <= r_total <= 69:
        return "2nd"
    elif 40 <= r_total <= 49:
        return "3rd"
    else:
        return "Fail"


def main():
    file_name = "exercise3sampledata.txt"

    try:
        with open(file_name, 'r') as f:
            lines = f.readlines()

        if not lines:
            print("Error: The file is empty.")
            return

        # Read header: Student count (n) and CW weighting percentage
        header = lines[0].split()
        n = int(header[0])
        cw_weight_percent = float(header[1])

        # Calculate multipliers
        cw_mult = cw_weight_percent / 100
        exam_mult = 1 - cw_mult

        # 1. Initialize 2D NumPy array for raw data
        # Columns: [RegNo, Exam, AvgCW, Overall]
        data_2d = np.array([[0, 0.0, 0.0, 0.0]] * n)

        # 2. Process data line-by-line
        for i in range(n):
            parts = [float(x) for x in lines[i + 1].split()]
            reg_no = parts[0]
            exam_mark = parts[1]

            # Robustly handle 1 or more coursework marks
            cw_marks = parts[2:]
            avg_cw = sum(cw_marks) / len(cw_marks)

            # Overall mark calculation
            overall = (exam_mark * exam_mult) + (avg_cw * cw_mult)

            data_2d[i] = [reg_no, exam_mark, avg_cw, overall]

        # 3. Define the structured data type (4 ints, 1 string)
        studType = np.dtype([
            ('reg_no', 'i4'),
            ('exam', 'i4'),
            ('cw', 'i4'),
            ('total', 'i4'),
            ('grade', 'U10')
        ])

        # Create 1D structured array
        structured_array = np.array([(0, 0, 0, 0, "")] * n, dtype=studType)

        # 4. Populate structured array with rounded values
        for i in range(n):
            r_reg = int(data_2d[i, 0])
            r_exam = int(round(data_2d[i, 1]))
            r_cw = int(round(data_2d[i, 2]))
            r_total = int(round(data_2d[i, 3]))

            grade_str = get_grade(r_exam, r_cw, r_total)
            structured_array[i] = (r_reg, r_exam, r_cw, r_total, grade_str)

        # 5. Sort by overall mark
        sorted_array = np.sort(structured_array, order='total')

        # 6. Output to file using requested print format
        with open("output_exercise_3.txt", "w") as out_f:
            print(sorted_array, file=out_f)

        # 7. Screen Output Statistics
        firsts = sorted_array[sorted_array['grade'] == "1st"]
        seconds = sorted_array[sorted_array['grade'] == "2nd"]
        thirds = sorted_array[sorted_array['grade'] == "3rd"]
        fails = sorted_array[sorted_array['grade'] == "Fail"]

        print(f"Number of students with 1st Class: {len(firsts)}")
        print(f"Number of students with 2nd Class: {len(seconds)}")
        print(f"Number of students with 3rd Class: {len(thirds)}")
        print(f"Number of students who failed:      {len(fails)}")

        if len(firsts) > 0:
            print(f"Registration numbers (1st Class): {firsts['reg_no'].tolist()}")

    except FileNotFoundError:
        print(f"Error: Could not open {file_name}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()