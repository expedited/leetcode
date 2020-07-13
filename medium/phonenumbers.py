class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combos = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        # this is a recursive solution
        # take all the solutions from letterCombinations(digits[1:]) and then to each answer, append 
        # all the choices from digits[0]
        def helper(digits):
            if len(digits) == 0:
                return None
            if len(digits) == 1:
                return combos[digits[0]]
            prev = helper(digits[1:])
            newAnswers = []
            for combo in combos[digits[0]]:
                for soln in prev: 
                    newAnswers.append(combo + soln)
            return newAnswers
        return helper(digits)
