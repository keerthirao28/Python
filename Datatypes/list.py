fruits=["apple", "banana", "orange","chikoo","pineapple"]
print(fruits[1])
print(type(fruits))

print(dir(fruits))
#operations:['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


#1 append
fruits.append("papaya")
print(fruits,"The list is appended")


#2 copy
fruits.copy()
print(fruits,"The list is copied")


#3 count
x=fruits.count("papaya")
print("The count is",x)

#4 extend
veggies=["tomato","carrot"]
fruits.extend(veggies)
print(fruits,"The list is extended")

#5 index
z=fruits.index("apple")
print("The index is ",z)

#6 insert
fruits.insert(5,"watermelon")
print("inserted watermelon",fruits)

#7 pop
p=fruits.pop()
print("The popped element is: ",p)
print("After popping ",fruits)

#8 remove
fruits.remove("apple")
print("Apple is removed",fruits)

#9 reverse
fruits.reverse()
print(fruits,"The list is reversed")

#10 sort
fruits.sort()
print(fruits,"The list is sorted")

#11 clear
fruits.clear()
print(fruits,"The list is cleared")