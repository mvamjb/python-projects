import random

tasksinfo = []

def addtask():
    des = input("Enter short description: ")
    def make_unique_id():
        while True:
            uid = random.randint(0,101)
            if all(task['id'] != uid for task in tasksinfo):
                return uid
    temp = {
        'id' : make_unique_id(),
        'description' : des,
        'completed' : False
    }
    tasksinfo.append(temp)
    print("Task added!")
def viewtask():
    if not tasksinfo:
        print("No tasks to show.")
        return
    for task in tasksinfo:
        status = "Done" if task['completed'] else "Pending"
        print(f"ID: {task['id']} | DESCRIPTION: {task['description']} | STATUS: {status}")
def taskstatus():
    try:
        tid = int(input("Enter task id: "))
    except ValueError:
        print("Invalid iD.")
        return
    for task in tasksinfo:
        if task['id'] == tid:
            task['completed'] = True
            print("Task marked as completed")
            return
    print("ID not found.")
def deletetask():
    try:
        tid = int(input("Enter task id: "))
    except ValueError:
        print("Invalid ID.")
        return
    for task in tasksinfo:
        if task['id'] == tid:
            tasksinfo.remove(task)
            print("Task deleted.")
            return
    print("ID not found.")

# Main loop
while True:
    action = input("[A]DD [V]IEW [M]ARK [D]ELETE [E]XIT\n> ").strip().upper()
    if action == 'A':
        addtask()
    elif action == 'V':
        viewtask()
    elif action == 'M':
        taskstatus()
    elif action == 'D':
        deletetask()
    elif action == 'E':
        print("Goodbye!")
        break
    else:
        print("Wrong input! Enter again.")
