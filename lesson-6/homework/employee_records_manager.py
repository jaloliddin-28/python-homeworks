with open('employees.txt', mode='a') as file:
    a = int(input("How many records do you want to add at first? "))
    for t in range(a):
        l = input("Record Template: ID, Name, Position, Salary: ")
        file.write(l + '\n')

def view_all():
    with open('employees.txt') as file1:
        for line in file1:
            print(line.strip())

s = 0
while s != 6:
    s = int(input("Choose one of the following options: \n1. Add new employee record \n2. View all employee records \n3. Search for an employee by Employee ID \n4. Update an employee's information \n5. Delete an employee record \n6. Exit\n"))
    if s == 1:
        with open('employees.txt', mode='a') as file2:
            b = int(input("How many records do you want to add? "))
            for y in range(b):
                l = input("Record Template: ID, Name, Position, Salary: ")
                file2.write(l + '\n')
    elif s == 2:
        view_all()
    elif s == 3:
        j = input("Enter Employee number: ")
        u = []
        with open('employees.txt') as file1:
            for them in file1:
                u.append(them.strip().split(','))
        for i in u:
            if i[0] == j:
                print(i)
    elif s == 4:
        lines = []
        with open('employees.txt') as file3:
            for us in file3:
                lines.append(us.strip().split(','))
        num_2 = input("Enter Employee number: ")
        new_content = input("Enter updated information in the same format: ")
        for p in lines:
            if p[0] == num_2:
                lines[lines.index(p)] = new_content.strip().split(',')
        with open("employees.txt", mode='w') as file4:
            file4.writelines([','.join(us) + '\n' for us in lines])
    elif s == 5:
        lines2 = []
        with open('employees.txt') as file5:
            for you in file5:
                lines2.append(you.strip().split(','))  
        num = input("Enter Employee number to delete: ")
        updated_lines = [k for k in lines2 if k[0] != num]
        with open("employees.txt", mode='w') as file6:
            file6.writelines([','.join(you) + '\n' for you in updated_lines])