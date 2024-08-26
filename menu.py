# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = []
# 2. Loop through each category in the menu
for category in menu:
     # 3. Loop through each item in the category
     for item, price in menu[category].items():
          # 4. Check if the item is a dictionary (i.e., it has sub-items
          # like "Cheese" or "Chicken")
          if isinstance(price, dict):
               # 5. Loop through each sub-item in the item
               for sub_item, sub_price in price.items():
                    # 6. Add the sub-item to the order list
                    order_list.append({
                         "name": f"{category} - {item} - {sub_item}",
                         "price": sub_price,
                         "quantity": 0})

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            #print(f"What {menu_category_name} item would you like to order?")
            #i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_item_number = input("Type menu item number: ")

            # 3. Check if the customer typed a number
            #menu_item_number.isdigit()
                # 4. Check if the customer typed a valid optionn
            #if menu_items in menu_items.keys():
                    # 5. Get the menu item name and price
            #menu_item_name = menu_items[int(menu_item_number)]["Item name"]
            #menu_item_price = menu_items[int(menu_item_number)]["Price"]
                    # 6. Print out the menu item name and price
            #print(f"You selected {menu_item_name} for ${menu_item_price}")
                    # 7. Ask customer if they want to add to cart
            cart = input()
            add_to_cart = input("Would you like to add to cart? (Y)es/(N)o): ")
            if add_to_cart.lower() == "(Y)es":
                        # 8. Add menu item to cart
                        cart.append(menu_items[int(menu_item_number)])
                        cart.append({"Item name": menu_items[int(menu_item_number)]["Item name"],
                             "Price": menu_items[int(menu_item_number)]["Price"]})
                        print(f"Added {menu_items[int(menu_item_number)]['Item name']} to cart")

                        #print("Order cancelled")

                        cart.expend(menu_item_name)
                        print(f"Added {menu_item_name} to cart")
                        print(f"Your cart: {cart}")
                        
            print("Not added to cart")
            # 9. Ask customer if they want to order another item
            order_again = input("Would you like to order another item? (Y)es/(N)o): ")
            if order_again.lower() == "(Y)es":
                # 10. Go back to step 1
                continue
            else:
                # 11. Print out the cart
                print("Your cart:")
                for item in cart:
                    print(item)
                    # 12. Ask customer if they want to checkout
                    checkout = input("Would you like to checkout? (Y)es/(N)o): ")
                    if checkout.lower() == "(Y)es":
                        # 13. Print out the total cost
                        total_cost = 0
                        for item in cart:
                            total_cost += menu_items[item]["Price"]
                            print(f"Total cost: ${total_cost}")
                            # 14. Ask customer if they want to pay
                            pay = input("Would you like to pay? (Y)es/(N)o): ")
                            if pay.lower() == "(Y)es":
                                # 15. Print out the payment confirmation
                                print("Payment confirmed")
                                # 16. Clear the cart
                                cart.clear()
                                # 17. End the program
                                break

                # Convert the menu selection to an integer
                menu_item_number = int(menu_item_number)

                # 4. Check if the menu selection is in the menu items
                if menu_item_number not in range(len(menu_items)):
                     print("Invalid menu selection")
                     # 5. Ask customer to select a menu item
                     menu_item_number = input("Please select a menu item: ")
                     # 6. Check if the menu selection is in the menu items
                     if menu_item_number not in range(len(menu_items)):
                          print("Invalid menu selection")
                     
                     # Store the item name as a variable
                menu_item_price = input()

                    # Ask the customer for the quantity of the menu item
                quantity = input("How many would you like to order? ")
                    # Check if the quantity is a positive integer
                if quantity.isdigit() and int(quantity) > 0:
                        # Calculate the total cost
                        total_cost = int(quantity) * menu_items[menu_item_name]["Price"]
                        total_cost = float(menu_item_price) * int(quantity)
                        # Add the menu item to the cart
                        cart.add(menu_item_name)
                        print(f"Added {menu_item_name} to cart")
                        print(f"Your cart: {cart}")
                        # Ask customer if they want to order another item
                        order_again = input("Would you like to order another item? (Y)es/(N)o")
                        # Print out the total cost
                        print(f"Total cost: ${total_cost}")

                    # Check if the quantity is a number, default to 1 if not
                quantity = int(quantity) if quantity.isdigit() else 1
                    # Calculate the total cost
                total_cost = float(menu_item_price) * quantity
            
                print("Invalid quantity. Please enter a positive integer.")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # Check if the customer wants to keep ordering
        if keep_ordering.lower() == "y":
            # Ask the customer to select a menu option
            menu_item_number = input("Please select a menu option: ")
            # Check if the customer selected a number
            if menu_item_number.isdigit():
                # Check if the number is in the menu items
                if int(menu_item_number) in menu_items:
                    # Store the item name as a variable
                    menu_item_name = menu_items[int(menu_item_number)]
                    # Ask the customer how many of the item they would like to order
                    quantity = input(f"How many {menu_item_name} would you like to order? ")
                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                        # Calculate the total cost
                        total_cost = int(quantity) * menu_item_price
                        # Print out the total cost
                        print(f"Your total for {menu_item_name} is ${total_cost}.")
                        # Add the item name, price, and quantity to the order list
                        order_list.append({"item": menu_item_name, "price": menu_item_price, "quantity":int(quantity)})
                        # Tell the customer that their input isn't valid
                        
        print("Invalid quantity. Please enter a positive integer.")
    
        print("You didn't select a number.")
    
        print(f"{menu_category} was not a menu option.")
        break

# Tell the customer that their input isn't valid
print("Invalid quantity. Please enter a positive integer.")
print("You didn't select a number.")
print(f"{menu_category} was not a menu option.")
            
                # Since the customer decided to stop ordering, thank them for
                # their order
print("Thank you for your order!")

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
print(order_list)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for item in order_list:
    #print(f"{item_name['item']}                 
          #| ${item_price['price']:.2f}
          #| {item_quantity['quantity']}")

    # 7. Store the dictionary items as variables
    item_name = item['item']
    item_price = item['price']
    item_quantity = item['quantity']

    # 8. Calculate the number of spaces for formatted printing
    spaces = 30 - len(item_name)
    print(" " * spaces, end="")
    print(f"{item_name}                 | ${item_price:.2f} | {item_quantity}")

    # 9. Create space strings
    price_spaces = 8 - len(str(item_price))
    quantity_spaces = 9 - len(str(item_quantity))
    print(" " * price_spaces, end="")
    print(" " * quantity_spaces, end="")
    print()

    # 10. Print the item name, price, and quantity
    print(f"${item_price:.2f} | {item_quantity}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
order_cost = sum(item['price'] * item['quantity'] for item in order_list)
print(f"Total cost: ${order_cost:.2f}")