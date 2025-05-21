def construct_matrix_from_input():
    
    matrix_size = int(input())
    matrix = []
    
    for _ in range(matrix_size):
        
        row_input = input()
        row_clean = row_input.strip().rstrip(',').lstrip('[').rstrip(']')
        row = [int(num) for num in row_clean.split(',')]
        matrix.append(row)
        
    return matrix


def debug_print_matrix(matrix, solution):
    
    display = []
    
    for i in range(len(matrix)):
        
        row_output = ""
        
        for j in range(len(matrix[i])):
            
            if ((i, j) in solution):
                row_output += "■ "
            elif (matrix[i][j] == 0):
                row_output += "▲ "
            else:
                row_output += "□ "
            
        display.append(row_output)
        
    return display

def bfs_shortest(matrix):
    import heapq

    queue = []
    visited = []

    heapq.heappush(queue, (0, [(0, 0)]))
    visited.append((0, 0))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    solution_weight = -1
    solution_path = []

    while (queue):
        curr_weight, curr_path = heapq.heappop(queue)
        curr_row, curr_col = curr_path[-1]

        for row_direction, col_direction in directions: 
            new_row = curr_row + row_direction
            new_col = curr_col + col_direction
            
            if (new_row >= 0 and new_row < len(matrix) and
                new_col >= 0 and new_col < len(matrix) and
                matrix[new_row][new_col] != 0 and 
                (new_row, new_col) not in visited
            ):
                visited.append((new_row, new_col))
                new_path = curr_path.copy()
                new_path.append((new_row, new_col))
                new_weight = curr_weight + matrix[new_row][new_col]
                heapq.heappush(queue, (new_weight, new_path))

                if (new_row == len(matrix) - 1 and new_col == len(matrix) - 1):
                    solution_weight = new_weight
                    solution_path = new_path

    return solution_weight, solution_path

def main():
    
    num_testcases = int(input())
    solutions = []
    
    for _ in range(num_testcases):
        matrix = construct_matrix_from_input()  
        weight, path = bfs_shortest(matrix)
        display = debug_print_matrix(matrix, path)
        solutions.append((weight, display))
    
    for weight, display in solutions:
        print(weight)
        for display_row in display:
            print(display_row)


if __name__ == "__main__":
    main()