#Create a variable called 'number' and assign it the two-digit number
number = 69
#Find the reverse of the number and assign it to a variable called 'answer'.
last_digit = number % 10
first_digit = (number - last_digit)/10
answer = last_digit, first_digit
#Print the value of the 'answer'
print(answer)