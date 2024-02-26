class Roommate:
    def __init__(self,name,days):
        self.name = name
        self.days = days

class Dorm:
    def __init__(self,price):
        self.price = price
    def calculate_dorm_cost(self, days_living):
        self.expense = []
        cost_perday = self.price/(int(days_living[0])+int(days_living[1]))
        self.expense.append([int(days_living[0])*cost_perday])
        self.expense.append([int(days_living[1])*cost_perday])
    def show_cost(self):
        print()
        print("{}'s payment: ".format(p1.name))
        print('-----------------')
        print(self.expense[0])
        print()
        print("{}'s payment: ".format(p2.name))
        print('-----------------')
        print(self.expense[1])

person1_name = input("What's the first person's name? ")
person2_name = input("What's the second person's name? ")

person1_days = input('{}, how many days have you been living here? '.format(person2_name))
person2_days = input('{} how many days have you been living here? '.format(person2_name))

p1 = Roommate(person1_name, person1_days)
p2 = Roommate(person2_name, person2_days)

print()
print('{} has been living for {} days and {} has been living for {} days'.format(p1.name,p1.days,p2.name,p2.days))

dorm = Dorm(6000)
dorm.calculate_dorm_cost([person1_days,person2_days])
dorm.show_cost()