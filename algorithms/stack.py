def stack_empty(stack):
    return True if len(stack) == 0 else False


def push(stack, x):
    stack.append(x)


def pop(stack):
    return stack.pop()


if __name__ == "__main__":
    stack = []
    push(stack, 0)
    push(stack, 1)
    print(stack)

    out = pop(stack)
    print(out)
    print(stack)