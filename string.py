def exercise_1(s):
    """Write a Python program to calculate the length of a string."""
    return len(s)

# print("Exercise 1:", exercise_1("hello"))

def exercise_2(s):
    """Write a Python program to count the number of characters (character frequency) in a string."""
    return {char: s.count(char) for char in set(s)}

# print("Exercise 2:", exercise_2("google.com"))

def exercise_3(s):
    """Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
    If the string length is less than 2, return the empty string instead."""
    return s[:2] + s[-2:] if len(s) >= 2 else ""

# print("Exercise 3:", exercise_3("merito jest super"))

def exercise_4(s):
    """Write a Python program to get a string from a given string where all occurrences of its first char
    have been changed to '$', except the first char itself."""
    return s[0] + s[1:].replace(s[0], '$')

# print("Exercise 4:", exercise_4("rabarbar"))

def exercise_5(s1, s2):
    """Write a Python program to get a single string from two given strings, separated by a space and
    swap the first two characters of each string."""
    return s2[:2] + s1[2:] + " " + s1[:2] + s2[2:]

# print("Exercise 5:", exercise_5("abc", "xyz"))

def exercise_6(s):
    """Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
    If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string
    is less than 3, leave it unchanged."""
    if len(s) < 3:
        return s
    elif s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'ing'

# print("Exercise 6:", exercise_6("abc"))

def exercise_7(s):
    """Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
    If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string."""
    not_pos = s.find('not')
    poor_pos = s.find('poor')
    if poor_pos > not_pos != -1 and poor_pos != -1:
        return s[:not_pos] + 'good' + s[poor_pos + 4:]
    return s

# print("Exercise 7:", exercise_7("The lyrics are not that poor!"))

def exercise_8(words):
    """Write a Python function that takes a list of words and return the longest word and the length of the longest one."""
    longest = max(words, key=len)
    return longest, len(longest)

# print("Exercise 8:", exercise_8(["hello", "world", "Exercises", "longestword"]))

def exercise_9(s, n):
    """Write a Python program to remove the nth index character from a nonempty string."""
    return s[:n] + s[n+1:]

# print("Exercise 9:", exercise_9("hello", 1))

def exercise_10(s):
    """Write a Python program to change a given string to a newly string where the first and last chars
    have been exchanged."""
    if len(s) < 2:
        return s
    return s[-1] + s[1:-1] + s[0]

# print("Exercise 10:", exercise_10("hello"))

def exercise_11(s):
    """Write a Python program to remove characters that have odd index values in a given string."""
    return s[::2]

# print("Exercise 11:", exercise_11("abcdefg"))

def exercise_12(sentence):
    """Write a Python program to count the occurrences of each word in a given sentence."""
    words = sentence.split()
    return {word: words.count(word) for word in set(words)}

# print("Exercise 12:", exercise_12("hello world hello"))

def exercise_13():
    """Write a Python script that takes input from the user and displays that input back in upper and lower cases."""
    user_input = input("Enter some text: ")
    return user_input.upper(), user_input.lower()

# print("Exercise 13:", exercise_13())

def exercise_14(words):
    """Write a Python program that accepts a comma-separated sequence of words as input and prints the
    distinct words in sorted form (alphanumerically)."""
    words_list = words.split(", ")
    return ', '.join(sorted(set(words_list)))

# print("Exercise 14:", exercise_14("red, white, black, red, green, black"))

def exercise_15(tag, words):
    """Write a Python function to create an HTML string with tags around the word(s)."""
    return f"<{tag}>{words}</{tag}>"

# print("Exercise 15:", exercise_15('h1', 'Python'))

def exercise_16(wrapper, word):
    """Write a Python function to insert a string in the middle of a string."""
    mid_index = len(wrapper) // 2
    return wrapper[:mid_index] + word + wrapper[mid_index:]

# print("Exercise 16:", exercise_16('<><><>', 'Python'))

def exercise_17(s):
    """Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2)."""
    if len(s) >= 2:
        return s[-2:] * 4
    return ""

# print("Exercise 17:", exercise_17('Python'))

def exercise_18(s):
    """Write a Python function to get a string made of the first three characters of a specified string.
    If the length of the string is less than 3, return the original string."""
    return s[:3] if len(s) >= 3 else s

# print("Exercise 18:", exercise_18('python'))

def exercise_19(url):
    """Write a Python program to get the last part of a string before a specified character."""
    return url.rsplit('/', 1)[0]

# print("Exercise 19:", exercise_19('https://moodle2.e-wsb.pl/mod/folder/view.php?id=123456'))

def exercise_20(s):
    """Write a Python function to reverse a string if its length is a multiple of 4."""
    if len(s) % 4 == 0:
        return s[::-1]
    return s

# print("Exercise 20:", exercise_20('PythonPython'))