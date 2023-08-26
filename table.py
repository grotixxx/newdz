import random

score = 0

while True:
    x = random.randint(1, 9)
    y = random.randint(1, 9)

    user_input = input(f'Введи {x} * {y} = ')

    if str(user_input).lower() == 'exit':
        print(f'Ти набрав {score} балів, вітаю!')
        exit()
    elif int(user_input) == x * y:
        print('Вірно!')
        score += 1
    else:
        print(f'Невірно, правильна відповідь була на цей приклад {x} * {y} = {x * y}')
        score -= 1