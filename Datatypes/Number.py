a=20
b=10
x=a+b
print(x)
print(type(x))

c=0.25
d=2.56
f=float(a*b)
print(f)
print(type(f))

print(dir(x))
print(dir(f))

#operations: __abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 'numerator', 'real', 'to_bytes']
# integer:
num=10

# Integer ratio
print("as_integer_ratio:", num.as_integer_ratio())

# Count number of set bits
print("bit_count:", num.bit_count())

# Bit length
print("bit_length:", num.bit_length())

# Conjugate (for complex compatibility)
print("conjugate:", num.conjugate())

# Denominator of rational representation
print("denominator:", num.denominator)

# Imaginary part
print("imag:", num.imag)

# Check if integer
print("is_integer:", isinstance(num, int))

# Numerator of rational representation
print("numerator:", num.numerator)

# Real part
print("real:", num.real)

# Convert integer to bytes
print("to_bytes:", num.to_bytes(2, byteorder='big'))

# Convert bytes to integer
print("from_bytes:", int.from_bytes(b'\x00\x0A', byteorder='big'))




