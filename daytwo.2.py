# VARIABILE IN PYTHONE

first_name = 'ebrima' # string
last_name = 'sonko' #string
skills = ['python', 'eletricista', 'device repaire'] # list containing string data type
is_maried = False # true or false data tpye
age = 24
myInfor = {
    'strugle': True,
    'occupation': 'eletricista',
    'salary': 1700,
    'hours': 10 and 30
}
# PRINT STATEMENT
print('First name:', first_name)
print('length of first name:', len(first_name))
print('my info:', myInfor)
print('length of myInfor:', len(myInfor))

#checking data types in python
print(type(myInfor))
# Casting: Converting one data type to another data type.

#int to float
number_as_it_data_type = 24
print(number_as_it_data_type)
print(type(number_as_it_data_type))
turn_it_to_float = float(number_as_it_data_type)
print(type(turn_it_to_float))

#float to int 
mySalary = 17.89
print(int(mySalary))

#int in to string
number_as_int = 10
turning_int_into_string = str(number_as_int)
print(turning_int_into_string)
print(type(turning_int_into_string))

# str to int or float
a_num_str = '10.10'
num_float = float(a_num_str)
print(a_num_str)
num_float1 = int(num_float)
print(type(num_float1))

# str to list
myName = 'ibra sonko'
str_to_list = list(myName)
print(str_to_list)
print(type(str_to_list))

#Exercises - Day 2
#Exercises: Level 1

#Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
#done
#Write a python comment saying 'Day 2: 30 Days of python programming'
#done
#Declare a first name variable and assign a value to it
my_variabile = 'eletricista'
print(my_variabile)
#Declare a last name variable and assign a value to it
last_name = 'sonko'
print(type(last_name))
#Declare a full name variable and assign a value to it
full_name = 'ebrima sonko'
print(full_name)
#Declare a country variable and assign a value to it
country = 'Gambia'
print(country)
#Declare a city variable and assign a value to it
city_variabile = 'Conegliano'
print(city_variabile)
#Declare an age variable and assign a value to it
my_age = '24'
print(my_age)
#Declare a year variable and assign a value to it
year = 2024
print(year)
#Declare a variable is_married and assign a value to it
is_maried = False
print(is_maried)
#Declare a variable is_true and assign a value to it
is_true = True
#Declare a variable is_light_on and assign a value to it
is_light_on = True
#Declare multiple variable on one line
name, last_name, age, city = 'ibra', 'sonko', 24, 'conegliano'
print(name, last_name, age, city)


#Exercises: Level 2

#Check the data type of all your variables using type() built-in function
#done
#Using the len() built-in function, find the length of your first name
print(len(name))
#Compare the length of your first name and your last name
first_name = 'ibra'
second_name = 'sonko'

length_of_first_name = len(first_name)
length_of_last_name = len(last_name)

print(length_of_first_name)
print(length_of_last_name)

if length_of_first_name < length_of_last_name:
    print('the length of fist name is less than last anme')
elif length_of_last_name > length_of_first_name:
    print('yes the length of last name is greater than the length of first name')
else:
     print("Your first and last names are the same length.")
#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
print(num_one)
print(num_two)
#Add num_one and num_two and assign the value to a variable total
num_one = 5
num_two = 4
total_sum = 9
print(total_sum)
#Subtract num_two from num_one and assign the value to a variable diff
substract = num_one - num_two
dif = substract
print(dif)
print(type(dif))
#Multiply num_two and num_one and assign the value to a variable product
multiply = num_one * num_two
product = multiply
print(product)

#Divide num_one by num_two and assign the value to a variable division
divide = num_one / num_two
division = divide
print(division)
#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
modules = num_one % num_two
print(modules)
print(type(modules))
#Calculate num_one to the power of num_two and assign the value to a variable exp
expo = num_one ** num_two
print(expo)
print(type(expo))
#Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division)
#The radius of a circle is 30 meters.
#Calculate the area of a circle and assign the value to a variable name of area_of_circle
radius = 30
pi = 3.14159
area_of_circle =  pi * (radius ** 2)
print("The area of the circle is:", area_of_circle, "square meters")
#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
radius = 30
pi =  3.14159
circum_of_circle = 2 * pi * radius
#Take radius as user input and calculate the area.
radius = 30
pi = 3.12159
area_of_circle = pi * (radius ** 2)

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
enter_first_name = input('enter your name')
enter_last_name = input('enter_last_name')
country = input("Enter your country: ")
age = input("Enter your age: ")

print("First Name:", first_name)
print("Last Name:", last_name)
print("Country:", country)
print("Age:", age)

#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help()
