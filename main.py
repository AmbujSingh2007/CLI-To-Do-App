import json
import os

def load_task():
    if os.path.exists("tasks.json"):
        with open("tasks.json",'r') as f:
            return json.load(f)
    else:
        return []
    

def task_list_afterload():
    Temp_Task=load_task()
    print(Temp_Task)
    for data in Temp_Task:
        print("Task ID:",data["id"])
        print("Task Name:",data["task_name"])
        print("Task Status:",data["status"])


#Our Main User Interface
def menu():
    print("------Welcome , Here Are Your Options Listed Below:----------")
    print("(1) Add Task")
    print("(2) Remove Task")
    print("(3) View Task")
    print("(4) Update Task Status")
    print("--------------------------------------------------------------")
    while True:
        choice = input("Enter Your Choice: ")
        if choice in ["1", "2", "3", "4"]:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1–4.")

#Main Body
def main():
    choice=menu()
    if choice==3:
        task_list_afterload()
#test
while True:
    main()