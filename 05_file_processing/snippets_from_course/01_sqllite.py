import sqlite3

# TODO: Basic methods
conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);''')
tasks = [
    ('My first task', 1),
    ('My second task', 5),
    ('My third task', 10),
]
c.executemany('INSERT INTO tasks (name, priority) VALUES (?,?)', tasks)
conn.commit()
conn.close()


# TODO: Class approach
# class Todo:
#     def __init__(self):
#         self.conn = sqlite3.connect('todo.db')
#         self.c = self.conn.cursor()
#         self.create_task_table()
#
#     def create_task_table(self):
#         self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
#                      id INTEGER PRIMARY KEY,
#                      name TEXT NOT NULL,
#                      priority INTEGER NOT NULL
#                      );''')
#
#     def add_task(self):
#         name = input('Enter task name: ')
#         priority = int(input('Enter priority: '))
#
#         self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
#         self.conn.commit()
#
#
# app = Todo()
# app.add_task()

# TODO: cursor as iterator
# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# for row in c.execute('SELECT * FROM tasks'):
#     print(row)
# conn.close()

# TODO: fetchall
# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# c.execute('SELECT * FROM tasks')
# rows = c.fetchall()
# for row in rows:
#     print(row)
# conn.close()

# TODO: fetchone
# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# c.execute('SELECT * FROM tasks')
# row = c.fetchone()
# print(row)
# row = c.fetchone()
# print(row)
# conn.close()

# TODO: Update
# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# c.execute('UPDATE tasks SET priority = ? WHERE id = ?', (20, 1))
# conn.commit()
# c.close()

# TODO: Delete
# conn = sqlite3.connect('todo.db')
# c = conn.cursor()
# c.execute('DELETE FROM tasks WHERE id = ?', (1,))
# conn.commit()
# c.close()
