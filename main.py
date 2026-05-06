import json
import os
# 1. Get the directory where main.py is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Join that directory path with your filename
file_path = os.path.join(script_dir, 'tasks.json')

def load_task():
    with open("tasks.json",'r') as f:
        Temp_Task= json.load(f)
        print(Temp_Task)
        for data in Temp_Task:
            print("Task ID:",(int(data["id"]))+1)
            print("Task Name:",data["task_name"])
            print("Task Status:",data["status"])

def add_task():    
    with open("tasks.json",'a') as f:
        ntasks=int(input("Number Of Tasks You Want To Add::"))
        mydata=[]
        for i in range(ntasks):
            data= {"id": i,"task_name:":input("Enter Your Task Name:"),"status":"Pending"}
            mydata.append(data)
        Temp_Task= json.dump(mydata,f,indent=4)

#Our Main User Interface
def menu():
    print("------Welcome , Here Are Your Options Listed Below:----------")
    print("(1) Add Task")
    print("(2) Remove Task")
    print("(3) View Task")
    print("(4) Update Task Status")
    print("(5) Exit")
    print("--------------------------------------------------------------")
    while True:
        choice = input("Enter Your Choice: ")
        if choice in ["1", "2", "3", "4","5"]:
            return int(choice)
        else:
            print("Invalid choice. Please enter 1–5.")

#Main Body
def main():
    choice=menu()
    if choice==1:
        add_task()
    elif choice==3:
        load_task()
    elif choice==5:
        exit
#test
main()