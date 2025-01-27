# Determine if a 9 x 9 Sudoku board is valid. 
# Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

board = [
["8","3","1",".","7",".",".",".","."]
,["6","4",".","1","9","5",".",".","."]
,[".","9",".",".",".",".",".","6","."]
,["1",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,["5","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,["2",".",".",".","8",".",".","7","9"]]

# First approach - solution
# def validSudoku(board):
#     colsDict = {key: set() for key in range(1, 10)}
#     rowsDict = {key: set() for key in range(1, 10)}
#     subgrids = {key: set() for key in range(9)}
#     for rowI, row in enumerate(board):
#         # visited = set()
#         for elemI, elem in enumerate(row):
#             subgrid_index = (rowI // 3) * 3 + (elemI // 3)

#             if(elem != "."):
#                 if(rowI in rowsDict[int(elem)]):
#                     print("Not Valid")
#                     return False
#                 if(elemI in colsDict[int(elem)]):
#                     print("Not Valid")
#                     return False
#                 if(int(elem) in subgrids[subgrid_index]):
#                     return False
                
                

#                 colsDict[int(elem)].add(elemI)
#                 rowsDict[int(elem)].add(rowI)
#                 subgrids[subgrid_index].add(int(elem))
#     return True
    

# Solution two - leetcode option - better solution/faster
def validSudoku2(board):
    N = 9
    # 9 rows, 9 columns, 9 subgrids
    rows = [set() for _ in range(N)]
    cols = [set() for _ in range(N)]
    boxes = [set() for _ in range(N)]

    # Rows loop
    for r in range(N):
        # Cols loops
        for c in range(N):
            
            val = board[r][c]
            if(val == '.'):
                continue
            
            # If the value is in the current row
            if(val in rows[r]):
                return False
            # Else we add it to the current row set 
            rows[r].add(val)
            
            # If the value is in the current col
            if(val in cols[c]):
                return False
            cols[c].add(val)
            
            subgrid_index = (r//3) * 3 + c // 3
            if(val in boxes[subgrid_index]):
                return False
            boxes[subgrid_index].add(val)
    return True

print(validSudoku2(board))
# Initial non working solution 
# def validSudoku(board):
#     dict = {key: [] for key in range(1, 10)}
#     for rowI, row in enumerate(board):
#         visited = set()
#         for index, el in enumerate(row):
#             if(el != "."):
#                 if(int(el) in visited):
#                     print("Not Valid")
#                     return False
                
#                 if(index in dict[int(el)]):
#                     print("Not Valid")
#                     return False
#                 if
#                 if(dict[int(el)]):
#                    if(index - 2 in dict[int(el)] or index - 1 in dict[int(el)]):
#                        print("Not Valid")
#                        return False
                
#                 dict[int(el)].append(index)
#                 visited.add(int(el))
#     return True
            



# between index 3 - 3 -> 0 : 3 

# RULE 1 -> Rows 
# | 0  | 1 | 2 | 3 | 4  | 5 | 6 | 7| 8 |
# if during iteration num in row, return False

# RULE 2 -> Cols
# | 0  | 1   | 2  | 3 | 4  | 5 | 6 | 7| 8 |
# 8,6   3,1,9  1,8   2   7,9  5     6
# break if another eight in row



# since 8 is in set, return False
# Rule 3 -> 3*3 
# Idea
# There can only be one number of each at each


# Rule1 -> each array must have unique numbers from 1 - 9
# Rule2 -> each index for each array must have unique numbers from 1 - 9 
# Rule3 -> arrays 0-2 -> index 0-2
#                 3-5 -> index 3-5
#                 6-8 -> index 6-8
# Those arrays and their indexes must have unique numbers from 1-9

