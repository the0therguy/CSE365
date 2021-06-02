grid = [
    [0, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 1],
]

col = []
column_col = []

for j in range(7):
    column_col.append(0)

for i in range(4):
    col.append(column_col)


def dfs(x, y):
    col[x][y] = 1
    # print(grid[x][y])

    if y - 1 >= 0 and grid[x][y - 1] == 1 and col[x][y - 1] == 0:
        print("yes")
        dfs(x, y - 1)

    elif y + 1 < len(grid[0]) and grid[x][y + 1] == 1 and col[x][y + 1] == 0:
        print("yes")
        dfs(x, y + 1)
    elif x - 1 >= 0 and grid[x - 1][y] == 1 and col[x][y] == 0:
        print("yes")
        dfs(x - 1, y)
    elif x + 1 < len(grid[0]) and grid[x + 1][y] == 1 and col[x + 1][y] == 0:
        print("yes")
        dfs(x + 1, y)
    else:
        print("wrong input")


endi = 0
endj = 6
# dfs(1, 0)
col[1][0] = True

print(col)
