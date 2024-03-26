from dots import Dot

class Ship:
    def __init__(self, head, lenght, orientation) -> None:
        self.head = head                # Dot
        self.lenght = lenght            # int
        self.orientation = orientation  # bool
        self.lives = lenght

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.lenght):
            cur_x = self.head.x
            cur_y = self.head.y

            if self.orientation:
                cur_x += i

            else:
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots
    
    def got_hit(self, shot):
        return shot in self.dots
    
    def __str__(self) -> str:
        return f"Dot:({self.head.x}, {self.head.y}, L: {self.lenght})"