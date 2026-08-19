#using if statement.
cars =['audi','bmw','thar','hilux']
for car in cars:
    if car =='bmw':
        print(car.upper())
    else:
        print(car.title())

#checking for equality.
car ="bmw"
car=="BMW" #false since equality is case sensitive.
car=="bmw" #True.

#checking for inequality.
answer = 17
if answer != 40:
    print("Answer is wrong. Please try again")

#Checking whether a value is in a list.
requested_toppings = ['mushroom','onion','pineapple']
'mushroom' in requested_toppings #True.
'pepperoni' in requested_toppings #False.

#Checking whether a value is not in list.
banned_users = ['sachin','amit','rahul']
user = 'sumit'
if user not in banned_users:
    print(user.title() + ", you can post a responce if you wish")

#Using if-else statement.
#And using if-elif-else chain for multiple tset cases.
age=17
if age>= 18:
    print("You are old enough to Vote.")
    print("Have you registered yourself to vote yet.")
else:
    print("Sorry you are not old enough to vote yet.")
    print("Register yourself to vote as soon as you turn 18") 

#USING if-elif-else STATEMENT.
age=15
if age<=5:
    print("Your ticket price is $5")
elif age<=10:
    print("Your ticket price is $10.")
else:
    print("Your ticket price is $15.")