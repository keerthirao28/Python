fruit_colors = {"apple": "red", "banana": "yellow", "cherry": "red"}
print(fruit_colors)
print(type(fruit_colors))

print(dir(fruit_colors))
#operations: ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

#class
print(fruit_colors.__class__)

#doc
print(fruit_colors.__doc__)

#getitem
print(fruit_colors.__getitem__("apple"))

#pop
print(fruit_colors.pop("apple"))

#keys
print(fruit_colors.update())

#clear
print(fruit_colors.clear(),"The dict is cleared")