class CoffeeShop:
    def __init__(self):
        self.menu = {
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
        self.order = {}

    def display_title(self):
        print("\n" + "=" * 55)
        print("              LYCHA COFFEE SHOP")
        print("          Fresh Coffee, Fresh Moments")
        print("=" * 55)

    def display_menu(self):
        print("\n-------------------- OUR MENU --------------------")
        print("{:<5} {:<30} {:>10}".format("NO.", "ITEM", "PRICE"))
        print("-" * 50)

        for number, item in self.menu.items():
            print("{:<5} {:<30} ₱{:>8.2f}".format(
                number,
                item[0],
                item[1]
            ))

        print("-" * 50)

    def ask_customer(self):
        while True:
            answer = input("\nWould you like to order? (Y/N): ").upper()

            if answer == "Y":
                return True
            elif answer == "N":
                return False
            else:
                print("Invalid input. Please enter Y or N.")

    def get_item_number(self):
        while True:
            try:
                number = int(input("\nEnter menu number: "))

                if number in self.menu:
                    return number

                print("That item is not on the menu.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_quantity(self):
        while True:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    return quantity

                print("Quantity must be greater than 0.")

            except ValueError:
                print("Invalid input. Please enter a whole number.")

    def add_item(self):
        item_number = self.get_item_number()
        quantity = self.get_quantity()

        item_name = self.menu[item_number][0]
        item_price = self.menu[item_number][1]

        if item_number in self.order:
            self.order[item_number] += quantity
        else:
            self.order[item_number] = quantity

        print("\n" + item_name, "x", quantity, "added to your order.")
        print("Price per item: ₱{:.2f}".format(item_price))

    def ask_another_item(self):
        while True:
            answer = input("\nWould you like to order another item? (Y/N): ").upper()

            if answer == "Y":
                return True
            elif answer == "N":
                return False
            else:
                print("Invalid input. Please enter Y or N.")

    def calculate_subtotal(self):
        subtotal = 0

        for item_number, quantity in self.order.items():
            price = self.menu[item_number][1]
            subtotal = subtotal + (price * quantity)

        return subtotal

    def calculate_discount(self, subtotal):
        if subtotal >= 500:
            return subtotal * 0.10
        else:
            return 0

    def display_order(self):
        print("\n" + "=" * 65)
        print("                       YOUR ORDER")
        print("=" * 65)

        print("{:<25} {:>8} {:>12} {:>15}".format(
            "ITEM", "QTY", "PRICE", "TOTAL"
        ))

        print("-" * 65)

        for item_number, quantity in self.order.items():
            item_name = self.menu[item_number][0]
            item_price = self.menu[item_number][1]
            item_total = item_price * quantity

            print("{:<25} {:>8} ₱{:>10.2f} ₱{:>13.2f}".format(
                item_name,
                quantity,
                item_price,
                item_total
            ))

        print("-" * 65)

    def print_receipt(self):
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount(subtotal)
        total = subtotal - discount

        print("\n\n" + "=" * 65)
        print("                 LYCHA COFFEE SHOP")
        print("                  OFFICIAL RECEIPT")
        print("=" * 65)

        print("Thank you for ordering!")
        print("-" * 65)

        print("{:<25} {:>8} {:>12} {:>15}".format(
            "ITEM", "QTY", "PRICE", "TOTAL"
        ))

        print("-" * 65)

        for item_number, quantity in self.order.items():
            item_name = self.menu[item_number][0]
            item_price = self.menu[item_number][1]
            item_total = item_price * quantity

            print("{:<25} {:>8} ₱{:>10.2f} ₱{:>13.2f}".format(
                item_name,
                quantity,
                item_price,
                item_total
            ))

        print("-" * 65)

        print("{:<50} ₱{:>12.2f}".format(
            "SUBTOTAL:",
            subtotal
        ))

        print("{:<50} ₱{:>12.2f}".format(
            "DISCOUNT:",
            discount
        ))

        print("-" * 65)

        print("{:<50} ₱{:>12.2f}".format(
            "TOTAL:",
            total
        ))

        print("=" * 65)
        print("             THANK YOU FOR VISITING!")
        print("                  COME AGAIN!")
        print("=" * 65)