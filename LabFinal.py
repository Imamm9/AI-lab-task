# 1. Find and print the Python version that you are using.

import sys
import platform

print("Python version (sys):", sys.version)
print("Python version (platform):", platform.python_version())
print("-" * 50)  # Separator for better readability

# 2. Use the Python command help('modules') to find the available built-in modules.


print("-" * 50)  

# 3. Print a value without a newline or space.
print("This is printed without a newline or space.", end="")
print("\n" + "-" * 50)  # Moving to the next line and adding a separator

# 4. Take an integer value as input and determine whether it is an even or odd number.
#    Therefore, print an appropriate message (even/odd).

num = int(input("Enter an integer: "))  
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

print("-" * 50)

# 5. Swap the values of two variables without using a function.

a = input("Enter the first value: ")
b = input("Enter the second value: ")
a, b = b, a
print("After swapping without function:")
print("a =", a)
print("b =", b)

print("-" * 50)

# 6. Swap the values of two variables using a function.

def swap_values(x, y):
    return y, x

a = input("Enter the first value: ")
b = input("Enter the second value: ")
a, b = swap_values(a, b)
print("After swapping with function:")
print("a =", a)
print("b =", b)

print("-" * 50)

# 7. Print all even numbers from a given list of numbers in the same order.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers in the list:")
for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")  # Print on the same line
print("\n" + "-" * 50)  # Moving to the next line and adding a separator

# 8. Take a character as input and determine whether it is a vowel or not.

char = input("Enter a character: ").lower()
if char in 'aeiou':
    print(f"{char} is a vowel.")
else:
    print(f"{char} is not a vowel.")

print("-" * 50)
