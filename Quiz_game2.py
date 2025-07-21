questions = [{'question':'What colour is the sky?','options': ['Blue','Green','Red','Yellow'],'correct_index':0},{'question':'First alphabet on keyboard?','options': ['W','R','E','Q'],'correct_index':3},{'question':'What is takes to build a unicorn?','options': ['Luck','Hard Work','Grit','Obsession'],'correct_index':3},{'question':'Elons is ','options': ['Gay','Straight','Bisexual','trans'],'correct_index':1},{'question':'Who is OpenAI Ceo?','options': ['Sam','Elon','Warren','Charlie'],'correct_index':0},{'question':'Where did warren buffet studied under graham?','options': ['Harvard','Columbia','Standford','UCberkely'],'correct_index':1}]


marks = 0
for qs in questions:
    print(qs['question'])
    print(f'A. {qs['options'][0]}\nB. {qs['options'][1]}\nC. {qs['options'][2]}\nD. {qs['options'][3]}')
    while True:
        ans = input("> ").lower()
        if ans in ('a','b','c','d'):
            break
        print("Wrong input! Enter again.")
    ans = ord(ans) - 97
    if ans == qs['correct_index']:
        marks += 1

print(f"You got {marks} out of {len(questions)} correct!")
    
