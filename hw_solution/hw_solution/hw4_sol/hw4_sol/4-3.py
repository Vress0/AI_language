import random
puzzle_num = random.randint(0, 100)
while(1):
    guess = eval(input('Please guess a number between 0 and 100: '))
    if int(guess) < 0 or int(guess) > 100:
        print('The number is not between 0 and 100. You lose!')
        exit()
    if guess == puzzle_num:
        print('You got it! You win!')
        break
    elif guess > puzzle_num:
        print('please guess a smaller number.')
    elif guess < puzzle_num:
        print('please guess a larger number.')
        
    