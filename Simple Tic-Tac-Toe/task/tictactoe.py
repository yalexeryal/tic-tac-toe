elements = ' ' * 9

grid = []
for i in range(0, 8, 3):
    grid.append([ch for ch in elements[i:i + 3]])


def show_grid(grid):
    print('---------')
    print('|', " ".join(grid[0]), '|')
    print('|', " ".join(grid[1]), '|')
    print('|', " ".join(grid[2]), '|')
    print('---------')


show_grid(grid)

while True:
    straights = [elements[:3], elements[3:6], elements[6:], elements[0:9:3], elements[1:9:3], elements[2:9:3],
                 elements[0:9:4],
                 elements[2:7:2]]
    if 'XXX' in straights:
        print('X wins')
        break
    elif 'OOO' in straights:
        print('O wins')
        break
    elif elements.count(' ') == 0:
        print('Draw')
        break
    try:
        first_cor, second_cor = map(int, input('Enter the coordinates: ').split())
    except:
        print("You should enter numbers!")
    else:
        if first_cor not in [1, 2, 3] or second_cor not in [1, 2, 3]:
            print("Coordinates should be from 1 to 3!")
        elif grid[int(first_cor) - 1][int(second_cor) - 1] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            grid[int(first_cor) - 1][int(second_cor) - 1] = "X"
            ind = ((int(first_cor) - 1) * 3) + int(second_cor) - 1
            elements = elements[:ind] + "X" + elements[ind:]
            show_grid(grid)
