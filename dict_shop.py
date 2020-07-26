gold = 100
shop = {
        "Juicebox":100,
        "Candy":50,
        "Gum":25,
        "Drugs":100000
        }
inventory = []

while True:
    print("Inventory: " +str( inventory))
    print("Gold: " + str(gold))
    print(shop)
    buyitem = str(input("What item would you like to buy?: "))
    for i in shop:
        if buyitem in shop:
            if gold >= shop[buyitem]:
                print("Item bought!")
                gold -= shop[buyitem]
                del shop[buyitem]
                inventory.append(buyitem)
                break
            else:
                print("You do not have enough money")
                break
        else:
            print("That item does not exist!")
            break

