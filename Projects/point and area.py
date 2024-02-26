import random

random_x1 = random.randint(1, 11)
random_y1 = random.randint(random_x1 + 1, 11)
random_x2 = random.randint(1, 11)
random_y2 = random.randint(random_y1 + 1, 11)


class Rectangle:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
    def is_inside(self, x, y):
        self.x = x
        self.y = y
        
        if self.x1 < self.x < self.x2 and self.y1 < self.y < self.y2:
            print("Your point is in the rectangle :)")
        else:
            print("Your point isn't in the rectangle :(")

        print("x1, y1:", (self.x1, self.y1))
        print('x2, y2:', (self.x2, self.y2))
        

    def is_area(self, guess):
        self.guess = guess 
        self.side1 = self.x2 - self.x1
        self.side2 = self.y2 - self.y1
        self.area  = self.side1 * self.side2
        
        if self.guess == self.area:
            print('You got the area right! :D')
            print('The area is', self.area)
            
        else:
            print('You got the area wrong >:(')
            print('The area is', self.area)


x_value = int(input("Enter your x value: "))
y_value = int(input("Enter your y value: "))

area_value = int(input('Enter the area of square: '))


p = Rectangle(random_x1,random_x2,random_y1,random_y2)

p.is_inside(x_value, y_value)
print()

p.is_area(area_value)