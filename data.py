############ Q1. Change the value of x to 5 and print the sum of x and y ############
# Topic: arithmetic/assignment operators

x = 9
y = 3

# Code here

x = 5
print(x+y)



############ 
# Q2. Change the value of x by the remainder of x divided by 3
# Print the sum of the new value of x and y
############
# Topic: arithmetic/assignment operators

x = 5
y = 2

# Code here

x %= 3
print(x+y)



############ 
# Q3. Print the sum of the 2 results:
# x divided by y  
# y times x
############
# Topic: arithmetic operators
# Hint: Should print 30

x = 9
y = 3

# Code here

print(x/y+y*x)


############ Q4.s
# 1) Create a new variable, z
# 2) Assign the remainder of x divided by y to variable z
# 3) Multiply the remainder with x 
# 4) Divide x by the result of #3
# 5) Print the value of x (should be 0.5)
# ############
# Topic: arithmetic/assignment operators

x = 8
y = 3

z = x % y
a = z*x
x /= a
print(x)





############# Q5. Print the square root of x IN 2 DIFFERENT WAYS ############
# Topic: arithmetic operators
# Hint: x to what power equals the square root of x?


import math #import the math module
x = 9

# Code here


#print(x^(1/2))
print(math.sqrt(x))



############# Q6. print the phrase "hello world" using the 2 variables defined below ############
# Topic: string concatenation

string1 = "hello"
string2 = "world"

# Code here

print (string1 + string2)


############# Q7. Print the phrase "5 dogs" using the 2 variables defined below ############
# Topic: string concatenation

integer = 5
string = "dogs"

# Code here



############# Q8. Print the sum of x and string ############
# Topic: string concatenation

x = 3
string = "5"

# Code here

print(x+'string')

############# Q9. Print the sum of the first and third element in the list "numbers" and print the result ############
# Topic: tuples

numbers = (3, 9, 16, 36)

# Code here





############# Q10. Fill out the next 3 nubmers in the pattern using the append() function and print the result ############
# Topic: lists, list functions

numbers = [3, 9, 16, 25]

# Code here







############# Q11. Append the sum of the 2nd and 4th element in the list "numbers" to itself and print the result ############
# Topic: lists, list functions

numbers = [3, 9, 16, 25]

# Code here





############# Q12. Fill in the missing number between 16 and 36 and print the result ############
# Topic: lists, list functions

numbers = [3, 9, 16, 36]

# Code here





############# 
# Q13. Create a dictionary with the following data and print the dictionary:
# Alex has $100
# Kevin has $50
# Henry has $500
############

# Topic: dictionaries

# Code here








############# 
# Q14 A. Create a dictionary with the following transactions and print the dictionary:
# Alex purchased a sweater for $100
# Kevin purchased a bookbag for $50
# Henry purchased a scarf for $500
############

# Topic: nested dictionaries

# Code here









############# Q14 B. Using the dictionary from Q14, add the following transactions and print the dictionary:
# Jason purchased a wallet for $250
# Michael purchased a pair of sneakers for $50
# Andrew purchased a t-shirt for $20 AND a hoodie for $30

# Also, print the value of Andrew's hoodie without using print(30)

### YOU MAY NOT EDIT THE ORIGINAL DICTIONARY

# Topic: nested dictionaries

# Code here








