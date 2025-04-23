veggies=("tomato","potato","brinjal","chilli")
print(veggies[2])
print(type(veggies))

print(dir(veggies))
#operations:['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

#add
fruits=("banana","apple")
print(veggies.__add__(fruits))

# index
print(veggies.index("tomato"))

# count
print(veggies.count("potato"))

# class
print(veggies.__class__)

# getitem
print(veggies.__getitem__(2))