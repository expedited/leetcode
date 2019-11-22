class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        prev = []
        for curr in s:
            if curr in [')', '}', ']']:
                if len(prev) == 0:
                    return False
                else:
                    last = prev[-1]
                    if last == '(' and curr == ')':
                        del prev[-1]
                    elif last == '[' and curr == ']':
                        del prev[-1]
                    elif last == '{' and curr == '}':
                        del prev[-1]
                    else:
                        return False
            elif curr in ['(', '{', '[']:
                prev.append(curr)
            else:
                return False
        if len(prev) > 0:
            return False
        return True
