class Solution:
    def compress(self, chars: list[str]) -> int:

        n = len(chars)
        index = 0
        i = 0
        while i < n :
            curr_char = chars[i]
            count  = 0
            while i < n and chars[i] == curr_char:
                count = count + 1
                i = i +1
            chars[index] = curr_char
            index = index + 1
            if count > 1:
                string_count = str(count)
                for char in string_count:
                    chars[index] = char
                    index = index + 1
        return index               
        