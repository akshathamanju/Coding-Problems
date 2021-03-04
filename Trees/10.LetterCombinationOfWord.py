class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:  # if no digits then return
            return []
        # hashmap for possible combinations of digit and letter
        m = {"2": "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
        ret = []  # list to store all possible digits in the path
        self.dfs(m, digits, "", ret)
        return ret

    def dfs(self, m, digits, path, ret):
        if not digits:
            ret.append(path)
            return
        for c in m[digits[0]]:
            self.dfs(m, digits[1:], path + c, ret)


'''
Time complexity : O(3**N ×4**M) where N is the number of digits 
in the input that maps to 3 letters (e.g. 2, 3, 4, 5, 6, 8) and M is the number of digits
in the input that maps to 4 letters (e.g. 7, 9), and N+M is the total number digits in the input.

Space complexity :O(3 **N ×4**M ) since one has to keep 3^N * 4^M solutions.
'''