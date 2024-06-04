from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# coffee_maker_object = CoffeeMaker()
# mm = MoneyMachine()
# men = Menu()
# # meni = MenuItem()
# is_on = True
# while is_on:
#     choice = input(f"What drink do you want? ({men.get_items()}) ")
#     a = (men.find_drink(choice))
#     if choice == "off":
#         is_on = False
#     # todo: check ingredients
#     elif choice == "report":
#         for i in coffee_maker_object.resources:
#             print(f"{i}: {coffee_maker_object.resources[i]}")
#         mm.report()
#     else:
#         # todo: check money
#         # mm.process_coins()
#         mm.make_payment(a.cost)
#         # todo: if make coffee
#         if coffee_maker_object.is_resource_sufficient(a):
#             coffee_maker_object.make_coffee(a)

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

coffee_maker.report()
money_machine.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if (coffee_maker.is_resource_sufficient(drink)) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
















