class Solution:
    def reverse(self, x: int) -> int:
        signed = -1 if x < 0 else 1
        x = abs(x)
        x = str(x)
        x = x[::-1]
        x = x.strip()
        x = int(x) * signed

        return x if -2 ** 31 <= x <= 2 ** 31 - 1 else 0
        