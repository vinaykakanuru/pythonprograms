# A given matrix consists of 1's and 0's with uneven heights and widths. 1 is being a part of river
# if two 1's are adjacent horizontally/vertically then it forms a river.
# We need to find length of rivers present in the given matrix.

# input
matrix = [[1, 0, 0, 1, 0],
          [1, 0, 1, 0, 0],
          [0, 0, 1, 0, 1],
          [1, 0, 1, 0, 1],
          [1, 0, 1, 1, 0]]

# Note: Output need to be in any order
# sample_otput = [1, 5, 2, 2, 2]


def river_sizes(matrix):
    marked = set()
    rivers = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1 and (row, col) not in marked:
                cur_river_len = 1
                marked.add((row, col))
                stack = [(row, col)]

                while stack:
                    current = stack.pop()
                    neighbours = get_neighbours(current, matrix)
                    for n in neighbours:
                        y, x = n
                        if matrix[y][x] == 1 and (y, x) not in marked:
                            marked.add((y, x))
                            cur_river_len += 1
                            stack.append((y, x))
                rivers.append(cur_river_len)
    return rivers


def get_neighbours(pos, matrix):
    y, x = pos
    ns = []

    if x >= 1:  # left
        ns.append((y, x-1))
    if x < len(matrix[0])-1:
        ns.append((y, x+1))
    if y >= 1:  # rights
        ns.append((y-1, x))
    if y < len(matrix)-1:
        ns.append((y+1, x))

    return ns


print(river_sizes(matrix))
