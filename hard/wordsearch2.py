from collections import defaultdict

class Solution:

    def findWord(self, board, word, curr, seen):
        grid = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        if curr[0] >= len(board) or curr[0] < 0 :
            return False
        if curr[1] >= len(board[0]) or curr[1] < 0:
            return False
        if word != "" and board[curr[0]][curr[1]] != word[0]:
            return False
        word = word[1:]
        if word == "":
            return True
        newcopy = seen.copy()
        newcopy.append(curr)
        for x, y in grid:
            if (curr[0] + x, curr[1] + y) not in seen:
                if self.findWord(board, word, (curr[0] + x, curr[1] + y), newcopy) == True:
                    return True
        return False


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = []
        start = defaultdict(list)
        if board == None:
            return
        # 1) Put all letters into dict with position
        for x in range(len(board)):
            for y in range(len(board[0])):
                start[board[x][y]].append((x, y))
        seen = 0
        while seen != len(words):
            seen = 0
            for word in words:
                if word == None or word in dontuse:
                    continue
                first = word[0]
                for entry in start[first]:
                    if self.findWord(board, word, entry, [entry]) == True:
                        result.append(word)
                        break
                    else:
                        # don't try any words that contain this word
                        for word1 in words:
                            if word1.find(word) != -1:
                                words.remove(word1)
        return result


