class Customer:
    def __init__(self, name, gender, membership):
        self.name = name
        self.gender = gender
        self.membership = membership

    def is_introducing(self):
        print('')
        print('This is', self.name)
        if self.gender == 'Male':
            print('His membership is', self.membership)
        elif self.gender == 'Female':
            print('Her membership is', self.membership)
        else:
            print('Their membership is', self.membership)


def main():
    count = int(input("How many people are there? "))
    customers = []

    for i in range(1, count + 1):
        asking_name = str(input("Person's %s name: " % i))
        asking_gender = input('Gender? (Male, Female, Others): ')
        asking_membership = input('Membership? (Gold, Diamond, Bronze): ')

        customer_info = Customer(asking_name, asking_gender, asking_membership)
        customers.append(customer_info)

        if i < count:
            print('-' * 30)  # Add a line break between each person's input

    for index, customer in enumerate(customers, start=1):
        customer.is_introducing()
        if index < count:
            print('-' * 30)  # Add a line break between each person's introduction


if __name__ == "__main__":
    main()
