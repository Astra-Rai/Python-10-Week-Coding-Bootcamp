# operation variable: operation = input("Would you like to add/subtract/multiply/divide?")
# operation variable: use .lower()method to convert user input for operation to all lower case letters

operation = input("Would you like to add/subtract/multiply/divide?").lower()
operation = operation.strip() #remove whitespace before or after string, if not
#space not removed, then the else statement : sorry but ...is not an option
#print( "You chose{} to ".format(operation)) # check if operation variable is defined
# if operation string has a whitespace before or after characters, program doesn't run


if operation == "divide" or operation == "subtract":  #branching statemntment begin with if statements. if statement checks if a given statement is True or False
    print("Alert: You chose to {}, please keep in mind the order matters.".format(operation))

#if operation == "add" or "subtract" or "multiply" or "divide":
# above is not correct, but didn't didn't note error
# correct version: if operation == "divide" or operation == "subtract": 
if operation == "add" or operation == "multiply":
    print("Alert: You chose to {}.".format(operation))


#   request user input, convert input to float
#   input by defalut is <class'string'>, use type converstion to convert input to <class'float'>
num1 = float(input("Enter first number: "))  # request user to enter a first number, input converted to a float and stored in num1 variable 
num2 = float(input("Enter second number: "))  # request user to enter a second number, input converted to float and stored in num2 variable 


# if condition is True, the assoicated code block runs, if condition is False, program continues without running associated code in code block
# if statement below is based on the what operation the user choses

if operation == "add":  # use if statement to provide branching logic based on operation chosen/entere by user
    result = num1 + num2 # add num1 and num2 and store in varaibe 'result'
    print("{} + {} = {}.".format(num1, num2, result)) #  output a statement that prints result of adding num1 and num2

elif operation == "subtract": #  if user doesn't enter "add" operation, this block of code runs and is executed if user enters "subtract" operation
    result = num1 - num2  #  add num1 and num2 and store in varaibe 'result'
    print("{} - {} = {}.".format(num1, num2, result)) #  output statement that prints the result of subtracing num1 from num2

elif operation == "multiply":#  if user doesn't enter the "add" or "subtract" , this block of code runs and is executed if user enters "multiply" operation
    result = num1 * num2  # multiply num1 and num2 and store in variable "result"
    print("{} * {} = {}.".format(num1, num2, result))   #  output statement that prints the result of subtracing num1 from num2

elif operation == "divide": # if user doesn't enter the "add", "subtract" or "multiply" operation, this block of code runs and is executed if user enters "divide"
    result = num1/num2
    print("{} / {} = {}".format(num1, num2, result))

else:  # if none of the conditions above have a value true, else statemetn will output
    print("Sorry, but {} is not an option.".format(operation))#  still working on this















# testing and notes 
# testing and accounting for errors
# user input: what if user enter a letter and an number, example: 2 + a
    # output value error: ValueError: could not convert string to float: 'a'
# user input: what if user enters a number and a number
# user input: what if users enters a leter and a letter, example: r + r
    # output ValueError:   ValueError: could not convert string to float: 'r'
#converting input to floats, cleaned up code

    #num1 = input("Enter first number: ")  # request user to enter a first number, store input in variable num1
    #num2 = input("Enter second number: ")  #request user to enter a second number, store input in variable num2
    #num1 = float(num1)  # num1 variable re-declared as a float, b/c by default, input data is a string
    #num2 = float(num2)  # num1 variable re-declared as a float, b/c by default, input data is a string

# use of or not correct
#if operation == "add" or "subtract" or "multiply" or "divide":
    #print("Alert: You chose to {}, please keep in mind the order matters.".format(operation))
    #print("You chose  to {}".format(operation)) print test
    #all number converted to floats b/c input value is a string; 
    #print("all number converted to floats /n For example: 5")

""" 
try and except #1
try:
        if operation != "add" or "subtract" or "multiply" or "divide":
            print("Invalid  operation entered...") 

except: 
    print("Please enter one of the following options: add, subtract") 

- if users enters divides, vs. divides, code still runs in try/accept
- Would you like to add/subtract/multiply/divide?divides
- Invalid  operation entered...
- Alert: You chose to divides, please keep in mind the order matters.
-Enter first number: 
-i think i want to catch if user enters a valid operation, then use try except
-the run the code for the calculator, ask for input again
-this is more advanced...cuz function are for chapter 3 not 2
-    
"""

#invalid option entered
#if option is invalid, there is an alert, but the code to enter first number still prints

#else statement doesn't catch error is operation isn't: add, subtract, multiply, divide

#testing: old comments and code

#testInput = float(testInput) #reconvert testInput, type conversion, from string to a float <class 'float'>
#print(" Data Type for variable testInput is: {}. ".format(type(testInput)))
#print(type(testInput)) #<class 'str'>, 
#print(float(testInput))


#code will break if the operation string has whitespace before or after: add, subtract, multiply, 

# remember, for example, the string 'Divde' isn't == to 'divide'
# to get the ASCII Code for a character 
# ASCI code for lowercase 'd' is 100:  print(ord('d'))
# ASCI code for uppercase 'D' is 68: print(ord('D'))
# convert user input for operation variable to lowercase.

#num2 = input("Enter second number: ") #TypeError: unsupported operand type(s) for /: 'str' and 'str', need to conver input to floats
#num1 = float(num1) # num1 variable re-declared as a float, b/c by default, input data is a string



#
#if operation == "add" or "subtract" or "multiply" or "divide":
    #print("Alert: You chose to {}, please keep in mind the order matters.".format(operation))
    #print("You chose  to {}".format(operation)) print test
    #all number converted to floats b/c input value is a string; 
    #print("all number converted to floats /n For example: 5")

# understand why this error occurrred: 
"""
if operation == "divide" or operation == "subtract":  #branching statemntment begin with if statements. if statement checks if a given statement is True or False
    print("Alert: You chose to {}, please keep in mind the order matters.".format(operation))

#if operation == "add" or "subtract" or "multiply" or "divide":
# above is not correct, but didn't didn't note error
# correct version: if operation == "divide" or operation == "subtract": 
if operation == "add" or operation == "multiply":
    print("Alert: You chose to {}.".format(operation))

#   request user input, convert input to float
#   input by defalut is <class'string'>, use type converstion to convert input to <class'float'>
#   errror when num1 and num2 indented within the if/else branching statement above




     #num1 = input("Enter first number: ")  # request user to enter a first number, store input in variable num1
    #num2 = input("Enter second number: ")  #request user to enter a second number, store input in variable num2
    #num1 = float(num1)  # num1 variable re-declared as a float, b/c by default, input data is a string
    #num2 = float(num2)  # num1 variable re-declared as a float, b/c by default, input data is a string



#what if user enters something other than a string?, num1 = k, num2 = 2, ValueError: could not convert string to float k
#use branching logic to check operation enter by user and excute code within the block of condition 





 """