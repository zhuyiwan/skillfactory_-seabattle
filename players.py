from dots import Dot
import exeptions
from random import randint

class Player:
    def __init__(self, board, enemy) -> None:
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()
    
    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shoot(target)
                return repeat
            except exeptions.BoardExeption as e:
                print(e)

class AI(Player):
    def ask(self):
        # Должен получать размер доски, чтобы понимать величину генерируемого числа
        # Желательно добавить добивание корабля
        # Можно сделать выбор уровня сложности
        d = Dot(randint(0, 5), randint(0,5))
        return d

class User(Player):
    def ask(self):
        while True:
            coords = input("Ходите: ").split()
            x,y = coords

            if len(coords) != 2:
                print(" Введите 2 координаты! ")
                continue
            
            x, y = coords
            
            if not(x.isdigit()) or not(y.isdigit()):
                print(" Введите числа! ")
                continue
            
            x, y = int(x), int(y)
            
            return Dot(x-1, y-1)