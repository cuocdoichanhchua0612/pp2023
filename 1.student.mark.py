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
        select = int(input("select course:"))
        for c in range(len(crs)):
            if crs[c]['course_ID'] == select :

                for s in range(number_student):
                    row = len(crs)
                    clm = len(std)
                    z=input("Student marks" + ' ' + str(s+1))
                    mark_2D_list = [[z for c in row] for s in range(clm)]
                    print(mark_2D_list)

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
    student_mark(std, crs, len(std))
    print_mark(std, crs)

main()