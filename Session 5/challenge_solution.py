class Things:
    def __init__(self, name, animate):
        print('A new thing was constructed!!')
        print('It is called %s!' % self.name)
        if self.animate:
            print('It is a living-thing!')
        else:
            print('It is a non-living thing!')

class Animate(Things):
    def breathe(self):
        print('I am breathing!')

    def grow(self):
        print('I am growing!')

    def eat(self):
        print('I am eating!')

class Animals(Animate):
    def move(self):
        print('I am moving!')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('I am feeding young with milk!')

class Giraffe(Mammals):
    def eat_leaves_from_trees(self):
        print('I am eating leaves from trees!')

    def role(self):
        print('I can do all of this!')
        self.move()
        self.feed_young_with_milk()
        self.eat_leaves_from_trees()
        self.eat()
        self.grow()
        self.breathe()
        print('And many more things!')

class Human(Animate):
    def move(self):
        print('I am moving!')
    
    def talk(self):
        print('I am talking!')

    #Change 1 - Creating the Dance Function
    def dance(self):
        print('This is my dance!')
        for i in range(3):
            self.move()
        print('My dance ends!')
    #End Change

    def role(self):
        print('I can do all of this!')
        self.move()
        self.talk()
        self.eat()
        self.grow()
        self.breathe()
        #Change 2 - Adding the Dance Function to the Role Function
        self.dance()
        #End Change
        print('And many more things!')

class Inanimate(Things):
    def role(self):
        print('Damn it! All I need to do is wait for an animate to use me... No free will...')

class Sidewalk(Inanimate):
    def stuff(self):
        print('A human walks on me near the roads')

class Building(Inanimate):
    def stuff(self):
        print('How rude of humans! They live inside me!')

sam = Human('Sam', True)
sam.role()
print('')
reginald = Giraffe('Reginald', True)
reginald.role()
print('')
mrsidewalk = Sidewalk('Mr Sidewalk', False)
mrsidewalk.stuff()
print('')
mrbuilding = Building('Mr Building', False)
mrbuilding.stuff()