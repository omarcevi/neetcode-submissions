class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        for i, char in enumerate(s):
            if char in hashmap1:
                hashmap1[char]+=1
            else:
                hashmap1[char]=1
        for i, char in enumerate(t):
            if char in hashmap2:
                hashmap2[char]+=1
            else:
                hashmap2[char]=1
        return hashmap1==hashmap2