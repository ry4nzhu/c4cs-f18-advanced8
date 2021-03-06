#!/usr/bin/env  python3
import math
import operator
import sys
from termcolor import colored,cprint

def calculate(arg):
    stack = []
    a = 1
    b = 2
    c = 3 #dummy element
    tokens = arg.split()

    for token in tokens:
        if token == '+':
    	    print("operator: ")
    	    cprint(token,'green')
        elif token == '-':
    	    print("operator: ")
    	    cprint(token,'green')
        elif token == '^':
    	    print("operator: ")
    	    cprint(token,'green')
        elif token == '*':
    	    print("operator: ")
    	    cprint(token,'green')
        elif token == '/':
            print("operator: ")
            cprint(token,'green')
        try:
            stack.append(int(token));

        except ValueError:
            val1 = stack.pop()
            val2 = stack.pop()
            if token == '+':
                result = val1 + val2
            elif token == '-':
                result = val2 - val1
            elif token == '^':
                result = operator.pow(val2,val1)
            elif token == '*':
                result = val1*val2
            elif token == '/':
                result = val2/val1
            stack.append(result)

    if len(stack) > 1:
        raise ValueError("Too many arguments on the Stack!!")
    return stack[0]

def main():
    while True:
        result = calculate(input("rpn calc> "))
        if result < 0:
        	print("result: ")
        	cprint(result,'red')
        else:
        	print("result: ")
        	print(result)

if __name__ == '__main__':
    main()
