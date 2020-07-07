from collections import defaultdict

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        while True:
            canCrush = False
            toCrush = defaultdict(set)
            # check horiz
            for row in range(len(board)):
                prev = -1
                matched = False
                for col in range(len(board[0])):
                    curr = board[row][col]
                    if curr == prev and curr != 0:
                        if matched == True:
                            toCrush[col].add(row)
                            toCrush[col-1].add(row)
                            toCrush[col-2].add(row)
                            canCrush = True
                        else:
                            matched = True
                    else:
                        prev = curr
                        matched = False
            # check vertical
            for col in range(len(board[0])):
                prev = -1
                matched = False
                for row in range(len(board)):
                    curr = board[row][col]
                    if curr == prev and curr != 0:
                        if matched == True:
                            toCrush[col].add(row)
                            toCrush[col].add(row-1)
                            toCrush[col].add(row-2)
                            canCrush = True
                        else:
                            matched = True
                    else:
                        prev = curr
                        matched = False
            
            if canCrush:
                for col in range(len(board[0])):
                    if col in toCrush:
                        for val in toCrush[col]:
                            board[val][col] = 0
                        nonZeros = []
                        for row in reversed(range(len(board))):
                            if board[row][col] != 0:
                                nonZeros.append(board[row][col])
                        diff = len(board) - len(nonZeros)
                        nonZeros = nonZeros + ([0] * diff)
                        curr = 0
                        for row in reversed(range(len(board))):
                            board[row][col] = nonZeros[curr]
                            curr += 1
            else: 
                return board

            
    # recognize that i can crush either horizontally or vertically, consider these seperately, then combine to identify all the blocks that need to be crushed. add to a dictionary that maps the column to different rows, so you go down the list and 
