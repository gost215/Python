class Mealy:
    state = "A"

    def stop(self):
        if self.state == "A":
            self.state = "B"
            return 0
        if self.state == "F":
            self.state = "G"
            return 7
        if self.state == "G":
            self.state = "H"
            return 9
        if self.state == "H":
            self.state = "F"
            return 10
        if self.state == "E":
            self.state = "A"
            return 6
        else:
            raise KeyError

    def run(self):
        if self.state == "B":
            self.state = "C"
            return 1
        if self.state == "C":
            self.state = "D"
            return 2
        if self.state == "D":
            self.state = "E"
            return 3
        if self.state == "E":
            self.state = "F"
            return 5
        if self.state == "F":
            self.state = "A"
            return 8
        else:
            raise KeyError

    def race(self):
        if self.state == "D":
            self.state = "H"
            return 4
        if self.state == "H":
            self.state = "A"
            return 11

        else:
            raise KeyError


def main():
    o= Mealy()
    return o

o = main()
print(o.stop()) # 0
print(o.run()) # 1
print(o.run()) # 2
print(o.run()) # 3
print(o.run()) # 5
#print(o.race()) # KeyError
print(o.stop()) # 7
print(o.stop()) # 9
print(o.race()) # 11
print(o.stop()) # 0
print(o.run()) # 1
#print(o.race()) # KeyError
print(o.run()) # 2
print(o.race()) # 4
print(o.stop()) # 10
print(o.run()) # 8
#print(o.run()) # KeyError
print(o.stop()) # 0
