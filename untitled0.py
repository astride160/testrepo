# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:12:10 2023

@author: Astride
"""
# print("Hello world")
# print("Hello world"*10)

# Name = "John Smith"
# Age = "20"
# patient = "new patient"

# print(Name + " is " + Age + " years old and is a " + patient) 

# name = input("What is your name? ")
# colour = input("What is your favourite colour? ")
# print(name +" likes " + colour)

# pounds= input("What is your weight in pounds? ")
# kg = int(pounds) * 0.453
# print("your weight in kg is " + str(kg) + " kg")

# print(Name[0:7])
# Name = Name[0:5].replace('h', 'p')
# print(Name) 


# price = 1000000
# good_credit = True

# if price:
#     down_payment = 0.1*price
# else:
#     down_payment = 0.2*price
    
# print(f"Down payment: {down_payment}")
    
#%%
number = 12
i= 0
while i < 3:
    Guess = int(input('Guess: '))
    i = i + 1 
    if Guess == number:
        print('You won!')
        break
else:
    print('Sorry, you Failed!')

       
Menu = input('menu: ')
if Menu == 'help' or 'Help':
    print('''
          start - to start the car
          stop- to stop the car
          quit- to exit
          ''')
elif Menu == 'start' or 'Start':
    print('start - to start the car')
elif Menu == 'stop' or 'Stop':
    print('stop- to stop the car')
elif Menu == 'quit' or 'Quit':
    print('quit- to exit')
else:
    print("I don't understand that")









