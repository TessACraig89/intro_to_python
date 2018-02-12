'''Fibonacci
Write a program in fibonacci/fib.py that will output the N-th term of the Fibonacci sequence.
a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers. The simplest is the series 1, 1, 2, 3, 5, 8, etc.
For example: print fib(6) should output 8.'''

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

print(fibo(2))
