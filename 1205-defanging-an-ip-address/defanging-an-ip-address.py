class Solution:
    def defangIPaddr(self, address: str) -> str:
        ans=""
        for _ in address:
            if _ !=".":
                ans+=_
            else:
                ans+="[.]"

        return ans

        