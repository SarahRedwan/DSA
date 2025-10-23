class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # Convert string of digits into list of integers
        digits = [int(c) for c in s]
        
        # Continue reducing until only two digits remain
        while len(digits) > 2:
            # Compute the new list by summing adjacent pairs modulo 10
            digits = [(digits[i] + digits[i+1]) % 10 for i in range(len(digits) - 1)]
        
        # Check if the final two digits are equal
        return digits[0] == digits[1]
