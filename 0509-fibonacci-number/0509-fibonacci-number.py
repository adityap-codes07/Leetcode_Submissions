class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        first = 0
        sec = 1
        for i in range(2, n + 1):
            next = first + sec
            first = sec
            sec = next
        return sec