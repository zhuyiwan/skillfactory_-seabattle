from boards import Board, Dot, Ship
import exeptions
from players import AI, User

from random import randint

class Game:
    def __init__(self, size: int = 6) -> None:
        self.size = size
        human_board = self.random_board()
        ai_board = self.random_board()
        ai_board.hid = True

        self.ai_player = AI(ai_board, human_board)
        self.human_player = User(human_board, ai_board)

    def greet(self):
        print("-------------------")
        print("  Приветсвуем вас  ")
        print("      в игре       ")
        print("    морской бой    ")
        print("-------------------")
        print(" формат ввода: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")

    def loop(self):
        num = 0 
        while True:
            print("-"*20)
            print("Доска игрока")
            print(self.human_player.board)
            print("-"*20)
            print("Доска AI")
            print(self.ai_player.board)
            print("-"*20)
            if num % 2 == 0:
                print("Ход игрока")
                repeat = self.human_player.move()
            else:
                repeat = self.ai_player.move()
            
            if repeat:
                num -= 1

            if self.ai_player.board.defeat():
                print("Вы выиграли")
                break

            if self.human_player.board.defeat():
                print("ИИ победил")
                break
            
            num += 1

    def create_board(self):
        fleet = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size = self.size)
        attempts = 0
        for ship_lenght in fleet:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), int(ship_lenght), randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except exeptions.BoardWrongShipException:
                    pass
        board.begin()
        return board
    
    def random_board(self):
        board = None
        while board is None:
            board = self.create_board()
        return board
    
    def start(self):
        self.greet()
        self.loop()