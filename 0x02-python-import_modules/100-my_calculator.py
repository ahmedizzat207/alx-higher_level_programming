#!/usr/bin/python3
def main():
    import sys
    import calculator_1
    opt = calculator_1
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if operator == "+":
        print("{} + {} = {}".format(a, b, opt.add(a, b)))
    elif operator == "-":
        print("{} - {} = {}".format(a, b, opt.sub(a, b)))
    elif operator == "*":
        print("{} * {} = {}".format(a, b, opt.mul(a, b)))
    elif operator == "/":
        print("{} / {} = {}".format(a, b, opt.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


if (__name__ == "__main__"):
    main()
