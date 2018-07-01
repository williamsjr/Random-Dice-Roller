import random

welcome = ''
yes_roll = 'r'
exit_roll = 'exit'
welcome_sum = 0
acum = 0

while welcome != 'exit':
    welcome = input("Roll the dice (press r to roll or type 'exit' to quit): ")
    if welcome == yes_roll.lower():
        welcome = random.randint(1, 6)
        print('You rolled: ', welcome)
        welcome_sum += welcome
        acum += 1
        avg = welcome_sum / acum
        print('Your average roll is: ', int(avg), '\n')
    elif welcome != yes_roll.lower() or welcome != exit_roll.lower():
        print('Incorrect key pressed')
    elif welcome == exit_roll.lower():
        print('Thanks for rolling!')

