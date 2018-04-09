import json

def loadSetupData():
    with open('gc_setup.json') as data_file:
        course = json.load(data_file)

    grades = course["course_setup"]
    return grades


def AskForAssignmentMarks(grades, ID):
    with open('gc_grades.json') as data_file:
        student_grades= json.load(data_file)

    for key in grades:
            if student_grades[ID][key]>-1:
                print("Your grade from "+ key + " is " + str(student_grades[ID][key]))
                needs_update = input("Do you need to update it? if yes, then enter 1, else enter 0")
                if needs_update == 1:
                    update=input("Please insert the correct Grade for: " + key + " . Please insert -1 if you don't have a grade yet")
                    if update>=100 or (update<=0 and update!=-1):
                        update=input("Please put in a grade between 0 and 100.")

                    student_grades[ID][key] = update


    return student_grades

def GradesToSave(student_grades, ID):
    print ("Your grades")
    for key in student_grades[ID]:
        print(key + ':', student_grades[ID][key])
    file = open("gc_grades.json", "w")
    file.write(json.dumps(student_grades))
    file.close()

def GradesCalculation(grades, student_grades, ID):
    curr_grade = 0.0
    for key in student_grades[ID]:
        if student_grades[ID][key] != -1:
            calc_grade = float(student_grades[ID][key]) * grades[key] / 100
            curr_grade = curr_grade + calc_grade
    print curr_grade
    return curr_grade

def printCurrentGrades(curr_grade, marks):
    for i in range(len(marks)):
        if curr_grade >= marks[i]["min"] and curr_grade <= marks[i]["max"]:
            print marks[i]["mark"]

def main():
    g = loadSetupData()
    grades=g["grade_breakdown"]
    ID= raw_input("Print student ID:")
    student_grades = AskForAssignmentMarks(grades, ID)
    GradesToSave(student_grades, ID)
    curr_grade = GradesCalculation(grades, student_grades, ID)
    marks=g["conv_matrix"]
    printCurrentGrades(curr_grade, marks)

main()
