class Stack:
    def __init__(self):
        self.stack = []

    def is_null(self):
        return len(self.stack) == 0

    def clear(self):
        self.stack.clear()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()


class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.push(c)
            elif stack.is_null():
                return False
            elif c == ")":
                if stack.pop() != "(":
                    stack.clear()
                    return False
            elif c == "}":
                if stack.pop() != "{":
                    stack.clear()
                    return False
            elif c == "]":
                if stack.pop() != "[":
                    stack.clear()
                    return False
        return stack.is_null()
