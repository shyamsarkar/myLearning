class Car:
    def __str__(self):
        return "Inside of STR"
    
    # def __repr__(self):
    #     return "Inside of REPR"
    

obj = Car()

print(obj)
print(str(obj))
print(repr(obj))