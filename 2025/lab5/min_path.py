def construct_matrix_from_input():
    matrix_size = int(input())
    matrix = []

    # process input by row
    for row in range(matrix_size):
        row_input = input()
        row_clean = row_input.strip().rstrip(',').lstrip('[').rstrip(']')
        row_matrix = [int(num) for num in row_clean.split(',')]
        matrix.append(row_matrix) 

    return matrix

def display_pathlen_matrix(matrix, solution):
    display = []

    for i in range(len(matrix)):
        row_output = ""
        for j in range(len(matrix[i])):
            if (i, j) in solution:
                row_output += "● "
            elif matrix[i][j] == 1:
                row_output += "  "
            elif matrix[i][j] == 0:
                row_output += "█ "

        display.append(row_output)

    return display

def bfs_solution(matrix):
    queue = [] # list of paths
    visited = [] # list of coordinates

    queue.append([(0, 0)]) # source node, initial path
    visited.append((0, 0))

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    solution = []

    while (queue):
        curr_path = queue.pop()
        curr_row, curr_col = curr_path[-1]

        # check neighbors
        for (row_direction, col_direction) in directions:
            new_row = curr_row + row_direction
            new_col = curr_col + col_direction

            # conditions: out of bounds, path should be 1, visited
            if (new_row >= 0 and new_row < len(matrix)
                and new_col >= 0 and new_col < len(matrix)
                and matrix[new_row][new_col] == 1
                and (new_row, new_col) not in visited):

                visited.append((new_row, new_col))
                new_path = curr_path.copy()
                new_path.append((new_row, new_col))
                queue.insert(0, new_path)

                if (new_row == len(matrix)-1 and new_col == len(matrix)-1):
                    solution = new_path

    return solution


def main():
    num_testcases = int(input())
    solutions = []
    
    for _ in range(num_testcases):
        matrix = construct_matrix_from_input()
        solution = bfs_solution(matrix)
        display = display_pathlen_matrix(matrix, solution)
        solutions.append((len(solution), display))

    for (path_len, display) in solutions:
        print(path_len - 1)
        for row in display:
            print(row)

if __name__ == "__main__":
    main()