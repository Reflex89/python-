users = ['admin','reflex','king','yingzi','losters']
for user in users:
    if user == 'admin':
        print(f"Hello {user.title()}, would you like to see a status report?\n")
    else:
        print(f"Hello,{user.title()},thank you for logging in again.\n")