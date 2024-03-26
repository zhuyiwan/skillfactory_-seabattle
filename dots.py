class Dot:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Dot({self.x}, {self.y})"
    
    def __eq__ (self, dompare_dot) -> str:
        # Сюда необходимо вставить проверку на класс.
        # Сравнение возможно только между двух одинаковых классов
        return self.x == dompare_dot.x and self.y == dompare_dot.y