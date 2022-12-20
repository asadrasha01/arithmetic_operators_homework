#Create a varaible 'number' and assign it the value of 43.
number = 43
#Create a variable 'answer' and assign it the sum of the number's digits.
last_digit = number % 10
first_digit = (number - last_digit)/10
answer = first_digit + last_digit
#Print the vallue of the 'answer'.
print(answer)