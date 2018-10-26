#!/usr/bin/env  python3

def calculate(arg):
    stack = []

    tokens = arg.split()

    for token in tokens:
        try:
            stack.append(int(token));
        except ValueError:
            val1 = stack.pop()
            val2 = stack.pop()
            if token == '+':
                result = val1 + val2
            elif token == '-':
                result = val2 - val1

            stack.append(result)
    
    return stack[0]

def main():
    while True:
        calculate(input("rpn calc> "))
        print(result)

if __name__ == '__main__':
    main()
