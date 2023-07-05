#CS1101 Learning Journal 2 - JM

#Question 1
def print_circum(rad):
    pi=3.14159
    temp = 2*pi*rad
    print("A circle with the radius of " + str(rad) + " has a circumference of " + str(temp) )

#example calls
print_circum(5)
print_circum(15)
print_circum(50)



#Question 2
def catalog(item1,item2,item3):
    print("Online Store")
    print("------------------")
    print("Product(s) \t \t " +  "Price")
    print("Item 1 \t \t \t" +  "$"+  str(item1) )
    print("Item 2 \t \t \t" +  "$"+  str(item2) )
    print("Item 3 \t \t \t" +  "$"+  str(item3) )
    print("Combo 1 (Item 1 + 2) \t" +  "$"+  str((item1+item2)*.90)) 
    print("Combo 2 (Item 2 + 3) \t" +  "$"+  str((item2+item3)*.90)) 
    print("Combo 3 (Item 1 + 3) \t" +  "$"+  str((item1+item3)*.90)) 
    print("Combo 4 (Item 1 + 2 + 3) \t" +  "$"+ str((item1+item2+item3)*.75)) 
    print("------------------")
    print("For delivery Contact 98764678899")

#example calls
catalog(5,10,15)
catalog(80,90,100)
catalog(250,500,750)
