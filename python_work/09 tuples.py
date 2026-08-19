#DEFINING A TUPLE. AND TUPLES ARE IMMUTABLE DATA TYPES.
dimensions = (100,50)
print(dimensions[0])
print(dimensions[1])

#USING FOR LOOP IN TUPLES SAME AS THE LISTS.
dimensions = (100,50)
for dimension in dimensions :
    print(dimension)

#WRITING OVER A TUPLE.
print("Original dimensions")
for dimension in dimensions:
    print(dimension)
dimensions = (400,600)
print("\nModified dimensions are")
for dimension in dimensions:
    print(dimension)

#MORE PRACTICE WITH TUPLES.
menu = ("pizza","burger","french fries","lassi","mango shake")
for food in menu :
    print(food)
#menu[0]= "samosa" ,at that time i make this line to practice that elements in a tuple can't be modified.
print("Origial Menu was:")
for food in menu :
    print(food)
menu = ("chaap","aam panna","french fries","lassi","mango shake")
print("Modified menu is:")
for food in menu:
    print(food)
 