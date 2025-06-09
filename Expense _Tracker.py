def add():
    category = input("Enter category: ").lower().strip()
    if category not in expense:
        print("Enter Category from one of these: Rent/transport/food")
        return
    else:        
        try:
            amount = int(input("Enter amount: "))
        except ValueError:
            print("Amount should be in numbers. Not added ")
            return
        expense[category] += amount
def edit(value):
    category = input("Enter Category: ")
    if value == 'remove':
        expense.pop(category,"Not Found")
    elif value == 'edit':
        try:
            amount = int(input("Enter new amount: "))
        except ValueError:
            print("Amount should be in numbers")
        expense.update({category:amount})
    else:
        print("Wrong input.Try again")
def display():
    total = 0
    print("Total spent per category: ")
    for item in expense:
        print(f"Category: {item} | Amount = {expense[item]}")
        total = total + expense[item]

    print("Total:",total)

expense = {
    'food': 0,
    'rent': 0,
    'transport': 0
}


while True:
    action = input("Add/Remove/Edit/list/Quit? ").strip().lower()
    if action == 'add':
        add()
    elif action == 'remove' or action == 'edit':
        edit(action)
    elif action == 'list':
        display()
    elif action == 'quit':
        break
    else:
        print("Wrong input!")
        