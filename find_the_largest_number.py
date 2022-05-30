# find the largest value in the list given
my_list = [5, 6, 7, 14, 56, 69, 100]
largest_value = 0
for num in my_list:
    if num > largest_value:
        largest_value = num
   
    
print(largest_value, "is the largest value in the list")        