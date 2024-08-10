import prompt


def run_game(game_type):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    MAX_ROUNDS = 3
    correct_answers = 0
    print(game_type.DESCRIPTION)
    while correct_answers < MAX_ROUNDS:
        question, correct_answer = game_type.get_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f'{user_answer} is wrong answer ;(.'
                  f'Correct answer was {correct_answer}.')
            print(f'Let\'s try again, {name}!')
            break
    if correct_answers == 3:
        print(f'Congratulations, {name}!')
