import json
import os

#moves current path to the folder in which main.py is located
if os.path.basename(os.getcwd()) != 'cli-to-do-app':
    if os.path.exists('cli-to-do-app'):
        os.chdir('cli-to-do-app')
FILENAME= "tasks.json"

def save_tasks(tasks):
    with open(FILENAME, 'w') as f:
        json.dump(tasks, f, indent=4)

def load_tasks():
    try:
        with open(FILENAME, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("\n--- No tasks found. ---")
        return tasks
    print("\n--- Your Tasks ---")
    for task in tasks:
        print(f"ID: {task['id']} | Name : {task['task_name']} | Task Status : {task['status']}")
    return tasks

def clear_tasks():
    temp_data = [] 
    save_tasks(temp_data)
    print("All Your Tasks Have Been Flushed!!")


def update_task():
    update=[]
    data=load_tasks()
    view_tasks()
    found= False
    tid=input("Enter Task ID for which you want to update Status:")
    for i in data:
        if int(i['id'])==int(tid):
            i['status'] = 'Completed'
            found=True
            break
    if found:
        save_tasks(data)
    else:
        print("Task id is invalid try again.")

def add_task():
    tasks=load_tasks()
    print("-"*25)
    ntasks = int(input("Number of tasks you want to add: "))
    last_id = tasks[-1]['id'] if tasks else 0
    data={}
    for i in range(ntasks):
        new_id = last_id + i + 1
        name = input(f"Enter Name for Task {new_id}: ")
        data = {
            "id": new_id,
            "task_name": name, # Removed the extra colon from key
            "status": "Pending"
        }
        tasks.append(data)
    save_tasks(tasks)



#Our Main User Interface
def menu():
    print("\n" + "-"*10 + " To-Do Menu " + "-"*10)
    print("(1) Add Task")
    print("(2) Flush All Tasks")
    print("(3) View Tasks")
    print("(4) Update Task Status")
    print("(5) Exit")
    print("-" * 32)
    choice = input("Enter Your Choice: ")
    if choice in ["1", "2", "3", "4","5"]:
        return int(choice)
    else:
        print("Invalid choice. Please enter 1–5.")

#Main Body
def main():
    choice=menu()
    if choice==1:
        print('-'*50)
        add_task()
        print('-'*50)
    elif choice==2:
        print('-'*50)
        clear_tasks()
        print('-'*50)
    elif choice==3:
        print('-'*15)
        view_tasks()
        print('-'*50)
    elif choice==4:
        print('-'*50)
        update_task()
        print('-'*50)
    else:
        exit()
#test
while True:
    main()