class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(n):
            return int(max(str(n)) * len(str(n)))
        return sum(map(encrypt, nums))