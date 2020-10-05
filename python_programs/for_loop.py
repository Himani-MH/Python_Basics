#!/usr/bin/python3

print("Enter the number whose multiples you want to find =")
number = int(input())
print("Enter the number of multiples you want to find =")
multiples = int(input())
for i in range(1, (multiples+1)):
    mul_table = number * i
    print("{} * {} = {}".format(number, i, mul_table))
