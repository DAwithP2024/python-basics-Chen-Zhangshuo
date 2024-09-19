# Dictionary of available products categorized by types
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

# Function to sort and display products based on price
def display_sorted_products(products_list, sort_order):
    if sort_order == "asc":
        sorted_list = sorted(products_list, key=lambda x: x[1])
    elif sort_order == "desc":
        sorted_list = sorted(products_list, key=lambda x: x[1], reverse=True)
    return sorted_list

# Function to display products in a category
def display_products(products_list):
    print("Available products:")
    for index, (product_name, price) in enumerate(products_list, start=1):
        print(f"{index}. {product_name} - ${price}")

# Function to display all available product categories
def display_categories():
    print("Available categories:")
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")

# Function to add selected products to the cart
def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))
    print(f"Added {quantity} x {product[0]} to the cart.")

# Function to display the cart contents
def display_cart(cart):
    total_cost = 0
    for product_name, price, quantity in cart:
        total = price * quantity
        total_cost += total
        print(f"{product_name} - ${price} x {quantity} = ${total}")
    print(f"Total cost: ${total_cost}")

# Function to generate and print the receipt
def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for product_name, price, quantity in cart:
        print(f"{quantity} x {product_name} - ${price} = ${price * quantity}")
    print(f"Total cost: ${total_cost}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days.")
    print("Payment will be accepted after successful delivery.")

# Function to validate user name (must contain first and last name)
def validate_name(name):
    if len(name.split()) == 2 and all(part.isalpha() for part in name.split()):
        return True
    return False

# Function to validate email format
def validate_email(email):
    return "@" in email

# Main program function
def main():
    name = input("Enter your name: ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid first and last name.")
        name = input("Enter your name: ")

    email = input("Enter your email: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email.")
        email = input("Enter your email: ")

    cart = []
    
    # Main loop for shopping categories and products
    while True:
        display_categories()
        category_choice = input("Choose a category (enter number): ")
        
        if not category_choice.isdigit() or int(category_choice) not in range(1, len(products) + 1):
            print("Invalid choice. Please enter a valid category number.")
            continue

        category = list(products.keys())[int(category_choice) - 1]
        product_list = products[category]
        
        # Loop to select products, sort, or finish shopping
        while True:
            display_products(product_list)
            print("Options: 1. Select a product to buy  2. Sort products by price  3. Go back to categories  4. Finish shopping")
            action = input("Enter your choice: ")

            if action == '1':
                product_choice = input("Enter the product number to buy: ")
                if not product_choice.isdigit() or int(product_choice) not in range(1, len(product_list) + 1):
                    print("Invalid product choice.")
                    continue
                product = product_list[int(product_choice) - 1]
                quantity = input("Enter the quantity: ")
                if not quantity.isdigit() or int(quantity) <= 0:
                    print("Invalid quantity.")
                    continue
                add_to_cart(cart, product, int(quantity))

            elif action == '2':
                sort_order = input("Enter 1 for ascending order or 2 for descending order: ")
                if sort_order == '1':
                    sorted_products = display_sorted_products(product_list, "asc")
                elif sort_order == '2':
                    sorted_products = display_sorted_products(product_list, "desc")
                else:
                    print("Invalid sort order.")
                    continue
                display_products(sorted_products)

            elif action == '3':
                break

            elif action == '4':
                if cart:
                    total_cost = sum(price * quantity for _, price, quantity in cart)
                    address = input("Enter your delivery address: ")
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for visiting. You didn't buy anything this time.")
                return
            
""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()
