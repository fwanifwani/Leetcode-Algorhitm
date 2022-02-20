class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2) # 10진수로 변경
        b = int(b,2)

        return format(a+b,'b')
        