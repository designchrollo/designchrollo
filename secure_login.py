import time 
password = "Cullen5426143567"
attempts = 0
while True:
    guess = input  ("\n[SECURITY] Enter Admin Password: ")
    attempts += 1
    if guess == password:
        print("Welcome back Cullen!")
        break
    else:
        print("Incorrect password.")
        if attempts >= 3:
            print("Too many failed attempts. Access denied.")
            break