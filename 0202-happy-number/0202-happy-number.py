class Solution:
    def isHappy(self, n: int) -> bool:
        #n: 0, n: 1

        seen = set()

        while n != 1:
            if n in seen:
                return False
            seen.add(n)

            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10

            n = total

        return True