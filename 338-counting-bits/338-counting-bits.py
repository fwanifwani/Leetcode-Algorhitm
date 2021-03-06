class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0]
        for i in range(1, num + 1):
            if i % 2 == 1:
                result.append(result[i - 1] + 1)
            else:
                result.append(result[i // 2])
        return result
        