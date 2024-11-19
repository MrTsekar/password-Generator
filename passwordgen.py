import random
import os

print("WELCOME TO PASSWORD GENERATOR")
numbers = ['1','2','3','4','5','6','7','8','9','0']
symbol = ['!','@','#','$','%','&','+','*','?']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def valid_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Error: Please enter a valid integer.")

platform = input("What Platform are you signing up for?\n").capitalize()
user_name = input("Enter your username: \n")
p_numbers= valid_input("How many numbers do you want in your password?\n")
p_symbols = valid_input("How many symbols do you want in your password?\n")
p_letters =  valid_input("How many letters do you want in your password?\n")

password = []
for char in range(0, p_numbers):
    password.append(random.choice(numbers))
for char in range(0, p_symbols):
    password.append(random.choice(symbol))
for char in range(0, p_letters):
    password.append(random.choice(letters))
random.shuffle(password)

final_password = "".join(password)

filename = 'password_logs.txt'
with open(filename, 'a') as file:
    file.write(f"Password for {platform}: {user_name} {final_password}\n\n")

file_path = os.path.abspath(filename)

print(f"Your Password is {final_password}")
print(f"Your registered for {platform} with USERNAME: {user_name} and generated a PASSWORD: {final_password}")
print(f"You can find your CREDENTIALS at:  {file_path}")
