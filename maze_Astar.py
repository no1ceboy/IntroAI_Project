from heapq import heappush, heappop

# Heuristic function: Manhattan distance for grid
def manhattan_heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, goal):
    # Open list (priority queue)
    open_list = []
    heappush(open_list, (0, start))  # (h_cost, node)
    print(open_list)
    # Dictionary to keep track of the best path
    came_from = {}
    
    # g_score: cost from start to node
    g_score = {start: 0}
    
    # f_score: estimated cost from start to goal
    f_score = {start: manhattan_heuristic(start, goal)}

    # A* algorithm
    while open_list:
        current_h, current_node = heappop(open_list)

        # If the goal is reached, reconstruct the path
        if current_node == goal:
            return reconstruct_path(came_from, current_node)

        # Explore neighbors (up, down, left, right)
        for neighbor in get_neighbors(maze, current_node):
            tentative_g_score = g_score[current_node] + 1  # Assuming uniform cost for each move

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = manhattan_heuristic(neighbor, goal)
                
                # Add neighbor to the open list
                heappush(open_list, (g_score[neighbor] + f_score[neighbor], neighbor))
                print(open_list)

    return "No solution"  # Return None if no path is found

def get_neighbors(maze, node):
    neighbors = []
    row, col = node
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
    for dr, dc in directions:
        r, c = row + dr, col + dc
        if 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] == 0:
            neighbors.append((r, c))
    return neighbors

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

path = astar(maze, start, goal)
print(path)