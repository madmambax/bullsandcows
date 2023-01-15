# import libraries
import random
import sys

# function returns list of digits
def get_digits(num):
    return [int(i) for i in str(num)]

# function checks duplicate for both numbers -
#  secret number and user guess
def no_duplicates(num):
    num_dup = get_digits(num)
 # for debug purpose   
 #   print(num_dup)
 #   print(len(num_dup))
 #   print(len(set(num_dup)))
    if len(num_dup) == len(set(num_dup)):
        return True
    else:
        return False
    

menu_options = {
    1: 'Play game',
    2: 'Manual',
    3: 'About',
    4: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
     print('Game started.')
     attempt = input("Enter a number: ")
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


def option2():
     print('Handle option \'Option 2\'')

def option3():
     print('Handle option \'Option 3\'')


# Run own program - choose a handle option
if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
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