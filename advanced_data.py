############# Q9. Print the sum of the first and third element in the list "numbers" and print the result ############
# Topic: tuples

numbers = (4, 9, 16, 36)

# Code here

print(numbers[0]+numbers[2])


############# Q10. Fill out the next 3 nubmers in the pattern using the append() function and print the result ############
# Topic: lists, list functions

numbers = [4, 9, 16, 25]

# Code here

numbers.append(6**2)
numbers.append(7**2)
numbers.append(8**2)
print(numbers)





############# Q11. Append the sum of the 2nd and 4th element in the list "numbers" to itself and print the result ############
# Topic: lists, list functions

numbers = [4, 9, 16, 25]

# Code here

numbers.append(numbers[1]+numbers[3])
print(numbers)



############# Q12. Fill in the missing number between 16 and 36 and print the result ############
# Topic: lists, list functions

numbers = [4, 9, 16, 36]

# Code here

numbers.insert(3,5**2)
print(numbers)


############# Q13. Remove the element that breaks the pattern and print the result ############
# Topic: lists, list functions

numbers = [3, 9, 16, 25, 36]









############# 
# Q14. Create a dictionary with the following data and print the dictionary:
# Alex has $100
# Kevin has $50
# Henry has $500
############

# Topic: dictionaries

# Code here

def price(number):
    return ("$" + str(number))

BankAccount = {
    "Alex": 100,
    "Kevin": 50,
    "Henry": 500
}
print(BankAccount)








############# 
# Q15 A. Create a dictionary with the following transactions and print the dictionary:
# Alex purchased a sweater for $100
# Kevin purchased a bookbag for $50
# Henry purchased a scarf for $500
############

# Topic: nested dictionaries

# Code here

TransactionSheet = {
    "Alex": {
        "sweater": 100
    },
    "Kevin": {
        "bookbag": 50
    },
    "Henry": {
        "scarf": 500
    }
}
print(TransactionSheet)
#print(TransactionSheet[TransactionSheet["Alex"]])


############# Q15 B. Using the dictionary from Q15, add the following transactions and print the dictionary:
# Jason purchased a wallet for $250
# Michael purchased a pair of sneakers for $50
# Andrew purchased a t-shirt for $20 AND a hoodie for $30

# Also, print the value of Andrew's hoodie without using print(30)

### YOU MAY NOT EDIT THE ORIGINAL DICTIONARY

# Topic: nested dictionaries

# Code here

TransactionSheet["Jason"] = {"wallet": 250}
TransactionSheet["Michael"] = {"pair of sneakers": 50}
TransactionSheet["Andrew"] = {"t-shirt": 20, "hoodie": 30}
print(TransactionSheet)
print(price(TransactionSheet["Andrew"]["hoodie"]))





############# Q162. Using the dictionary from Q15 B, MODIFY the following transactions and print the dictionary:
# Jason's wallet purchase: $100
# Alex's sweater purchase: $20
# Henry's scarf purchase: $200

### YOU MAY NOT EDIT THE ORIGINAL DICTIONARY

# Topic: nested dictionaries

# Code here
TransactionSheet["Jason"]["wallet"] = 100
TransactionSheet["Alex"]["sweater"] = 20
TransactionSheet["Henry"]["scarf"] = 200
print(TransactionSheet)









############# Q16. Using the dictionary from Q15, give every purchase a 10% discount and print the dictionary:

### YOU MAY NOT EDIT THE ORIGINAL DICTIONARY

# Topic: nested dictionaries

# Code here

entrynumber = 0
for x in TransactionSheet:
    for y in TransactionSheet[x]:
        Value = TransactionSheet[x][y]
        DiscountValue = Value / 10 * 9
        TransactionSheet[x][y] = DiscountValue
        print(DiscountValue)

print(TransactionSheet)






