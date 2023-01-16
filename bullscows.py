""""
bullscows.py: Second project to Engeto Online Python Academy
author: Martin Mannsbarth
email: mann.m@seznam.cz
discord: Martin M.#4226
"""

# import libraries
import random
import sys

# delimeters
delimeter = "-" * 64
delimeter2 = "*" * 64

#function bull/bulls singular or plural
def bull_s(bull_cow):
    if bull_cow[0] == 1:
        bull = "bull"
        return bull
    else:
        bull = "bulls"
        return bull

# function cow/cows singular or plural
def cow_s(bull_cow):
    if bull_cow[1] == 1:
        cow = "cow"
        return cow
    else:
        cow = "cows"
        return cow

# generate number without duplicates, use
# for check function no_duplicates()
def generate_number():
    while True:
        num = random.randint(1000,9999)
        if no_duplicates(num):
            return num

# function returns list of digits
def get_digits(num):
    return [int(i) for i in str(num)]

# function checks duplicate for both numbers -
#  secret number and user guess
def no_duplicates(num):
    num_dup = get_digits(num)
 # for debug purpose possible print function run   
 #   print(num_dup)
 #   print(len(num_dup))
 #   print(len(set(num_dup)))
    if len(num_dup) == len(set(num_dup)):
        return True
    else:
        return False

def num_bulls_cows(num,attempt):
    bulls_cows = [0,0]
    gen_num = get_digits(num)
    attempt_num = get_digits(attempt)
    
# use built-in function zip() 
# function returns a zip object, which is an iterator of tuples
# where the first item in each passed iterator is paired together, 
# and then the second item in each passed iterator are paired together etc.  
    for gen,att in zip(gen_num,attempt_num):
          
# check digit present
        if att in gen_num:
          
# if digit exact match, plus bull
            if gen == att:
                bulls_cows[0] += 1
              
# if digit match but in incorrect position, plus cow
            else:
                bulls_cows[1] += 1
                 
    return bulls_cows

    
# menu construction
menu_options = {
    1: 'Play game',
    2: 'Manual',
    3: 'About',
    4: 'Exit',
}

# function print menu and offer options
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )
    print(delimeter)

def option1():
    print('Game started.')
     
# insert number for guess counter and attempt counter, check insert purpose
    num = generate_number()
    guess = 0
    counter = 0
    guess = input('Enter number of attempts for guess: ')
    while guess.isdigit() == False:
        guess = input('Enter number of attempts for guess: ')
        
    while int(guess) > 0:

# insert user attempt and verify that match conditions - no duplicates, 4 digits, don´t start with 0, no any character
         attempt = input("Enter a number for guess: ")
         while (attempt.isdigit() and int(len(attempt)) == 4 and
                (9999 > int(attempt) > 1000) and (no_duplicates(attempt) == True)) == False:
             if attempt.isdigit() == False:
                 print("Please enter number from range, your enter:\"", attempt,"\".use number in range 1000-9999.")
             elif int(len(attempt)) != 4:
                 print("Please enter longer number, your enter: \"",attempt,"\" and it is out of range 1000-9999.")
             elif (9999 > int(attempt) > 1000) == False:
                 print("Please number in ranger, your enter: \"",str(attempt),"\"and it is out of range 1000-9999.")
             elif no_duplicates(attempt) == False:
                 print("Number should not have repeated digits.")
             attempt = input("Enter a number: ")
         
# return count bulls, cows from function, check single/plural for words, attempts counter        
         bull_cow = num_bulls_cows(num,attempt)
         bull = bull_s(bull_cow)
         cow = cow_s(bull_cow)
         print(f"{bull_cow[0]} {bull}, {bull_cow[1]} {cow}.")
         print(delimeter)
         counter += 1
         guess = int(guess) -1
         
# verification and resolution for guess- great, no bad. weak...        
         if bull_cow[0] == 4 and counter < 6:
             print(f"Success,it is right nunber! Great performance!\nOnly {counter} attempts! End of game.")
             print(delimeter)
             break
         elif bull_cow[0] == 4 and 6 <= counter <= 12:
             print(f"Success,it is right nunber! That's not bad! {counter} attempts!")
             print(delimeter)
             break
         elif bull_cow[0] == 4 and counter > 12:
             print(f"Success,it is right nunber! Pretty weak guess - {counter} attempts.")
             print(delimeter)
             break
# out of attempts set when game start    
    else:
        print(f"Game over. All tipping attempts exhausted. Number was {num}.\n{delimeter}")
         
# print manual    
def option2():
    print(delimeter)
    print('Simple manual for game:\n')
    print("""
Bulls and Cows is a game usually played between 2 players.
In this, a player tries to guess a secret code number chosen
by the second player. 
The rules are as follows:      
1) A player will create a secret code, usually a 4-digit number.
2) This number should have no repeated digits.
3) Another player makes a guess (4 digit number) to crack the secret number.
   Upon making a guess, 2 hints will be provided- Cows and Bulls.
4) Bulls indicate the number of correct digits in the correct position and
   cows indicates the number of correct digits in the wrong position. 
   For example, if the secret code is 1234 and the guessed number is 1246 then
   we have 2 BULLS (for the exact matches of digits 1 and 2) and 1 COW (for the match
   of digit 4 in the wrong position)
5) The player keeps on guessing until the secret code is cracked.
   The player who guesses in the minimum number of tries wins.          
           """)
    print(delimeter)

# print info about author, contact
def option3():
    print(delimeter2)
    print('About - author details:')
    print(
"""
bullscows.py: Second project to Engeto Online Python Academy
type of program: text game
author: Martin Mannsbarth
email: mann.m@seznam.cz
discord: Martin M.#4226
"""
     )
    print(delimeter2)

# Run own program - choose a handle option
if __name__=='__main__':
    print("Welcome to the game Bulls and Cows.")
    print(delimeter)
    while(True):
        print("Choose your option from menu ->")
        print_menu()
        option = ''
        try:
            print(delimeter)
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
            
# Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('bye bye')
            sys.exit("exiting ...")
        else:
            print('Invalid option. Please enter a number between 1 and 4.')