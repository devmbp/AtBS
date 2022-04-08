# A simple program that asks for a name and password.
# This program illustrates the combined usage of break and continue statements

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':   # Case-sensitivity is key here
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish': # Case-sensitivity is key here too
        break
print('Access granted.')
