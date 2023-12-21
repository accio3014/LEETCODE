class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort(key=len)                  # Sorting for element lenght
        prefix = ""

        for i in range(len(strs[0])):       # Loop for minimum element lenght
            same = strs[0][i]
            for j in range(len(strs)):
                if(strs[j][i] != same):
                    return prefix
            prefix += same

        return prefix