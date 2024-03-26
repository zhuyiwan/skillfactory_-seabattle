from ships import Ship, Dot
import exeptions

class Board:
    def __init__(self, hid = False, size: int  = 6) -> None:
        self.size = size
        self.hid = hid

        self.count = 0

        self.field = [ [" "]*size for _ in range(size) ]
        
        self.busy = []
        self.ships = []
    
    def __str__(self):
        # res = "  | 1 | 2 | 3 | 4 | 5 | 6 | "
        # Меняем поле с заданого размера на размер заданный при создании класса.
       
        res = "  |" 
        for s in range(self.size):
            res += f" {s+1} |"

        res += "\n---" + "----"*self.size

        for i, row in enumerate(self.field):
            res += f"\n{i+1} | " + " | ".join(row) + " |"
        
        if self.hid:
            res = res.replace("■", " ")
        return res
    
    def miss_the_mark(self, d: Dot):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))
    
    def contour(self, ship: Ship, verb = False):
        near = [
            (-1, -1), (-1, 0) , (-1, 1),
            (0, -1), (0, 0) , (0 , 1),
            (1, -1), (1, 0) , (1, 1)
        ]

        for d in ship.dots:
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                if not(self.miss_the_mark(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = "·"
                    self.busy.append(cur)

    def add_ship(self, ship):
        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()
        for d in ship.dots:
            self.field[d.x][d.y] = "■"
            self.busy.append(d)
        
        self.ships.append(ship)
        self.contour(ship)

    
    def add_ship(self, ship: Ship):
        for d in ship.dots:
            if self.miss_the_mark(d) or d in self.busy:
                raise exeptions.BoardWrongShipException()
        for d in ship.dots:
            self.field[d.x][d.y] = "■"
            self.busy.append(d)
        
        self.ships.append(ship)
        self.contour(ship)

    def begin(self):
        self.busy = []

    def shoot(self, d: Dot):
        if self.miss_the_mark(d):
            raise exeptions.BoardOutExeption()
        
        if d in self.busy:
            raise exeptions.BoadrUsedExeption()
        
        self.busy.append(d)

        for ship in self.ships:
            if ship.got_hit(d):
                ship.lives -= 1
                self.field[d.x][d.y] = "X"
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb = True)
                    print ("Корабль уничтожен")
                    return False
                else:
                    print ("Корабль ранен")
                    return True
                
        self.field[d.x][d.y] = "·"
        print("Мимо")
        return False
    
    def defeat(self):
        return self.count == len(self.ships)
