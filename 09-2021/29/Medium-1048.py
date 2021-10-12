"""
https://leetcode.com/problems/longest-string-chain/

Similar problem: https://leetcode.com/problems/one-edit-distance/

"""

#Slow solution
class Solution:
    def longestStrChain(self, words) -> int:
        words.sort(key=lambda x: len(x))
        q = []
        words_s = set(words)

        def bfs():
            while q:
                size = len(q)
                counter[0] += 1
                for i in range(size):
                    word = q.pop(0)
                    for j in range(len(word)+1):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            new_word = word[:j] + c + word[j:]

                            if new_word in words_s:
                                words.remove(new_word)
                                words_s.remove(new_word)
                                q.append(new_word)

        best = 0
        for word in words:
            if word not in words_s: continue

            q, counter = [word], [0]
            bfs()
            best = max(best, counter[0])

        return best

#Fast Solution
class Solution:
    def longestStrChain(self, words) -> int:
        words.sort(key=lambda x: len(x), reverse=True)
        q = []
        words_s = set(words)

        def bfs():
            while q:
                size = len(q)
                counter[0] += 1
                for i in range(size):
                    word = q.pop(0)
                    for j in range(len(word)):
                        new_word = word[:j] + word[j+1:]
                        if new_word in words_s:
                            words.remove(new_word)
                            words_s.remove(new_word)
                            q.append(new_word)

        best = 0
        for word in words:
            if word not in words_s: continue

            q, counter = [word], [0]
            bfs()
            best = max(best, counter[0])

        return best

s = Solution()
print(s.longestStrChain(["a","b","ba","bca","bda","bdca"]))
