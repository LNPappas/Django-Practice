###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

import random

def number():
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join([str(i) for i in digits[:3]])

def get_guess():
    return input("What is your guess? ")

def clues(num, guess):
    if num == guess:
        return "CODE CRACKED!"

    clue = []

    for index, value in enumerate(guess):
        if value == num[index]:
            clue.append("match")
        elif value in num:
            clue.append("close")

    if clue == []:
        return ['nope!']
    else:
        return clue




code = number()
print(code)
clue = []
print("I'm thinking of a 3 digit number...")
print("Can you guess what it is? \n")

while(clue != 'CODE CRACKED!'):
    guess = get_guess()
    clue = clues(code, guess)
    if type(clue) == list:
        for x in clue:
            print(x)

print(clue)
