# filter numbers greater than 20 in the list and print them out in a list
my_list = [2,5,12,34,56,7,83,7,843,8,9,20,34,67,9,3,6]

above_twenty = []
below_twenty = []

for num in my_list:
    if num >= 20:
        above_twenty.append(num)
    else:
        below_twenty.append(num)
        
print("These are the values that are above 20 in the given list: ", above_twenty)      
print("These are the values that are below 20 in the given list: ", below_twenty)  
    