import sys

# get user from server
user = sys.argv[1]

# check if user is DB
if user=='Maria':
    print(0)
    exit(0)
else:
    print(-1)
    exit(-1)

# print(f'User {user} is logged!')