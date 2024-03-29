# -*- coding: utf-8 -*-
"""todo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YMSeVdPy2gqSomWmJneZikOLeFNdnJ_c
"""

tasks=[]
def addTask():
    task=input("please enter a task:")
    tasks.append(task)
    print(f"Task '{task}'' added to the list.")
def listTasks():
    if not tasks:
        print("there are no tasks currently.")
    else:
        print("current tasks:")
        for index,task in enumerate(tasks):
            print(f"task #{index}. {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete =int(input("Enter the # to delete:"))
        if taskToDelete >=0 and taskToDelete <len(tasks):
            tasks.pop(taskToDelete)
            print(f"task {taskToDelete} has been removed.")
        else:
            print(f"task #{taskToDelete} was not found .")
    except:
        print("invalid input.")
if __name__ == "__main__":
    print("Welcome to the to do list app:)")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice=input("enter your choice:")
        if(choice=="1"):
            addTask()
        elif (choice == "2"):
            deleteTask()
        elif (choice == "3"):
            listTasks()
        elif (choice == "4"):
            break
        else:
            print("invalid input.please try again.")

    print("goodbye")