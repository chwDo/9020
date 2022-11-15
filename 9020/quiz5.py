import numpy as np
import queue



def display_leftmost_topmost_boundary(*grid):
    column_size = len(grid[0])
    row_size = len(grid)
    m = np.zeros(((row_size + 2), (column_size + 2)), dtype=int)
    answer_m = np.zeros(((row_size + 2), (column_size + 2)), dtype=int)
    for i in range(row_size):
        for j in range(column_size):
            if grid[i][j] == '*':
                m[i + 1][j + 1] = 1
    q = queue.Queue()
    for i in range(row_size):
        for j in range(column_size):
            if m[i][j] == 1:
                q.put((i, j))
                break
        if not q.empty():
            break

    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    while not q.empty():
        x, y = q.get()
        answer_m[x][y] = 1
        for i, j in directions:
            if m[x+i][y + j] == 1:
                m[x + i][y + j] = -1
                q.put((x + i, y + j))
    for i in range(row_size):
        for j in range(column_size):
            if m[i][j+1] and m[i][j-1] and m[i-1][j] and m[i+1][j]:
                answer_m[i][j] = 0

    for i in answer_m[1:-1]:
        print(' '.join('*' if _ == 1 else ' ' for _ in i[1:-1]))


def display(*grid):
    for i in grid:
        print(' '.join(_ for _ in i))


grid_1 = ('  *    ',
          ' ****  ',
          '*****  ',
          '****** ',
          ' ****  ',
          ' **    '
          )
grid_2 = ('      '
          , '  *  *'
          , ' ** **'
          , ' **** '
          , ' *****'
          , '   *  '
          , '**    '
          , '**    '
          , '      ')

display_leftmost_topmost_boundary(*grid_2)

