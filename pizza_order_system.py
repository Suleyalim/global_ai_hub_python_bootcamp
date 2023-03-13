import csv
import datetime

with open("Menu.txt", "w") as menu:
    menu.write("""* Please Choose a Pizza Base:
1: Classic
2: Margherita
3: TurkPizza
4: PlainPizza
* and toppings of your choice:
11: Olives
12: Mushrooms
13: GoatCheese
14: Meat
15: Onions
16: Corn
* Thank you!\n""")


# makes a dict out of the menu options:
with open("Menu.txt") as menu:
    menu_dict = {}
    for line in menu:
        if "*" in line:
            continue
        (key, val) = line.split(": ")
        val = val[:-1]
        menu_dict[int(key)] = val


class Pizza:
    def get_description(self):
        return self.__class__.__name__

    def get_cost(self):
        return self.__class__.cost


class Classic(Pizza):
    cost = 70.0

    def __init__(self):
        self.description = "tomato sauce, cheese and olives/mushrooms"


class Margherita(Pizza):
    cost = 80.0

    def __init__(self):
        self.description = "tomato sauce, Mozzarella and Basil"


class TurkPizza(Pizza):
    cost = 90.0

    def __init__(self):
        self.description = "tomato sauce, extra cheese, eggplant, bell pepper and jalapeno"


class PlainPizza(Pizza):
    cost = 75.0

    def __init__(self):
        self.description = "tomato sauce, cheese"


class Decorator(Pizza):
    def __init__(self, topping):
        self.component = topping

    def get_cost(self):
        return self.component.get_cost() + \
          Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + \
          ' ' + Pizza.get_description(self)


class Olives(Decorator):
    cost = 3.25

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Mushrooms(Decorator):
    cost = 7.25

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class GoatCheese(Decorator):
    cost = 12.75

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Meat(Decorator):
    cost = 19.5

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Onions(Decorator):
    cost = 3.25

    def __init__(self, topping):
        Decorator.__init__(self, topping)


class Corn(Decorator):
    cost = 3.25

    def __init__(self, topping):
        Decorator.__init__(self, topping)


def main():
    with open("Menu.txt") as cust_menu:
        for l in cust_menu:
            print(l, end="")

    class_dict = {1: Classic, 2: Margherita, 3: TurkPizza, 4: PlainPizza, 11: Olives, 12: Mushrooms, 13: GoatCheese, 14: Meat, 15: Onions, 16: Corn}

    code = input("Please choose the number of a basic pizza: ")
    while code not in ["1", "2", "3", "4"]:
        code = input("enter a valid number from 1-4 for the pizza base: ")

    order = class_dict[int(code)]()

    while code != "0":
        code = input("Please choose toppings codes ('0' to exit when finished): ")
        if code in ["11", "12", "13", "14", "15", "16"]:
            order = class_dict[int(code)](order)

    print("\n"+order.get_description().strip() +
          ": $" + str(order.get_cost()))

    name = input("Enter your name: ")
    ID = input("Enter your ID number: ")
    credit_card = input("Enter your credit number: ")
    credit_password = input("Enter your credit card password: ")
    time_of_order = datetime.datetime.now()

    with open('Orders_Database.csv', 'a') as orders:
        orders = csv.writer(orders, delimiter=',')

        orders.writerow([name, ID, credit_card, credit_password, order.get_description(), time_of_order])


if __name__ == '__main__':
    main()