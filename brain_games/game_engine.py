import prompt


def game_engine(game_rule, game_type):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    MAX_ROUNDS = 3
    correct_answers = 0
    print(game_rule)
    while correct_answers < MAX_ROUNDS:
        game_question, game_answer = game_type()
        print(f'Question: {game_question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == game_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f'{user_answer} is wrong answer ;(.'
                  f'Correct answer was {game_answer}.')
            print(f'Let\'s try again, {name}!')
            break
    if correct_answers == 3:
        print(f'Congratulations, {name}!')
