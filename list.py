def exercise_1(numbers):
    """Sum all the items in a list."""
    result = sum(numbers)
    # Example usage
    print("Exercise 1:", result)
    return result

# Example usage
# exercise_1([1, 2, 3, 4, 5])

def exercise_2(numbers):
    """Multiply all the items in a list using math.prod."""
    import math
    result = math.prod(numbers)
    print("Exercise 2:", result)
    return result

# Example usage
# exercise_2([1, 2, 3, 4])

def exercise_3(numbers):
    """Get the largest number from a list."""
    result = max(numbers)
    print("Exercise 3:", result)
    return result

# exercise_3([1, 2, 3, 4, 5])

def exercise_4(numbers):
    """Get the smallest number from a list."""
    result = min(numbers)
    print("Exercise 4:", result)
    return result

# exercise_4([1, 2, 3, 4, 5])

def exercise_5(strings):
    """Count the number of strings where the string length is 2 or more and
    the first and last characters are the same."""
    count = sum(1 for s in strings if len(s) >= 2 and s[0] == s[-1])
    print("Exercise 5:", count)
    return count

# exercise_5(['abc', 'xyz', 'aba', '1221'])

def exercise_6(tuples):
    """Sort a list of tuples in increasing order by the last element in each tuple."""
    result = sorted(tuples, key=lambda x: x[1])
    print("Exercise 6:", result)
    return result

# exercise_6([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])

def exercise_7(items):
    """Remove duplicates from a list."""
    result = list(set(items))
    print("Exercise 7:", result)
    return result

# exercise_7([1, 2, 2, 3, 4, 4])

def exercise_8(items):
    """Check if a list is empty or not."""
    result = len(items) == 0
    print("Exercise 8: Empty?", result)
    return result

# exercise_8([])

def exercise_9(original):
    """Clone or copy a list."""
    copy = original[:]
    print("Exercise 9: Original and Copy", original, copy)
    return copy

# exercise_9([1, 2, 3, 4])

def exercise_10(words, n):
    """Find the list of words that are longer than n from a given list of words."""
    result = [word for word in words if len(word) > n]
    print("Exercise 10:", result)
    return result

# exercise_10(['hello', 'world', 'list', 'examples', 'Python'], 4)

def exercise_11(list1, list2):
    """Check if two lists have at least one common member."""
    result = any(i in list2 for i in list1)
    print("Exercise 11:", result)
    return result

# exercise_11([1, 2, 3], [3, 4, 5])

def exercise_12(items):
    """Print a specified list after removing the 0th, 4th and 5th elements."""
    filtered = [items[i] for i in range(len(items)) if i not in [0, 4, 5]]
    print("Exercise 12:", filtered)
    return filtered

# exercise_12(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])

def exercise_13():
    """Generate a 3*4*6 3D array whose each element is '*'. """
    array = [[[ '*' for _ in range(6)] for _ in range(4)] for _ in range(3)]
    print("Exercise 13:", array)
    return array

# exercise_13()

def exercise_14(numbers):
    """Print the numbers of a specified list after removing even numbers from it."""
    result = [num for num in numbers if num % 2 != 0]
    print("Exercise 14:", result)
    return result

# exercise_14([1, 2, 3, 4, 5, 6])


def exercise_15(lst):
    """Shuffle and print a specified list."""
    import random
    random.shuffle(lst)
    print("Exercise 15:", lst)
    return lst

# exercise_15([1, 2, 3, 4, 5])

def exercise_16():
    """Generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30."""
    squares = [i ** 2 for i in range(1, 31) if 1 <= i ** 2 <= 30]
    result = squares[:5] + squares[-5:]
    print("Exercise 16:", result)
    return result

# exercise_16()

def exercise_17(numbers):
    """Check if all numbers in the list are prime."""
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    result = all(is_prime(num) for num in numbers)
    print("Exercise 17:", result)
    return result

# exercise_17([3, 5, 7, 13])


def exercise_18(lst):
    """Generate all permutations of a list."""
    import itertools
    result = list(itertools.permutations(lst))
    print("Exercise 18:", result)
    return result

# exercise_18([1, 2, 3])

def exercise_19(list1, list2):
    """Calculate the difference between the two lists."""
    result = list(set(list1) - set(list2))
    print("Exercise 19:", result)
    return result

# exercise_19([1, 2, 3], [2, 4])

def exercise_20(lst):
    """Access the index of a list."""
    for index, value in enumerate(lst):
        print(f"Exercise 20: Index {index}: {value}")

# exercise_20([10, 20, 30, 40, 50])
