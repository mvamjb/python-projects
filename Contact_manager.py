contact = []


def add_contact():
    name = input("Enter name: ").strip().capitalize()
    phone = input("Enter phone number: ").strip()
    while True:
        email = input("Enter email: ").strip()
        if '@' in email: 
            break
        else:
            print("Wrong email!")
    temp = {
        'name':name,
        'phone':phone,
        'email':email
    }
    contact.append(temp)
def search_contact():
    flag = False
    sh = input("Enter search string: ")
    for items in contact:
        if items['name'].lower() == sh.lower() or items['phone'] == sh or items['email'].lower() == sh.lower():
            print(f'Name: {items['name']} | phone: {items['phone']} | email: {items['email']}') 
            flag = True
    if flag == False:
        print("No match found")
def delete_contact():
    key = input("Enter name or phone of the contact to be removed: ").strip().capitalize()
    for items in contact:
        if items['name'].lower() == key.lower() or items['phone'] == key:
            contact.remove(items)
            print("Removed")
            break
    else:
        print("Not found")
def list_all():
    for items in contact:
        print(f'Name: {items['name']} | phone: {items['phone']} | email: {items['email']}') 

while True:
    action = input("Add/Search/Delete/list/Quit? ").strip().lower()
    if action == 'add':
        add_contact()
    elif action == 'search':
        search_contact()
    elif action == 'delete':
        delete_contact()
    elif action == 'list':
        list_all()
    elif action == 'quit':
        break
    else:
        print("Wrong input")
