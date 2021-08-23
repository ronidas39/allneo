
# Create abstract class to define the behavior

class Animal:
    def move(self):
        print('Everything must move!')
    def shout(self):
        pass


class Rat(Animal):
    def move(self):
        print('Slow Rat')

    def shout(self):
        print('Chi chi Rat')

class Monkey(Animal):
    def move(self):
        print('Jumping Monkey')


rat = Rat()
rat.move()
rat.shout()

chap = Monkey()
chap.move()
chap.shout()