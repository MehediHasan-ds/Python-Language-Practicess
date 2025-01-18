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

#LAMBDA Functions: Filter high-value orders (above $500)
orders = [100, 250, 600, 1200, 50]
high_value_orders = list(filter(lambda x: x > 500, orders))
print(high_value_orders)

#MAP and REDUCE: Calculating the discounted prices of all items
from functools import reduce
prices = [100, 200, 300, 400]
discounted_prices = list(map(lambda price: price * 0.9, prices))
total_discounted_price = reduce(lambda x, y: x + y, discounted_prices)
print(discounted_prices)
print(total_discounted_price)



#NESTED FUNCTIONS: Generate unique invoice numbers automatically
from datetime import datetime
def generate_invoice(order_id,total_amount):
    def format_invoice():
        return f"INV-{order_id}-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    calculate_tax = lambda amount,tax_rate = 0.15:amount*tax_rate
    
    tax = calculate_tax(total_amount)
    grand_total = total_amount + tax

    return{
        "invoice_number":format_invoice(),
        "order_id": order_id,
        "tax": tax,
        "grand_total": grand_total,
        "generated_at": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
print(generate_invoice(123,1000))


#Function Annotations (Type Hints):  while defining the functions giving hints to the calculate_total function as it will return integer value
def calculate_total(price: float, quantity: int) -> int:
    return int(price * quantity)

total = calculate_total(50.5, 3)
print(f"Total: ${total}")


#FIRST CLASS FUNCTION: functions that can be assigned to variables, passed as arguments, or returned from other functions
from datetime import datetime
def email_generator(email_type):

    def promotional_email(customer): #closure
        subject = "Premium Offer Just for You!"
        message = f"Hi {customer['name']}, enjoy 20% off on your next purchase."
        return send_email(customer['email'], subject, message)

    def transactional_email(customer, transaction_details):#closure
        subject = "Your Transaction Receipt"
        message = (
            f"Hi {customer['name']},\n"
            f"Thank you for purchasing {transaction_details['item']}.\n"
            f"Amount Paid: ${transaction_details['amount']}.\n"
            f"Transaction Date: {datetime.now().strftime('%Y-%m-%d')}."
        )
        return send_email(customer['email'], subject, message)

    # Returning the appropriate nested function based on `email_type`
    if email_type == "promotional":
        return promotional_email #first class function use
    elif email_type == "transactional":
        return transactional_email #first class function use
    else:
        raise ValueError("Invalid email_type specified!")

# helper function to send email
def send_email(email, subject, message):
    return f"Email sent to {email} with \nSubject: {subject}\nMessage: {message}\n"

customers = [
    {"name": "Subin", "email": "subin398@gmail.com"},
    {"name": "Rossi", "email": "rossi398@gmail.com"},
]

promotional_email = email_generator("promotional")
transactional_email = email_generator("transactional")

promotional_result = promotional_email(customers[0])
print("Promotional Email Result\n",promotional_result)

transaction_details = {"item": "Laptop", "amount": 1500}
transactional_result = transactional_email(customers[1], transaction_details)
print("Transactional Email Result\n",transactional_result)


#FUNCTOOLS.PARTIAL : dynamically creates a new function by pre-filling arguments of an existing function at runtime
from functools import partial
from datetime import datetime

# generating base report
def generate_report(report_type, report_data, start_date, end_date):
    report_header = f"*** {report_type.upper()} REPORT ***\n"
    report_header += f"Period: {start_date} to {end_date}\nGenerated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report_content = f"Details:\n{report_data}\n"
    return report_header + report_content

# partial functions for specific report types
customer_sales_report = partial(generate_report, "Customer Sales")
product_performance_report = partial(generate_report, "Product Performance")
revenue_summary_report = partial(generate_report, "Revenue Summary")

# report data
customer_sales_data = "Customer: rossi | Total Purchases: $500"
product_performance_data = "Product: Laptop | Units Sold: 300"
revenue_summary_data = "Total Revenue: $150,000"

# generating reports by only providing remaining arguments (data and date range)
customer_sales = customer_sales_report(
    report_data=customer_sales_data,
    start_date="2025-01-01",
    end_date="2025-01-15"
)

product_performance = product_performance_report(
    report_data=product_performance_data,
    start_date="2025-01-01",
    end_date="2025-01-15"
)

revenue_summary = revenue_summary_report(
    report_data=revenue_summary_data,
    start_date="2025-01-01",
    end_date="2025-01-15"
)

print(customer_sales)
print("\n" + "=" * 35 + "\n")
print(product_performance)
print("\n" + "=" * 35 + "\n")
print(revenue_summary)


#DECORATORS: 


