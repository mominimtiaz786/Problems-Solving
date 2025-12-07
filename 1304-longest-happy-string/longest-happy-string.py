class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        counter = {'a': a, 'b': b, 'c': c}
        
        req_string = ""
        last_two = ""

        chars = "".join(sorted(
            [ch for ch in 'abc' if counter[ch]],
            key = lambda x: (counter[x], x),
            reverse = True
        ))

        for i in range(a+b+c):
            valid_choices = [
                ch for ch in chars
                if counter[ch] and 2*ch != last_two
                ]

            if not valid_choices:   break

            choice = sorted(valid_choices,
                key = lambda x: (counter[x], x),
                reverse = True
            )[0]
            
            req_string+=choice
            counter[choice]-=1
            last_two = last_two[-1]+ choice if len(last_two) == 2 else last_two+ choice

        return req_string