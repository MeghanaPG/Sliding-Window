class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #HASHMAP to store the close to open 
        closeToOpen = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for c in s:
            #below condition is if we have the close parenthesis 
            if c in closeToOpen:
                # we have to make sure that the stack is not empty and we have the corresponding open paranthesis 
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(c)
        # return True if stack is empty else false 
        return True if not stack else False 
        
        

