# documentation:
# https://docs.google.com/document/d/e/2PACX-1vTragRHILyj76AvVgpWeOlEaLBXoxPM_43SdEyffIKtOgarj42SoSAsK6LwLAdHQs2qFLGthRZds6ok/pub
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

still_continue = True
all_items = Menu()
maker = CoffeeMaker()
money = MoneyMachine()

while still_continue:
    choice = input(f"What would you like?({all_items.get_items()}): ")
    if choice == 'off':
        still_continue = False
    elif choice == 'report':
        maker.report()
        money.report()
    else:
        option = all_items.find_drink(choice)
        sufficient = maker.is_resource_sufficient(option)
        money_enough = money.make_payment(option.cost)
        if sufficient and money_enough:
            maker.make_coffee(option)

# Answer code
# Still have some bug
# from menu import Menu
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine
#
# money_machine = MoneyMachine()
# coffee_maker = CoffeeMaker()
# menu = Menu()
#
# is_on = True
#
# while is_on:
#     options = menu.get_items()
#     choice = input(f"What would you like? ({options}): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink = menu.find_drink(choice)
#         is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
#         is_payment_successful = money_machine.make_payment(drink.cost)
#         if is_enough_ingredients and is_payment_successful:
#             coffee_maker.make_coffee(drink)
