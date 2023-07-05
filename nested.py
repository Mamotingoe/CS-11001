#In this example, the code checks multiple conditions by using nested conditionals.
#It checks the year the book was published first and then goes deeper into checking whether you’re a member of the store’s book club and discount eligibility.
#Depending on all these conditions, it finally assigns the appropriate book for you to buy.
year = 2023
is_member = False
on_discount = False

if year < 2024:
    if is_member:
        book = "Year of Yes" 
    else:
        book = "Collective Amnesia" 
else:
    if is_member and on_discount:
        book = "The Bluest Eye on Discount" 
    elif is_member:
        book = "The Bluest Eye" 
    elif on_discount:
        book = "A Beautiful Sunday on Discount" 
    else:
        book = "A Beautiful Sunday"

print(book)
