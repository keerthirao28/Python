set1 = {1, 2, 3, 4, 5}
set2={6, 7, 8, 9, 10}

print(dir(set1))
# Adding elements to the set
set1.add(6)
set1.add(7)
print(set1)
# Removing elements from the set
set1.remove(3)  # Raises KeyError if 3 is not found
print(set1)

# Alternatively, you can use discard() to avoid the KeyError
set1.discard(8)  # No error if 8 is not found
print(set1)

# Union of two sets
union_set = set1.union(set2)
print(union_set)

# Intersection of two sets
intersection_set = set1.intersection(set2)
print(intersection_set)

# Elements in my_set but not in another_set
difference_set = set1.difference(set2)
print(difference_set)