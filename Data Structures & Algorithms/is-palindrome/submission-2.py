class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean=s
        l, r = 0, len(clean)-1
        while l<r:
            if clean[l].isalnum():
                if clean[r].isalnum():
                    if clean[l].lower() == clean[r].lower():
                        l, r = l+1, r-1
                    else:
                        return False
                else:
                    r -= 1
            else:
                l += 1
        return True