# find the smallest value in the list given
my_list = [10, 6, 7, 14, 56, 69, 100, 5]
smallest_value = None
for num in my_list:
    if smallest_value is None or num < smallest_value:
        smallest_value = num
    print("Loop:", num, smallest_value)
    
print(smallest_value, "is the smallest value in the list")   