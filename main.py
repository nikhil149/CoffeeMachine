MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# print(MENU["espresso"])
should_stop = True


def another(check_coffee, check_resources):
    if check_coffee == 'espresso':
        if MENU[check_coffee]['ingredients']['water'] > check_resources['water']:
            return "Sorry water is less"
        elif check_resources['coffee'] < MENU[check_coffee]['ingredients']['coffee']:
            return "Sorry coffee is low"
        else:
            return True
    else:
        if MENU[check_coffee]['ingredients']['water'] > check_resources['water']:
            return "Sorry water is less"
        elif check_resources['milk'] < MENU[check_coffee]['ingredients']['milk']:
            return "Sorry Milk is very low"
        elif check_resources['coffee'] < MENU[check_coffee]['ingredients']['coffee']:
            return "Sorry coffee is low"
        else:
            return True


def sum_coins():
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickel = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = 0.25 * quarters + dimes * 0.10 + nickel * 0.05 + pennies * 0.01
    return round(total, 2)


def remaining_ingredients(using_coffee, using_resources, answer):

    if answer:
        if using_coffee == 'espresso':
            remaining_water = using_resources['water'] - MENU[using_coffee]['ingredients']['water']
            remaining_milk = using_resources['milk']
            remaining_coffee = using_resources['coffee'] - MENU[using_coffee]['ingredients']['coffee']
        else:
            remaining_water = using_resources['water'] - MENU[using_coffee]['ingredients']['water']
            remaining_milk = using_resources['milk'] - MENU[using_coffee]['ingredients']['milk']
            remaining_coffee = using_resources['coffee'] - MENU[using_coffee]['ingredients']['coffee']
        using_resources = {
            "water": remaining_water,
            "milk": remaining_milk,
            "coffee": remaining_coffee
        }
        return using_resources


while should_stop:

    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee == 'off':
        break

    if coffee == 'report':
        print(resources)
    else:
        another_answer = another(coffee, resources)
        print(another_answer)
        my_report = remaining_ingredients(coffee,resources, another_answer)
        if another_answer:

            if coffee == 'latte' or coffee == 'espresso' or coffee == 'cappuccino':
                print("Please insert coins")
                inserted_price = sum_coins()
                print(inserted_price)

                for coffee_type in MENU:
                    if coffee == coffee_type:
                        if inserted_price > MENU['latte']['cost']:
                            change = inserted_price - MENU['latte']['cost']
                            print(f"Please take a change {round(change, 2)}")

                        else:
                            print("Insufficient money! Money refunded")
                resources = my_report
            else:
                print("Enter valid input")

