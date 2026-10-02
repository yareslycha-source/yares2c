menu = {
    1: ["Iced Coffee", 80.00],
    2: ["Caffe Latte", 100.00],
    3: ["Cappuccino", 110.00],
    4: ["Caramel Macchiato", 120.00],
    5: ["Mocha", 115.00],
    6: ["Americano", 90.00],
    7: ["Chocolate Cake", 130.00],
    8: ["Croissant", 75.00],
    9: ["Blueberry Muffin", 85.00],
    10: ["Cheesecake", 140.00]
}

def display_title():
    print("\n" + "=" * 55)
    print("              LYCHA COFFEE SHOP")
    print("          Fresh Coffee, Fresh Moments")
    print("=" * 55)

def display_menu():
    print("\n-------------------- OUR MENU --------------------")
    print("{:<5} {:<30} {:>10}".format("NO.", "ITEM", "PRICE"))
    print("-" * 50)

    for number, item in menu.items():
        print("{:<5} {:<30} ₱{:>8.2f}".format(
            number,
            item[0],
            item[1]
        ))

    print("-" * 50)

def get_item_number():
    while True:
        try:
            number = int(input("\nEnter menu number: "))
            if number in menu:
                return number
            print("That item is not on the menu.")
        except ValueError:
            print("Invalid input. Please enter a number.")