from random import randrange
from time import sleep

y= input('Enter Your Name')
x= y.upper()
a=[]
empty_character=''
for i in x:
    while True:
        random_char=chr(randrange(65,90))
        print('\r'+empty_character + random_char )
        sleep(0.4)
        if random_char==i:
            empty_character=empty_character+random_char
            break
