import random

puzzle_num = random.randint(10, 99)
guess = input('Please guess a number between 10 and 99: ')
if int(guess) < 10 or int(guess) > 99:
    print('The number is not between 10 and 99. You lose!')
    exit()
if guess == str(puzzle_num):
    print('You got it! You win $10,000')
else:
    c  = 0
    for d in guess:
        if d in str(puzzle_num):
            c += 1
    if c == 0:
        print('No digits match. You lose!')
    elif c == 1:
        print('One digit matches. You win $1,000!')
    elif c == 2:
        print('Two digits match. You win $3,000!')
    print('The correct number was ' + str(puzzle_num))