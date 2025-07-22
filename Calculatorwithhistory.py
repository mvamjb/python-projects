history = []


while True:
    action = input("[C]alculation [H]istory [E]xit\n> ").lower()
    if action == 'c':
        while True:
            term = input("Enter the values (e.g. 5 / 2): ").strip()
            term = term.split()
            if len(term) == 3:
                break
            else:
                print("Wrong input!")
        if term[1] not in ("+","*","/","-"):
            print("Wrong operator!")
            continue
        try:
            firstdigit = int(term[0])
            seconddigit = int(term[2])
        except ValueError:
            print("Wrong input!")
            continue
        if term[1] == '/':
            if seconddigit == 0:
                print("Error! Cant divide by zero.")
            else:
                result = firstdigit / seconddigit
                temp = str(firstdigit) + " / " + str(seconddigit) + " = " + str(result)
                print(temp)
                history.append(temp)
        elif term[1] == '*':
            result = firstdigit * seconddigit
            temp = str(firstdigit) + " * " + str(seconddigit) + " = " + str(result)
            print(temp)
            history.append(temp)
        elif term[1] == '-':
            result = firstdigit - seconddigit
            temp = str(firstdigit) + " - " + str(seconddigit) + " = " + str(result)
            print(temp)
            history.append(temp)
        else:
            result = firstdigit + seconddigit
            temp = str(firstdigit) + " + " + str(seconddigit) + " = " + str(result)
            print(temp)
            history.append(temp)
    elif action == 'h':
        if history:
            for index,term in enumerate(history,start=1):
                print(f"{index}. {term}")
        else:
            print("Nothing to show!")
    elif action == 'e':
        break
    else:
        print("Wrong input")