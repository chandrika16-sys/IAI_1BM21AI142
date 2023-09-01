from queue import PriorityQueue

def find_path(rows, cols, pacman_row, pacman_col, food_row, food_col, maze):
    # Define the movement directions (UP, DOWN, LEFT, RIGHT)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited = [[False] * cols for _ in range(rows)]

  
    priority_queue = PriorityQueue()
    priority_queue.put((0, pacman_row, pacman_col))  # (cost, row, column)

    parents = {}

    while not priority_queue.empty():
        cost, current_row, current_col = priority_queue.get()

 
        visited[current_row][current_col] = True

      
        if current_row == food_row and current_col == food_col:
            break

  
        for i in range(4):
            new_row, new_col = current_row + dr[i], current_col + dc[i]

            
            if 0 <= new_row < rows and 0 <= new_col < cols and maze[new_row][new_col] != '%' and not visited[new_row][new_col]:
                new_cost = cost + 1
                priority_queue.put((new_cost, new_row, new_col))
                parents[(new_row, new_col)] = (current_row, current_col)

    
    path = []
    while (food_row, food_col) != (pacman_row, pacman_col):
        path.append((food_row, food_col))
        food_row, food_col = parents[(food_row, food_col)]
    path.append((pacman_row, pacman_col))

    
    return len(path) - 1, list(reversed(path))


pacman_row, pacman_col = map(int, input().split())
food_row, food_col = map(int, input().split())
rows, cols = map(int, input().split())
maze = [input() for _ in range(rows)]


path_length, path = find_path(rows, cols, pacman_row, pacman_col, food_row, food_col, maze)


print(path_length)
for node in path:
    print(node[0], node[1])
