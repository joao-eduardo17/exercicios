# 1. Two Sum
def twoSum(nums: list[int], target: int) -> list[int]:
        l = []
        for i, c in enumerate(nums):
            for i1, k in enumerate(nums):
                if i == i1:
                    continue
                if (c + k) == target:
                    l.append(i)
                    l.append(i1)
                    break
            if len(l) > 0:
                break 
        return l

# 9. Palindrome Number
def isPalindrome(x: int) -> bool:
        return str(x) == str(x)[::-1]

# 344. Reverse String *daily
def reverseString(s: list[str]) -> None:
        x = ""
        for c in s:
            x+=c
        x = x[::-1]
        s.clear()
        for c in x:
            s.append(c)

# 1704. Determine if String Halves Are Alike
def halvesAreAlike(s: str) -> bool:
        a,b = s[0:len(s)//2], s[len(s)//2:]
        vog = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        v1,v2 = 0,0
        for c in a:
            if c in vog:
                v1+=1
        for c in b:
            if c in vog:
                v2+=1
        return v1 == v2

# 3110. Score of a String *daily
def scoreOfString(s: str) -> int:
        lista = [ord(c) for c in s]
        i = len(lista) - 1
        soma = 0
        for c in range(i):
            if c == i:
                break
            soma += abs(lista[c] - lista[c+1])
        return soma