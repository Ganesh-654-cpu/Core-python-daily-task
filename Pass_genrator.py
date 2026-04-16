import random
import string

# Step 1: Ask user for password length
length = int(input("Enter password length: "))

# Step 2: Create character set
letters = string.ascii_letters      # a-z, A-Z
digits = string.digits              # 0-9
symbols = string.punctuation        # !@#$%^&* etc.

all_characters = letters + digits + symbols

# Step 3: Generate password
password = ""
for i in range(length):
    password += random.choice(all_characters)

# Step 4: Show password
print("Generated Password:", password)