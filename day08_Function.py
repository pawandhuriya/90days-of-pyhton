# def great():
#     print("Hello")
#     print("Hi")
#     print("Hows doing")    
# great()
# # Function with name
# def greet_with(name):
#     print(f"hello {name}")
#     print(f"How do you do {name}")
# greet_with("pawan")

# Fucntion with name and location

# def greet_with(name,location):
#     print(f"Heloo {name}")
#     print(f"Where are you been living in {location}")
# greet_with(name="pawan",location="nagpur")
# ------------------------------------------------
# excersize 8.1 wall paint
# import math
# def paint_calc(height,width,cover):
#     num_can=((height*width)/cover)
#     print("You will be needing ",math.ceil(num_can),"cans")
# test_h=int(input("Height of wall: " ))
# test_w=int(input("Width of the wall: "))
# coverage=5
# paint_calc(height=test_h,width=test_w,cover=coverage)

# how to find prime number
# def prime_checker(number):
#         for i in range(2,number):
#                 if number%i==0:
#                         print("This is a prime Number",n)
#                 else:
#                         print("not a prime")
# n=int(input("Enter the Number: "))
# prime_checker(number=n)          

# Excerisize of caesar-cipher
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=input("Type 'Encode' to encrypt,type'decode 'fot decrypt:\n")
text=input("Type your msg:\n ").lower()
shift=int(input("type the shift number: \n"))
def encrypt_text(plaintext,n):
    ans=""
    for i in range(len(plaintext)):
        ch=plaintext(i)
        






    



