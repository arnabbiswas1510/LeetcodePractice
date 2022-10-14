"""
https://leetcode.com/problems/smallest-rotation-with-highest-score/
Explanation:

Related topics:
"""

def bestRotation(A):
    N = len(A)
    change = [1] * N
    for i in range(N): change[(i - A[i] + 1) % N] -= 1
    for i in range(1, N): change[i] += change[i - 1]
    return change.index(max(change))

print(bestRotation([2,3,1,4,0]))