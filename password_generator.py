import random


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"


def generate_password(length):
    password = "" 
    for _ in range(length):
   
        password += random.choice(chars)
    return password 

# 3. The 'Business 8' Interface
print("\n--- Password Generator ---")
how_many = int(input("How many passwords do you need? \t"))
how_long = int(input("How many characters per password? \t"))

print(f"\nGenerating {how_many} secure passwords...\n")


for i in range(how_many):
    result = generate_password(how_long)
    
    # Rating Logic
    if how_long < 8:
        security = "WEAK "
    elif how_long < 15:
        security = "STRONG "
    else:
        security = "PHD LEVEL "
        

    print(f"{i + 1}.\t{result}\t[{security}]")

print("\n" + "="*30 + "\nEncryption Complete.")

# .
