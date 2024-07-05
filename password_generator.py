import string
import random

charValues = string.ascii_letters + string.digits + string.punctuation
len=int(input("Enter length of password:")) #input length of password
password=""
for i in range(len):
    password += random.choice(charValues)   #Generating Random Password

print("Your random generated Password is : ",password)  #print Password