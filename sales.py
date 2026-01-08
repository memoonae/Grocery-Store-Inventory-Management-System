from inventory import load_inventory, adjust_stock

SALES_FILE = "sales.txt"


def buy_item():
    inventory = load_inventory()
    cart = []
    total = 0

    while True:
        item = input("Enter item name to buy: ").lower()
        if qty <= 0:
         print("Quantity must be greater than zero.")
         continue

        if item not in inventory:
            print("Item not available.")
            continue

        try:
            qty = int(input("Enter quantity: "))
        except ValueError:
            print("Invalid quantity.")
            continue

        if qty > inventory[item]["quantity"]:
            print("Not enough stock.")
            continue

        cost = inventory[item]["price"] * qty
        cart.append((item, qty, cost))
        total += cost

        adjust_stock(item, -qty)

        if input("Add another item? (y/n): ").lower() != "y":
            break

    generate_bill(cart, total)


def return_item():
    inventory = load_inventory()
    item = input("Enter item name to return: ").lower()

    if item not in inventory:
        print("Item not found.")
        return

    try:
        qty = int(input("Enter quantity to return: "))
    except ValueError:
        print("Invalid quantity.")
        return

    adjust_stock(item, qty)

    with open(SALES_FILE, "a", encoding="utf-8") as file:
        file.write(f"RETURN,{item},{qty}\n")

    print("Item returned successfully!")


def generate_bill(cart, total):
    print("\n----- BILL -----")
    for item, qty, cost in cart:
        print(f"Per unit price of {item.title()} = {item.price()}")
        print(f"{item.title()} x {qty} = {cost}")
    print("Total:", total)

    with open(SALES_FILE, "a", encoding="utf-8") as file:
        for item, qty, cost in cart:
            file.write(f"SALE,{item},{qty},{cost}\n")
        file.write(f"TOTAL,,,{total}\n\n")
