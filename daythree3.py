#BOOLEAN and OPERATORS
#boolean are two values TRUE or FALSE
#operators are use to assigne values
#  
#Example:Complex numbers
print('multiplying complex numbers: ',(1 + 1j) * (1 - 1j))
print('complex numbers: ', 4j +1j)
# Floating numbers
print('Floating Point Number, PI', 3.14)
print('Floating Point Number, gravity', 9.81)

#Arithmetic Operators:
# Declaring values and organizing them together

num_one = 4
num_two = 2

total = num_one + num_two
dif = num_one - num_two
product = num_one * num_two
division = num_one / num_two
reminder = num_one % num_two
floordivision = num_one // num_two
exponential = num_one ** num_two

print('total: ', total)
print('difrent: ', dif)
print('product: ', product)
print('division: ', division)
print('reminder: ', reminder)
print('floordivision: ', floordivision)
print('exponential: ', exponential)

#Comparison Operators
print(4 == 3)
print(3 != 4)
print(5 > 4)
print(5 < 3)
print(6 >= 3)
print(2 <= 4)

print(len('mango') == len('avocado'))  # False
print(len('eletricista') == ('avocato'))
print(len('operaio') > len('doctore'))
print(len('pulizia') >= len('educatore'))
print(len('dio') <= len('signor'))
print(len('programatore') < len('python'))
print(len('skill') != len('jobe'))

#In addition to the above comparison operator Python uses:

#is: Returns true if both variables are the same object(x is y)
#is not: Returns true if both variables are not the same object(x is not y)
#in: Returns True if the queried list contains a certain item(x in y)
#not in: Returns True if the queried list doesn't have a certain item(x in y)

print('eletricista' in ['intarutore', 'eletricista', 'eletrico'])
print('eletrico' is not 'eletrico')
print('s' in 'strugle')
print('r' not in 'pass')

#Logical Operators 
print(3 > 6 and 6 < 3)
print(4 > 8 or 8 < 4)
print(not 8 < 9)


#Exercises - Day 3
#Declare your age as integer variable
age = 25
#Declare your height as a float variable
height = 125
#Declare a variable that store a complex number
complex_number = '1-4j'
#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    #Enter base: 20
    #Enter height: 10
    #The area of the triangle is 100
base = int(input('enter base'))
height = int(input('enter height'))
area = 0.5 * base * height
print('area: ', area)

#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
#Enter side a: 5
#Enter side b: 4
#Enter side c: 3
#The perimeter of the triangle is 12
side_a = int(input('enter side a: '))
side_b = int(input('enetr side b: '))
side_c = int(input('enter side c: '))
perimeter = side_a + side_b + side_c
print('perimeter: ', perimeter)

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input('Enter length: '))
width = int(input('enter width: '))
area = length * width
perimeter = 2 * length + width
print('Area of retangle is: ', area)
print('perimeter: ', perimeter)

#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
radius = int(input('enter radius: '))
area = pi * radius * radius
circumference = 2 * pi * radius
print('area: ', area)
print('circumference: ', circumference)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
#CHART GPT TO CONFIRM
#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

#Compare the slopes in tasks 8 and 9.

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out2'
#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
length_of_python = 'python'
length_of_dragon = 'dragon'

print('length_of_python: ', len(length_of_python))
print('length_of_dragon: ', len(length_of_dragon))

print(length_of_python < length_of_dragon)

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
python = 'python'
dragon = 'dragon'
if 'on' in python and 'on' in dragon:
    print("The substring 'on' is found in both 'python' and 'dragon'.")
elif 'on' in python:
    print('The substring is found in python.')
elif 'on' in dragon:
    print('The substring is found in ragon.')
else:
    print("The substring 'on' is not found in either 'python' or 'dragon'.")
#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
word_string = 'I hope this course is not full of jargon'
if 'jargon' in word_string:
    print('The substring is found in the sentence.')
else:
    print('the substring is not found in the sentence.')

#There is no 'on' in both dragon and python

#Find the length of the text python and convert the value to float and convert it to string
python = 'python'
length_of_python = len(python)
converted_to_float = float(length_of_python)
converted_to_str = str(converted_to_float)

print('length of python: ', length_of_python)
print('result converted to float: ', converted_to_float)
print('result converted to str from float:', converted_to_str)


#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
numbers = [2, 4, 7, 13, 11, 10,12]
for number in numbers:
    if number % 2 == 0:
        print(f' {number} is even number.')
    else:
        print(f'{number} is not even number.')
    
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
#Check if type of '10' is equal to type of 10
#Check if int('9.8') is equal to 10
#Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person? 
#Enter hours: 40
#Enter rate per hour: 28 
#Your weekly earning is 1120