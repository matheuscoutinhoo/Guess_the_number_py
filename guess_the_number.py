from random import randint

init = input('Would you like to play a game (y/n)? ').lower()
init = init.strip()

num = randint(1,50)
print(num)

while True:
    if init == 'y':
        guess = int(input('Guess a number from 1 to 50: '))
        if guess < num:
            print('Very low.')
            repeater = input('Would you like to play again (y/n)? ').strip()
            repeater.lower()
            if repeater == 'y':
                guess = int(input('Guess a number from 1 to 50: '))
            else:
                print('Thanks for playing.')
                break
        elif guess == num:
            print('Congratulations! You guessed right!')
            repeater = input('Would you like to play again (y/n)? ').strip()
            repeater.lower()
            if repeater == 'y':
                guess = int(input('Guess a number from 1 to 50: '))
            else:
                print('Thanks for playing.')
                break
        elif guess > num:
            print('Very high.')
            repeater = input('Would you like to play again (y/n)? ').strip()
            repeater.lower()
            if repeater == 'y':
                guess = int(input('Guess a number from 1 to 50: '))
            else:
                print('Thanks for playing.')
                break
        else:
            print('Thanks for playing.')
            break
        
    
