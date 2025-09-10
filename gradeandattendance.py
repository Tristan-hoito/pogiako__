# Student Grading and Attendance System
# 
# Tatanungin ang user kung ano grade nya, 0-100. Ilan ren absents nya. May corresponding letter,
#
# 5 absents above, di pasado
#
# Pag below 60, F.
# 60 - 69, D.
# 70 - 79, C.
# 80 - 80, B.
# 90 - 100, A.
#
# If, elif, and else
#
# Status ( Passed or Failed )
#
# If student have a grade A-C and absent nya is below 5, passed
# If student have a grade F-D and absent nya is above or equal to 5, dropped
# Nested condition
#
# Do while loop, do you want to continue to input grade or end
# Kapag nag end, print na.
#
# Match case (Remark)
# A, excellent
# B, Good Job
# C, Needs improvement
# D, On Probation
# F, Failed
# Case default, Invalid Grade
#

def grading_system():

    while True:
        try:
            grade = int(input("\nWhat is your grade: "))
            absence = int(input("How many absences do you have: "))

            if 100 >= grade and grade >= 90:
                letter = "A"
                status1 = "Passed"

                if absence < 5:
                    status2 = "Passed"
                    

                elif absence >= 5:
                    status2 = "Failed"
                    

            elif 89 >= grade and grade >= 80:
                letter = "B"
                status1 = "Passed"

                if absence < 5:
                    status2 = "Passed"
                    

                elif absence >= 5:
                    status2 = "Failed"
                    

            elif 79 >= grade and grade >= 70:
                letter = "C"
                status1 = "Passed"

                if absence < 5:
                    status2 = "Passed"
                    

                elif absence >= 5:
                    status2 = "Failed"
                    

            elif 69 >= grade and grade >= 60:
                letter = "D"
                status1 = "Failed"

                if absence < 5:
                    status2 = "Passed"
                    

                elif absence >= 5:
                    status2 = "Failed"
                    

            elif 59 >= grade and grade >= 0:
                letter = "F"
                status1 = "Failed"

                if absence < 5:
                    status2 = "Passed"
            

                elif absence >= 5:
                    status2 = "Failed"

            else:
                print("\nInvalid Input, please put a grade 0-100 and a proper number of absents.")
                grading_system()

        except ValueError:
            print("\nPlease input a proper number!")
            grading_system()

        end(grade, absence, letter, status1, status2)

def end(grade, absence, letter, status1, status2):

    match letter:
        case "A":
            remark = "Excellent!"
        
        case "B":
            remark = "Good Job!"

        case "C":
            remark = "Needs Improvement!"

        case "D":
            remark = "On Probation!"

        case "F":
            remark = "Failed!"
        
        case default:
            remark = "Invalid Grade!"

    if status1 == "Passed" and status2 == "Passed":
        print("\nYou passed this semester with no problems!")

    elif status1 == "Failed" and status2 == "Passed":
        print(f"\nYou have not passed this semester, you failed because of your Grades!")

    if status1 == "Passed" and status2 == "Failed":
        print(f"\nYou have not passed this semester, you failed because of your Absences!")

    if status1 == "Failed" and status2 == "Failed":
        print(f"\nYou have not passed this semester, you failed because of your Grades and Absences!")

    print(f"\nYour Grade: {grade}, {letter}. {remark} {status1}!")
    print(f"Number of Absence: {absence}, {status2}!")
    pass

    while True:

        stop = input("\nDo you want to continue to input grades?\n y/n > ").lower().strip()

        try:

            if stop == "y":
                return grading_system

            elif stop == "n":
                print("\nExiting.....\n")
                exit()

            else:
                print("\nPlease choose between y/n only!")
            
        except ValueError:
            print("\nPlease choose between y/n only!")

print("\nGrading and Attendance Checker!")
grading_system()

        