class CoffeeShopMenu:
    def __init__(self):
        self.menu = {
            "Espresso": 2.50,
            "Latte": 3.00,
            "Cappuccino": 3.50,
            "Americano": 2.75,
            # Add more menu items as needed
        }
        self.order = {}

    def display_menu(self):
        print("Coffee Shop Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price:.2f}")

    def take_order(self):
        while True:
            self.display_menu()
            item = input("Enter the item you'd like to order (or 'done' to finish): ")

            if item.lower() == 'done':
                break

            if item in self.menu:
                quantity = int(input(f"How many {item}s would you like? "))
                if item in self.order:
                    self.order[item] += quantity
                else:
                    self.order[item] = quantity
                print(f"{quantity} {item}(s) added to your order.")
            else:
                print("Invalid item. Please try again.")

    def generate_receipt(self):
        print("\nReceipt:")
        total_amount = 0
        for item, quantity in self.order.items():
            subtotal = self.menu[item] * quantity
            total_amount += subtotal
            print(f"{quantity} {item}(s) - ${subtotal:.2f}")

        print(f"\nTotal: ${total_amount:.2f}")