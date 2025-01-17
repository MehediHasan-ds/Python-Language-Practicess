#Practising functions with example of Customer Relationship Management (CRM) System for an e-commerce business

#DEFINE a function to calculate the total price of items in a shopping cart
def calculate_total(cart):
    total = sum(item['price'] * item['quantity'] for item in cart)
    return total
cart_total_price = [{"item": "Laptop", "price": 1000, "quantity": 1}, {"item": "Mouse", "price": 50, "quantity": 2}]
total_price = calculate_total(cart_total_price)


#DEFAULT Arguments: A function to apply a discount with a default value
def apply_discount(total, discount=0.1):
    return total - (total * discount)
discounted_price = apply_discount(total_price)
print(discounted_price)


#Variable-Length Arguments (*args):creating a function to calculate customer points for multiple orders
def calculate_loyalty_points(*totals):
    return sum(total // 10 for total in totals)
loyalty_points = calculate_loyalty_points(100, 250, 400)
print(loyalty_points)


#Keyword Arguments (**kwargs): tracking customer details dynamically
def customer_profile(**details):
    return details
profile = customer_profile(name="Mehedi", email="mehedihasan398@gmail.com", phone="1234567890")
print(profile)

#LAMDA Functions: Filter high-value orders (above $500)
orders = [100, 250, 600, 1200, 50]
high_value_orders = list(filter(lambda x: x > 500, orders))
print(high_value_orders)

