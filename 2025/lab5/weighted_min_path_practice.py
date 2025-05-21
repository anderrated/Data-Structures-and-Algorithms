def construct_matrix_from_input():
    matrix_size = int(input())
    matrix = []

    # process matrix by row
    for row in range(matrix_size):
        row_input = input()
        row_clean = row_input.strip().rstrip(',').lstrip('[').rstrip(']')
        row_matrix = [int(num) for num in row_clean.split(',')]
        matrix.append(row_matrix)

    return matrix

def display_pathlen_matrix(matrix, solution):
    display = []
    position = {tuple(pos) for _,pos in solution}

    for i in range(len(matrix)):
        row_output = ""
        for j in range(len(matrix[i])):
            if (i, j) in position:
                row_output += "● "
            elif matrix[i][j] != 0:
                row_output += "  "
            elif matrix[i][j] == 0:
                row_output += "█ "

        display.append(row_output)

    return display

def bfs_pq_solution(matrix):
    import heapq
    p_queue = [] # list of total cost and path
    visited = [] # list of coordinates

    p_queue.append((0, [(0, 0)])) # total cost and then path of source node
    visited.append((0, 0))

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    solution = []

    while(p_queue):
        cost, curr_path = heapq.heappop(p_queue)
        curr_row, curr_col = curr_path[-1]

        for row_direction, col_direction in directions:
            new_row = curr_row + row_direction
            new_col = curr_col + col_direction

            # check conditions and mark visited
            if (new_row >= 0 and new_row < len(matrix)
                and new_col >= 0 and new_col < len(matrix)
                and matrix[new_row][new_col] != 0
                and (new_row, new_col) not in visited):
                    visited.append((new_row, new_col))
                    new_path = curr_path.copy()
                    new_path.append((cost + matrix[new_row][new_col], (new_row, new_col)))
                    p_queue.append(new_path)
                    heapq.heapify(p_queue)

                    if (new_row == len(matrix)-1 and new_col == len(matrix)-1):
                        solution = heapq.heappop(p_queue)
        
    return solution

def main():
    num_testcases = int(input())
    solutions = []

    for _ in range(num_testcases):
        matrix = construct_matrix_from_input()
        solution = bfs_pq_solution(matrix)
        display = display_pathlen_matrix(matrix, solution)
        solutions.append((len(solution), display))

    for path_len, display in solutions:
        print(path_len - 1)
        for row in display:
            print(row)

if __name__ == "__main__":
    main()