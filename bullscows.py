""""
bullscows.py: Second project to Engeto Online Python Academy
author: Martin Mannsbarth
email: mann.m@seznam.cz
discord: Martin M.#4226
"""

# import libraries
import random
import sys

# delimeter
delimeter = "-" * 64

#function bull/bulls
def bull_s(bull_cow):
    if bull_cow[0] == 1:
        bull = "bull"
        return bull
    else:
        bull = "bulls"
        return bull

# function cow/cows
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
    print(num_dup)
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
     
# generate number for guess purpose
    num = generate_number()
    counter = 0
    guess =int(input('Enter number of attempts for guess: '))
    while guess > 0:
# insert user attempt and verify that match conditions - no duplicates, 4 digits, don´t start with 0
         attempt = input("Enter a number for guess: ")
         while (attempt.isdigit() and int(len(attempt)) == 4 and (9999 > int(attempt) > 1000) and (no_duplicates(attempt) == True)) == False:
             if attempt.isdigit() == False:
                 print("Please enter number from range, your enter:\"", attempt,"\".use number in range 1000-9999.")
             elif int(len(attempt)) != 4:
                 print("Please enter longer number, your enter: \"",attempt,"\" and it is out of range 1000-9999.")
             elif (9999 > int(attempt) > 1000) == False:
                 print("Please number in ranger, your enter: \"",str(attempt),"\"and it is out of range 1000-9999.")
             elif no_duplicates(attempt) == False:
                 print("Number should not have repeated digits.")
             attempt = input("Enter a number: ")
         
         bull_cow = num_bulls_cows(num,attempt)
         bull = bull_s(bull_cow)
         cow = cow_s(bull_cow)
         print(f"{bull_cow[0]} {bull}, {bull_cow[1]} {cow}.")
         print(delimeter)
         counter += 1
         guess -=1
         
         if bull_cow[0] == 4 and counter < 6:
             print("Success,it is right nunber! Great performance!")
             print(delimeter)
             break
         elif bull_cow[0] == 4 and 6 <= counter <= 12:
             print("Success,it is right nunber! That's not bad!")
             print(delimeter)
             break
         elif bull_cow[0] == 4 and counter > 12:
             print("Success,it is right nunber! Pretty weak")
             print(delimeter)
             break
         
    else:
        print(f"Game over. All tipping attempts exhausted. Number was {num}.\n{delimeter}")
         
     
def option2():
     print('Simple manual for game')

def option3():
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
        #Check what choice was entered and act accordingly
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