#Lists (mutability checking)
items = ["Computer","Processor","CPU","Motherboard","RAM","Monitor"]
print(id(items))

#adding new item to the list
items.append("Keyboard")
print(id(items)) #id same as before

items = ["Computer","Processor","CPU","Motherboard","RAM","Monitor","Mouse"]
print(id(items)) #id changed because of redeclaration
#lists used for its mutability(dynamic data change), ordered collections, duplicate data and indexing,slow(linear search)



#Tuples (mutability checking)
os_components_tuple = ("Kernel", "File System", "Memory Management", "Device Drivers", "User Interface")
print("Operating System Components (Tuple):", os_components_tuple)

# Trying to add a new component to the tuple (will raise an error)
try:
    os_components_tuple.append("Network Management")  # This will raise an error
except AttributeError as e:
    print("Error:", e)

#Converting tuple to a list (comment out line 19-22 before running this part)
os_components_list = list(os_components_tuple)
# Trying to add a new component to the list (will not raise any error)
try:
    os_components_list.append("Network Management")  # This will not raise any error
    print("Operating System Components (List):",os_components_list)
except AttributeError as e:
    print("Error:", e)
#tuples used for its immutability(data cannot be changed), ordered collections, duplicate data and indexing,slow(linear search)



#sets mutability checking(comment out previous part before running the following)
os_components_set = {"Kernel","Kernel", "File System", "Memory Management", "Device Drivers", "User Interface", "Kernel"}
print("Set:", os_components_set)
try:
    os_components_set.add("Network Management")  # This will not raise any error
    print("Operating System Components (set):",os_components_set)
except AttributeError as e:
    print("Error:", e)
#set is used for its mutability, unordered and unique collections, no indexing properties, fast and optimized for searching



#dictionary
os_components_dict = {
    "Kernel": "Core part of the OS managing resources",
    "File System": "Handles data storage and retrieval",
    "Memory Management": "Manages memory allocation",
    "Device Drivers": "Facilitates communication with hardware",
    "User Interface": "Interacts with the user"
}
# Accessing a value using key
print("Kernel Description:", os_components_dict["Kernel"])

# Adding a new key-value pair
os_components_dict["Security"] = "Handles authentication and encryption"

# Updating an existing key-value pair
os_components_dict["Kernel"] = "Manages CPU, memory, and devices"

# Deleting a key-value pair
os_components_dict.pop("User Interface")
print("Updated Dictionary:", os_components_dict)
#dictionary is used for its mutability, ordered collections, indexing properties, fast and optimized for searching by key, accessing values by keys



#List comprehension
os_components = ["Kernel", "File System", "Memory Management", "Device Drivers", "User Interface"]

components_with_space = [component.upper() for component in os_components if " " in component]
print(components_with_space)

#creating a dictionary from a list
components_dict = {component: len(component) for component in os_components}
print(components_dict)

#creating a list of all characters in each component
characters_list = [[character.capitalize() for character in component] for component in os_components]
print(characters_list)
#list comprehension is used to create a list from an existing list. this comprehension method can also be used for set and dictionary as well.


PRODUCT_CATEGORIES = ["Electronics", "Clothing", "Home & Kitchen", "Books", "Toys"]
PRODUCT_SUBCATEGORIES = {
    "Electronics": ["Smartphones", "Laptops", "Accessories"],
    "Clothing": ["Men's Wear", "Women's Wear", "Kids' Wear"],
    "Home & Kitchen": ["Furniture", "Cookware", "Decor"],
    "Books": ["Fiction", "Non-Fiction", "Educational"],
    "Toys": ["Action Figures", "Board Games", "Stuffed Toys"]
}

# print the categories with values by providing each category an index. (for indexing using enumerate)
for index, (key, values) in enumerate(PRODUCT_SUBCATEGORIES.items(),start=1):
    print(f'Category-{index}: {key}')
    for value in values:
        print(value)

# print the available brands for each subcategory under each category
for cat_index, (category,subcategory) in enumerate(PRODUCT_SUBCATEGORIES.items(),start=1):
    for sub_index, subcat in enumerate(subcategory,start=1):
        print(f'category_id-{cat_index}, category name-{category} subcategory_id-{sub_index}, subcategory name-{subcat}')

# which brand falls into which category and subcategory
for cat_index, (category,subcategory) in enumerate(PRODUCT_SUBCATEGORIES.items(),start=1):
    for sub_index, subcat in enumerate(subcategory,start=1):
        for subcat_idx,(_,brands) in enumerate(BRANDS.items()):
            for brand_idx, brand in enumerate(brands,start=1):
                print(f'category_id-{cat_index}, category name-{category} subcategory_id-{sub_index}, subcategory name-{subcat}, brand-{brand}')



