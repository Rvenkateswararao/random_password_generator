# create a random password generator by using random module ....import random it gives random numbers...
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$',"%",'&','*','-']
print("welocome to password generator !")
n_letters = int(input("how many letters you want in your password: "))
n_numbers = int(input("how many numbers you want in your password: "))
n_symbols = int(input("how many symbols you want in your password: "))
password = []
# we use the for loop because the nummbers and letters and symbols will be itterated by using for loop  
for i in range(0,n_letters+1):
    char = random.choice(letters)
    password += char

for i in range(0,n_numbers+1):
    num = random.choice(numbers)
    password += num


for i in range(0,n_symbols+1):
    sym = random.choice(symbols)
    password += sym
print(password)
random.shuffle(password)
# print("ofter shuffle password is :",password)2
print(password)

print("thank you ")
# succesfully completed password generator project...



