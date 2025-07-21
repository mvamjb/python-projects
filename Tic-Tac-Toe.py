game = [[1,2,3],[4,5,6],[7,8,9]]
print("Welcome to the Tic-Tac-Toe Game!")
print()
def change(value:int,letter:str):
    for x in game:
        if x[0] == value:
            x[0] = letter
            break
        if x[1] == value:
            x[1] = letter
            break
        if x[2] == value:
            x[2] = letter
            break
    printing()
def printing():
    for x in game:
        print(f"{x[0]} | {x[1]} | {x[2]}")
        print("----------")
def check(playernum : int,letter:str):
    while True:
        try:
            player = int(input(f"Player {playernum} ({letter}) : "))
            if player in game[0] or player in game[1] or player in game[2]:
                return player
            print("Wrong Input! Enter again.")
        except ValueError:
            print("Wrong Input! Enter again.")
def is_draw():
    return all(isinstance(cell,str) for row in game for cell in row)
            


printing()
while True:
    player1 = check(1,"X")
    change(player1,"X")
    if ((game[0][0] == "X" and game[0][1] == "X" and game[0][2] == "X" ) or (game[1][0] == "X" and game[1][1] == "X" and game[1][2] == "X") or (game[2][0] == "X" and game[2][1] == "X" and game[2][2] == "X" )) or ((game[0][0] == "X" and game[1][0] == "X" and game[2][0] == "X") or (game[0][1] == "X" and game[1][1] == "X" and game[2][1] == "X") or (game[0][2] == "X" and game[1][2] == "X" and game[2][2] == "X")) or ((game[0][0] == "X" and game[1][1] == "X" and game[2][2] == "X") or (game[0][2] == "X" and game[1][1] == "X" and game[2][0] == "X")) :
        print("Player 1 Wins!")
        break
    if is_draw():
        print("Its a draw!")
        break
    player2 = check(2,"O")
    change(player2,"O")
    if ((game[0][0] == "O" and game[0][1] == "O" and game[0][2] == "O" ) or (game[1][0] == "O" and game[1][1] == "O" and game[1][2] == "O") or (game[2][0] == "O" and game[2][1] == "O" and game[2][2] == "O" )) or ((game[0][0] == "O" and game[1][0] == "O" and game[2][0] == "O") or (game[0][1] == "O" and game[1][1] == "O" and game[2][1] == "O") or (game[0][2] == "O" and game[1][2] == "O" and game[2][2] == "O")) or ((game[0][0] == "O" and game[1][1] == "O" and game[2][2] == "O") or (game[0][2] == "O" and game[1][1] == "O" and game[2][0] == "O")) :
        print("Player 2 Wins!")
        break
    if is_draw():
        print("Its a draw!")
        break

