questions = [
    { "q": "What is 2 + 2?", "choices": ["3", "4", "5"], "answer": "4" },
    { "q": "What is the capital of France?", "choices": ["Paris", "Rome", "Berlin"], "answer": "Paris" },

]


def ask_question(q_dict:dict) -> bool:
    """
    Display one question with choices, primpt until valid choice is selected,
    and returns true if correct, else false.
    """
    print('\nQuestion:',q_dict['q'])
    for index,n in enumerate(q_dict['choices'],start = 1):
        print(f"{index}. {n}")
    while True:
        while True:
            try:
                answer = int(input("Enter your answer: ").strip())
                break
            except ValueError:
                print("The value must be a number.")
        if 0 < answer <= len(q_dict['choices']):
            break
        else:
            print("Please choose one of the listed options.")
    return q_dict['choices'][answer-1] == q_dict['answer']


def run_quiz(question_list):
    "Iterate through questions, tallying and printing the finals score."
    score = 0
    for question in question_list:
        status = ask_question(question)
        if status:
            score += 1
    print(f"\nYou got {score} out of {len(question_list)}")


run_quiz(questions)