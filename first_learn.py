# Mutability vs Immutability

# Immutable objects are common in functional programming, while mutable objects are widely used in object-oriented programming. Because Python is a multiparadigm programming language, it provides mutable and immutable objects for you to choose from when solving a problem.

# To understand how mutable and immutable objects work in Python, you first need to understand a few related concepts. To kick things off, you’ll take a look at variables and objects.



# Naming Convention 

# x = "JohnhnSmith"
# # x,z, y = x.split('n')
# lst = x.split()

# # print(f"{x} zzzz {z}, yyyyy {y}")
# print(lst)




# Change this as per structure way of nameing

# name= 'vishal singh'
# first_name,Last_name=name.split()
# print(f"{first_name}, {Last_name}")



# class classWith_method:
#    def first_method(self, height, weight):
#       return f"hello my name vishal and height {height}  and weight{weight}"
  
# person=classWith_method()

# result=person.first_method(178,78)
# print(result)
   
# def calculatesum():
#     Total_sum=0
#     n=int(input("How many number would like to add "))
#     for i in range(n):
#         number=float(input(f"Enter number  {i+1}  "))
#         Total_sum+=number
#         print("this is the total sum   "Total_sum)

# calculatesum()
# def get_number_input():
#     while True:
#         try:
#             # Ask user for a number
#             number = float(input("Please enter a number: "))
#             return number  # Return the valid input if no error occurs
#         except ValueError:
#             # Handle the case where the input is not a valid number
#             print("That's not a valid number. Please try again.")
#         except Exception as e:
#             # Catch any other unexpected errors
#             print(f"An unexpected error occurred: {e}")
#         finally:
#             print("This block always runs.")

# def calculate_sum():
#     total_sum = 0
#     n = int(input("How many numbers would you like to sum? "))
    
#     for i in range(n):
#         number = get_number_input()  # Call the function to get valid user input
#         total_sum += number

#     print(f"The total sum is: {total_sum}")

# # Call the function
# calculate_sum()

# def get_number_input():
#     while True:
#         try:
#             # Ask user for a number
#             number = float(input("Please enter a number: "))
#             return number  # Return the valid input if no error occurs
#         except ValueError:
#             # Handle the case where the input is not a valid number
#             print("That's not a valid number. Please try again.")
#         except Exception as e:
#             # Catch any other unexpected errors
#             print(f"An unexpected error occurred: {e}")
#         finally:
#             print("This block always runs.")

# def calculate_sum():
#     total_sum = 0
#     n = int(input("How many numbers would you like to sum? "))
    
#     for i in range(n):
#         number = get_number_input()  # Call the function to get valid user input
#         total_sum += number

#     print(f"The total sum is: {total_sum}")

# # Call the function
# calculate_sum()
t=(2,)
print(type(t))