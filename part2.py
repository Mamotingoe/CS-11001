#The first funtion I used was to define the overall code, which is finding the pricing of the items and combos on the catalog before and after discount has been added
def calculate_catalog(item, quantity):
    #Then I gave each item a price by assigning their variables
    item_prices = {
        'Item1': 200,  # Price of individual item 1
        'Item2': 400,  # Price of individual item 2
        'Item3': 600   # Price of individual item 3
    }
#I used the below IF statement to get the price of the gift pack combo
    if item == 'combo_4':
        pack_price = sum(item_prices.values()) * 0.75  # if a customer buys a gift pack which consists of all 3 items, they get 25% discount for gift pack
        return pack_price * quantity
#I then assigned variables for the combo prices as per image output in the question
    combo_prices = {
        ('Item1', 'Item2'): 540,  # Price of combo 1 (Item1 + Item2)
        ('Item1', 'Item3'): 720,  # Price of combo 2 (Item1 + Item3)
        ('Item2', 'Item3'): 900   # Price of combo 3 (Item2 + Item3)
    }

    if isinstance(item, tuple):
        if item in combo_prices:
            combo_price = combo_prices[item]  # Get the price for the specific combo
            combo_discounted_price = combo_price * 0.9  # if a customer buys a gift pack which consists of all 2 unique items, they get 10% discount for combo packs
            return combo_discounted_price * quantity

    if item in item_prices:
        return item_prices[item] * quantity

    return 0.0  # Return 0 if the item is not found


# Output example:
print(calculate_catalog('gift_pack', 1))           # Price of 1 gift pack (all three items)

#In the output, if a customer buys the gift pack, the function will give them a 25% discount on the original combo price, and it will do this with all other combo discounts
