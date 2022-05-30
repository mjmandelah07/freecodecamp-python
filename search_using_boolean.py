# search for values using boolen variables 
# search if 10 is avaliable in the list and return True if found or False if not found

my_list = [1,2,3,4,5,6,7,8,9,10,11,12]
found = False
# ask for number to be found in the list from users
number_to_be_found = int(input("Enter the number you want to find in the list: "))

for num in my_list:
    if num == number_to_be_found:
        found = True
        break
print("Is ",number_to_be_found, "available in the given list ",my_list, " : ", found)    
        
