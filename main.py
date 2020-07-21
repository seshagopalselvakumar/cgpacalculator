# author :  Seshagopal Selvakumar
import csv
import os
gpaArray = []
creditsArray = []
candidateName = input("Enter your name: ")
usnNumber = input("Enter your University Serial Number (USN): ")
semestersAttended = int(input(
    "Enter the number of semesters for which you have the marks: "))
for i in range(0, semestersAttended):
    gpaValue = float(input("Enter the gpa of semester {}: ".format(i + 1)))
    creditValue = int(
        input("Enter the total credits for semester {}: ".format(i + 1)))
    gpaArray.append(gpaValue)
    creditsArray.append(creditValue)


def calculateSum():
    creditsSum = 0
    gpaSum = 0
    for i in range(0, semestersAttended):
        creditsSum += creditsArray[i]
        gpaSum += gpaArray[i] * creditsArray[i]

    cumulativeGpa = gpaSum/creditsSum
    print("Your cumulative GPA for {} semesters is {:.2f}".format(
        semestersAttended, cumulativeGpa))

    if os.path.isfile("gpa.csv"):
        os.remove("gpa.csv")
        with open("gpa.csv", "x") as file:
            fieldnames = ["Student Name", "University Serial Number", "GPA for each semester",
                          "Credits for each Semester", "Total CGPA"]
            csv_file = csv.DictWriter(file, fieldnames=fieldnames)
            csv_file.writeheader()
            # csv_file.writerow({"Student Name": candidateName,
            #                    "University Serial Number": usnNumber, "Total CGPA": cumulativeGpa})
            for gpa, credit in zip(gpaArray, creditsArray):
                if gpa == gpaArray[0]:
                    csv_file.writerow(
                        {"GPA for each semester": gpa, "Credits for each Semester": credit, "Student Name": candidateName,
                         "University Serial Number": usnNumber, "Total CGPA": cumulativeGpa})
                else:
                    csv_file.writerow(
                        {"GPA for each semester": gpa, "Credits for each Semester": credit})
            print("A gpa.csv file with all the details has been generated!")
    else:
        with open("gpa.csv", "x") as file:
            fieldnames = ["Student Name", "University Serial Number", "GPA for each semester",
                          "Credits for each Semester", "Total CGPA"]
            csv_file = csv.DictWriter(file, fieldnames=fieldnames)
            csv_file.writeheader()
            # csv_file.writerow({"Student Name": candidateName,
            #                    "University Serial Number": usnNumber, "Total CGPA": cumulativeGpa})
            for gpa, credit in zip(gpaArray, creditsArray):
                if gpa == gpaArray[0]:
                    csv_file.writerow(
                        {"GPA for each semester": gpa, "Credits for each Semester": credit, "Student Name": candidateName,
                         "University Serial Number": usnNumber, "Total CGPA": cumulativeGpa})
                else:
                    csv_file.writerow(
                        {"GPA for each semester": gpa, "Credits for each Semester": credit})
            print("A gpa.csv file with all the details has been generated!")


calculateSum()
