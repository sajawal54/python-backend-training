students = []

def show_menu():
    print("\n" + "=" * 45)
    print("      STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("=" * 45)

def add_student():

    student_id = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    age = int(input("Enter Student Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)

    print("\nStudent Added Successfully.")

def show_students():

    if len(students) == 0:
        print("\nNo Students Found.")
        return

    print("\nStudent Records")

    for student in students:

        print("-" * 35)
        print(f"ID     : {student['id']}")
        print(f"Name   : {student['name']}")
        print(f"Age    : {student['age']}")
        print(f"Course : {student['course']}")
        print(f"Marks  : {student['marks']}")


def search_student():

    student_id = int(input("Enter Student ID: "))

    for student in students:

        if student["id"] == student_id:

            print("\nStudent Found")

            print(student)

            return

    print("Student Not Found.")


def update_student():

    student_id = int(input("Enter Student ID: "))

    for student in students:

        if student["id"] == student_id:

            student["name"] = input("Enter New Name: ")
            student["age"] = int(input("Enter New Age: "))
            student["course"] = input("Enter New Course: ")
            student["marks"] = float(input("Enter New Marks: "))

            print("Student Updated Successfully.")

            return

    print("Student Not Found.")


def delete_student():

    student_id = int(input("Enter Student ID: "))

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            print("Student Deleted Successfully.")

            return

    print("Student Not Found.")



def main():

    while True:

        show_menu()

        choice = input("Choose an Option: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            show_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()


        elif choice == "6":
            print("Thank you for using Student Management System.")
            break

        else:
            print("Invalid Choice.")



main()

