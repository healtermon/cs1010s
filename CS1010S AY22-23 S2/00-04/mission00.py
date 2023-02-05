# CS1010S --- Programming Methodology
# Mission 0

############################################################################
# Note that written answers are commented out to allow us to run your code #
# easily while grading your problem set.                                   #
#                                                                          #
# The expected answer is what you think the line of code will produce if   #
# it were to be run in IDLE.                                               #
#                                                                          #
# The final answer is the actual output after running the line of code.    #
# You may leave the final answer blank if the output is what you expected. #
############################################################################

############################################################################
# The first line has already been uncommented for you.                     #
# If a line causes an error, you should leave it commented out.            #
#                                                                          #
# Just press F5 to run this file in IDLE.                                  #
# On Mac, the shortcut for running your script is <fn> + F5 or <cmd> + F5. #
# In some Windows systems, it may be <fn> + F5 or <ctrl> + F5.             #
############################################################################

##########
# Task 1 #
##########

# Example 1:
# My expected result is zero but upon printing the result is 0.
print(0)
# expected answer: zero
# final answer: 0

# Example 2:
# My expected result is 1 which turns out to be correct after I run the
# print statements, so I don't need to do anything for the final answer.
print(1)
# expected answer: 1
# final answer:

# Example 3:
# This print statement results in an error,
# so I need to comment it and put the specific error as shown.
#print(a)
# expected answer: NameError: name 'a' is not defined
# final answer:

##############################
## YOUR MISSION STARTS HERE ##
##############################

print(42)
# expected answer: 42
# final answer: 42

print(0000)
# expected answer:0
# final answer:0

print("the force!")
# expected answer:the force!
# final answer:the force!

print("Hello World")
# expected answer:Hello World
# final answer:Hello World

print(6 * 9)
# expected answer:54
# final answer:54

print(2 + 3)
# expected answer:
# final answer:5

print(2 ** 4)
# expected answer:
# final answer:16

print(2.1**2.0)
# expected answer:
# final answer:4.41

print(15 > 9.7)
# expected answer:
# final answer:True

print((5 + 3) ** (5 - 3))
# expected answer:
# final answer:64

print(--4)
# expected answer:
# final answer:4

print(1 / 2)
# expected answer: 0.5
# final answer:0.5

#print(1 / 3)
# expected answer:0.333333
# final answer:0.3333333333333333

#print(1 / 0)
# expected answer:
# final answer:ZeroDivisionError: division by zero

print(7 / 3 == 7 / 3.0)
# expected answer: True
# final answer:True

#print(3 * 6 == 6.0 * 3.0)
# expected answer:False, 'cuz int and float are different types. The equality may not convert them to the same type before checking.
# final answer:True

#print(11 % 3)
# expected answer:2
# final answer:2

#print(2 > 5 or (1 < 2 and 9 >= 11))
# expected answer:
# final answer:False

#print(3 > 4 or (2 < 3 and 9 > 10))
# expected answer:
# final answer:False

#print("2" + "3")
# expected answer:
# final answer:23

#print("2" + "3" == "5")
# expected answer:
# final answer:False

#print("2" <= "5")
# expected answer: error
# final answer:True

#print("2 + 3")
# expected answer:
# final answer:2 + 3

#print("May the force" + " be " + "with you")
# expected answer:
# final answer:May the force be with you

#print("force"*2)
# expected answer:
# final answer:forceforce

#print('daw' in 'padawan')
# expected answer:True
# final answer:True

a, b = 3, 4 # Do not comment or remove this line

print(a)
# expected answer:
# final answer:3

print(b)
# expected answer:
# final answer:4

a, b = b, a # Do not comment or remove this line

print(a)
# expected answer:
# final answer:4

print(b)
# expected answer:
# final answer:3

#print(red == 44)
# expected answer:False
# final answer:True

red, green = 44, 43 # Do not comment or remove this line

#print(red == 44)
# expected answer:
# final answer:True

#print(red = 44)
# expected answer:44
# final answer:TypeError: 'red' is an invalid keyword argument for print()

#print("red is 1") if red == 1 else print("red is not 1")
# expected answer:SyntaxError, need colons for if and else
# final answer:red is not 1

#print(red - green)
# expected answer:
# final answer:1

purple = red + green # Do not comment or remove this line

#print("purple")
# expected answer:
# final answer:purple

#print("purple"[7])
# expected answer:bounds accessing error, purple is < 7 lines
# final answer:IndexError: string index out of range

#print(red + green != purple + purple / purple - red % green)
# expected answer: 87 != 87 + 1 - 1, so False
# final answer:False

#print(green > red)
# expected answer:
# final answer:False

#print("green bigger") if green > red else print("red equal or bigger")
# expected answer:
# final answer:red equal or bigger

#print(green + 5)
# expected answer:
# final answer:48

#print(round(3.8))
# expected answer:3.5, expected ceil() function to return 4. Apparently round goes to nearest int, if samae then even value
# final answer:4

#print(int(3.8))
# expected answer:
# final answer:3

#print(int("3.8"))
# expected answer:3
# final answer:ValueError: invalid literal for int() with base 10: '3.8'

# Run these lines of code before proceeding to the next question!
# Do not comment these lines or remove it from your submission!
def f(n):
    if n == 1: return 1
    return n + f(n - 1)

#print(f(4))
# expected answer:incrementing sequence, 1+2+3+4
# final answer:10

#print(f(f(2)))
# expected answer:
# final answer:6

#print(f(0))
# expected answer:error, doesn't stop
# final answer:RecursionError: maximum recursion depth exceeded in comparison

d = {1: 2} # Do not comment or remove this line

#print(d[1]),
# expected answer: with key 1, access value 2, so 2. At first I thought it would be out of range error
# final answer:2

#print(d[2])
# expected answer:no key called 2, error
# final answer: KeyError: 2

d[2] = "apple" # Do not comment or remove this line

#print(d[2])
# expected answer:apple
# final answer:apple

###########################################################
# The following 7 questions are to ensure that you have   #
# installed all the packages correctly:                   #
# - PILLOW        - matplotlib       - scipy              #
# - seaborn       - numpy            - pyglet             #
# - cocos                                                 #
#                                                         #
# Just uncomment the line "from <package> import *",      #
# run the line, and observe the output.                   #
#                                                         #
# If there is no output, the packages have been installed #
# correctly, so answer "Nothing" to let us know that it's #
# working properly. Otherwise, if you see some errors, do #
# refer to the troubleshooting guide in the PDF file.     #
###########################################################

from PIL import *
# expected answer:
# final answer:Nothing

from matplotlib import *
# expected answer:
# final answer:Nothing

from scipy import *
# expected answer:
# final answer:Nothing

from seaborn import *
# expected answer:
# final answer:Nothing

from numpy import *
# expected answer:
# final answer:Nothing

from pyglet import *
# expected answer:
# final answer:Nothing

from cocos import *
# expected answer:
# final answer:Nothing
