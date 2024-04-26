def exercise_1(dic):
    """Sort a dictionary by value in both ascending and descending order."""
    sorted_asc = sorted(dic.items(), key=lambda item: item[1])
    sorted_desc = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    print("Ascending:", sorted_asc)
    print("Descending:", sorted_desc)
    return sorted_asc, sorted_desc

# exercise_1({1: 2, 3: 1, 4: 3, 2: 4})

def exercise_2(dic, key, value):
    """Add a key to a dictionary."""
    dic[key] = value
    print("Updated dictionary:", dic)
    return dic

# exercise_2({0: 10, 1: 20}, 2, 30)

def exercise_3(dic1, dic2, dic3):
    """Concatenate dictionaries to create a new one."""
    result = {**dic1, **dic2, **dic3}
    print("Concatenated dictionary:", result)
    return result

# exercise_3({1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50, 6: 60})

def exercise_4(dic, key):
    """Check whether a given key already exists in a dictionary."""
    exists = key in dic
    print(f"Key {key} exists:", exists)
    return exists

# exercise_4({1: 10, 2: 20}, 1)

def exercise_5(dic):
    """Iterate over dictionaries using for loops."""
    for key, value in dic.items():
        print(f"Key: {key}, Value: {value}")

# exercise_5({1: 10, 2: 20, 3: 30})

def exercise_6(n):
    """Generate and print a dictionary that contains a number in the form (x, x*x)."""
    result = {x: x * x for x in range(1, n + 1)}
    print("Dictionary of squares:", result)
    return result

# exercise_6(5)

def exercise_7():
    """Print a dictionary where the keys are numbers between 1 and 15 and the values are the square of the keys."""
    dic = {x: x ** 2 for x in range(1, 16)}
    print("Dictionary of squares 1-15:", dic)
    return dic

# exercise_7()

def exercise_8(dic1, dic2):
    """Merge two Python dictionaries."""
    merged_dic = {**dic1, **dic2}
    print("Merged dictionary:", merged_dic)
    return merged_dic

# exercise_8({1: 10, 2: 20}, {3: 30, 4: 40})

def exercise_9(dic):
    """Iterate over dictionaries using for loops (demonstrating another use-case)."""
    for key, value in dic.items():
        print(f"Key: {key}, Value: {value}")

# exercise_9({1: 'apple', 2: 'banana'})

def exercise_10(dic):
    """Sum all the items in a dictionary."""
    total = sum(dic.values())
    print("Sum of all items:", total)
    return total

# exercise_10({1: 10, 2: 20, 3: 30})

def exercise_11(dic):
    """Multiply all the items in a dictionary using math.prod."""
    import math
    result = math.prod(dic.values())
    print("Product of all items:", result)
    return result

# exercise_11({'a': 10, 'b': 20, 'c': 30})

def exercise_12(dic, key):
    """Remove a key from a dictionary."""
    if key in dic:
        del dic[key]
    print("Dictionary after deletion:", dic)
    return dic

# exercise_12({'a': 1, 'b': 2, 'c': 3}, 'b')

def exercise_13(keys, values):
    """Map two lists into a dictionary."""
    result = dict(zip(keys, values))
    print("Mapped dictionary:", result)
    return result

# exercise_13(['a', 'b', 'c'], [1, 2, 3])

def exercise_14(dic):
    """Sort a given dictionary by key."""
    sorted_dic = dict(sorted(dic.items()))
    print("Sorted dictionary by key:", sorted_dic)
    return sorted_dic

# exercise_14({'b': 2, 'c': 3, 'a': 1})

def exercise_15(dic):
    """Get the maximum and minimum values of a dictionary."""
    max_value = max(dic.values())
    min_value = min(dic.values())
    print("Maximum value:", max_value, "Minimum value:", min_value)
    return max_value, min_value

# exercise_15({'a': 10, 'b': 20, 'c': 5})

def exercise_16():
    """Get a dictionary from an object's fields."""
    class Example:
        def __init__(self):
            self.a = 10
            self.b = 20
    obj = Example()
    result = obj.__dict__
    print("Dictionary from object's fields:", result)
    return result

# exercise_16()

def exercise_17(dic):
    """Remove duplicates from the dictionary (based on values)."""
    reverse_dic = {}
    for key, value in dic.items():
        if value not in reverse_dic:
            reverse_dic[value] = key
    result = {value: key for key, value in reverse_dic.items()}
    print("Dictionary after removing duplicates:", result)
    return result

# exercise_17({'a': 1, 'b': 2, 'c': 1, 'd': 2})

def exercise_18(dic):
    """Check if a dictionary is empty or not."""
    is_empty = not bool(dic)
    print("Is dictionary empty:", is_empty)
    return is_empty

# exercise_18({})

def exercise_19(d1, d2):
    """Combine two dictionaries by adding values for common keys."""
    from collections import Counter
    result = dict(Counter(d1) + Counter(d2))
    print("Combined dictionary:", result)
    return result

# exercise_19({'a': 100, 'b': 200, 'c': 300}, {'a': 300, 'b': 200, 'd': 400})

def exercise_20(data):
    """Print all distinct values in a dictionary."""
    unique_values = {dic[key] for dic in data for key in dic}
    print("Unique Values:", unique_values)
    return unique_values

# exercise_20([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}])
