#starting with lists.

bicycles=['trek','cannondale','redline','specialized']
#print(bicycles)
#print(bicycles[0])
#print(bicycles[2].title())
message="My first cycle as a kid was a " + bicycles[0].title() + "!."
print(message)
message="I am planning to buy a new " + bicycles[2].title() + " cycle this year by the november 2026."
print(message)

#Applying index slicing concept
print(bicycles[0:2])
print(bicycles[-1])
print(bicycles[2:4])
print(bicycles[2:3])

#printing names of my friends using lists
names=['aditya','shivam','tanuj','sachin','chetan']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())
message=" how are you!."        #printing names form list with greetings  to everyone .
print("Hi " + names[0].title() + " " + message)
print("Hi " + names[1].title() + " " + message)
print("Hi " + names[2].title() + " " + message)
print("Hi " + names[3].title() + " " + message)
print("Hi " + names[4].title() + " " + message)


#creating and printing my own list of my fav bikes.
bikes=['ninza h2','zx10r','himalayan','gt650']
message="I would like to own a "
print(message + bikes[0].title() + ".")
message=" is one of the bike which i am going to own whenever i will get my job."
print(bikes[2].title() + message)
#%%
#MODIFYING ELEMENTS IN A LIST.
bikes=['ninza h2','zx10r','himalayan','gt650']
bikes[1]='harley davidson'  #replaces current existing value with new passed value.
print(bikes)
#%%
#ADDING ELEMENTS TO A LIST.
bikes=['ninza h2','zx10r','himalayan','gt650']
bikes.append('duke') #APPEND () ADDS ELEMENTS TO THE END OF THE LIST WITHOUT AFFECTING THE ORDER OF THE LIST.
print(bikes)

#APPENDING ELEMENTS INTO AN EMPTY LIST.
bikes=[]
bikes.append('ninza h2')
bikes.append('himalayan')
bikes.append('duke 390')
bikes.append('gt 650')

#INSERTING ELEMENTS INTO A LIST AT A SPECIFIC POSITION.
bikes=[]
bikes.insert(0,'bmws1000rr') #INSERTING ELEMENTS AT THE BEGINNING OF THE LIST.
print(bikes) #AFTER INSERTING ELEMENTS WE NEED TO USE PRINT FUNCTION TO SEE THE CHANGES.

#REMOVING THE ELEMENTS FROM LIST USING del STATEMENT.
bikes=['ninza h2','zx10r','himalayan','gt650']
del bikes[0] #DELETING THE FIRST ELEMENT FROM THE LIST.
print(bikes)
del bikes[2] #DELETING THE THIRD ELEMENT FROM THE LIST.
print(bikes) #HERE LAST ELEMENT IS DELETED SINCE BY USING LINE61 WE HAVE ALREADY DELETED FIRST INDEX.
#%%
#REMOVING THE ITEM USING POP() FUNCTION.
# THE POP() FUNCTION REMOVES THE LAST ITEM IN A LIST,
# BUT IT LETS YOU WORK WITH THAT ITEM AFTER REMOVING IT
bikes=['bmws1000rr','duke390','himalayan','gt 650']
popped_bikes=bikes.pop()
print(popped_bikes)
#%%
#POPPING ITEMS AT ANY INDEX.
popped_bikes=bikes.pop(0)
print(popped_bikes)

#REMOVING AN ITEM BY ITS VALUE.
bikes=['duke390','gt650']
removed_bikes=bikes.remove('duke390')
print(bikes)

#SORTING A LIST USING sort() METHOD.
cars=['bmw','thar','audi','hilux']
cars.sort()
print(cars)

#SORTING IN REVERSE ALPHABETICAL ORDER.
cars.sort(reverse=True)
print(cars)

#PRINTING A LIST IN REVERSE ORDER.
cars.reverse()
print(cars)

#FINDING THE LENGTH OF A LIST.
print(len(cars))

#EXTRA TIP 1: list[-1] ALWAYS RETURNS THE LAST ITEM OF LIST.
#EXTRA TIP 2: INDEX ERROR CAN OCCUR WHEN YOU PROVIDE THE INDEX NUMBER GREATER THAN THE LENGTH OF INDEX.
#EXTRA TIP 3: WE CAN ALSO SORT A LIST USING sorted() METHOD TO MAINTAIN THE ORIGINAL ORDER OF THE LLIST.
#EXTRA TIP 4: \n IS USED TO CREATE A NEW LLINE .
#EXTRA TIP 5: \t IS USED TO CREATE A TAB (MEANS SPACE).
# %%
