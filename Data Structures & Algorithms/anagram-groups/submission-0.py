class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_map = {str(sorted(strs[0])): [strs[0]],}
        for i in range(1, len(strs)):
            if str(sorted(strs[i])) in res_map.keys():
                res_map[str(sorted(strs[i]))].append(strs[i])
            else:
                res_map[str(sorted(strs[i]))] = [str(strs[i])]
        return [v for k, v in res_map.items()]

