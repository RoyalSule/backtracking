# Sudoku
board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9],
]

def show(board):
    for i in range(len(board)):
        if i % 3 == 0:
            print("+-------+-------+-------+")
        
        for j in range(len(board[0])):
            if j % 3 == 0:
                print( "| ", end="")
            
            if j == 8:
                print(str(board[i][j]) + " |")
            else:
                print(str(board[i][j]) + " ", end="")

    print("+-------+-------+-------+")

# +-------+-------+-------+
# | 5 3   |   7   |       | 
# | 6     | 1 9 5 |       |
# |   9 8 |       |   6   |
# +-------+-------+-------+
# | 8     |   6   |     3 |
# | 4     | 8   3 |     1 |
# | 7     |   2   |     6 |
# +-------+-------+-------+
# |   6   |       | 2 8   |
# |       | 4 1 9 |     5 |
# |       |   8   |   7 9 |
# +-------+-------+-------+

show(board)

def empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, col
            
    return None

def valid(board, num, pos):
    # Check row
    for j in range(len(board[0])): 
        if board[pos[0]][j] == num and pos[1] != j:
            return False
        
    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check 3x3 box
    box_x = pos[1] // 3 
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
            
    return True

def solve(board):
    find = empty(board)
    if not find:
        return True
    else:
        row, col = find

    for num in range(1, 10):
        if valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True
            
            board[row][col] = 0

    return False

solve(board)
show(board)

# Eight Queens Puzzle
def queens(n, i, a, b, c):
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a

for solution in queens(8, 0, [], [], []):
    print(solution)

# Subset Sum Problem

# Graph Coloring Problem

# Hamiltonian Path
