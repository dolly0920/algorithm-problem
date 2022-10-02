import sys

sys.stdin = open("input.txt", "rt")

if __name__ == "__main__" :
    words = input()
    target = input()

    lastChar = target[-1]
    length = len(target)

    stack = []

    for char in words :
        stack.append(char)
        if char == lastChar and ''.join(stack[-length:]) == target :
            for _ in range (length) :
                stack.pop()

    print(''.join(stack) if stack else "FRULA")

