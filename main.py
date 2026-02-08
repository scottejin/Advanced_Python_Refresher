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

# For Mrs.F, attached is the website link for the following souurce...

# https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2 -> Website used for advice

# A* pathfinding notes (simple, step-by-step):

# 1) Make two lists: open_list (nodes to check) and closed_list (nodes already checked).

open_list = []
closed_list = []

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

    for current_list in range(0,len(open_list)): #loop...
        index_current = open_list[current_list] #Calling the list to retrieve the dict
        calling_dictionary = index_current['total_cost'] #Calling the index key with 'total cost'
        if calling_dictionary < current_lowest: #If checked cost is higher that the one already stored
            current_lowest = calling_dictionary #Setting current_lowest to the value stored
            current = index_current #Setting current to the cheapest path
        else:
            continue

    open_list.remove(current) #Removing current from unchecked nodes
    closed_list.append(current) #Adding current to checked nodes

# 6)   If current is the goal, stop and backtrack using parents to build the path.
    path = []

    if current['position'] == (14,24): #When current reaches the end
        while current is not None: # Checking if the parent position is existent or not after running the loop
            path.append(current['position']) #Appends the current loops position to path
            current = current['parent'] # Resetting path
        path.reverse()
        break


# 7)   Find all neighbors of current (up, down, left, right, etc.). Call them children.
    current_row, current_col = current['position']
    neighbours =[]


    # You can move Up/down/left/right
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for movable_directions in directions:
        new_row = current_row + movable_directions
        new_col = current_col + movable_directions

        if 0 <= new_row < 15 and 0 <= new_col <25:
            if grid[new_row][new_col] in['.','E']:
                neighbour_position = (new_row, new_col)
                already_checked = any(node['position'] == neighbour_position for node in closed_list)

                if not already_checked:
                    neighbours.append(neighbour_position)






# 8)   For each child:
# 9)     If child is already in closed_list, skip it and go to the next child.
# 10)    Compute costs:
# 11)      g = cost from start to child (current.g + step cost).
# 12)      h = estimated distance from child to goal.
# 13)      f = g + h.
# 14)    If child is already in open_list with a lower g, skip this child.
# 15)    Otherwise, set child's parent to current and add child to open_list.
