class Solution:
    def isValid(self, s: str) -> bool:
        dict1 = {')': '(', "}": "{", "]": "["}
        stack = []
        for char in s:
            if char in dict1.values():
                stack.append(char)
            elif char in dict1.keys():
                if stack == [] or dict1[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
    
            
        
