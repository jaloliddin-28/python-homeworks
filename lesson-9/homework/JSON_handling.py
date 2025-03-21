import json
import csv
with open("tasks.json", 'r') as jsonfile:
    data = json.load(jsonfile)
total_tasks = len(data)
completed = 0
pending = 0
for dic in data:
    if dic['completed'] == True:
        completed += 1
    else:
        pending += 1
priority = []
for dic in data:
    priority.append(dic['priority'])
average_priority = sum(priority) / len(priority)
print(f'Total tasks: {total_tasks}\nCompleted Tasks: {completed}\nPending Tasks: {pending}\nAverage Priority: {average_priority}')

with open("tasks.csv", 'w', newline='') as csvfile:
    fieldnames = ['ID', 'Task', 'Completed', 'Priority']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()  
    for dic in data:
        writer.writerow({
            'ID': dic['id'],
            'Task': dic['task'],
            'Completed': dic['completed'],
            'Priority': dic['priority']
        })