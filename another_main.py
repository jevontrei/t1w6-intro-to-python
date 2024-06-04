import os
os.system('cls')
# ^ why don't this work?


# Variables

num1 = 5
num2 = 7

print(num1 + num2)

# Conventions
# snake_case for python variables
# camelCase for JavaScript
# PascalCase for classes in all languages
# kebab-case for ???

NUM30 = 27  # bad practice? equal to num30 or nah?

num2 = 1

print(num1 + num2)

# assign the value of num2 to num1
# num1 <- num2
num1 = num2
print(num1 + num2)

num3 = 5

num3 = num3 + 2
print(num3)

num3 += 3
print(num3)
total = num1 + num2 + num3
# String interpolation
print("The total addition is", total)
print(f"The total addition is {total}")
#  ^^ learn this. go with f string?


