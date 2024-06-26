
#practical 1.
Import math

def calculate_rectangle_area(length, width):
    return length * width

def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

def calculate_average_marks(subject1, subject2, subject3):
    return (subject1 + subject2 + subject3) / 3

def calculate_compound_interest(principal, rate, time):
    return principal * (pow((1 + rate / 100), time))

# 1.1
# Calculate area and perimeter of a rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = calculate_rectangle_area(length, width)
perimeter = calculate_rectangle_perimeter(length, width)
print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)

# 1.2 
#Calculate average marks of three subjects
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
average_marks = calculate_average_marks(subject1, subject2, subject3)
print("Average marks of three subjects:", average_marks)
#1.3
# Compute compound interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate: "))
time = float(input("Enter time period in years: "))
compound_interest = calculate_compound_interest(principal, rate, time)
print("Compound Interest:", compound_interest)
