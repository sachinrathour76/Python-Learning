#working with input() function.
message = input("Tell me something i will repeat it for you:")
print(message)

#Finding square root of any input number.
new_message = int(input("Enter a number than i will tell you the square of it:"))
sqrt = new_message**2
print("Square root is:",sqrt)

# Taking input from the user to check some kind of eligibility.
height = input("How tall are you, in inches:")
height=int(height)
if height >= 36:
    print("You are old enough to ride a roler coaster")
else:
    print("You are a little sorter to ride a roller coster, sorry Bro.")


