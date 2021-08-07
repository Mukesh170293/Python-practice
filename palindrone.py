class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for i in s:
            if(i.isalpha()):
                res = res+i.lower()
        if(res == res[::-1]):
            return True
        return False

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
