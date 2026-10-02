from menu import display_title, display_menu
from order import ask_customer, add_item, ask_another_item, display_order
from receipt import print_receipt


def main():
    order = {}

    display_title()
    display_menu()

    if ask_customer() == False:
        print("\nThank you for visiting Lycha Coffee Shop!")
        print("Have a wonderful day!")
        return

    add_item(order)

    while ask_another_item():
        add_item(order)

    display_order(order)

    print_receipt(order)


if __name__ == "__main__":
    main()