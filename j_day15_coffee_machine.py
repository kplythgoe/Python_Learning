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


def resource_check(drink, left):
    water = drink["ingredients"]["water"]
    if "milk" in drink["ingredients"].keys():
        milk = drink["ingredients"]["milk"]
    coffee = drink["ingredients"]["coffee"]
    if water > left["water"]:
        print("Sorry, there is not enough water.")
    elif "milk" in drink["ingredients"].keys() and milk > left["milk"]:
        print("Sorry, there is not enough milk")
    elif coffee > left["coffee"]:
        print("sorry, there is not enough coffee")
    else:
        print(f"Please insert coins (${drink["cost"]})")
        return True


def money_check(drink_cost):
    inserted = [int(input("How many Quarters: ")), int(input("How many Dimes: ")), int(input("How many Nickles: ")),
                int(input("How many Pennies: "))]
    total = round(inserted[0] * 0.25 + inserted[1] * 0.1 + inserted[2] * 0.05 + inserted[3] * 0.01, 2)
    print(f"You have paid: {total}")
    if total < drink_cost:
        print("Sorry, that's not enough money. Money refunded.")
    elif total > drink_cost:
        change = round(total - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        return True


def make_drink(drink_ingredients, resources):
    resources["water"] -= drink_ingredients["water"]
    if "milk" in drink_ingredients.keys():
        resources["milk"] -= drink_ingredients["milk"]
    resources["coffee"] -= drink_ingredients["coffee"]


def test_function(drink_choice, enough, has_paid):
    enough = resource_check(MENU[drink_choice], resources)
    if enough:
        has_paid = money_check(MENU[drink_choice]["cost"])
        if has_paid:
            make_drink(MENU[drink_choice]["ingredients"], resources)
            print(f"Here's your {drink_choice}. Enjoy!")
            return MENU[drink_choice]["cost"]
        else:
            return 0
    else:
        return 0


enough_resources = False
paid = False
money = 0
running = True
while running:
    choice = input("What would you like? (espresso, latte, cappuccino): ").lower()
    if choice != "off":
        if choice == "report":
            for key, value in resources.items():
                print(key, ":", value)
            print(f"money : ${money}")
        elif choice == "espresso":
            money += test_function(choice, enough_resources, paid)
        elif choice == "latte":
            money += test_function(choice, enough_resources, paid)
        elif choice == "cappuccino":
            money += test_function(choice, enough_resources, paid)
    elif choice == "off":
        print("Turning off machine...")
        running = False

