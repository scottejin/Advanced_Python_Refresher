#Make Grid
grid = [
    ["" for _ in range(15)],
    ["" for _ in range(15)],
    ["" for _ in range(15)],
    ["" for _ in range(15)],
    ["" for _ in range(15)],
    ["" for _ in range(15)],
    ["" for _ in range(15)],
    ["" for _ in range(15)],
]
def setup_grid():
    for i in range(8):
        for j in range(15):
            grid[i][j] = "."
    grid[0][0] = "S"  # Start
    grid[7][14] = "E"  # End
setup_grid()
for row in grid:
    print(row)



