class Solution:
    def check_if_balanced(self, s):
        stack = []
        for ch in s:
            if ch in ["{", "(", "["]:
                stack.append(ch)
            else:
                if not stack:
                    return False
            if ch == "]" and stack[-1] != "[" or \
            ch == ")" and stack[-1] != "(" or \
            ch == "}" and stack[-1] != "}":
                return False

            stack.pop()

        return len(stack) == 0
