class Solution:
    corresponding_paranthesis = {
        '(': ')',
        '{': '}', 
        '[': ']'
    }    

    def isValid(self, s: str) -> bool:
        paranthesis_stack = []

        for elem in s:
            last_elem = paranthesis_stack[-1] if paranthesis_stack else None
            if self.corresponding_paranthesis.get(last_elem, None) == elem:
                paranthesis_stack.pop()
            else:
                paranthesis_stack.append(elem)

        return not bool(paranthesis_stack)