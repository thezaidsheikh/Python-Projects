import random

print('''The Game is Started,
You have to guess the number 
between 0 to 20.
So please Enter the number ..''')

x = int(input("Enter the number between 0 to 20 :"))
randomNumber = random.randint(0,20)
print(randomNumber)
print('your guess is high') if x>randomNumber else print('your guess is correct') if x==randomNumber else print('your guess is low')



