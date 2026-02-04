#Make Grid
grid = [
    ["" for _ in range(10)],
    ["" for _ in range(10)],
    ["" for _ in range(10)],
    ["" for _ in range(10)],
    ["" for _ in range(10)],
    ["" for _ in range(10)],
]
def setup_grid():
    for i in range(6):
        for j in range(10):
            grid[i][j] = "."
    grid[0][0] = "S"  # Start
    grid[5][9] = "E"  # End
setup_grid()
for row in grid:
    print(row)



