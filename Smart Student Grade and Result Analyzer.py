subjects = ["Python", "PSNM", "Data Structures",
            "Database Management Systems", "Enterpreneurship Skills"]

def calculate_result(student):
    marks = student["marks"]
    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B+"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 35:
        grade = "D"
    else:
        grade = "F"

    passed = True
    for mark in marks:
        if mark < 35:
            passed = False

    if passed:
        result = "PASS"
    else:
        result = "FAIL"

    lowest_mark = min(marks)
    lowest_subject = ""
    for i in range(5):
        if marks[i] == lowest_mark:
            if lowest_subject != "":
                lowest_subject = lowest_subject + ", "
            lowest_subject = lowest_subject + subjects[i]

    return total, percentage, grade, result, lowest_subject, lowest_mark


def show_student(student):
    total, percentage, grade, result, lowest_subject, lowest_mark = calculate_result(student)

    print("\nRoll Number:", student["roll"])
    print("Name:", student["name"])
    for i in range(5):
        print(subjects[i] + ":", student["marks"][i])
    print("Total:", total, "/ 500")
    print("Percentage: %.2f%%" % percentage)
    print("Grade:", grade)
    print("Result:", result)
    print("Lowest subject:", lowest_subject, "-", lowest_mark)


def add_student(students):
    roll = input("Enter roll number: ").strip()

    for student in students:
        if student["roll"] == roll:
            print("Error: Roll number already exists.")
            return

    name = input("Enter full name: ").strip()
    if name == "":
        print("Name cannot be blank.")
        return

    marks = []
    for subject in subjects:
        while True:
            try:
                mark = float(input("Enter marks for " + subject + " (0-100): "))
                if mark < 0 or mark > 100:
                    print("Marks must be between 0 and 100.")
                else:
                    marks.append(mark)
                    break
            except ValueError:
                print("Invalid input. Enter a number.")

    student = {"roll": roll, "name": name, "marks": marks}
    students.append(student)
    print("Student added successfully.")


def view_students(students):
    if len(students) == 0:
        print("No student records available.")
    else:
        for student in students:
            show_student(student)


def search_student(students):
    roll = input("Enter roll number to search: ").strip()
    found = False

    for student in students:
        if student["roll"] == roll:
            show_student(student)
            found = True
            break

    if not found:
        print("Student not found.")


def show_topper(students):
    if len(students) == 0:
        print("No student records available.")
        return

    highest = -1
    for student in students:
        total, percentage, grade, result, lowest_subject, lowest_mark = calculate_result(student)
        if percentage > highest:
            highest = percentage

    print("\nClass topper percentage: %.2f%%" % highest)
    print("Topper(s):")
    for student in students:
        total, percentage, grade, result, lowest_subject, lowest_mark = calculate_result(student)
        if percentage == highest:
            print(student["name"], "- Roll:", student["roll"])


def show_average(students):
    if len(students) == 0:
        print("No student records available.")
        return

    total_percentage = 0
    for student in students:
        total, percentage, grade, result, lowest_subject, lowest_mark = calculate_result(student)
        total_percentage = total_percentage + percentage

    average = total_percentage / len(students)
    print("\nNumber of students:", len(students))
    print("Class average percentage: %.2f%%" % average)


def main():
    students = []

    while True:
        print("\n===== STUDENT GRADE AND RESULT ANALYZER =====")
        print("1. Add student")
        print("2. View all results")
        print("3. Search by roll number")
        print("4. Display class topper")
        print("5. Display class average")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            show_topper(students)
        elif choice == "5":
            show_average(students)
        elif choice == "6":
            print("Thank you for using the program.")
            break
        else:
            print("Invalid choice. Please enter 1 to 6.")


if __name__ == "__main__":
    main()