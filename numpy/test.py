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