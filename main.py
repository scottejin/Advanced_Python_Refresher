#Make Grid
grid = [["" for _ in range(25)] for _ in range(15)]
def setup_grid():
    for i in range(15):
        for j in range(25):
            grid[i][j] = "."
    grid[0][0] = "S"  # Start
    grid[14][24] = "E"  # End
setup_grid()
for row in grid:
    print(row)

#Making the algorithm


