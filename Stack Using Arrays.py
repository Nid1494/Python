from sys import maxsize


def createstack():
    stack1 = []
    return stack1


def isempty(stack2):
    return len(stack2) == 0


def push(stack3, item):
    stack3.append(item)
    print(item + " pushed to stack")


def pop(stack4):
    if isempty(stack4):
        return str(-maxsize - 1)
    return stack4[len(stack4) - 1]


stack = createstack()
push(stack, str(10))
push(stack, str(20))
push(stack, str(30))
push(stack, str(40))
print(pop(stack) + " popped from stack ")
