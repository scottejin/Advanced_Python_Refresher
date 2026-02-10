import random as rnd

# Grid dimensions
ROWS = 30 # sets row
COLS = 35 # sets columns ....

#Make Grid
grid = [["" for _ in range(COLS)] for _ in range(ROWS)]

def setup_grid():
    for i in range(ROWS):
        for j in range(COLS):
            grid[i][j] = "."
    grid[0][0] = "S"  # Start
    grid[ROWS - 1][COLS - 1] = "E"  # End
setup_grid()

def run_a_star(grid):
    # 1) Make two lists: open_list (nodes to check) and closed_list (nodes already checked).
    open_list = []
    closed_list = []

    starting_node = {
        'position': (0,0),   # Starting pos
        'actual_cost': 0,  # Cost so far
        'heuristic_cost': abs(0-(ROWS - 1)) + abs(0-(COLS - 1)), # Goal distance as a absolute value
        'total_cost': abs(0-(ROWS - 1)) + abs(0-(COLS - 1)), # How much distance still needed
        'parent': None # Which node told me to 'get to' this??
    }

    open_list.append(starting_node) # Did not know you could append a dictionary to a list.

    found_path = None  # Store the final path once found

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

        if current['position'] == (ROWS - 1, COLS - 1): #When current reaches the end
            while current is not None: # Checking if the parent position is existent or not after running the loop
                path.append(current['position']) #Appends the current loops position to path
                current = current['parent'] # Resetting path
            path.reverse() # reverse as this is now the end
            found_path = path #saving to global variable
            break


    # 7)   Find all neighbors of current (up, down, left, right, etc.). Call them children.
        current_row, current_col = current['position'] # saving (x,y) to x y
        neighbours =[] #neighbours to current


        # You can move Up/down/left/right
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        for movable_directions in directions:
            new_row = current_row + movable_directions[0] #down up
            new_col = current_col + movable_directions[1] # Left right

            if 0 <= new_row < ROWS and 0 <= new_col < COLS: # if they are in the grid
                if grid[new_row][new_col] in['.','E']:
                    neighbour_position = (new_row, new_col)
                    already_checked = any(node['position'] == neighbour_position for node in closed_list)

                    if not already_checked: # if not in already checked
                        neighbours.append(neighbour_position) # append tgo positions in neighbour


        for neighbour in neighbours:
            actual_cost = current['actual_cost'] + 1 #Cost of moving one grid square
            heuristic_cost = abs(neighbour[0] - (ROWS - 1)) + abs(neighbour[1] - (COLS - 1)) #Absolute -> cost to end
            total_cost = actual_cost + heuristic_cost #Adding together == Cost predicted at end

            found = None # No match found yet
            for path in open_list:
                if path['position'] == neighbour: #if calling dict with kky == value of neighbour
                    found = path #Set found to the value of the dict in open_list
                    break

            if found is not None:  # If we find a path already in list
                if actual_cost < found['actual_cost']: # Is cheaper or not?
                    found['actual_cost'] = actual_cost
                    found['heuristic_cost'] = heuristic_cost
                    found['total_cost'] = total_cost
                    found['parent'] = current
                continue

            open_list.append({ #Appending to the list the value of the final dict
                'position': neighbour,
                'actual_cost': actual_cost,
                'heuristic_cost': heuristic_cost,
                'total_cost': total_cost,
                'parent': current
            })

    return found_path


user_seed = input('What seed do you want to enter? ')

if user_seed.strip().isdigit(): #Needed some ASSISTANCE to do this, i had no idea what this meant
    rnd.seed(int(user_seed))

obstacles = 0
final_path = None #temp var
max_obstacles = (ROWS * COLS) // 2 + ROWS # Makes obstacle generation cooler, serious talk == better as they scale to the requirements
while obstacles < max_obstacles:
    empty_cells = [
        (i, j)
        for i in range(ROWS)
        for j in range(COLS)
        if grid[i][j] == "."
    ]
    if not empty_cells:
        break

    r, c = rnd.choice(empty_cells) #picking random to assign obstacle
    grid[r][c] = "x"

    final_path = run_a_star(grid) #running the final path to retrieve result
    if final_path is None:
        grid[r][c] = "."  # Remove the obstacle that blocked the path
        continue

    obstacles += 1 # adding one to sum obstacle count

