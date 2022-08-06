import random

print('\t***Welcome To Word Guessing Game !!!***')

name = input('\nWhat is your name?\n')

print('Good luck ' + name + '!, you have only 3 chances.')


words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

guess = random.choice(words)

#just added this print statement to test my code xd
#print(guess)

count = 0
while count < 3:
	count += 1

	wr = input('\nChoose a word:\n')

	if wr == guess:
		print('Congrats, you did it !!!')
		break
   
	elif count == 1 and wr != guess:
		print('Nope, try again!!!')

	elif count == 2 and wr != guess:
		print('babe, try harder !!!')
	
	elif count == 3 and wr != guess:
		print('Sorry, you have exceeded your chances\nGood luck next time!!!')