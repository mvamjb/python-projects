pegA = [8,7,6,5,4,3,2,1]
pegB = []
pegC = []

def hanoi(n,start,end,helper):
    if n == 1:
        end.append(start.pop())
        return
    hanoi(n-1,start,helper,end)
    end.append(start.pop())
    hanoi(n-1,helper,end,start)
    print(end)



    

    

hanoi(5,pegA,pegC,pegB)