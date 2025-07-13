from collections import defaultdict

class Solution:
    # take a look at the inputs and make sure you don't "."
    def checkRow(self,board:List[List[str]],i:int)-> bool:
        hist = defaultdict(int)

        row = board[i]

        for item in row:
            if item == ".":
                continue
            hist[item] +=1

        for key in hist.keys():
            val = hist[key]
            if val >=2:
                return False
        
        return True

    def checkColumn(self,board:List[List[str]],j:int)-> bool:
        hist = defaultdict(int)

        for i in range(9):
            # no easy way to get the column, so we need to iterate through the row
            item = board[i][j]
            if item == ".":
                continue
            hist[item] += 1

        for key in hist.keys():
            val = hist[key]
            if val >= 2:
                return False
        return True 

    def checkBox(self,board:List[List[str]],box:int)-> bool:
        hist = defaultdict(int)

        # mapping 0 - 8 
        row = (box // 3) * 3
        column = (box % 3) * 3

        for i in range(3):
            for j in range(3):
                item = board[row+i][column+j]
                if item == ".":
                    continue
                hist[item] += 1

        for key in hist.keys():
            val = hist[key]

            if val >= 2:
                return False

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            result = self.checkRow(board,i)
            if result == False:
                return False
        
        for j in range(9):
            result = self.checkColumn(board,j)
            if result == False:
                return False 
        
        for k in range(9):
            result = self.checkBox(board,k)
            if result == False:
                return False
        
        return True
        
        