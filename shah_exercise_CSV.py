import csv

def calculate_average(exam1, exam2, exam3):
    return (exam1 + exam2 + exam3) / 3

with open('grades.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    while True:
        first_name = input("Enter first name of student (or 'q' to quit): ")
        if first_name == 'q':
            break
        last_name = input("Enter last name of student: ")
        exam1 = int(input("Enter exam 1 grade: "))
        exam2 = int(input("Enter exam 2 grade: "))
        exam3 = int(input("Enter exam 3 grade: "))
        
        csvwriter.writerow([first_name, last_name, exam1, exam2, exam3])

with open('grades.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    print("Student Records:")
    for row in csvreader:
        first_name, last_name, exam1, exam2, exam3 = row
        print(f"{first_name} {last_name} | Exam 1: {exam1}, Exam 2: {exam2}, Exam 3: {exam3}")
