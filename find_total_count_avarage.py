# find the total, count and average of list of numbers input by users
# Output the total, count and average of numbers if users enters "done"

count = 0
total = 0


while True:
    # ask for users input
    num = input("Enter a number or 'done': ")
    if num == "done":
        break
    # chnage input to floating point number
    try:
       float_num = float(num)
    except:
        print("Invalid input")   
        continue
    count += 1
    total += float_num
    
average = total / count
print("Total: ", total, ", Count: ", count, ", Average: ", average)