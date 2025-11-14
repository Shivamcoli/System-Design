# PYTHON LIST AND DICTIONARY MANIPULATION CHEATSHEET

# ==========================
# LIST MANIPULATION
# ==========================

# 1. Add items
# - append(x)
# - insert(i, x)
# - extend(list)
# - new_list = list1 + list2

# 2. Remove items
# - remove(x)
# - pop()
# - pop(i)
# - del list[i]
# - clear()

# 3. Accessing items
# - list[i]
# - list[-1]
# - list[start:end]
# - list[:]
# - list.copy()

# 4. Searching
# - x in list
# - list.index(x)
# - list.count(x)

# 5. Looping
# - for value in list:
# - for index, value in enumerate(list):
# - while loop

# 6. Sorting
# - list.sort()
# - list.sort(reverse=True)
# - sorted(list)
# - list.sort(key=function)

# 7. List Comprehension
# - [x for x in list]
# - [x*2 for x in list]
# - [x for x in list if condition]
# - [x if cond else y for x in list]

# 8. Copy
# - list.copy()
# - list[:]

# 9. Merge
# - list1 + list2
# - list1.extend(list2)

# 10. Convert
# - list("hello")
# - "a,b,c".split(",")


# ==========================
# DICTIONARY MANIPULATION
# ==========================

# 1. Accessing values
# - dict[key]
# - dict.get(key, default)

# 2. Add / Update
# - dict[key] = value
# - dict.update({key: value})

# 3. Remove keys
# - dict.pop(key)
# - dict.popitem()
# - del dict[key]
# - dict.clear()

# 4. Looping
# - for key in dict:
# - for key, value in dict.items():
# - for value in dict.values():
# - for key in dict.keys():

# 5. Searching
# - key in dict
# - value in dict.values()

# 6. Dictionary Comprehension
# - {k: v for k, v in dict.items()}
# - {v: k for k, v in dict.items()}
# - {k: v for k, v in dict.items() if condition}

# 7. Copy dictionary
# - dict.copy()
# - dict(dict)

# 8. Merge dictionaries
# - merged = dict1 | dict2
# - merged = {**dict1, **dict2}
# - dict1.update(dict2)

# 9. Default values
# - dict.setdefault(key, default)

# 10. Sorting dict
# - sorted(dict.items())
# - sorted(dict.items(), key=lambda x: x[1])

# END OF CHEATSHEET
