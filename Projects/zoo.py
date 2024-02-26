class Building:
  def __init__(self, name, color, object):
    self.name = name
    self.color = color
    self.object = object
    
  def building_name(self):
    print('This building is a', self.name)
    print("It's", self.color)
    print("It's selling", self.object)
    print('')
    
b1 = Building("Ticket booth", 'purple', 'tickets')
b2 = Building("Food booth", 'red','food')

class Park:
  def __init__(self, object, color, amount):
    self.object = object
    self.color = color
    self.amount = amount
    
  def park_object(self):
    print('This object is a', self.object)
    print("It's", self.color)
    print('There are', self.amount, 'of them')
    print('')
    
p1 = Park('Bench', 'white', '3')
p2 = Park('Waterfall', 'light grey', '1')
p3 = Park('Bin', 'grey', '2')
p4 = Park('Road', 'cream', '1')
p5 = Park('Trees', 'tree color 😎', '3')

class Animal:
  def __init__(self, name, type, amount, food):
    self.name = name
    self.type = type
    self.amount = amount
    self.food = food
    
  def animal_info(self):
    print("This is a", self.name)
    print('Its type is a', self.type)
    print('There are', self.amount, 'of them')
    
  def eating(self):
    print('The', self.name, 'is eating', self.food)
    print()
    
  def sleeping(self):
    print('The',self.name, 'is currently sleeping')
    print()
    
  def looking(self):
    print('The', self.name, 'is looking at people')
    print()
    
  def drinking(self):
    print('The', self.name, 'is drinking water')
    print()
    
a1 = Animal('Tiger', 'Mammal', '1', '')
a2 = Animal('Lion', 'Mammal', '2','')
a3 = Animal('Crocodile', 'Reptile', '1','')
a4 = Animal('Monkey', 'Mammal', '2', 'bananas')
a5 = Animal('Giraffe', 'Mammal', '1','')
a6 = Animal('Zebra', 'Mammal', '1','')

class Employee:
  def __init__(self, name, id, phone, depart):
    self.name = name
    self.id = id
    self.phone = phone
    self.depart = depart
  
  def introduce(self):
    print("Hi! I'm", self.name)
    print('My employee ID is',self.id)
    print('My phone number is', self.phone)
    print("I'm in department", self.depart)
    print('')

e1 = Employee('Jack', '8374859', '067xxxxxxx', 'Zookeeper')
e2 = Employee('James', '8162495', '081xxxxxxx', 'Zookeeper')
e3 = Employee('David', '8235902', '099xxxxxxx', 'Zookeeper')
e4 = Employee('Alisa', '8274567', '062xxxxxxx', 'Ticket seller')
e5 = Employee('Paul', '8120493', '094xxxxxxx', 'Car waver')
e6 = Employee('Felix', '87530495', '089xxxxxxx', 'Ticket checker')



print('Hi! Welcome to the Zoo :)')
print('There are Buildings, Animals, Park, Employees')
print()
print('Where would you like to check?')

while True:
    check = input('Type 1 for buildings, 2 for animals, 3 for park, 4 for employees')
    print()
    if check == ('1'):
        print('Buildings:')
        print('----------')
        b1.building_name()
        print('Tickets for adults: 150 Baht')
        print('Tickets for child: 30 Baht')
        print('Tickets for foreigner: 250 Baht')
        print()
        print()
        b2.building_name()
        print('Chips: 5-20 Baht')
        print('Water: 10 Baht')
        print()
        
    elif check == ('2'):
        print('Animals:')
        print('----------')
        a1.animal_info(), a1.looking()
        a2.animal_info(), a2.sleeping()
        a3.animal_info(), a3.sleeping()
        a4.animal_info(), a4.eating()
        a5.animal_info(), a5.looking()
        a6.animal_info(), a6.drinking()
        print()
        
    elif check == ('3'):    
        print('Park:')
        print('----------')
        p1.park_object()
        p2.park_object()
        p3.park_object()
        p4.park_object()
        p5.park_object()  
        print()
        
    elif check == ('4'):
        print('Employees:')
        print('----------')
        e1.introduce()
        e2.introduce()
        e3.introduce()
        e4.introduce()
        e5.introduce()
        e6.introduce()
        print()
        
    if check == "":
        print('Hope to see you soon!')
        break 
    

#not fully done yet