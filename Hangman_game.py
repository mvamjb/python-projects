WORDS = ["PYTHON", "JAVASCRIPT", "VARIABLE",'OPENAI','ALEXANDER','CODING','BOOK','MIRROR','PANTS','SHOPIFY','SOCIALS','CHAIR','PAGANI','PORSCHE','CARPOOL','SWITZERLAND','SANFRANCISCO','SILICON','NVIDIA','JENSEN']
import random

def choose_word(words:list[str]):
    return random.choice(words)
def display_progress():
    for x in range(0,len(secret)):
        if secretbool[x] == True:
            print(secret[x],'',end ='')
        else:
            print("_ ",end = '')
    print()
    print()
def update_reveled(guess:str):
    index = 0
    global tries
    if guess in secret :
        print("Good guess!")
        for item in secret:
            if item == guess:
                secretbool[index] = True
            index += 1  
    else:
        tries = tries - 1
        print(f"Wrong! {tries} tries left")
def is_word_complete():
    count = 0
    for item in secretbool:
        if item == True:
            count += 1
    if count == len(secret):
        print("YOU Won!")
        return None
    else:
        return 1


secret = choose_word(WORDS)
secretbool = []
guessed_letter = []
for x in range(0,len(secret)):
    secretbool.append(False)


tries = len(secret)*(2)
print(f"Welcome to hangman! You have {tries} wrong guesses allowed")
print()
display_progress()
while True:
    status = is_word_complete()
    if status == None:
        break
    if tries == 0:
        print("You lost!")
        print("The word was:",secret)
        break
    while True:
        letter = input("Enter a letter: ").strip().upper()
        if len(letter) == 1:
            if letter not in guessed_letter:
                guessed_letter.append(letter)
                break
            else:
                print("You already tried that letter!")
        else:
            print("Wrong input!")
    update_reveled(letter)
    display_progress()     
    print("Wrong guesses:", [l for l in guessed_letter if l not in secret])