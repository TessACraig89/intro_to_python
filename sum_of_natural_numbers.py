'''Project Euler Problem 1
Project Euler's first problem is:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

Write the code to complete this in euler_1/sum_of_natural_numbers.py'''

def euler(number):
    sum_of_natural_numbers = []
    for i in range (0, number):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_natural_numbers.append(i);
    print(sum(sum_of_natural_numbers))

euler(1000);
