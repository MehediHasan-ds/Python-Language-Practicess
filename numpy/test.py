orders = [100, 250, 600, 1200, 50]

high_value_orders = list(filter(lambda x: x > 500, orders))
print(high_value_orders)