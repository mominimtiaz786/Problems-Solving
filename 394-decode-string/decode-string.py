class Solution:
    def decodeString(self, s: str) -> str:
        N = len(s)
        if N < 4:  return s

        stack = []
        for i in range(N):
            ch = s[i]
            stack.append(ch)

            if stack[-1] == ']':
                string_to = stack.pop()

                x = ''
                while string_to[0] != '[': 
                    string_to = stack.pop() + string_to
                
                
                number = ""
                while stack and '0' <= stack[-1] <= '9':
                    number = stack.pop() + number
                
                number = int(number)

                stack.append(number*self.decodeString(string_to[1:-1]))
            
        return "".join(stack)
        # i = 0

        # while i < N:
        #     ch = s[i]
            
        #     if 'a' <= ch <= 'z':
        #         required_string+=ch
        #         i+=1

        #     elif '0' <= ch <= '9':
        #         j = i

        #         while s[j] != '[':  j+=1
                
        #         parsed_number = int(s[i:j])

        #         i=j+1

        #         count = 0
        #         j+=1
        #         while count:
        #             if s[j] == '[': count+=1
        #             if s[j] == ']': count-=1

        #             j+=1

        #         print(i,j)
        #         break
        #         string_to = s[i:j]
        #         required_string+=(parsed_number*self.decodeString(string_to))

        #         i = j

        # return required_string

        