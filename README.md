# Student Grade and Result Analyzer

A simple, menu-driven Python program that stores student marks, calculates results, and shows class statistics, all from the command line.

## Features

- **Add a student** with roll number, name, and marks in 5 subjects
- **View all results** with total, percentage, grade, and PASS/FAIL
- **Search by roll number** to see one student's result
- **Class topper** (handles ties, so every top scorer is shown)
- **Class average** percentage
- **Lowest subject** shown for each student
- **Input validation** for duplicate roll numbers, blank names, non-numeric input, and marks outside 0-100

## Subjects

1. Python
2. PSNM
3. Data Structures
4. Database Management Systems
5. Entrepreneurship Skills

Each subject is out of 100, so the total is out of 500.

## Grading Scale

| Percentage | Grade |
|-----------|-------|
| 90 and above | A+ |
| 80 - 89.99 | A |
| 70 - 79.99 | B+ |
| 60 - 69.99 | B |
| 50 - 59.99 | C |
| 35 - 49.99 | D |
| Below 35 | F |

**Pass rule:** a student passes only if they score **35 or more in every subject**. Scoring below 35 in even one subject means FAIL.

## Requirements

- Python 3.x
- No external libraries needed

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. Run the program:
   ```bash
   python student_analyzer.py
   ```
   (Use your actual file name in place of `student_analyzer.py`.)

## Menu

```
===== STUDENT GRADE AND RESULT ANALYZER =====
1. Add student
2. View all results
3. Search by roll number
4. Display class topper
5. Display class average
6. Exit
```

## Sample Output

```
Roll Number: 101
Name: Daksh
Python: 80.0
PSNM: 75.0
Data Structures: 90.0
Database Management Systems: 85.0
Entrepreneurship Skills: 70.0
Total: 400.0 / 500
Percentage: 80.00%
Grade: A
Result: PASS
Lowest subject: Entrepreneurship Skills - 70.0
```

## Concepts Used

- Lists and dictionaries
- Functions with multiple return values
- `if / elif / else` and loops
- `try / except` for input validation
- `if __name__ == "__main__"`

## Notes

- Data is stored in memory only, so all records are lost when the program exits.

## Possible Improvements

- Save and load records from a file (CSV or JSON)
- Edit or delete a student
- Sort students by percentage (rank list)

## Author

Made by **Daksh** as a beginner Python project.
