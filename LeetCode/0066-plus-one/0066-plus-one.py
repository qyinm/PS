class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        
        for i in range(len(digits)-1, -1, -1):
            value = digits[i] + carry
            digits[i] = value % 10
            carry = value // 10
        if carry == 1:
            digits.insert(0, 1)
        
        return digits