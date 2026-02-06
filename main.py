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

# For Mrs.F, attached is the website link for the following souurce... Bro, there is no way im coding this without guidance,
# Why is a* so hard ....

# https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2 -> Website used for advice

# A* pathfinding notes (simple, step-by-step):

# 1) Make two lists: open_list (nodes to check) and closed_list (nodes already checked).
open_list = []
closed_list = []

# 2) Put the start node into open_list with initial costs:
#    - Create a node for the start position (0, 0)
#    - Set g = 0 (no cost yet, we're at the start)
#    - Calculate h = Manhattan distance from start to goal
#    - Set f = g + h
#    - Set parent = None (start has no parent)
#    - Add this single node to open_list
position = 0

starting_node = {
    'position': (0,0),   # Starting pos ig?
    'actual_cost': 0,  # Cost so far
    'heuristic_cost': abs(0-14) + abs(0-24), # Goal distance as a absolute value
    'total_cost': abs(0-14) + abs(0-24), # How much distance still needed
    'parent': None # Which node told me to 'get to' this??
}
open_list.append(starting_node) # Did not know you could append a dictionary to a list.


while open_list != []:# While there are still nodes to look at run steps below:

    current_lowest = float('inf') # Set this to -inf and was confused for so long
    current = None

    for current_list in range(0,len(open_list)):
        index_current = open_list[current_list]
        calling_dictionary = index_current['total_cost']
        if calling_dictionary < current_lowest:
            current_lowest = calling_dictionary
            current = index_current
            #MORE CODE HERE
        else:
            continue


# 4)   Pick the node in open_list with the lowest f. Call it current. DONE



# 5)   Move current from open_list to closed_list.



# 6)   If current is the goal, stop and backtrack using parents to build the path.



# 7)   Find all neighbors of current (up, down, left, right, etc.). Call them children.



# 8)   For each child:
# 9)     If child is already in closed_list, skip it and go to the next child.
# 10)    Compute costs:
# 11)      g = cost from start to child (current.g + step cost).
# 12)      h = estimated distance from child to goal.
# 13)      f = g + h.
# 14)    If child is already in open_list with a lower g, skip this child.
# 15)    Otherwise, set child's parent to current and add child to open_list.
