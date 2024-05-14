class Solution:
    def compress(self, chars: list[str]) -> int:
        res = [chars[0]]

        count = 0

        for char in chars:
            if res[-1] == char:
                count += 1
            else:
                if count > 1:
                    for ch in str(count):
                        res.append(ch)
                res.append(char)
                count = 1

        if count > 1:
            for ch in str(count):
                res.append(ch)

        for i in range(len(res)):
            chars[i] = res[i]
        
        return len(res)    