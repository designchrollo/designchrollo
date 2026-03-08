import time 
users = {
    "009": "Cullen O'Brien",
    "010": "John Doe",
    "101": "Admin",
    "999": "Owner"
}
print ("\n--- SECURE VAULT ACCESS ---")
user_id = input("\nEnter Your User ID: ")
if user_id in users:
    name = users[user_id]
    print(f"User ID recognized. Welcome back! {name}")
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_data = [timestamp, user_id, name, "ACCESS_GRANTED"]
    log_entry = "\t".join(log_data)
    with open("vault_log.txt", "a") as file:
        file.write(log_entry + "\n")
        
    print(f"User {name} has been logged in 'vault_log.txt'.")
else:
    print(" User ID not recognized: Unknown ID.")
    # fixing the + button