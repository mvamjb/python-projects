products = {"5001":{"name":'Mouse',"quantity":50}}

def restock():
    id = input("Enter product id to restock: ").strip()
    while True:
        try:
            quantity = int(input("Enter quantity to add: "))
            break
        except ValueError:
            print("Wrong input!")
    flag = False
    for prod in products:
        # for tid in prod:
        if prod == id:
            products[prod]['quantity'] += quantity
            print(f"{products[prod]['name']} Restocked.")
            flag = True
    if flag == False:
        name = input("Enter product name: ").strip()
        temp = {
            id : {'name':name,'quantity':quantity}
        }
        products.update(temp)
def sell():
    id = input("Enter product id to sell: ").strip()
    while True:
        try:
            quantity = int(input("Enter amount to be subtract: "))
            break
        except ValueError:
            print("Wrong input")
    flag = False
    for prod in products:
        if prod == id:
            flag = True
            if products[prod]['quantity'] >= quantity:
                products[prod]['quantity'] -= quantity
            else:
                print("Error!")
    if flag == False:
        print(f'No product with id: "{id}" found')
def view():
    if products:
        for index,item in enumerate(products,start = 1):
            print(f'{index}. ID: {item} | Name: {products[item]['name']} | Quantity: {products[item]['quantity']}')
    else:
        print("No items to show")

while True:
    action = input(f"[R]estock [S]ell [V]iew [E]xit\n> ").strip().lower()
    if action == 'r':
        restock()
    elif action == 's':
        sell()
    elif action == 'v':
        view()
    elif action == 'e':
        break
    else:
        print("Wrong input!")


