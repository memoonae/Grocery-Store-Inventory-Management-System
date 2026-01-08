import csv

INVENTORY_FILE = "inventory.csv"


def load_inventory():
    inventory = {}

    with open(INVENTORY_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            inventory[row["Item"].lower()] = {
                "id": int(row["ID"]),
                "category": row["Category"],
                "price": float(row["Price"]),
                "quantity": int(row["Quantity"])
            }

    return inventory


def save_inventory(inventory):
    with open(INVENTORY_FILE, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["ID", "Item", "Category", "Price", "Quantity"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for item, data in inventory.items():
            writer.writerow({
                "ID": data["id"],
                "Item": item.title(),
                "Category": data["category"],
                "Price": data["price"],
                "Quantity": data["quantity"]
            })


def view_items():
    inventory = load_inventory()
    print("\nAvailable Items:")
    for name, data in inventory.items():
        print(
            f"{name.title()} | {data['category']} | "
            f"Price: {data['price']} | Qty: {data['quantity']}"
        )


def adjust_stock(item, qty_change):
    inventory = load_inventory()
    if item in inventory:
        inventory[item]["quantity"] += qty_change
        save_inventory(inventory)
