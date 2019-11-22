class Solution:
    def helper(self, s, wordDict):
        if s == "":
            return True
        possible = []
        didMatch = 0
        for word in wordDict:
            if s.startswith(word):
                possible.append(self.helper(s.replace(word, '', 1), wordDict))
                didMatch = 1
        if didMatch == 0:
            return False
        return any(possible)


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        for item in wordDict:
            if item == "":
                wordDict.remove(item)

        if s == None or wordDict == None:
            return False

        return self.helper(s, wordDict)

