PRODUCT_CATEGORIES = ["Electronics", "Clothing", "Home & Kitchen", "Books", "Toys"]
PRODUCT_SUBCATEGORIES = {
    "Electronics": ["Smartphones", "Laptops", "Accessories"],
    "Clothing": ["Men's Wear", "Women's Wear", "Kids' Wear"],
    "Home & Kitchen": ["Furniture", "Cookware", "Decor"],
    "Books": ["Fiction", "Non-Fiction", "Educational"],
    "Toys": ["Action Figures", "Board Games", "Stuffed Toys"]
}

for index, (key, values) in enumerate(PRODUCT_SUBCATEGORIES.items(),start=1):
    print(f'Category-{index}: {key}')
    for value in values:
        print(value)