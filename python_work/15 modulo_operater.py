# Modulo operater used to devide any number with a given number and returns the remainder.
result = 6%3 
print(result)

#Check if a enterd number is even or odd.
number = int(input("Enter a number and i will tell you it is even or odd"))
if number%2 == 0:
    print("The number " + str(number) + " is even.")
else:
    print("The number " + str(number) + ' is odd.')
