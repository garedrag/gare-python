# -*- coding: utf-8 -*-
#print ('Welcome to the text game')
#name = raw_input('Enter your name: ')
#while len(name) == 0 or not name.isalpha():
 #   print ("You don't fool me")
 #   name = raw_input('Enter your name: ')
#else:
 #   if len(name) > 0 and name.isalpha():
  #    print ("Hello", name)
   # else:
    #  quit(1)
#year = input('How old arr you? ')
#if year >= 8:
 #   if year >= 99:
 #     print ("You too old for this game")
  #    quit(1)
#elif year <= 18:
 #     print ("You too yang for this game")
  #    quit()
#elif year.isalpha():
 #   print ("Something wrong with your age ")
  #  year = input('How old arr you? ')
#else:
 #     print ("Samsing wrong with you age ")
  #    year = input('How old arr you? ')
#print("Ok")
import random
#lst = []
#for x in range(0, 6):
#  b = random.choice(['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']) + random.choice([' Clubs', ' Diamonds', ' Hearts', ' Spades'])
#print lst
n = 1
#def card():
#   n = 1
result = []
while n <= 6:
      n += 1
      result[:0] = random.choice(['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']) + random.choice([' Clubs', ' Diamonds', ' Hearts', ' Spades'])  # see below
print result


#print (n)




#print ('''Thank's for you chois''', name)
