big_box = True
book_author = "Toni Morrison"

if big_box:
    if book_author == "Toni Morrison":
        read_book = "The Bluest Eye"
    elif book_author == "Shonda Rhimes":
        read_book = "Year of Yes"
    elif book_author == "Koleka Putuma":
        read_book = "Collective Amnesia"
    else:
        read_book = "no book"
else:
    read_book = "no book"

print(read_book)
