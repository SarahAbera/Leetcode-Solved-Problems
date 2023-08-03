class Solution:
    def closestPrimes(self, left: int, right: int) -> list[int]:
        sieve = [False] * (right+1)
        
        last_prime = -1
        result = [-1, -1]
        for p in range(2, right+1):
            if not sieve[p]:
                for p2 in range(p*2, right+1, p):
                    sieve[p2] = True
                if left <= p <= right:
                    if last_prime == -1:
                        last_prime = p
                    elif result == [-1, -1]:
                        result = [last_prime, p]
                    elif p - last_prime < result[1] - result[0]:
                        result = [last_prime, p]
                    last_prime = p
        return result
