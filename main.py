from inventory import view_items
from sales import buy_item, return_item

while True:
    print("\n===== GROCERY STORE MENU =====")
    print("1. View Inventory")
    print("2. Buy Item")
    print("3. Return Item")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        view_items()

    elif choice == "2":
        buy_item()

    elif choice == "3":
        return_item()

    elif choice == "4":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice. Try again.")
