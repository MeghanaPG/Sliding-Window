class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackVar = []
        for c in tokens:
            if c == "+":
                stackVar.append(stackVar.pop() + stackVar.pop())
            elif c == "*":
                stackVar.append(stackVar.pop() * stackVar.pop())
            elif c == "-":
                a, b = stackVar.pop(), stackVar.pop()
                stackVar.append(b-a)
            elif c == "/":
                a, b = stackVar.pop(), stackVar.pop()
                stackVar.append(int(b / a))
            else:
                stackVar.append(int(c)) 
        return stackVar[0]





