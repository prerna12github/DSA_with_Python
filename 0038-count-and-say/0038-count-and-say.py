
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        say = self.countAndSay(n - 1)
        result = ""
        i = 0
        while i < len(say):
            ch = say[i]
            count = 1
            while i < len(say) - 1 and say[i] == say[i + 1]:
                count += 1
                i += 1
            result += str(count) + ch
            i += 1
        return result
