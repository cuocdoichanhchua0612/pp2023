students = {}
courses = {}
marks = {}

std = []
crs = []
def student_information():
    number_student = int(input("input number of students in a class: "))
    for i in range(number_student):
        student_name = input("Enter a name: ")
        student_ID = input("Enter a ID: ")
        student_DoB = input("Enter a DoB: ")
        students["student_ID"] = student_ID
        students["student_DoB"] = student_DoB
        students["student_name"] = student_name
        dict_copy = dict(students)
        std.append(dict_copy)
    return std
def print_student(x):
    for i in range(len(x)):
        print(x[i])

student_information()
print_student(std)

number_course = int(input("input number of courses: "))
# student_information()

    # return {'sid': student_ID, 'sname': student_name, 'sDoB': student_DoB}

# def course_information():
#     course_name = input("Enter a name: ")


# def print_student():
#     for student in students:
#         print(f'{students[sname]}')



