#DICTIONARIES ARE KEY VALUE PAIRS AND ARE DEFINED WITHIN PARENTHESIS.
#Every key represents it's unique value.
alien_0 = {'colour': 'green', 'point':5}
print(alien_0['colour'])
print(alien_0['point'])

new_points= alien_0['point']
print("You just earened " + str(new_points) + " points!")
 
#ADDING NEW KEY VALUE PAIRS TO DICTIONARIES.
print(alien_0)
alien_0['x-position']=0
alien_0['y-position']=25
print(alien_0)

#STARTING WITH AN EMPTY DICTIONARIES.
alien_0={}
alien_0['color']='green'
alien_0['point']=5
print(alien_0)

#MODIFYING VALUES IN A DICTIONARY.
alien_0['color']='yelloow'
print(alien_0)

#A MORE INTERESTING PRACTICE SESSION.
alien_0={'x-position':0,'y-position':25,'speed':'medium'}
print("Original x-position:" + str(alien_0['x-position']))
#MOVE THE ALIEN TO THE RIGHT.
#DETERMINE HOW FAR TO MOVE THE ALIEN BASED ON IT'S CURRENT SPEED.
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3
    #This must be a fast alien.
#The new position is the old position plus the increment.
alien_0['x-position']=alien_0['x-position'] + x_increment
print("New position: " + str(alien_0['x-position']))

#REMOVING KEY VALUE PAIRS. del METHOD IS USED.
alien_0={'color':'blue','point':5}
del alien_0['point']
print(alien_0)

#PRACTICE.
person= {'first_name':'sanjay','last_name':'gaurav','age':21,'city':'bareilly'}
print("First Name:" + person['first_name'].title())
print("Last Name:" + person['last_name'].title())
print("Age:" +str(person['age']))
print("City in which live:" + person['city'].title())

#Creating a dictionary to represent the favourite numbers of peopl's.
fav_numbers= {
    'sachin':7,
    'tanuj':8,
    'sumit':42,
    'rohit':11,
    }
print("Sachin's favourite number is: " + str(fav_numbers['sachin']))
print("Rohit's favourite numbeer is: " + str(fav_numbers['rohit']))
print("Tanuj said that,my fav number is: " + str(fav_numbers['tanuj']))
print("Sumit's jersey number is: " + str(fav_numbers['sumit']))

#