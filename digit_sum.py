# !/usr/bin/env python3

# Name: Jacob St Lawrence
# Date: November 12, 2023

# Description:
# This program proompts the user to enter a positive integer.
# It then recursively calculates the sum of the integer's digits
# and displays the result. The program will repeat for as many
# integers as the user wishes.

# Logic:
# main:
#   get num
#   if user pressed enter, display goodbye and end program
#   get sum
#   display Number Entered and Sum of Digits
#   go again
# get num:
#   prompt for positive integer, or enter to exit
#   if pressed enter, return None
#   try: int(num)
#   except: display error, go again
#   if num < 0: display error, go again
#   else: return num
# get sum:
#   base case: if num < 10:
#       return num
#   else:
#       return (num % 10) + (get sum(num // 10))


# main function
def main():
    # begin while loop to repeat until user is done
    while True:
        # call function to get integer input from user
        num = get_num()
        # check if input was empty
        if num is None:
            # if so, user pressed enter and is done, exit loop
            break
        # call function to calculate sum of digits
        sum_dig = get_sum(num)
        # display formatted result
        print(f'\nNumber Entered: {num}'
              f'\nSum of Digits: {sum_dig}\n')
        # continue to next iteration of loop to go again
        continue
    # end of program, display goodbye message
    print(f'\nGoodbye!')


# function to get integer input from user
def get_num():
    # begin while loop for input validation
    while True:
        # prompt user for positive integer
        entry = input(f'Enter a positive integer, or press ENTER to exit: ')
        # check if input was empty
        if not entry:
            # if so, return None to indicate no input
            return None
        # try to convert input to integer type
        try:
            entry = int(entry)
        # if error when converting to integer...
        except:
            # user entered a non-integer, display error
            print(f'Invalid entry. Input must be an integer.')
            # continue to next iteration of loop to try again
            continue
        # check if input value is negative
        if entry < 0:
            # if it is, no good, display error
            print(f'Invalid entry. Integer must be non-negative.')
            # continue to next iteration of loop to try again
            continue
        # if non-negative, input is good
        else:
            # return integer input value
            return entry


# function to sum the digits of the integer
def get_sum(val):
    # base case if integer is single digit (reached first digit)
    if val < 10:
        # return the integer
        return val
    # if not single digit, base case not reached
    else:
        # return last digit +
        # recursively call this function for integer with last digit dropped
        return (val % 10) + (get_sum(val // 10))
    

# call main to begin program execution  
if __name__ == '__main__':
    main()
