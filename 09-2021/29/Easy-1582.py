"""
https://leetcode.com/problems/special-positions-in-a-binary-matrix/

Similar problem: https://leetcode.com/problems/lonely-pixel-i/ (identical)
and more involved: https://leetcode.com/problems/lonely-pixel-ii/
"""

class Solution:
    def numSpecial(self, mat) -> int:

        M, N, result = len(mat), len(mat[0]), 0

        mat_t = list(zip(*mat)) # transpose

        #Below is quadratic time, can be optimized
        for i in range(M):
            for j in range(N):
                if mat[i][j] == 1 and \
                        sum(mat[i]) == 1 and \
                        sum(mat_t[j]) == 1:
                    result += 1

        return result

s = Solution()
mat = [[0,0,0,0,0],
       [1,0,0,0,0],
       [0,1,0,0,0],
       [0,0,1,0,0],
       [0,0,0,1,1]]
print(s.numSpecial(mat))
