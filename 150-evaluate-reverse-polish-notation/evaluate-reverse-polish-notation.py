class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for letter in tokens:
            if letter.lstrip('-').isdigit():
                stack.append(int(letter))
            elif letter == '+':
                tmp = stack.pop()
                stack.append(stack.pop() + tmp)
            elif letter == '-':
                tmp = stack.pop()
                stack.append(stack.pop() - tmp)
            elif letter == '*':
                tmp = stack.pop()
                stack.append(stack.pop() * tmp)
            elif letter == '/':
                tmp = stack.pop()
                stack.append(int(stack.pop() / tmp))
            # print(stack)
        return stack.pop()