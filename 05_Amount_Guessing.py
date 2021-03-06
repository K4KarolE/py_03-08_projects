# Amount Guessing Game - input validation
# In 3 rounds it will display random amount* of characters and you have to guess the quantity
# * = from a range which is increasing after every round (1nd, 2nd)
# Displaying your points / %

import random

print()
answer = input('Are you ready for playing?\n')

if answer.lower() != 'yes':
    print('Bye!\n')
    quit()

print()



#Character/Caharacterlist
characterlist = ['¬', '£', '$', '%', '&', '#', '@', '?', '=', '+']

charset = list(set(characterlist))                       # set(it is a list type) = data is randomly placed 

character = charset[2]                                   # any number-> position -> character -the list is randomly generated, pls see previous comment



# 1st PLAY
targetnumber = random.randrange(300,500)
print(character * targetnumber)
characterlist.remove(charset[2])                          # removing the used character from the list

while True:
    answer = input('Guess the amount of characters: ')
    if answer.isdigit(): 
        answer = int(answer)
    else:
        print('Invalid answer')
        continue
    if answer == 0:
        print('Invalid answer')
        continue
    break
        
score = targetnumber - answer

print()



# 2nd PLAY
targetnumber2nd = random.randrange(600,800)
charset = list(set(characterlist))
character = charset[2]   
characterlist.remove(charset[2])

print(character * targetnumber2nd)

while True:
    answer = input('Guess the amount of characters: ')
    if answer.isdigit(): 
        answer = int(answer)
    else:
        print('Invalid answer')
        continue
    if answer == 0:
        print('Invalid answer')
        continue
    break

score = score + (targetnumber2nd - answer)

print()



# 3rd PLAY
targetnumber3rd = random.randrange(900,1200)
charset = list(set(characterlist))
character = charset[2]   
characterlist.remove(charset[2])

print(character * targetnumber3rd)

while True:
    answer = input('Guess the amount of characters: ')
    if answer.isdigit(): 
        answer = int(answer)
    else:
        print('Invalid answer')
        continue
    if answer == 0:
        print('Invalid answer')
        continue
    break

score = score + (targetnumber3rd - answer)



print()
print()

allchar = targetnumber + targetnumber2nd + targetnumber3rd
percent = (allchar - abs(score)) / allchar
percentprint = format( percent, '.2%')
print('Your score: ', allchar - abs(score), '/', allchar,  ' - ', percentprint)

print()

print('Thx for playing!')

print()
