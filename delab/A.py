import heapq

# Goal state of the 8 puzzle
goal_state = [[1,2,3],[4,5,6],[7,8,0]]

# Function to find the position of a value in the goal state
def find_pos(value):
    for i in range(3):
        for j in range(3):
            if goal_state[i][j] == value:
                return (i, j)

# Heuristic: Manhattan distance
def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_i, goal_j = find_pos(val)
                distance += abs(goal_i - i) + abs(goal_j - j)
    return distance

# Function to generate next possible moves
def get_neighbors(state):
    neighbors = []
    # Find position of 0 (empty tile)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j

    directions = [(-1,0),(1,0),(0,-1),(0,1)]  # up, down, left, right
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# A* Search
def a_star(start_state):
    visited = set()
    heap = [(manhattan(start_state), 0, start_state, [])]

    while heap:
        f, g, state, path = heapq.heappop(heap)
        if state == goal_state:
            return path + [state]
        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        for neighbor in get_neighbors(state):
            heapq.heappush(heap, (g + 1 + manhattan(neighbor), g + 1, neighbor, path + [state]))
    return None

# Starting state of puzzle
start = [[1,2,3],[4,0,6],[7,5,8]]

# Solve and print steps
solution = a_star(start)
for step in solution:
    for row in step:
        print(row)
    print()
