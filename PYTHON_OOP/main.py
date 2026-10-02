from CoffeeShop import CoffeeShop


def main():
    shop = CoffeeShop()

    shop.display_title()
    shop.display_menu()

    if not shop.ask_customer():
        print("\nThank you for visiting Lycha Coffee Shop!")
        print("Have a wonderful day!")
        return

    shop.add_item()

    while shop.ask_another_item():
        add_item_result = shop.add_item()

    shop.display_order()
    shop.print_receipt()


if __name__ == "__main__":
    main()