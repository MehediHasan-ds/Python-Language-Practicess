PRODUCT_CATEGORIES = ["Electronics", "Clothing", "Home & Kitchen", "Books", "Toys"]
PRODUCT_SUBCATEGORIES = {
    "Electronics": ["Smartphones", "Laptops", "Accessories"],
    "Clothing": ["Men's Wear", "Women's Wear", "Kids' Wear"],
    "Home & Kitchen": ["Furniture", "Cookware", "Decor"],
    "Books": ["Fiction", "Non-Fiction", "Educational"],
    "Toys": ["Action Figures", "Board Games", "Stuffed Toys"]
}
BRANDS = {
    "Smartphones": ["Apple", "Samsung", "Xiaomi", "Google", "OnePlus", "Sony", "LG", "Huawei", "Motorola", "Nokia"],
    "Laptops": ["Dell", "HP", "Lenovo", "Asus", "Acer", "Microsoft", "Razer", "Apple", "MSI", "Toshiba"],
    "Accessories": ["Logitech", "Anker", "Belkin", "Samsung", "Apple", "Bose", "JBL", "Sony", "Microsoft", "Canon"],
    "Men's Wear": ["Nike", "Adidas", "Levi's", "Puma", "Under Armour", "Calvin Klein", "Tommy Hilfiger", "Ralph Lauren", "H&M", "Zara"],
    "Women's Wear": ["Zara", "H&M", "Gucci", "Prada", "Chanel", "Louis Vuitton", "Versace", "Dior", "Calvin Klein", "Tommy Hilfiger"],
    "Kids' Wear": ["Carter's", "Gap Kids", "Disney", "Nike", "Adidas", "Puma", "Levi's", "H&M", "Zara", "Under Armour"],
    "Furniture": ["IKEA", "Ashley", "Wayfair", "Herman Miller", "Steelcase", "West Elm", "Crate & Barrel", "Pottery Barn", "La-Z-Boy", "Ethan Allen"],
    "Cookware": ["Tefal", "Prestige", "Cookworks", "Le Creuset", "All-Clad", "Calphalon", "Cuisinart", "KitchenAid", "Ninja", "Instant Pot"],
    "Decor": ["Home Centre", "Fabindia", "Urban Ladder", "IKEA", "West Elm", "Crate & Barrel", "Pottery Barn", "Wayfair", "Ashley", "Ethan Allen"],
    "Fiction": ["Penguin", "HarperCollins", "Random House", "Simon & Schuster", "Hachette", "Macmillan", "Scholastic", "Bloomsbury", "Vintage", "Oxford"],
    "Non-Fiction": ["Simon & Schuster", "Hachette", "Macmillan", "Penguin", "HarperCollins", "Random House", "Scholastic", "Bloomsbury", "Vintage", "Oxford"],
    "Educational": ["Pearson", "McGraw-Hill", "Oxford", "Cambridge", "Wiley", "Cengage", "Springer", "Elsevier", "Kogan Page", "Sage"],
    "Action Figures": ["Hasbro", "Mattel", "Funko", "Bandai", "McFarlane", "NECA", "Hot Toys", "Sideshow", "Good Smile", "Kotobukiya"],
    "Board Games": ["Ravensburger", "Asmodee", "Hasbro", "Mattel", "Parker Brothers", "Fantasy Flight", "Days of Wonder", "Z-Man Games", "Rio Grande", "Blue Orange"],
    "Stuffed Toys": ["Ty", "Gund", "Steiff", "Aurora", "Melissa & Doug", "Jellycat", "Manhattan Toy", "Douglas", "Wild Republic", "Hansa"]
}

# print the categories with values(sub-categories) by providing each category an index. (for indexing using enumerate)
# for index, (key, values) in enumerate(PRODUCT_SUBCATEGORIES.items(),start=1):
#     print(f'Category-{index}: {key}')
#     for value in values:
#         print(value)

# print the available brands for each subcategory under each category
for cat_index, (category,subcategory) in enumerate(PRODUCT_SUBCATEGORIES.items(),start=1):
    for sub_index, subcat in enumerate(subcategory,start=1):
        print(f'category_id-{cat_index}, category name-{category} subcategory_id-{sub_index}, subcategory name-{subcat}')


