def exercise_1():
    """Find numbers divisible by 7 and multiples of 5 between 1500 and 2700."""
    result = [num for num in range(1500, 2701) if num % 35 == 0]
    print("Exercise 1:", result)
    return result

# exercise_1()

def exercise_2(temp, unit):
    """Convert temperatures to and from Celsius and Fahrenheit."""
    if unit.lower() == "celsius":
        converted = (temp * 9/5) + 32
        print(f"{temp}°C is {converted} in Fahrenheit")
    else:
        converted = (temp - 32) * 5/9
        print(f"{temp}°F is {int(converted)} in Celsius")
    return converted

# exercise_2(60, 'Celsius')
# exercise_2(45, 'Fahrenheit')

def exercise_3():
    """Python program to guess a number between 1 and 9."""
    import random
    target = random.randint(1, 9)
    while True:
        guess = int(input("Guess a number between 1 and 9: "))
        if guess == target:
            print("Well guessed!")
            break

# exercise_3()

def exercise_4():
    """Construct a pattern using a nested for loop."""
    n = 5
    pattern = "\n".join("* " * i for i in range(1, n + 1)) + "\n" + "\n".join("* " * i for i in range(n-1, 0, -1))
    print(pattern)
    return pattern

# exercise_4()

def exercise_5(word):
    """Accept a word and reverse it."""
    reversed_word = word[::-1]
    print("Reversed word:", reversed_word)
    return reversed_word

# exercise_5("hello")

def exercise_6(numbers):
    """Count the number of even and odd numbers in a series."""
    evens = sum(1 for num in numbers if num % 2 == 0)
    odds = len(numbers) - evens
    print(f"Number of even numbers: {evens}")
    print(f"Number of odd numbers: {odds}")
    return evens, odds

# exercise_6((1, 2, 3, 4, 5, 6, 7, 8, 9))

def exercise_7(datalist):
    """Print each item and its corresponding type from a list."""
    for item in datalist:
        print(f"Item: {item}, Type: {type(item)}")

# exercise_7([1452, 11.23, 1+2j, True, 'merito', (0, -1), [5, 12], {"class":'V', "section":'A'}])

def exercise_8():
    """Print all numbers from 0 to 6 except 3 and 6 using 'continue'."""
    result = []
    for i in range(7):
        if i in [3, 6]:
            continue
        result.append(i)
    print("Exercise 8:", result)
    return result

# exercise_8()

def exercise_9():
    """Get the Fibonacci series between 0 and 50."""
    a, b = 0, 1
    fibonacci = []
    while a <= 50:
        if a > 0:
            fibonacci.append(a)
        a, b = b, a + b
    print("Fibonacci up to 50:", fibonacci)
    return fibonacci

# exercise_9()

def exercise_10():
    """Iterate integers from 1 to 50 with FizzBuzz rules."""
    for i in range(1, 51):
        if i % 15 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

# exercise_10()

def exercise_11(m, n):
    """Generate a two-dimensional array with element values i*j."""
    return [[i * j for j in range(n)] for i in range(m)]

# print("Exercise 11:", exercise_11(3, 4))

def exercise_12():
    """Accept a sequence of lines and print them in lower case."""
    lines = []
    while True:
        line = input("Enter a line (blank line to stop): ")
        if line == "":
            break
        lines.append(line.lower())
    for line in lines:
        print(line)

# exercise_12()

def exercise_13(data):
    """Print binary numbers divisible by 5."""
    result = ','.join([num for num in data.split(',') if int(num, 2) % 5 == 0])
    print("Exercise 13:", result)
    return result

# exercise_13("0100,0011,1010,1001,1100,1001")

def exercise_14(text):
    """Calculate the number of digits and letters in a string."""
    digits = sum(c.isdigit() for c in text)
    letters = sum(c.isalpha() for c in text)
    print(f"Letters {letters}. Digits {digits}.")
    return letters, digits

# exercise_14("Python 3.2")

def exercise_15(passwords):
    """Check the validity of passwords."""
    import re
    criteria = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])[A-Za-z0-9$#@]{6,16}$')
    valid_passwords = [pw for pw in passwords if criteria.fullmatch(pw)]
    print("Valid passwords:", valid_passwords)
    return valid_passwords

# exercise_15(["Abc123#", "abcdefg2#", "ABCD1234"])

def exercise_16():
    """Find numbers where each digit is an even number."""
    result = [str(num) for num in range(100, 401) if all(int(digit) % 2 == 0 for digit in str(num))]
    print("Exercise 16:", ', '.join(result))
    return result

# exercise_16()

def exercise_17():
    """Print the alphabet pattern 'A'."""
    pattern = ["  ***  ", " *   * ", " *   * ", " ***** ", " *   * ", " *   * ", " *   * "]
    for line in pattern:
        print(line)
    return pattern

# exercise_17()

def exercise_18():
    """Print the alphabet pattern 'D'."""
    pattern = [" **** ", " *   * ", " *   * ", " *   * ", " *   * ", " *   * ", " **** "]
    for line in pattern:
        print(line)
    return pattern

# exercise_18()

def exercise_19():
    """Print the alphabet pattern 'E'."""
    pattern = [" ***** ", " * ", " * ", " **** ", " * ", " * ", " ***** "]
    for line in pattern:
        print(line)
    return pattern

# exercise_19()

def exercise_20():
    """Print the alphabet pattern 'G'."""
    pattern = ["  ***  ", " *   * ", " * ", " * *** ", " *   * ", " *   * ", "  *** "]
    for line in pattern:
        print(line)
    return pattern

# exercise_20()
