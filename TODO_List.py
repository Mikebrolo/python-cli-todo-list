import time
import os
import json

_list = []

script_directory = os.path.dirname(__file__)
save_file_dir = os.path.join(script_directory, "file.json")

def options():
    clear()
    print("Welcome to the TODO list")
    time.sleep(1)
    print("What would you like to do?")
    print("""1. See your list
2. Add to your list
3. Remove from your list
4. Delete All Tasks     
5. Complete A Task          
6. Exit          """)

    choice = input("> ")

    if choice == "1":
        displayTODO(True)
    elif choice == "2":
        addToList()
    elif choice == "3":
        removeFromList()
    elif choice == "4":
        deleteAllTasks()
    elif choice == "5":
        completeTask()
    elif choice == "6":
        closeProgram()
    else:
        print("Not a valid input")
        time.sleep(1)
        options()

def addToList():
    print("What would you like to add?")
    _addition = input("> ")
    
    _list.append({"task": _addition, "completion": ' '})
    time.sleep(0.5)
    print("Successfully added task!\n")
    displayTODO()
    
    print("Do you want to add more?")
    _confirm = input("y/n > ")
    if _confirm == "y":
        addToList()
    elif _confirm == "n":
        options()
    else:
        print("Not a valid input")
        addToList()

def displayTODO(goHome = False):
    clear()
    print("----------TODO LIST----------\n")
    iteration = 0
    for task in _list:
        print(f"{iteration}. {task['task']} [{task['completion']}]")
        iteration += 1
    
    if goHome:
        print("\nGo home?")
        choice = input("y/n > ")
        if choice == 'y':
            options()
        elif choice == 'n':
            displayTODO(True)
        else:
            print("Not a valid input")
            time.sleep(1)
            options()

def removeFromList():
    print("What would you like to remove from your list?")
    
    displayTODO()

    print("\nType 'exit' to leave!")
    _subtraction = input("\nEnter number > ")
    
    try:
        print(f"Are you sure you want to remove {_list[int(_subtraction)]['task']}?")
    except:
        if len(_list) == 0:
            print("List is empty....")
            time.sleep(1)
            options()
        else:
            print("Not a valid form of input, please enter a number")
            time.sleep(1)
            removeFromList()
    confirmation = input("y/n > ")
    
    if confirmation == "y":
        _list.remove(_list[int(_subtraction)])
    elif confirmation == "n":
        removeFromList()
    elif confirmation.lower() == "exit":
        options()
    else:
        print("Not a valid input")
        removeFromList()
    options()

def deleteAllTasks():
    _list.clear()
    print("Successfully Removed All Tasks!!")
    time.sleep(1.5)
    displayTODO(True)

def completeTask():
    print("Which task do you want to tick off?")
    displayTODO()
    choice = input("> ")
    
    print("\nType 'exit' in order to leave !!\n")

    try:
        _list[int(choice)]["completion"] = 'X'
        print("Successfully Completed Task!!")
        time.sleep(2)
    except:
        print("Not a valid input...")
        time.sleep(1)
        completeTask()
    
    if choice.lower() == 'exit':
        options()

    displayTODO(True)
  
def saveToFile():
    with open(save_file_dir, "w+") as file:
        json.dump(_list, file)

def loadFromFile():
    global _list
    if os.path.exists(save_file_dir):
        with open(save_file_dir, 'r') as file:
            _list = json.load(file)

def closeProgram():
    print("Closing and saving the list....")
    time.sleep(1)
    saveToFile()
    time.sleep(1)
    exit()

def clear():
    os.system('cls')

loadFromFile()
options()
