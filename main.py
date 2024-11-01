import sqlite3 as sq
import os

def clear_term():
    os.system("clear")


conn = sq.connect("tasks.db")
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS todolist
            (
            id INTEGER PRIMARY KEY, 
            date TEXT, 
            deadline TEXT,
            task TEXT,
            description TEXT,
            state TEXT
            )
            ''')
#state: done, not done, in progress
conn.commit()
print("table was created")

def add_task(date, deadline, task, description, state):
    with conn:
        cur.execute('''INSERT INTO todolist(date, deadline, task, description, state)
                    VALUES(?,?,?,?,?)''', (date, deadline, task, description, state))
        print("task has been saved")

def delete_task(task_id):
    with conn:
        cur.execute('''DELETE FROM todolist WHERE id = ?''', (task_id,))
    print("task deleted")
    

def update_full_task(task_id, date, deadline, task, description, state):
    with conn:
        cur.execute('''UPDATE todolist
                    SET date = ?, deadline = ?, task = ?, description = ?, state = ?
                    WHERE id = ?''', (date, deadline, task, description, state, task_id))
    print("task updated")
    
def update_deadline_task(task_id, deadline):
    with conn:
        cur.execute('''UPDATE todolist
                    SET deadline = ?
                    WHERE id = ?''', (deadline, task_id))
    print("task deadline updated")

def update_task_task(task_id, task):
    with conn:
        cur.execute('''UPDATE todolist
                    SET task = ?
                    WHERE id = ?''', (task, task_id))
    print("task task updated")

def update_description_task(task_id, description):
    with conn:
        cur.execute('''UPDATE todolist
                    SET description = ?
                    WHERE id = ?''', (description, task_id))
    print("task description updated")

def update_state_task(task_id, state):
    with conn:
        cur.execute('''UPDATE todolist
                    SET state = ?
                    WHERE id = ?''', (state, task_id))
    print("task state updated")

def view_all_tasks():
    with conn:
        cur.execute('''SELECT * FROM todolist''')
        rows = cur.fetchall()
        for row in rows:
            print(row)

def view_done_tasks():
    with conn:
        cur.execute('''SELECT * FROM todolist WHERE state = "done" ''')
        rows = cur.fetchall()
        print("DONE TASKS >>> ")
        for row in rows:
            print(row)

def view_not_done_tasks():
    with conn:
        cur.execute('''SELECT * FROM todolist WHERE state = "not done" ''')
        rows = cur.fetchall()
        print(" NOT DONE TASKS >>> ")
        for row in rows:
            print(row)

def view_in_progress_tasks():
    with conn:
        cur.execute('''SELECT * FROM todolist WHERE state = "in progress" ''')
        rows = cur.fetchall()
        print("IN PROGRESS TASKS >>> ")
        for row in rows:
            print(row)

def task_summary():
    print("Total Statistics >>> ")

    with conn:
        cur.execute('''SELECT COUNT(*) FROM todolist WHERE state = "done" ''')
        done = cur.fetchone()[0] or 0
        print(f"DONE: {done}")

        cur.execute('''SELECT COUNT(*) FROM todolist WHERE state = "not done" ''')
        notdone = cur.fetchone()[0] or 0
        print(f"NOT DONE: {notdone}")

        cur.execute('''SELECT COUNT(*) FROM todolist WHERE state = "in progress" ''')
        inprogress = cur.fetchone()[0] or 0
        print(f"IN PROGRESS: {inprogress}")

        total = done + notdone + inprogress
    print(f"Total amount of tasks: {total} ")


def menu():
    while True:
        print("\n||Wellcome to TaskTracker||")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. View Summary")
        print("6. Exit")
        choice = input("Enter your choice: ")
        clear_term()

        if choice == "1": #add task
            date = input("ENTER task date: ")
            deadline = input("ENTER task deadline: ")
            task = input("ENTER task name: ")
            description = input("ENTER task description: ")
            state = "not done"
            add_task(date, deadline, task, description, state)
        elif choice == "2": # view task
            while True:
                print("Choose an option: ")
                print("1. View all tasks")
                print("2. View Done Tasks")
                print("3. View In Progress Tasks")
                print("4. View Not Done Tasks")
                print("5. Exit")

                choice = input("Enter your choice: ")
                clear_term()

                if choice == "1":
                    view_all_tasks()
                elif choice == "2":
                    view_done_tasks()
                elif choice == "3":
                    view_in_progress_tasks()
                elif choice == "4":
                    view_not_done_tasks()
                elif choice == "5":
                    break
                else:
                    print("INVALID CHOICE!")
        elif choice == "3": #update task
            while True:
                print("Choose an option: ")
                print("1. Update full task")
                print("2. Update task deadline")
                print("3. Update task name")
                print("4. Update task description")
                print("5. Update task state")
                print("6. Exit")

                choice = input("Enter your choice: ")
                clear_term()

                if choice == "1":
                    task_id = int(input("Eneter task ID: "))
                    date = input("ENTER task date: ")
                    deadline = input("ENTER task deadline: ")
                    task = input("ENTER task name: ")
                    description = input("ENTER task description: ")
                    state = input("ENTER task state: ")
                    update_full_task(task_id, date, deadline, task, description, state)
                elif choice == "2":
                    task_id = int(input("Eneter task ID: "))
                    deadline = input("ENTER new deadline: ")
                    update_deadline_task(task_id, deadline)
                elif choice == "3":
                    task_id = int(input("Eneter task ID: "))
                    task = input("ENTER new task name: ")
                    update_task_task(task_id, task)
                elif choice == "4":
                    task_id = input("Enter task ID: ")
                    description = input("ENTER new task description: ")
                    update_description_task(task_id, description)
                elif choice == "5":
                    task_id = int(input("Eneter task ID: "))
                    state = input("ENTER new task state: ")
                    update_state_task(task_id, state)
                elif choice == "6":
                    break
                else:
                    print("INVALID CHOICE!")

        elif choice == "4": #Delete task
            task_id = int(input("Eneter task ID: "))
            delete_task(task_id)
        elif choice == "5": #Summary
            task_summary()
        elif choice == "6":# Exit
            break
        else:
            print("INVALID CHOICE, TRY AGAIN")

if __name__ == "__main__":
    menu()