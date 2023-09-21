#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ask user's needs
print("Welcome to the PyPassword Generator!")
hm_letters= int(input("How many letters would you like in your password?\n")) 
hm_numbers = int(input(f"How many numbers would you like?\n"))
hm_symbols = int(input(f"How many symbols would you like?\n"))

# creat a list
password_list = []

# put random elements(letters, numbers, symbols) into the list
for char in range(0, hm_letters):
    password_list += random.choice(letters)

for char in range(0, hm_numbers):
    password_list += random.choice(numbers)

for char in range(0, hm_symbols):
    password_list += random.choice(symbols)

# shuffle the list
random.shuffle(password_list)

# convert list into string
final_password = ''.join(password_list)

print(final_password)
