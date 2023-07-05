#In the modified code, we use a single conditional with multiple if, elif, and else statements to determine the appropriate book to buy.
#It checks the year published first and then goes through the different possibilities of membership and discount to assign the book accordingly.
year = 2023
is_member = False
on_discount = False

if year < 2024:
    if is_member:
        book = "Year of Yes"
    else:
        book = "Collective Amnesia"
else:
    if is_member:
        if on_discount:
            book = "The Bluest Eye on Discount"
        else:
            book = "The Bluest Eye"
    else:
        if on_discount:
            book = "A Beautiful Sunday on Discount"
        else:
            book = "A Beautiful Sunday"

print(book)
