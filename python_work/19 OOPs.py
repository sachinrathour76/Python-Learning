#starting with class and object
# class is a blueprint for object
class Student:
    def __init__(self, name, Age, personality): #This is a constructor which is used to initialize the object.
        self.name = name
        self.Age = Age
        self.personality = personality
s1 = Student("Sachin", 20, "Eager")
s2= Student("Tanuj", 20, "Aesthetic")
print(s1.name.title())
print(s2.Age)
print(s1.personality, s2.personality)


#%%
#New class for cars

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

print("Congratulations Sachin," \
" You have succesfully undestood" \
" the concept of class and object.")



#%%

class Childs:
    family_name = "rathour's" # class attribute

    def __init__(self, name, age):
        self.name = name # object attributes
        self.age = age

m1 = Childs("Nandu", 3)
m2 = Childs("Shree", 1)

print(m1.name + " belongs to " + m1.family_name  + " family.")
print("And his age is =" , m1.age)

# %%

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @staticmethod    #decorator
    def collage():
        print("Future Collage")
s1 = Student("Aditya", 95)
s2 = Student("Shivam", 97)
s3 = Student("Tanuj", 96)
s1.collage()
average = (s1.marks + s2.marks + s3.marks)/3

print(s1.name,s1.marks)
print(s2.name, s2.marks)
print(s3.name, s3.marks)

print( "Average of their marks is:",average)


# %%
# creating a banking system.

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total amount is:", self.get_bal())
        
    # credit method
    def credit(self, amount):                                                                                                                                                       
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total amount is:", self.get_bal())
    # balance checking method.
    def get_bal(self):
        return self.balance

acc1 = Account(10000, 12345)
print("Your balance is:",acc1.balance)
#print(acc1.account_no)

acc1.debit(500)
acc1.credit(1500)
acc1.credit(50)
acc1.get_bal()



# %%
