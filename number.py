import random

mode = ['easy', 'medium', 'hard'][int(input('Вибери режим, 0 - легко, 1 - середнє, 2 - тяжко\n'))]

if mode == 'easy':
    secret = random.randint(1, 5)
elif mode == 'medium':
    secret = random.randint(1, 10)
else:
    secret = random.randint(1, 15)

attempts = 0

while True:
    if attempts == 3:
        print("Ти програв! Спробуй ще)")
        exit()

    user_input = int(input('Enter guess\n'))

    attempts += 1

    if user_input > secret:
        print('Багато!')
    elif user_input < secret:
        print('Мало(')
    elif user_input == secret:
        print(f'Ти вгадав з {attempts} спроби')
        exit()
