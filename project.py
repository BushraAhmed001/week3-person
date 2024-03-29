import colorama
from colorama import init, Fore, Back, Style
colorama.init(autoreset=True)

drink_menu = {
    "Tea": 1.00,
    "Americano": 1.70,
    "Latte": 1.90,
    "Cappuccino": 1.90,
    "Mocha": 2.00,
    "Hot chocolate": 2.20}
food_menu = {
    "Croissant": 1.50,
    "Muffin": 2.10,
    "Toast": 1.00,
    "Panini": 2.90,
    "Buttered Roll": 0.70,
    "Stroopwafel": 0.50}
}
def start():
    while True:
        welcome_message = input("""Hello and welcome to the cafe, here is the menu:
    
      Drinks                                      
Tea           : £1.00    
Americano     : £1.70     
Latte         : £1.90     
Cappuccino    : £1.90    
Mocha         : £2.00     
Hot Chocolate : £2.20     
Bottled Water : £1.00   
      Food                    
 Croissant     : £1.50  
 Muffin        : £2.10  
 Toast         : £1.00  
 Panini        : £2.90  
 Buttered Roll : £0.70  
 Stroopwafel   : £0.50  
 Potato Cake   : £1.00   
    Would you like to place an order y/n: """)
        if welcome_message == "y":
            print("Good choice")
        elif welcome_message == "n":
            start()
        else:
            print("invalid input, enter 'y' or 'n' ")
            continue
        break

    total_cost = 0
    while True:
        order_input = input("What would you like to order?: ").capitalize()
        if order_input.capitalize() not in menu:
            print(Fore.RED + "Sorry, that item is not available.")
            continue
        order_count = int(input("How many would you like: "))
        total_cost += menu[order_input] * order_count
        print(Fore.GREEN + f"{order_count} {order_input}(s) have been added to your order. Current total: £{total_cost:.2f}")
        
        next_order = input("Would you like to place another order? (y/n) or 'restart' to cancel all items and start again: ")
        if next_order.lower() == 'n':
            break
        elif next_order.lower() == 'restart':
            total_cost = 0
            start()
    print(Fore.BLUE + f"The total is £{total_cost:.2f}. Thank you for visiting our cafe, have a good day")

start()