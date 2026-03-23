class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD=10**9+7

        even=(n+1)//2
        odd=(n)//2

        even_part=pow(5,even,MOD)
        odd_part=pow(4,odd,MOD)

        return (even_part*odd_part)%MOD