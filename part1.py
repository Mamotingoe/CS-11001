def print_circum(radius):
   circumference = 2 * 3.14159 * radius
   print("The circumference of a circle with radius {radius} is {circumference}.")
   print_circum(3)
   print_circum(1)
   print_circum(4)
#In the part where I coded the function, I used the keyword “def” to define the function and added the argument “radius” in the parentheses because that’s what we will need to input in order to get the circumference using “print_circum” to show the output. 
#I then assigned the variable “circumference” to the mathematical formula needed to calculate the output based on whatever integer input we give to the function. 
#I picked my 3 numbers, which are 3, 1, 4 and called the function using them as my inputs.
#Below are the outputs that come to be after calling the function for each input.
 #Input: 3
#Output: The circumference of a circle with radius 3 is 18.84956.
 #Input: 2
#Output: The circumference of a circle with radius 1 is 6.28319.
 #Input: 3
#Output: The circumference of a circle with radius 4 is 25.13274.
