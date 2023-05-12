import random

class BoardOutException(Exception):
    pass


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Ship:
    def __init__(self, length, bow, direction):
        self.length = length
        self.bow = bow
        self.direction = direction
        self.lives = length

    def dots(self):
        ship_points = []
        for i in range(self.length):
            cur_x = self.bow.x + (i if self.direction == 0 else 0)
            cur_y = self.bow.y + (i if self.direction == 1 else 0)
            ship_points.append(Point(cur_x, cur_y))
        return ship_points


class Board:
    def __init__(self, hid=False):
        self.hid = hid
        self.ships = []
        self.cells = [['0' for _ in range(6)] for _ in range(6)]
        self.alive_ships = 0

    def contour(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots():
            for dx, dy in near:
                cur = Point(d.x + dx, d.y + dy)
                if not self.out(cur) and self.cells[cur.x][cur.y] != '*':
                    self.cells[cur.x][cur.y] = '.' if verb else '0'

    def add_ship(self, ship):
        for d in ship.dots():
            if self.out(d) or self.cells[d.x][d.y] in ['*', '.']:
                raise BoardOutException('Can\'t add ship')
        for s in ship.dots():
            self.cells[s.x][s.y] = '*'
        self.contour(ship)
        self.alive_ships += 1
        self.ships.append(ship)

    def out(self, d):
        return not (0 <= d.x < 6 and 0 <= d.y < 6)

    def shot(self, d):
        if self.out(d):
            raise BoardOutException('Point out of board')
        if self.cells[d.x][d.y] in ['*', '.']:
            raise BoardOutException('Already shot here')

        for ship in self.ships:
            if d in ship.dots():
                ship.lives -= 1
                self.cells[d.x][d.y] = 'X'
                if ship.lives == 0:
                    self.alive_ships -= 1
                    self.contour(ship, True)
                    return 'ship is destroyed'
                else:
                    return 'ship is damaged'

        self.cells[d.x][d.y] = '.'
        return 'miss'

    def display(self):
        for row in self.cells:
            for cell in row:
                if cell == '*' and self.hid:
                    print('0', end=' ')
                else:
                    print(cell, end=' ')
            print()


class Player:
    def __init__(self, board, enemy_board):
        self.board = board
        self.enemy_board = enemy_board

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                result = self.enemy_board.shot(target)
                print(result)
                return result != "miss"
            except BoardOutException as e:
                print(e)


class AI(Player):
    def ask(self):
        return Point(random.randint(0, 5), random.randint(0, 5))


class User(Player):
    def ask(self):
        while True:
            coords = input('Enter coordinates (x, y): ').split()
            if len(coords) != 2:
                print('Enter 2 numbers')
                continue
            x, y = coords
            if not (x.isdigit() and y.isdigit()):
                print('Enter numbers')
                continue
            x, y = int(x), int(y)
            return Point(x, y)


class Game:
    def __init__(self):
        player_board = self.random_board()
        ai_board = self.random_board()
        self.user = User(player_board, ai_board)
        self.ai = AI(ai_board, player_board)

    def random_board(self):
        lengths = [3, 2, 2, 1, 1, 1, 1]
        board = Board()
        attempts = 0
        for length in lengths:
            while True:
                attempts += 1
                if attempts> 2000:
                    return self.random_board()
                ship = Ship(length, Point(random.randint(0, 5), random.randint(0, 5)), random.randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardOutException:
                    pass
        return board

    def greet(self):
        print('Welcome to the game "Battleship"!')
        print('Enter the coordinates in the format: "x y"')
        print('Good luck!')

    def loop(self):
        num = 0
        while True:
            print('-' * 20)
            print('User board:')
            self.user.board.display()
            print('\nAI board:')
            self.ai.board.display()
            if num % 2 == 0:
                print('-' * 20)
                print("User's move:")
                repeat = self.user.move()
            else:
                repeat = self.ai.move()
                if repeat:
                    print("AI's move:")
            if self.ai.board.alive_ships == 0:
                print('User won!')
                break
            if self.user.board.alive_ships == 0:
                print('AI won!')
                break
            if not repeat:
                num += 1

    def start(self):
        self.greet()
        self.loop()


if __name__ == "__main__":
    game = Game()
    game.start()