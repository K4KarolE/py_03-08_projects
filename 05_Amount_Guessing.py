# Amount Guessing Game - input validation

import random
from tkinter.messagebox import YES

print()
answer = input('Are you ready for playing?\n')

if answer.lower() != 'yes':
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
    try: 
        answer = int(input('Guess the amount of characters: '))
    except ValueError:
        print('Invalid answer')
        continue
    else:
        break
score = targetnumber - int(answer)

print()

# 2nd PLAY
targetnumber2nd = random.randrange(600,800)
charset = list(set(characterlist))
character = charset[2]   
characterlist.remove(charset[2])

print(character * targetnumber2nd)


while True:
    try: 
        answer = int(input('Guess the amount of characters: '))
    except ValueError:
        print('Invalid answer')
        continue
    else:
        break
score = score + (targetnumber2nd - int(answer))


print()

# 3rd PLAY
targetnumber3rd = random.randrange(900,1200)
charset = list(set(characterlist))
character = charset[2]   
characterlist.remove(charset[2])

print(character * targetnumber3rd)


while True:
    try: 
        answer = int(input('Guess the amount of characters: '))
    except ValueError:
        print('Invalid answer')
        continue
    else:
        break
score = score + (targetnumber3rd - int(answer))





print()
print()

allchar = targetnumber + targetnumber2nd + targetnumber3rd
print('Your score: ' + str(allchar - score) + '/' + str(allchar))

print()