final_path = run_a_star(grid)
if final_path is None:
    print("No path found.") # Won't happen, but just to tick off an optional task in teams
else:
    for r, c in final_path: # setting the variables to improve readability '#' and  '*' was bad
        if grid[r][c] == ".":
            grid[r][c] = "@"
    for row in grid:
        print(row) # showing result

#BELOW IS MY ORIGINAL CODE BEFORE USING FUNCTIONS

# 1) Make two lists: open_list (nodes to check) and closed_list (nodes already checked).
#
# open_list = []
# closed_list = []
#
# position = 0
#
# starting_node = {
#     'position': (0,0),   # Starting pos ig?
#     'actual_cost': 0,  # Cost so far
#     'heuristic_cost': abs(0-14) + abs(0-24), # Goal distance as a absolute value
#     'total_cost': abs(0-14) + abs(0-24), # How much distance still needed
#     'parent': None # Which node told me to 'get to' this??
# }
#
# open_list.append(starting_node) # Did not know you could append a dictionary to a list.
#
# found_path = None  # Store the final path once found
#
# while open_list != []:# While there are still nodes to look at run steps below:
#
#     current_lowest = float('inf') # Set this to -inf and was confused for so long
#     current = None
#
#     for current_list in range(0,len(open_list)): #loop...
#         index_current = open_list[current_list] #Calling the list to retrieve the dict
#         calling_dictionary = index_current['total_cost'] #Calling the index key with 'total cost'
#         if calling_dictionary < current_lowest: #If checked cost is higher that the one already stored
#             current_lowest = calling_dictionary #Setting current_lowest to the value stored
#             current = index_current #Setting current to the cheapest path
#         else:
#             continue
#
#     open_list.remove(current) #Removing current from unchecked nodes
#     closed_list.append(current) #Adding current to checked nodes
#
# # 6)   If current is the goal, stop and backtrack using parents to build the path.
#     path = []
#
#     if current['position'] == (14,24): #When current reaches the end
#         while current is not None: # Checking if the parent position is existent or not after running the loop
#             path.append(current['position']) #Appends the current loops position to path
#             current = current['parent'] # Resetting path
#         path.reverse()
#         found_path = path
#         break
#
#
# # 7)   Find all neighbors of current (up, down, left, right, etc.). Call them children.
#     current_row, current_col = current['position']
#     neighbours =[]
#
#
#     # You can move Up/down/left/right
#     directions = [(-1,0),(1,0),(0,-1),(0,1)]
#     for movable_directions in directions:
#         new_row = current_row + movable_directions[0]
#         new_col = current_col + movable_directions[1]
#
#         if 0 <= new_row < 15 and 0 <= new_col <25:
#             if grid[new_row][new_col] in['.','E']:
#                 neighbour_position = (new_row, new_col)
#                 already_checked = any(node['position'] == neighbour_position for node in closed_list)
#
#                 if not already_checked:
#                     neighbours.append(neighbour_position)
#
#
#     for neighbour in neighbours:
#         actual_cost = current['actual_cost'] + 1 #Cost of moving one grid square
#         heuristic_cost = abs(neighbour[0] - 14) + abs(neighbour[1] - 24) #Absolute -> cost to end
#         total_cost = actual_cost + heuristic_cost #Adding together == Cost predicted at end
#
#         found = None # No match found yet
#         for path in open_list:
#             if path['position'] == neighbour: #if calling dict with kky == value of neighbour
#                 found = path #Set found to the value of the dict in open_list
#                 break
#
#         if found is not None:  # If we find a path already in list
#             if actual_cost < found['actual_cost']: # Is cheaper or not?
#                 found['actual_cost'] = actual_cost
#                 found['heuristic_cost'] = heuristic_cost
#                 found['total_cost'] = total_cost
#                 found['parent'] = current
#             continue
#
#         open_list.append({ #Appending to the list the value of the final dict
#             'position': neighbour,
#             'actual_cost': actual_cost,
#             'heuristic_cost': heuristic_cost,
#             'total_cost': total_cost,
#             'parent': current
#         })
