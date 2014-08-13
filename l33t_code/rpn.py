import sys

__author__ = 'abhishekanurag'


def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token in ["+", "-", "*", "/"]:
            op1 = stack.pop()
            op2 = stack.pop()
            if token == "+":
                stack.append(op2 + op1)
            elif token == "-":
                stack.append(op2 - op1)
            elif token == "*":
                stack.append(op2 * op1)
            else:
                print op1*1.0
                print op2/op1
                print op2/(op1*1.0)
                print int(op2/(op1*1.0))
                stack.append(int(op2 / (op1*1.0)))
        else:
            stack.append(int(token))
    return stack.pop()


# Main
def main():
    s = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print evalRPN(s)
    print int(6/-132.0)


if __name__ == "__main__":
    sys.exit(main())