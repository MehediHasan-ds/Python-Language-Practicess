from numpy import *
import numpy as np

# # working with salaries of employees


# #linspace function uses
# employee_salaries = linspace(30000,70000,10)
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



# # Generates a sequence of numbers as a NumPy array
# arr = arange(10, 20, 1)
# # print(type(arr))
# salaries = employee_salaries.astype(int)

# # Creating a 2D array by stacking of arr and salaries 
# # two_d_array = np.column_stack((arr, salaries)).T  # Transpose to match row-wise layout
# two_d_array = np.vstack((arr, salaries)).T  # Transpose to match column-wise layout
# print(two_d_array)

# # Getting the salary of the employee with ID 19
# id = 12
# salary_of_id = two_d_array[np.where(two_d_array[:, 0] == id)[0][0],1]
# print(f"salary of id {id} is {salary_of_id}")



# #ZEROES and ONES array
# zeros_array = zeros(5)
# print(zeros_array)

# ones_array = ones(5,int)
# print(ones_array)



# #ADD bonus of 5000 to salaries of every employee
# new_salaries = salaries + 5000
# print(new_salaries)



# #TOTAL employee salaries using SUM function
# total_employee_salaries = sum(new_salaries)
# print("Total Employee Salaries: ",total_employee_salaries)



# #MAXIMUM and MINIMUM salary
# print("Maximum salary: ", max(new_salaries))
# print("minimum salaries: ",min(new_salaries))

# # a new array with employee_expenses_without_salary
# employee_expenses_without_salary = linspace(10000,15000,10).astype(int)
# print("employee_expenses_without_salary: ",employee_expenses_without_salary)



# # finding TOTAL EXPENSES after each of the employee by
# # ADDING salary and other expenses together
# total_expenses_on_each_employee = salaries+employee_expenses_without_salary
# print("total_expenses_on_each_employee: ",total_expenses_on_each_employee)



# print(f"type of salaries: {type(salaries)}, type of expense without salary: {type(employee_expenses_without_salary)}")

# #MERGING total expenses using CONCATENATE function
# merged_expenses = concatenate([salaries,employee_expenses_without_salary])
# print("Merged expenses :",merged_expenses)


# #SORTING the expenses
# sorted_expenses = sort(merged_expenses)
# print("Sorted expenses: ", sorted_expenses)


# #COPY all the expenses to a new location
# copied_expenses = merged_expenses.view() #shallow copy: means changing in any of the two array(original/copied)
#                                          #will change the value in another array. 

# copied_expenses = merged_expenses.copy() #deep copy: means changing in any of the two array(original/copied)
#                                          #will not change the value in another array. Hence will create a completely new array in different location



#MATRIX function to create a matrix
matrx = matrix('1 2 3 4; 5 6 7 8; 9 10 11 12')
print("Matrix created using the matrix function: \n",matrx)

#creating two different matrix
matrix1 = np.random.randint(0, 10, (3, 4))
matrix2 = np.random.randint(0, 10, (4, 3))
print("\nMatrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)


#DIMENSION of the matrix1
print("Dimension of matrix 1: ",matrix1.ndim)
# SHAPE of matrix1
print("Shape of matrix 1: ",matrix1.shape)
#SIZE of matrix1
print("Size of matrix 1: ",matrix1.size)


#FLATTEN: convert 2D array into 1D array
flattened_data = matrix1.flatten()
print("Flattened data of matrix 1: ",flattened_data)


#RESHAPE to create 3D array from 1D array
three_D_matrix = flattened_data.reshape(3,2,2) # 3D matrix has three rows of 2D matrix,
                                               #each 2D matrix has 2 rows and two columns
print("3D matrix is displayed here \n",three_D_matrix)


#DIAGONAL of a matrix
print("Diagonal of matrx are: ",matrx.diagonal())


#ADDING matrices
resulting_added_matrix = add(matrix1,matrx)
print("\nMatrix created using the matrix function: \n",matrx)
print("\nMatrix 1 \n",matrix1)
print("\nresulting_added_matrix \n",resulting_added_matrix )

#MULTIPLYING matrices
resulting_multiplied_matrix = dot(matrix1,matrix2)
print("\nMatrix created using the matrix function: \n",matrix1)
print("\nMatrix 1 \n",matrix2)
print("\nresulting_multiplied_matrix \n",resulting_multiplied_matrix )



