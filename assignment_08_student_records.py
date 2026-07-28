def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    return round(total / len(scores), 2)


def add_student(students):
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    try:
        student_id = int(input("Student ID: "))
    except ValueError:
        print("Error: Student ID must be a number.")
        return

    try:
        count = int(input("How many scores? "))
    except ValueError:
        print("Error: Please enter a valid number of scores.")
        return

    if count <= 0:
        print("Error: Number of scores must be positive.")
        return

    scores = []
    for index in range(1, count + 1):
        try:
            score = int(input(f"Enter score {index}: "))
        except ValueError:
            print("Error: Please enter valid integer scores.")
            return
        scores.append(score)

    students.append({
        "name": name,
        "id": student_id,
        "scores": scores
    })
    print(f'Student "{name}" added successfully.')


def display_students(students):
    if not students:
        print("No students have been added yet.")
        return

    print("-" * 50)
    print(f"{'Name':<15} {'ID':<10} {'Scores':<20} {'Average'}")
    print("-" * 50)
    for student in students:
        average = calculate_average(student["scores"])
        scores_text = ", ".join(str(score) for score in student["scores"])
        print(f"{student['name']:<15} {student['id']:<10} {scores_text:<20} {average:.2f}")
    print("-" * 50)


def calculate_student_average(students):
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Error: Student ID must be a number.")
        return

    for student in students:
        if student["id"] == student_id:
            average = calculate_average(student["scores"])
            print(f"{student['name']}'s average score: {average:.2f}")
            return

    print("Error: Student ID not found.")


def main():
    students = []

    while True:
        print("===============================")
        print("STUDENT RECORD SYSTEM MENU")
        print("===============================")
        print("1. Add student")
        print("2. Display all students")
        print("3. Calculate average score")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            calculate_student_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice.")


if __name__ == "__main__":
    main()

