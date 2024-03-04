# Define class can be create only one object. If the user create second object 
# then it should return the first object 

class Singleton(cls):
    instanse = {}

    def __new__():
        pass
        

singleton1 = Singleton("Instance 1")
singleton2 = Singleton("Instance 2")

print(singleton1 is singleton2)
print(singleton1)
print(singleton2)