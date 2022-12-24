import random

letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

symbol = ['@', '#', '$', '%', '^', '&', '*', '~', '_']


# ------------------------Take user input------------------------------------
print("Welcom to password generator!")

lr_letter = int(input("How many letters would you like in your password!\n"))
nr_number = int(input("How many numbers would you like in your password!\n"))
sr_symbol = int(input("How many symbols would you like in your password!\n"))


# ------------------------used to generating password-------------------------
password_list = []

for ltr in range(1, lr_letter+1):
    password_list.append(random.choice(letter))
    # password_list.append = password + random_ltr

for nm in range(1, nr_number+1):
    password_list.append(random.choice(number))

for sym in range(1, sr_symbol+1):
    password_list.append(random.choice(symbol))
random.shuffle(password_list)

# -------------------converting list to string----------
password = ""
for chr in password_list:
    password += chr
print("\nYour new system generated password is:")
print(password)

