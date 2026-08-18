class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        while n:
            bits.append(n%2)
            n=n//2
        bits = bits + [0]*(32-len(bits))
        bits=bits[::-1]
        m=0
        p=0
        for bit in bits:
            if bit:
                m+=pow(2, p)
            p+=1
        return m