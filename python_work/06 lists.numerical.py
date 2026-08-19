#MAKING NUMERICAL LIST.
for value in range(1,6):
    print(value)
#MAKING A LIST USIING NUMBERS.
numbers=list(range(1,6))
print (numbers)
 
#LIST OF EVEN NUMBERS.
even_numbers = list(range(2,20,2))
print(even_numbers)

#SQUARE VALUES IN A LIST.
squares =[]
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

#SIMPLE STASTICS WITH A LIST OF NUMBERS.
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

# LIST COMPREHENSIONS.
squares = [value**2 for value in range(1,11)]
print(squares) # By using this method we can do the same work in just 2 lines of code.
 
#Counting to twenty.
value = list(range(1,21))
print(value)

#EXPERIMENT WITH NUMBERS FROM 1 TO 1 MIILION.
numbers = [value for value in range(1,1000001)]
print(sum(numbers))

#ENOUGH OF LISTS.