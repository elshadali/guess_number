import random


number = random.randint(1, 100)
guess_number = int(input('Guess the number: '))

while guess_number != number:
    
    guess_number = int(input('Guess the number: '))

    if guess_number < number:
        print('More')
    elif guess_number > number:
        print('Less')
    else:
        break
    
print('You won!')

        