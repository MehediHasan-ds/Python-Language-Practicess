from functools import reduce

prices = [100, 200, 300, 400]
discounted_prices = list(map(lambda price: price * 0.9, prices))
total_discounted_price = reduce(lambda x, y: x + y, discounted_prices)
print(discounted_prices)
print(total_discounted_price)

