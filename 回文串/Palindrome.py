class Solution:
    def isPalindrome(self, s: str) -> bool:
        if  len(s) == 0 :
            return True
        length = len(s)
        index_1, index_2 = 0, length - 1
        while index_1 < index_2:
            if not s[index_1].isalnum():
                index_1 += 1
                continue
            if not s[index_2].isalnum():
                index_2 -= 1
                continue
            if s[index_1].lower() != s[index_2].lower():
                return False
            else:
                index_1 += 1
                index_2 -= 1
        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        s1 = ""
        for i in s:
            if i.isalnum():
                s1 += i.lower()
        s2 = "".join(list(reversed(s1)))
        if s1 == s2:
            return True
        else:
            return False
