 What paradigms does Python support?

- Functional: Every statement is treated as a mathematical equation and any form of state or mutable data are avoided. The main advantage of this approach is that there aren’t any side effects to consider. In addition, this coding style lends itself well to parallel processing because there is no state to consider. Many developers prefer this coding style for recursion and for lambda calculus.

- Imperative: Computation is performed as a direct change to program state. This style is especially useful when manipulating data structures and produces elegant, but simple, code.

- Object-oriented: Relies on data fields that are treated as objects and manipulated only through prescribed methods. Python doesn’t fully support this coding form because it can’t implement features such as data hiding. However, this remains a useful coding style for complex applications because it supports encapsulation (concept that binds together the data and functions that manipulate the data, and that keeps both safe from outside interference and misuse) and polymorphism(the ability to present the same interface for differing underlying forms (data types)). This coding style also favors code reuse.

- Procedural: Tasks are treated as step-by-step iterations where common tasks are placed in functions that are called as needed. This coding style favors iteration, sequencing, selection, and modularization.

What typing discipline does it follow?

dynamic:
- every variable name is (unless it is null) bound only to an object
- names are bound to objects at execution time by means of assignment statements, and it is possible to bind a name to objects of different types during the execution of the program

Is it a high or low level language?

high level

Does it have built in memory management and garbage collection?

memory management is built in but garbage collection is not

What languages was Python influenced by?

- ABC

Is it a compiled or interpeted language?

interpreted: easy to code, test, and change. However, it is not very efficient. The trade-off is machine resources for programmer time.

Does it have strong support for functional programming?

no

What's the deal with Python 2 vs Python 3?

There are subtle differences between the two. But the biggest difference is the print statement.

How do you open a REPL for Python?

use command 'python' in terminal

How does one execute a Python program?

use command 'python filename.py' in terminal


Read: The Zen of Python by Tim Peters

Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than right now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!

Hello World
Write a program in hello_world/hello_world.py that prints 'Hello, World!' to the standard output (terminal).

Fizzbuzz
Write a program in fizzbuzz/fizzbuzz.py that does the following:

For numbers 1 through 100, print fizz if the number is divisible by 3, buzz if the number is divisible by 5 and fizzbuzz if the number if the number is divisible by both 3 and 5. If the number isn't divisible by 3 or 5, just output the number itself.

The output should look something like 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 Fizz Buzz 16 17 Fizz...

Fibonacci
Write a program in fibonacci/fib.py that will output the N-th term of the Fibonacci sequence.

For example: print fib(6) should output 8.

Project Euler Problem 1
Project Euler's first problem is:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

Write the code to complete this in euler_1/sum_of_natural_numbers.py

Conclusion
How does Python compare to other langauges you've used? Which language is is closest to?
