import random, time, copy
import os

w = 6
h = 6
live = "🟩"
dead = "⬛"
next_cells = []


for i in range(w):
    col = []
    for j in range(h):
        if random.randint(0, 1) == 0:
            col.append('e')  #alive cell`
        else:
            col.append(' ')  #dead cell
    next_cells.append(col)

while True:

    curr_cells = copy.deepcopy(next_cells)

    for y in range(h):
        for x in range(w):
            print(live if curr_cells[x][y] == 'e' else dead, end='')
        print()
    print('--' * w)

    for x in range(w):
        for y in range(h):
            lcord = (x - 1) % w
            rcord = (x + 1) % w
            abovecord = (y - 1) % h
            bcord = (y + 1) % h

            num_neighbors = 0
            if curr_cells[lcord][abovecord] == "e":
                num_neighbors += 1
            if curr_cells[x][abovecord] == "e":
                num_neighbors += 1
            if curr_cells[rcord][abovecord] == "e":
                num_neighbors += 1
            if curr_cells[lcord][y] == "e":
                num_neighbors += 1
            if curr_cells[rcord][y] == "e":
                num_neighbors += 1
            if curr_cells[lcord][bcord] == "e":
                num_neighbors += 1
            if curr_cells[x][bcord] == "e":
                num_neighbors += 1
            if curr_cells[rcord][bcord] == "e":
                num_neighbors += 1

            if curr_cells[x][y] == "e" and num_neighbors in (2, 3):
                next_cells[x][y] = "e"
            elif curr_cells[x][y] == " " and num_neighbors == 3:
                next_cells[x][y] = "e"
            else:
                next_cells[x][y] = " "

    time.sleep(1)
