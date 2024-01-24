class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = list(s.split(" "))
        s_list.reverse()
        
        for i in range(len(s_list)):
            if(len(s_list[i]) != 0):
                return len(s_list[i])