class Exeption():
    pass

class Dot():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    def __repr__(self):
        return f'{self.x},{self.y}'

class Ship():
    def __init__(self,start,l,orient):
        self.start=start
        self.l=l
        self.orient=orient
        self.lives=l
    def dots(self):
        dot=[]
        cur_x=self.start.x
        cur_y=self.start.y
        for i in range(self.l):
            if self.orient == 0:
                cur_x+=1
            if self.orient==1:
                cur_y+=1
            dot.append(Dot(cur_x,cur_y))
        return dot


class Board:
    def __init__(self, hid=False, size=6):
        self.size = size
        self.hid = hid


    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("■", "O")
        return res



