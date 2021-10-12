"""
https://leetcode.com/problems/remove-comments/

We can build this state machine:

State 0: Not in coment
State 1: Got /, not in comment
State 2: Got /*, in comment, need to pop /* from the output
State 3: Got /* ...*, in comment
"""


class Solution:
    def removeComments(self, source):
        state = 0
        output = []
        buf = []
        for line in source:
            for char in line:
                if state not in (2,3):
                    buf.append(char)
                if state == 0 and char =='/':
                    state = 1
                elif state == 1:
                    if char == '/':
                        buf.pop()
                        buf.pop()
                        state = 0
                        break
                    elif char == '*':
                        buf.pop()
                        buf.pop()
                        state = 2
                    else:
                        state = 0
                elif state == 2 and char == '*':
                    state = 3
                elif state == 3:
                    if char == '/':
                        state = 0
                    elif char != '*':
                        state = 2
            if state in (0,1):
                l = ''.join(buf)
                if l: output.append(''.join(buf))
                buf = []
        return output


s = Solution()
print(s.removeComments(["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]))
