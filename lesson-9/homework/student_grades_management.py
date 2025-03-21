import csv
with open(r'C:\Users\user\Desktop\MAAB\python-homeworks\lesson-9\homework\grades.csv', 'r') as csvfile:
    csvread = csv.DictReader(csvfile)
    data_list = []
    for row in csvread:
        data_list.append(row)
subject_grades = {}
for i in data_list:
    subject = i['Subject']
    grade = float(i['Grade'])

    if subject not in subject_grades:
        subject_grades[subject] = []
    
    subject_grades[subject].append(grade)

average_grades = {}
for subject, grades_list in subject_grades.items():
    average_grades[subject] = sum(grades_list) / len(grades_list)
with open('average_grades.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Subject', 'Average Grade']) 
    for subject, average in average_grades.items():
        writer.writerow([subject, round(average, 2)])