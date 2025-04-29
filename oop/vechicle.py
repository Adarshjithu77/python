class vechicle:
    def engine(self):
        print('engine')
    def keys(self):
        print('keys')
    def wheels(self):
        print('wheels')
    def seats(self):
        print('seats')

class car(vechicle):
    def engine(self):
        print('engine')
    def wheel(self):
        print('4wheel')
    def key(self):
        print('key')
    def seat(self):
        print('5seats')

swift=car()
swift.engine()
swift.key()
swift.seat()
swift.wheel()
