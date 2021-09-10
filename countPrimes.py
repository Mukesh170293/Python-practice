class Solution:
    def countPrimes(self, n):
        if(n==2):
            return 1
        if(n==3):
            return 2

        count = 2
        for m in range(4,n+1):
            if Solution.checkprime(self,m):
                count += 1
        return count
    def checkprime(self, m):
            for i in range(2,m//2 +1):
                if(m%i == 0):
                    return False
            return True

s = Solution()
print(s.countPrimes(5))
