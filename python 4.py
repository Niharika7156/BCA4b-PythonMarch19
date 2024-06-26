
# 4.2 Working of a while Loop with Numbers
num = 1
while num <= 5:
    print(num)
    num += 1
# 4.3 Working of break and continue statement
num = 0
while num < 10:
    num += 1
    if num == 5:
        continue  # Skip printing 5
    print(num)
    if num == 8:
        break  # Exit loop when num equals 8
        
# 4.4 Use of else statement with while and break
num = 1
while num <= 5:
    print(num)
    num += 1
else:
    print("While loop completed without breaking")
    
# 4.5 Compute the Sum of the Series 4 + 8 + 12 + … + 40
total = 0
num = 4
while num <= 40:
    total += num
    num += 4
print("Sum of the series:", total)

# 4.6 Display the Fibonacci sequences up to nth term
n = int(input("Enter the value of n: "))
a, b = 0, 1
count = 0
print("Fibonacci sequence:")
while count < n:
    print(a, end=' ')
    a, b = b, a + b
    count += 1
    
# 4.7 Print multiplication table of a number using for loop
num = int(input("Enter the number whose multiplication table you want to print: "))
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)

# 4.8 Print a Triangle Pattern
rows = int(input("Enter the number of rows for the triangle: "))
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2*i - 1))

# 4.9 Compute the Sum of the series 3 + 6 + 9 + … + 30
total = 0
for i in range(3, 31, 3):
    total += i
print("Sum of the series:", total)

# 4.10 Print the product of the series m = 15 * 13 * 11 * 9 * 7
product = 1
for i in range(15, 6, -2):
    product *= i
print("Product of the series:", product)

# 4.11 Compute factorial of a Number
num = int(input("Enter a number to compute factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is:", factorial)

# 4.13 Compute sum of first n natural numbers
n = int(input("Enter the value of n: "))
sum_of_natural_numbers = (n * (n + 1)) // 2
print("Sum of first", n, "natural numbers:", sum_of_natural_numbers)



# 4.12 Display the Cube of first 10 even numbers
for i in range(2, 21, 2):
    print("Cube of", i, ":", i ** 3)

# 4.14 Display 1 to 10 numbers in reverse order
for i in range(10, 0, -1):
    print(i)
    
# 4.15 Create a list of any specific size, arrange all the elements in ascending order,
# and display the list before and after sorting
size = int(input("Enter the size of the list: "))
my_list = []

# Input elements into the list
for i in range(size):
    element = int(input(f"Enter element {i + 1}: "))
    my_list.append(element)

print("List before sorting:", my_list)

# Sort the list
my_list.sort()

print("List after sorting:", my_list)
