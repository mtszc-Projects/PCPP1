"""
1.2.1.1 LAB: sqlite3 - Lab 1
https://edube.org/learn/pcpp1-5/lab-sqlite3-lab-1
Our TODO application requires you to add a little security and display the data saved in the database. Your task is to
implement the following functionalities:
Create a find_task method, which takes the task name as its argument. The method should return the record found or None
otherwise.
Block the ability to enter an empty task (the name cannot be an empty string).
Block the ability to enter a task priority less than 1.
Use the find_task method to block the ability to enter a task with the same name.
Create a method called show_tasks, responsible for displaying all tasks saved in the database.
Test data:
Example input:
Enter task name: My first task
Enter priority: 1
Example output:
(1, 'My first task', 1)
Example input:
Enter task name: My second task
Enter priority: 2
Example output:
(1, 'My first task', 1)
(2, 'My second task', 2)
Example input:
Enter task name: My first task
Enter priority: 1
Example output:
(1, 'My first task', 1)
(2, 'My second task', 2)
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

    def show_tasks(self):
        for row in self.c.execute('SELECT * FROM tasks'):
            print(row)


if __name__ == '__main__':
    app = Todo()
    app.add_task()
    app.show_tasks()
