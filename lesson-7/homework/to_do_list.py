import json
import csv
from abc import ABC, abstractmethod

class StorageStrategy(ABC):
    @abstractmethod
    def save(self, tasks, filename):
        pass

    @abstractmethod
    def load(self, filename):
        pass

class CSVStorage(StorageStrategy):
    def save(self, tasks, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Task ID", "Title", "Description", "Due Date", "Status"])
            for task in tasks:
                writer.writerow([task['id'], task['title'], task['description'], task['due_date'], task['status']])

    def load(self, filename):
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                return [dict(row) for row in reader]
        except FileNotFoundError:
            return []

class JSONStorage(StorageStrategy):
    def save(self, tasks, filename):
        with open(filename, 'w') as file:
            json.dump(tasks, file, indent=4)

    def load(self, filename):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

class ToDoApp:
    def __init__(self, storage: StorageStrategy, filename):
        self.tasks = []
        self.storage = storage
        self.filename = filename
        self.load_tasks()

    def add_task(self, task_id, title, description, due_date, status):
        self.tasks.append({
            'id': task_id,
            'title': title,
            'description': description,
            'due_date': due_date,
            'status': status
        })
        print("Task added successfully!")

    def view_tasks(self):
        for task in self.tasks:
            print(f"{task['id']}, {task['title']}, {task['description']}, {task['due_date']}, {task['status']}")

    def update_task(self, task_id, **updates):
        for task in self.tasks:
            if task['id'] == task_id:
                task.update({k: v for k, v in updates.items() if v is not None})
                print("Task updated successfully!")
                return
        print("Task not found!")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        print("Task deleted successfully!")

    def filter_tasks(self, status):
        return [task for task in self.tasks if task['status'] == status]

    def save_tasks(self):
        self.storage.save(self.tasks, self.filename)
        print("Tasks saved successfully!")

    def load_tasks(self):
        self.tasks = self.storage.load(self.filename)
        print("Tasks loaded successfully!")

if __name__ == "__main__":
    storage_type = input("Choose storage format (csv/json): ").strip().lower()
    filename = "tasks." + storage_type
    storage = CSVStorage() if storage_type == "csv" else JSONStorage()
    app = ToDoApp(storage, filename)

    while True:
        print("""
        1. Add a new task
        2. View all tasks
        3. Update a task
        4. Delete a task
        5. Filter tasks by status
        6. Save tasks
        7. Load tasks
        8. Exit
        """)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ")
            status = input("Enter Status (Pending/In Progress/Completed): ")
            app.add_task(task_id, title, description, due_date, status)
        elif choice == "2":
            app.view_tasks()
        elif choice == "3":
            task_id = input("Enter Task ID to update: ")
            title = input("New Title (leave blank to keep unchanged): ") or None
            description = input("New Description (leave blank to keep unchanged): ") or None
            due_date = input("New Due Date (YYYY-MM-DD) (leave blank to keep unchanged): ") or None
            status = input("New Status (Pending/In Progress/Completed) (leave blank to keep unchanged): ") or None
            app.update_task(task_id, title=title, description=description, due_date=due_date, status=status)
        elif choice == "4":
            task_id = input("Enter Task ID to delete: ")
            app.delete_task(task_id)
        elif choice == "5":
            status = input("Enter status to filter (Pending/In Progress/Completed): ")
            filtered = app.filter_tasks(status)
            for task in filtered:
                print(f"{task['id']}, {task['title']}, {task['description']}, {task['due_date']}, {task['status']}")
        elif choice == "6":
            app.save_tasks()
        elif choice == "7":
            app.load_tasks()
        elif choice == "8":
            break
        else:
            print("Invalid choice, please try again.")