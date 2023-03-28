# lets build coffe machine
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
profit = 0


def is_resource_sufficient(order_ingredients):
    """returns true when order can be made and false intergart insufficnet"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough resources{item}")
            return False
    return True


def is_transanction_successful(money_received, drink_cost):
    """return true payment is enough and false money is not enough"""
    if money_received >= drink_cost:
        change = round(money_received-drink_cost,2)
        print(f"here is your {change}")
        global profit
        profit+=drink_cost
        return True
    else:
        print("sorry we cannot give drink,Money refunded")
    return False


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins")
    total = int(input("How many quarters?:")) * 0.25
    total += int(input("How many dimes?:")) * 0.1
    total += int(input("How many nickles?:")) * 0.25
    total += int(input("How many pennies?:")) * 0.25
    return total


# step 1 user for asking "what would you Like"?(espresso/latte/cappuccino))
is_on = True
while is_on:
    choice = input(f" What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            is_transanction_successful(payment,drink['cost'])

# check the resources sufficent
