students = {}
courses = {}
marks = {}

std = []
crs = []
mrks = []
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

def course_information():
    number_course = int(input("input number of courses in a class: "))
    for i in range(number_course):
        course_name = input("Enter a name of course: ")
        course_ID = input("Enter a ID of course: ")
        courses["course_name"] = course_name
        courses["course_ID"] = course_ID
        dict_copy = dict(courses)
        crs.append(dict_copy)
    return crs
def print_course(x):
    for i in range(len(x)):
        print(x[i])

def student_mark(std: list, crs: list, number_student: int):
    for coures in crs:
        print(coures)
        select = int(input("select course:"))
        for i in range(number_student):
            std[i].append(int(input("Student marks" + str(i+1))))
            dict_copy = dict(marks)
            mrks.append(dict_copy)
            return mrks

def print_mark(std: list, crs: list):
    for coures in crs:
        print(coures)
        select = int(input("Select course: "))
        for i in range(len(std)):
            print("student_ID", std[i][0], "student_name: ", std[i][1], 
            "Mark: ", std[i][select + 2])
          
def main():
    student_information()
    print_student(std)
    course_information()
    print_course(crs)
    student_mark()
    print_mark(mrks)

main()