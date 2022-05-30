# use find and slicing to extract the position of the string after the colon character
# and use float funtion to convert the string into a floating point number

str = "X-DSPAM-Confidence: 0.8475 "

# find the position of the first whitespace after the colon character
first_space = str.find(' ')

# find the position of the second whitespace after the colon character
second_space = str.find(' ', first_space + 1)

# slice the characters after the colon out of the string
slice_char = str[first_space + 1 : second_space]

# change the sliced characters to floating point number
float_num = float(slice_char)

print(float_num)
