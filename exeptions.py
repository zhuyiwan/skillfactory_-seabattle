class BoardExeption(Exception):
    # Сюда необходимо добавить логер, чтобы все исключения записывались в файл
    # Нужно сделать это стандартным для всех классов.
    # указывать какой класс, в какой функции вызвал данное исключение.
    pass

class BoardOutExeption(BoardExeption):
    def __str__(self) -> str:
        return "Точка вне игровой доски"
    
class BoadrUsedExeption(BoardExeption):
    def __str__(self):
        return "Вы уже стреляли в данную точку"
    
class BoardWrongShipException(BoardExeption):
    pass