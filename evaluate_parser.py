# TODO: Refactor repeated operand-finding loops into helper functions later.
# This is v1.0 of the expression evaluator; improvements (unary minus, decimal parsing, new operators) will come in later versions if i get the time.


def evaluate(expression):
    parts = expression.split()
    parts = "".join(parts)
    try:
        left = parts.rindex("(")
        right = parts.index(")",left)   
        mini = parts[left+1:right]
        result = compute_simple(mini)
        newtext = parts[0:left] + str(result) + parts[right+1:]
        if newtext.count("(") == 0:
            print("Answer:",compute_simple(newtext))
            return
        else:
            evaluate(newtext)
    except ValueError:
        parts = "(" + parts + ")"
        evaluate(parts)
    


def compute_simple(sub):
    sub = sub.split()
    sub = "".join(sub)
    for item in sub:
        if item == '/':
            place = sub.index(item)
            count = 0
            while True:
                count += 1
                try:
                    if (place - count) >= 0:
                        lefts = sub[place - count]
                    else:
                        break
                except IndexError:
                    break
                if lefts != '*' and lefts != '+' and lefts != '-' and lefts != '':
                    leftindex = place  - count
                else:
                    break
            count = 0
            while True:
                count += 1
                try:
                    rights = sub[place + count]
                except IndexError:
                    break
                if rights != '/' and rights != '*' and rights != '+' and rights != '-' and rights != '':
                    rightindex = place + count
                else:
                    break
            try:
                result = float(sub[leftindex:place]) / float(sub[place+1:rightindex+1])
            except ZeroDivisionError:
                text = ("ZeroDivisionError")
                return text
            sub = sub[0:leftindex] + str(result) + sub[rightindex+1:]
    if "/" not in sub:
        for x in sub:    
            if x == '*':
                place = sub.index(x)
                count = 0
                while True:
                    count += 1
                    try:
                        if (place - count) >= 0:
                            lefts = sub[place - count]
                        else:
                            break
                    except IndexError:
                        break
                    if lefts != '/' and lefts != '+' and lefts != '-' :
                        leftindex = place  - count
                    else:
                        break
                count = 0
                while True:
                    count += 1
                    try:
                        rights = sub[place + count]
                    except IndexError:
                        break
                    if rights != '*' and rights != '/' and rights != '+' and rights != '-' and rights != '':
                        rightindex = place + count
                    else:
                        break
                result = float(sub[leftindex:place]) * float(sub[place+1:rightindex+1])
                sub = sub[0:leftindex] + str(result) + sub[rightindex+1:]
    if "*" not in sub:
        for y in sub:    
            if y == '+':
                place = sub.index(y)
                count = 0
                while True:
                    count += 1
                    try:
                        if (place - count) >= 0:
                            lefts = sub[place - count]
                        else:
                            break
                    except IndexError:
                        break
                    if lefts != '/' and lefts != '*' and lefts != '-':
                        leftindex = place  - count
                    else:
                        break
                count = 0
                while True:
                    count += 1
                    try:
                        rights = sub[place + count]
                    except IndexError:
                        break
                    if rights != '*' and rights != '/' and rights != '+' and rights != '-' and rights != '':
                        rightindex = place + count
                    else:
                        break
                result = float(sub[leftindex:place]) + float(sub[place+1:rightindex+1])
                sub = sub[0:leftindex] + str(result) + sub[rightindex+1:]
    if "+" not in sub:
        for z in sub:    
            if z == '-':
                place = sub.index(z)
                count = 0
                while True:
                    count += 1
                    try:
                        if (place - count) >= 0:
                            lefts = sub[place - count]
                        else:
                            break
                    except IndexError:
                        break
                    if lefts != '/' and lefts != '*' and lefts != '+':
                        leftindex = place  - count
                    else:
                        break
                count = 0
                while True:
                    count += 1
                    try:
                        rights = sub[place + count]
                    except IndexError:
                        break
                    if rights != '*' and rights != '/' and rights != '+' and rights != '-' and rights != '':
                        rightindex = place + count
                    else:
                        break
                result = float(sub[leftindex:place]) - float(sub[place+1:rightindex+1])
                sub = sub[0:leftindex] + str(result) + sub[rightindex+1:]
    return sub




i = input("Enter Expression: ")
evaluate(i)
# compute_simple(i)