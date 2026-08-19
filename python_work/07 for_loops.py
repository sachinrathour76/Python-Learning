#JUST A SIMPLE PRACTICE BLOCK OF CODE.
guest_list=['tanuj','sachin','aditya','shivam']
message=" please come to dinner at my house today ."
print(guest_list[0].title() + message)
print(guest_list[1].title() + message)
print(guest_list[2].title() + message)
print(guest_list[3].title() + message)

#LOOPING THROOUGH ENTIRE LIST.

#FOR LOOP
magicians = ['alice','bob','david'] #FOR LOOP ALLOWES TO RETRIEVE ENTIRE LIST IRRESPECTIVE OF ITS LENGTH.
for magician in magicians:
    print (magician)
for magician in magicians:
    print(magician.title() + ",that was a great trick!")
    print(magician.title() + " I can't wait to see your next trick!")
print("Thank you , everyone . That was a great magic show!")

#PRINTING NMAES OF PIZZAS FROM LIST USNG FOR LOOP.
pizzas = ['cheese','california style','roman style']
for pizza in pizzas:
    print(pizza.title())
    print(pizza.title() + " is my favourite pizza!")
print("I really love pizza")

animals =['dog','cat','rabbit']
for animal in animals:
    print(animal.title())
print("All of them are very friendly and cute pet animals.")
          