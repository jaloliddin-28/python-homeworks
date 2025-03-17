class Employee:
    def __init__(self, employee_id: int, name, position, salary: int):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f'{self.employee_id}, {self.name}, {self.position}, {self.salary}'

class EmployeeManager:
    def __init__(self, filename = r"C:\Users\user\Desktop\MAAB\python-homeworks\lesson-7\homework\employee.txt"):
        self.filename = filename
    
    def display_file_path(self):
        print(f"Employee records are stored in: {self.filename}")
    
    def add(self, new: Employee):

        with open(self.filename, 'a') as file:
            file.write(str(new) + "\n")

        print("Employee added successfully!\n")
    
    def view_all(self):
        with open(self.filename, 'r') as file:
            records = file.readlines()
            if not records:
                print("No employees found.\n")
                return
            print("Employee Records: ")
            for record in records:
                print(record.strip())
            print()
    
    def search(self, id: str):
        with open(self.filename) as file:
            records = file.readlines()
        for record in records:
            data = record.strip().split(', ')
            if data[0] == id:
                print("Employee Found!")
                print(f'ID: {data[0]}, Name: {data[1]}, Position: {data[2]}, Salary: {data[3]}')
                return
        print("Employee not found!\n")
    
    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ").strip()
        employees = self.load_employees()
        updated = False

        with open(self.filename, "w") as file:
            for emp in employees:
                if emp.employee_id == emp_id:
                    print("\n Updating Employee Details:")
                    emp.name = input("Enter New Name: ").strip() or emp.name
                    emp.position = input("Enter New Position: ").strip() or emp.position
                    emp.salary = input("Enter New Salary: ").strip() or emp.salary
                    updated = True
                file.write(str(emp) + "\n")

        if updated:
            print("\n Employee record updated successfully!\n")
        else:
            print("\n Employee not found.\n")
    def delete(self):
        id = input("Enter the employee id:").strip()
        employees = self.load_employees()
        total = len(employees)
        employees_new = [i for i in employees if i.employee_id != id]
        with open(self.filename, 'w') as file:
            for i in employees_new:
                file.write(str(i) + '\n')
        if len(employees_new) < total:
            print("\nEmployee record is deleted successfully.")
        else:
            print('\nEmployee not found.')
    def run(self):
        while True:
            print("Employee Records Manager:")
            print("1. Add new employee record")
            print("2. View all employee records")
            print("3. Search for an employee by Employee ID")
            print("4. Update an employee's information")
            print("5. Delete an employee record")
            print("6. Exit")

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                employee_id = input("Enter Employee ID: ")
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = input("Enter salary: ")
                new = Employee(employee_id, name, position, salary)
                self.add(new)
            elif choice == "2":
                self.view_all()
            elif choice == "3":
                id = input("Enter Employee ID: ")
                self.search(id)
            elif choice == "4":
                self.update_employee()
            elif choice == "5":
                self.delete()
            elif choice == "6":
                print("\nGoodbye! Exiting the program...\n")
                break
            else:
                print("\nInvalid choice! Please enter a number between 1 and 6.\n")
    
    def load_employees(self):
        employees = []
        with open(self.filename) as file:
            records = file.readlines()
            for record in records:
                data = record.strip().split(", ")
                if len(data) == 4:
                    employees.append(Employee(*(data)))
        return employees
manager = EmployeeManager()
manager.run()