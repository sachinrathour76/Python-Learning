#Say happy birthday to Rohit
age = 23
name="Rohit"
message="Happy " + str(age) + "rd birthday" + " " + name +"."
print(message)

#Working with integers
print(5+3)
print(15-7)
print(4*2)
print(24/3)

#Revealing my favourite number.
fav_number=11
message="My favourite number is " + str(fav_number) + '.'
print(message)
#%%
import this
from turtle import color 
 #This is a special command to show the "ZEN OF PYTHON"

#%% 
# Asking a user to what kind of rental car they want.
car = input("Please tell me what kind of car you want:")
print("Let me see if i can find you a " + car + ".")
print("Thanks for choosing our services.")

# %%
# Asking the user hoe many seats they to dinner in our restaurant.
peoples= int(input("Hello sir, please let me how many people are there in your dinner group: "))
if peoples > 8:
    print("Sorry sir,you have to wait for a table.")
else:
    print("Your table is ready sir")

# %%
#Checking for a number is multiple of ten or not.
number = int(input('Enter a number to check it is a multiple of ten or not: '))
if number== 0:
    print("The number," + str(number) + " is not a multiple of ten.")
elif number%10 == 0:
    print("The number," + str(number) + " is a multiple of ten.")
else:
    print("Number " + str(number) + " is not a multiple of ten.")


# %%
#Trying to print the length of a string.
name = input("Enter your name: ")
print(len(name))


# %%
# Write a program to print occurence of any letter in a string.
str = "This is a sample string"
print(str.count("i")) 

# %%
marks = int(input("Enter your marks: "))
if(marks >= 90):
    grade = "A"
elif(marks >= 80):
    grade = "B"
elif(marks >= 70):
    grade = "C"
else:
    grade = "D"
print(grade)


# %%
# WAP to check a number is even or odd.
number = int(input("Enter a number: "))
if(number%2 == 0):
    print("Number is Even")
else:
    print("Number is Odd")

# %%
#WAP to check greatest among three numbers.
a = int(input("Enter first Number: "))
b = int(input("Enter scond Number: "))
c = int(input("Enter third Number: "))

if (a > b and a > c):
    print("A is greatest among all three: ", a)
elif(b > a and b > c):
    print("B is the greatest among all three: ",b)
else:
    print("C is greatest among all the three: ",c)
    


# %%
# WAP to check a number is multiple of 7 or not.
number = int(input("Enter a nmber: "))
if(number%7 == 0 and number != 0):
    print("Entered number is a multiple of 7: ",number)
else:
    print("Enterred number is not a multiple of 7: ",number)

# %%
#Practice with lists.
list = [1, 2, 5, 3]
print(list.append(4)) # append() returns none.
print(list.sort()) # sort() returns none.
print(list)

# %%
# sorting a list into descending order.
list = [5, 1, 4, 2, 3]
list.sort(reverse= True) # this method is used to sort in descending order.
print(list)

#Sorting in strings.
list = ['banana', 'apple', 'mango', 'kiwi']
list.sort()
print(list)

# %%
# Inserting into a list.
list = ['a','b','c','e']
list.insert(3,'d')
list.insert(5,'f')
print(list)
# %%
# working with tuples.
data = (5,4,6,2)
print(type(data), data)

# %%
# WAP to ask for user their fav movie nd store them in a list.
list = []
movie1 = input("Enter your first fav" \
"ourite movie name: ")
list.append(movie1)

movie2 = input("Enter your 2nd fav movie: ")
list.append(movie2)

movie3 = input("Enter your 3rd Fav movie: ")
list.append(movie3)

print(list)

# %%
# WAP to check if a listt contains palindrome or not.
list = [1, 2, 3, 2, 1 ]
copy = list.copy()
copy.reverse()
if(list == copy):
    print("List is palindrome.")
else:
    print("List isn't palindrome.")
print(list)
# %%
# WAP to count the number of students with a grade in tuple.
tup = ('a','b','a','a','c','b','a','a')
print(tup.count('a'))
# %%
# Storing the values and keys in a dictionary.
dict = {
    "table": ["a piece of furniture","table of facts"],
    "cat":"a small animal",
}
print(dict)
# %%
# Implementing while loop.
count = 1
while count <= 10 :
    print("Hello World")
    count += 1
    

# %%
# print numbers from 1 to 100
count = 1
while count <= 100 :
    print(count)
    count += 1

# %%
count = 100
while count >= 1:
    print(count)
    count -= 1

# %%
# Print the multiplication table of a number n.
count = 1
i = int(input("Enter a number: "))
print("Table of number " + str(i) + " is: ")
while count <= 10:
    print(count*i)
    count += 1
print("End of Table.")

# %%
# print the elements of a list using a loop.
list = [1,4,9,16,25,36,49,64,81,100]  # using index[]

idx = 0
while idx < len(list):
    print(list[idx])
    idx += 1



# %%
tup = (1,4,9,16,25,36,49,64,81,100)

x = int(input("Enter number to be searched: "))

i = 0
while i < len(tup):
    if(tup[i] == x):
        print("Found at Index: ", i)
        break
    else:
        print("Not found")  
    i += 1


# %%
# CAPTCHA GENERATER

import random

# Define the characters allowed in the CAPTCHA
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Length of the CAPTCHA text
captcha_length = 5

# Generate random CAPTCHA text
captcha_text = "".join(random.sample(characters, captcha_length))

# Print the generated CAPTCHA text
print("Your CAPTCHA:", captcha_text)



# %%

# ROCK PAPER SCISSOR GAME , COPIED CODE FROM REPOSITORY!


import random

def game():
    choices = ["rock", "paper", "scissor"]
    computer = random.choice(choices)

    user = input("Enter your choice (rock/paper/scissor): ").lower()
    while user not in choices:
        user = input("Invalid input. Enter your choice (rock/paper/scissor): ").lower()

    print(f"\nComputer chose {computer}, you chose {user}.\n")

    if user == computer:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "rock":
        if computer == "scissor":
            print("Rock smashes scissor! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user == "paper":
        if computer == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissor cuts paper! You lose.")
    elif user == "scissor":
        if computer == "paper":
            print("Scissor cuts paper! You win!")
        else:
            print("Rock smashes scissor! You lose.")

if __name__ == "__main__":
    game()

# %%
class Cars :
    def __init__(self, name, brand, year, color):
        self.name = name
        self.brand = brand
        self.year = year
        self.color = color

Car1 = Cars("Hilux", "Toyota", 2030, "Black")
Car2 = Cars("Thar", "Mahindra", 2031, "Black")

print(Car1.name, Car1.color)
print(Car2.name, Car2.year)

print("Congratulations, You have succesfully undestood class and object.")
# %%

class Student:

    @staticmethod   #decorator
    def collage():
        print("Abc collage")
# %%

# checking if a string is palindrome or not.
str = input("Enter a word:")

rev_str = str[::-1]

if str == rev_str:
    print("String is palindrome.")
else:
    print("String is not palindrome.")



# %%

#creating a circle with radius r.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22/7) * self.radius ** 2

    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())
    

# %%

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Role is:", self.role)
        print("Department is:", self.dept)
        print("Salary is:", self.salary)

emp1 = Employee("Python developer", "Development", 50000)

print(emp1.showDetails())

# %%
