

# Write a Python program that prompts the user for a number, x, and displays a pyramid of numbers. 
# Each row in the pyramid should contain increasing numbers, starting from 1 up to x.
# Example: 

# Enter x: 5
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

pyramid_nb = int(input("Enter a number : "))
printing_lines = ""

for i in range(pyramid_nb):
    printing_lines += str(i+1) + " " # added one since it starts with Zero
    print(printing_lines)          