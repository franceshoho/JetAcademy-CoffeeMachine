# Coffee Class
INITIAL_WATER = 400
INITIAL_MILK = 540
INITIAL_COFFEE = 120
INITIAL_CUPS = 9
INITIAL_MONEY = 550

class Coffee_Machine:

    # initiate coffee machine instance
    def __init__(self, water, milk, coffee, cups, money=550):
        self.water = water # ml
        self.milk = milk # ml
        self.coffee = coffee # grams
        self.cups = cups
        self.state = None  # default value so don't need to passed in.
        self.money = money  # state can be buy, fill, take


    # print out existing contents in coffee machine
    def get_contents(self):
        print("The coffee machine has:")
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money \n')

    def add_contents(self, water, milk, coffee, cups):
        self.water += water
        self.milk += milk
        self.coffee += coffee
        self.cups += cups
        self.money += 0

    def update_contents(self, water, milk, coffee, cups, money):
        self.water -= water
        self.milk -= milk
        self.coffee -= coffee
        self.cups -= cups
        self.money += money

    def make_espresso(self, cups):
        # require 250 ml water, 16g coffee and $4
        # first check if there's enough contents
        water_needed = 250 * cups
        coffee_needed = 16 * cups
        money_needed = 4 * cups
        if(self.water >= water_needed) and (self.coffee >= coffee_needed):
            self.update_contents(water_needed, 0, coffee_needed,
                                 cups, money_needed)
            print(f'Making {cups} of espresso....')
        else:
            print(f"You don't have enough contents "
                  f"in machine to make {cups} of espresso!")

    def make_cappuccino(self, cups):
        # requires 200ml of water, 100ml of milk, 12g of coffee
        # costs $6.
        water_needed = 200 * cups
        milk_needed = 100 * cups
        coffee_needed = 12 * cups
        money_needed = 6 * cups
        if (self.water >= water_needed) and \
                (self.coffee >= coffee_needed) and \
                (self.milk >= milk_needed) :
            self.update_contents(water_needed, milk_needed,
                                 coffee_needed, cups, money_needed)
            print(f'Making {cups} of latte....')
        else :
            print(f"You don't have enough contents "
                  f"in machine to make {cups} of latte!")

    def make_latte(self, cups):
        # requires 350ml of water, 75ml of milk, 20g of coffee
        # costs $7.
        water_needed = 350 * cups
        milk_needed = 75 * cups
        coffee_needed = 20 * cups
        money_needed = 7 * cups
        if (self.water >= water_needed) and \
            (self.coffee >= coffee_needed) and \
            (self.milk >= milk_needed):
            self.update_contents(water_needed, milk_needed,
                                 coffee_needed, cups, money_needed)
            print(f'Making {cups} of latte....')
        else :
            print(f"You don't have enough contents "
                  f"in machine to make {cups} of latte!")

    def fill_contents(self):
        water = int(input("How much water do you want to fill? "))
        milk = int(input("How much milk do you want to fill? "))
        coffee = int(input("How much coffee do you want to fill? "))
        cups = int(input("How much cups do you want to fill? "))
        if (water >= 0) and (milk >= 0) and (coffee >= 0) and (cups >= 0):
            self.add_contents(water, milk, coffee, cups)
        else:
            print("you cannot have negative numbers to add")

    def take_money(self):
        print(f"I gave you $ {self.money} \n")
        self.money = 0





if __name__ == '__main__':
    # starts with INIT_Money in machine using param args
    # so note INIT_MONEY is optional param and may not be needed
    my_coffee_machine = Coffee_Machine(INITIAL_WATER, INITIAL_MILK,
                                       INITIAL_COFFEE,INITIAL_CUPS,
                                       )
    #my_coffee_machine.get_contents()

    while True:
        choice = input("What do you want to do?  buy, fill, take, remaining, exit ")
        my_coffee_machine.state = choice
        if (my_coffee_machine.state == "buy"):
            choice2 = input(
                "What type of coffee do you want? 1-espresso, 2-latte, 3-cappuccino, back - back to main ")
            if (choice2 == "1") :
                my_coffee_machine.make_espresso(1)
            elif (choice2 == "2") :
                my_coffee_machine.make_latte(1)
            elif (choice2 == "3") :
                my_coffee_machine.make_cappuccino(1)
            elif (choice2 == "back"):
                continue
            else:
                print(f'{choice2} is not a valid choice of coffee!')

        elif (my_coffee_machine.state == "fill"):
            my_coffee_machine.fill_contents()
        elif (my_coffee_machine.state == "take"):
            my_coffee_machine.take_money()
        elif (my_coffee_machine.state == "remaining"):
            my_coffee_machine.get_contents()
        elif (my_coffee_machine.state == "exit"):
            break
        else:
            print ("Please enter a valid choice of action.")





