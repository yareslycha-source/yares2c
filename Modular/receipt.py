from menu import menu

def calculate_subtotal(order):
    subtotal = 0
    for item_number, quantity in order.items():
        price = menu[item_number][1]
        subtotal += (price * quantity)
    return subtotal

def calculate_discount(subtotal):
    if subtotal >= 500:
        return subtotal * 0.10
    else:
        return 0

def print_receipt(order):
    subtotal = calculate_subtotal(order)
    discount = calculate_discount(subtotal)
    total = subtotal - discount

    print("\n\n" + "=" * 65)
    print("                 LYCHA COFFEE SHOP")
    print("                  OFFICIAL RECEIPT")
    print("=" * 65)

    print("Thank you for ordering!")
    print("-" * 65)

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
    print("{:<50} ₱{:>12.2f}".format("SUBTOTAL:", subtotal))
    print("{:<50} ₱{:>12.2f}".format("DISCOUNT:", discount))
    print("-" * 65)
    print("{:<50} ₱{:>12.2f}".format("TOTAL:", total))
    print("=" * 65)
    print("             THANK YOU FOR VISITING!")
    print("                  COME AGAIN!")
    print("=" * 65)