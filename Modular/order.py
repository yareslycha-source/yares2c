from menu import menu, get_item_number

def ask_customer():
    while True:
        answer = input("\nWould you like to order? (Y/N): ").upper()
        if answer == "Y":
            return True
        elif answer == "N":
            return False
        else:
            print("Invalid input. Please enter Y or N.")

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                return quantity
            print("Quantity must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def add_item(order):
    item_number = get_item_number()
    quantity = get_quantity()

    item_name = menu[item_number][0]
    item_price = menu[item_number][1]

    if item_number in order:
        order[item_number] += quantity
    else:
        order[item_number] = quantity

    print("\n" + item_name, "x", quantity, "added to your order.")
    print("Price per item: ₱{:.2f}".format(item_price))

def ask_another_item():
    while True:
        answer = input("\nWould you like to order another item? (Y/N): ").upper()
        if answer == "Y":
            return True
        elif answer == "N":
            return False
        else:
            print("Invalid input. Please enter Y or N.")

def display_order(order):
    print("\n" + "=" * 65)
    print("                       YOUR ORDER")
    print("=" * 65)
    print("{:<25} {:>8} {:>12} {:>15}".format("ITEM", "QTY", "PRICE", "TOTAL"))
    print("-" * 65)

    for item_number, quantity in order.items():
        item_name = menu[item_number][0]
        item_price = menu[item_number][1]
        item_total = item_price * quantity

        print("{:<25} {:>8} ₱{:>10.2f} ₱{:>13.2f}".format(
            item_name, quantity, item_price, item_total
        ))

    print("-" * 65)