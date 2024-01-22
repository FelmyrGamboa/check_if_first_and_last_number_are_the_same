# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# Given:

# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]

#Create a function to check the first and last number
def check_first_and_last_number(number_list):
#Write a condition to return if first and last number of the list is same
    if number_list[0] == number_list[4]:
        return True
#If not return false
    else:
        return False
    
#Give the list
number_list_1 = [10, 20, 30, 40, 10]
number_list_2 = [75, 65, 35, 75, 30]

#Call out the function
check_first_and_last_number(number_list_1)
check_first_and_last_number(number_list_2)

#Display the result