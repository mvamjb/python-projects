def add_task(tasks: list[tuple[str,int]]) -> None:
    '''asks for task and its priority and add it to the to_do_list.
    priority must be a number, 1 being the highest priority'''
    description = input("Enter task description: ").strip()
    while True:
        try:
            priority = int(input("Enter priority (1=high, larger=lower): "))
            break
        except ValueError:
            print("Priority must be a number.")
    tasks.append((description,priority))


def mark_complete(tasks:list[tuple[str,int]]) -> None:
    '''takes index number from user and then removes tasks from that index in to_do_list.'''
    if len(tasks) == 0:
        print("No tasks available.")
    else:      
        while True:
            try:
                index = int(input("Enter task you have finished: "))
                if 1 <= index <= len(tasks):
                    break
                else:
                    print("No such task number.")
            except ValueError:
                print("Should be a number!")
        sortedtodo = sorted(tasks,key=lambda x : (x[1],x[0]))
        task = sortedtodo[index - 1]
        tasks.remove(task)
        print(f"\"{task[0]}\" marked complete.")


def view_tasks(tasks:list[tuple[str,int]]) -> None:
    '''print to_do_list in ascending order of priority.'''
    if len(tasks) == 0:
        print("No tasks available.")
    else:      
        newtodo = sorted(tasks,key= lambda x : (x[1],x[0]))
        index = 0
        for item in newtodo:
            index += 1
            print(f"{index}. [Priority {item[1]}] {item[0]}")

to_do_list = []

while True:
    action = input("Menu: [A]dd  [V]iew  [C]omplete  [E]xit  \n> ").strip().upper()
    if action == 'A':
        add_task(to_do_list)
        print()
    elif action == 'C':
        mark_complete(to_do_list)
        print()
    elif action == 'V':
        view_tasks(to_do_list)
        print()
    elif action == 'E':
        print("Goodbye!")
        break
    else:
        print("Wrong input!")