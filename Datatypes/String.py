a_12="Hello world"
b_24="this is"
c_36="Keerthi!"
print(a_12,  b_24,  c_36)
print(type(a_12))

print(dir(a_12))
#operations: __add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# Capitalize first letter
print("capitalize:", text.capitalize())

# Casefold for case-insensitive comparison
print("casefold:", text.casefold())

# Center align
print("center:", text.center(20, '*'))

# Count occurrences of character
print("count:", text.count("o"))

# Encode string to bytes
print("encode:", text.encode())

# Check suffix
print("endswith:", text.endswith("!"))

# Expand tabs
print("expandtabs:", "Hello World".expandtabs(4))

# Find substring index
print("find:", text.find("World"))

# String formatting
print("format:", "Hello, {}".format("Python"))

# Right justify
print("rjust:", text.rjust(20, '-'))

# Check if whitespace
print("isspace:", " ".isspace())

# Check title case
print("istitle:", "Hello World".istitle())

# Check if uppercase
print("isupper:", "HELLO".isupper())

# Join strings
print("join:", "-".join(["Hello", "World"]))

# Left justify
print("ljust:", text.ljust(20, '-'))