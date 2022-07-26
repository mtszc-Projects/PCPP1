"""
1.4.1.1 LAB: sqlite3 - Lab 2
https://edube.org/learn/pcpp1-5/lab-sqlite3-lab-2
The application is almost ready. Let's add the missing functionalities to it:
Create a method called change_priority, responsible for updating task priority. The method should get the id of the task
from the user and its new priority (greater than or equal to 1).
Create a method called delete_task, responsible for deleting single tasks. The method should get the task id from the
user.
Implement a simple menu consisting of the following options:
1. Show Tasks
2. Add Task
3. Change Priority
4. Delete Task
5. Exit
where:
Show Tasks (calls the show_tasks method)
Add Task (calls the add_task method)
Change Priority (calls the change_priority method)
Delete Task (calls the delete_task method)
Exit (interrupts program execution)
The program should obtain one of these options from the user, and then call the appropriate method of the TODO object.
Choosing option 5 must terminate the program. A menu should be displayed in an infinite loop so that the user can choose
an option multiple times.
"""
import sqlite3


class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()

    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );''')

    def add_task(self):
        name = input('Enter task name: ')
        if name == '':
            print('Task name can\'t be empty string.')
            return None
        elif self.find_task(name) is not None:
            print('Task with that name already exist in database.')
            return None
        priority = int(input('Enter priority: '))
        if priority < 1:
            print('Priority must be >=1.')
            return None
        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
        self.conn.commit()

    def find_task(self, name):
        self.c.execute(f'SELECT * FROM tasks')
        match = self.c.fetchone()
        if match is None or name not in match:
            return None
        else:
            return match

    def change_priority(self):
        task_id = int(input('Choose task to be changed (provide tasks ID): '))
        priority = int(input('Enter new priority: '))
        if priority < 1:
            print('Priority must be >=1.')
            return None
        self.c.execute('UPDATE tasks SET priority = ? WHERE id = ?', (priority, task_id))
        self.conn.commit()

    def delete_task(self):
        task_id = int(input('Provide task ID to be deleted: '))
        self.c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        self.conn.commit()

    def show_tasks(self):
        for row in self.c.execute('SELECT * FROM tasks'):
            print(row)


app = Todo()


while True:
    print("""
1. Show Tasks 
2. Add Task 
3. Change Priority 
4. Delete Task
5. Exit
""")
    choice = input("Choose action: ")
    if choice == '5':
        app.conn.close()
        exit(0)
    elif choice == '1':
        app.show_tasks()
    elif choice == '2':
        app.add_task()
    elif choice == '3':
        app.change_priority()
    elif choice == '4':
        app.delete_task()
