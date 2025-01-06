from numpy import *
import numpy as np

# working with salaries of employees


#linspace function uses
employee_salaries = linspace(30000,70000,10)
# print(employee_salaries)  # Prints salaries in floating-point format with evenly spaced numbers
#     #output : [30000.         34444.44444444 38888.88888889 43333.33333333 47777.77777778 52222.22222222 56666.66666667 61111.11111111 65555.55555556 70000.        ]

# # Convert salaries to integer format (truncates the decimal part)
# print(employee_salaries.astype(int))  # Outputs salaries as integers by truncating the decimals
#     #output : [30000 34444 38888 43333 47777 52222 56666 61111 65555 70000]

# # Round salaries to the nearest whole number (still floating-point numbers, but without decimals displayed)
# print(np.round(employee_salaries))  # Rounds and provides floating-point numbers without precision issues
#     #output : [30000. 34444. 38889. 43333. 47778. 52222. 56667. 61111. 65556. 70000.]

# # Convert rounded salaries to integers
# print(np.round(employee_salaries).astype(int))  # Rounds salaries first, then converts to integers
#     #output : [30000 34444 38889 43333 47778 52222 56667 61111 65556 70000]

# # Reason of using two different import for numpy is
# # When using from numpy import *, the round function from Python's built-in namespace (not NumPy) takes precedence,
# # so round refers to the standard Python rounding function.
# # With import numpy as np, i am explicitly calling np.round(), ensuring you use NumPy's version of the function.


# Generates a sequence of numbers as a NumPy array
arr = arange(10, 20, 1)
# print(type(arr))
salaries = employee_salaries.astype(int)

# Creating a 2D array by stacking of arr and salaries 
# two_d_array = np.column_stack((arr, salaries)).T  # Transpose to match row-wise layout
two_d_array = np.vstack((arr, salaries)).T  # Transpose to match column-wise layout
print(two_d_array)

# Getting the salary of the employee with ID 19
id = 12
salary_of_id = two_d_array[np.where(two_d_array[:, 0] == id)[0][0],1]

# Print the salary of employee with ID 19
print(salary_of_id)