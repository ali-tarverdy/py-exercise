from time import sleep


def menu():
    # TODO : Show menu for users
    print("1) read")
    print("2) print")
    print("3) average")
    print("4) max")
    print("5) increment")
    print("6) decrement")
    print("7) personal increment")
    print("8) personal decrement")
    print("9) min")
    print("10) search with id")
    print("11) search with grade")
    print("12) exit")


def read_info_student(ids: list, grades: list, number_of_students: int):
    # TODO : Read information of students
    for i in range(number_of_students):
        try:
            ids.append(int(input("Enter ids of the students: ")))
            grades.append(int(input("Enter grades of the students: ")))
        except ValueError:
            print("Only can accept integer in the output!")


def print_info(ids: list, grades: list):
    # TODO : Print information about student
    print(f"ids of the students is: {ids}")
    print(f"Grades of the students is: {grades}")


def average_grade_of_students(grades: list):
    # TODO : Calculate average of the grades for students
    total = 0
    length = 0
    for i in range(len(grades)):
        length = len(grades)
        total += grades[i]
    return f"Average of grades is: {float(total // length)}"


def max_grade_of_student(grades: list):
    # TODO : Find biggest grade between students
    mx = grades[0]
    for i in range(len(grades)):
        if mx < grades[i]:
            mx = grades[i]
    return f"The biggest grade between students is: {mx}"


def increment_grade_of_students(grades: list):
    # TODO : Increment mark of students by one
    for i in range(len(grades)):
        grades[i] += 1
    return f"Increment result of the grades is: {grades}"


def personal_increment_grade_of_students(grades: list):
    # TODO : Increment mark of students personally
    try:
        out = grades[int(input("Which index of grade you want to increase? "))] = int(input("What is new grade? "))
    except IndexError:
        return "Your index of the student is out of the range!"
    return f"New grade is: {out}"


def personal_decrement_grade_of_students(grades: list):
    # TODO : Decrement mark of students personally
    try:
        out = grades[int(input("Which index of grade you want to decrease? "))] = int(input("What is new grade? "))
    except IndexError:
        return "Your index of the student is out of the range!"
    return f"New grade is: {out}"


def decrement_grade_of_students(grades: list):
    # TODO : Decrement mark of students by one
    for i in range(len(grades)):
        grades[i] -= 1
    return f"Decrement result of the grades is: {grades}"


def min_grade_of_student(grades: list):
    # TODO : Find smallest grade between students
    mx = grades[0]
    for i in range(len(grades)):
        if mx > grades[i]:
            mx = grades[i]
    return f"The smallest grade between students is: {mx}"


def search_with_id(ids: list, grades: list):
    # TODO : Search with id for find info of student
    search_id = int(input("Enter the id of the student you want to search for: "))
    for i in range(len(ids)):
        if ids[i] == search_id:
            return f"Grade of the student with id {search_id} is: {grades[i]}"
    return "Student information not found!"


def search_with_grade(ids: list, grades: list):
    # TODO : Search with grade for find info of student
    search_grade = int(input("Enter the grade of the student you want to search for: "))
    for i in range(len(grades)):
        if grades[i] == search_grade:
            return f"Id of the student with grade {search_grade} is: {ids[i]}"
    return "Student information not found!"


def exit_from_menu():
    # TODO : Exit from the menu
    exit("Exited from the menu was successful.")


def main():
    # TODO : Main function for doing tasks for each functions
    id = []
    grade = []
    running = True
    while running:
        menu()
        answer = int(input("Which task you want to run? "))
        match answer:
            case 1:
                num_of_student = int(input("How many students you want to enter: "))
                read_info_student(id, grade, num_of_student)
            case 2:
                print_info(id, grade)
            case 3:
                print(average_grade_of_students(grade))
            case 4:
                print(max_grade_of_student(grade))
            case 5:
                print(increment_grade_of_students(grade))
            case 6:
                print(decrement_grade_of_students(grade))
            case 7:
                print(personal_increment_grade_of_students(grade))
            case 8:
                print(personal_decrement_grade_of_students(grade))
            case 9:
                print(min_grade_of_student(grade))
            case 10:
                print(search_with_id(id, grade))
            case 11:
                print(search_with_grade(id, grade))
            case 12:
                print(exit_from_menu())
                running = False
            case _:
                print("Your choice should be between <1> to <12>")
        sleep(0.1)


main()
