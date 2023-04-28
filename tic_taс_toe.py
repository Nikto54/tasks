print(
    f'Для того чтобы ввести координаты своего значка,введите сначала номер ряда,\nа потом номер столбца. Например: 2 3')
field = [['o', 'o', 'o'],['o', 'o', 'o'],['o', 'o', 'o']]
count = 1


def print_field(field):
    print(f'    1 2 3')
    for i in range(len(field)):
        print(i + 1, ' ', *field[i])


def check(arr):
    while True:
        x, y = map(int,input().split())
        if x > 3 or y > 3 or x < 1 or y < 1:
            print('Координаты вне диапазона')
            continue
        elif arr[x-1][y-1] != 'o':
            print('Эта клетка занята.Введите другие значения')
            continue
        else:
            return x,y


def win(arr):
    if      arr[0][0] == arr[1][0] == arr[2][0] != 'o' or \
            arr[0][1] == arr[1][1] == arr[2][1] != 'o' or \
            arr[0][2] == arr[1][2] == arr[2][2] != 'o' or \
            arr[0][0] == arr[0][1] == arr[0][2] != 'o' or \
            arr[0][1] == arr[1][1] == arr[2][1] != 'o' or \
            arr[0][2] == arr[1][2] == arr[2][2] != 'o' or \
            arr[0][0] == arr[1][1] == arr[2][2] != 'o' or \
            arr[2][2] == arr[1][1] == arr[2][0] != 'o':
        return True
    else:
        return False


while count < 9:

    if count % 2 == 1:
        print('Ходят крестики.Введите координаты')
        x1, y1 = check(field)
        print(x1,y1)
        field[x1-1][y1-1]="X"
        print_field(field)
        count += 1
        if win(field):
            print('Победа крестиков')
            break
    else:
        print('Ходят нолики.Введите координаты')
        x1, y1 = check(field)
        field[x1 - 1][y1 - 1] = "0"
        print_field(field)
        count += 1
        if win(field):
            print('Победа ноликов')
            break

    if count == 9:
        print('Ничья')
