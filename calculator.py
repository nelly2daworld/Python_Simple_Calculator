print("Please insert your first number")
first_number_string = input(">> ")
first_number = int(first_number_string)
# print(first_number)

print("Please insert your second number")
second_number_string = input(">> ")
second_number = int(second_number_string)
# print(second_number)

print("Your numbers are " + first_number_string + " and " + second_number_string)
print("Select your operator: ADD, MULTIPLY or SUBTRACT")
operator = str(input(">> "))

if operator == "ADD":
    result = first_number + second_number
elif operator == "MULTIPLY":
    result = first_number * second_number
elif operator == "SUBTRACT":
    result = first_number - second_number
else:
    print("Sorry, that option is not supported")
    
resultString = str(result)
print("Your result is " + str(resultString))
    
