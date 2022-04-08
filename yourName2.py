# break Statements
# Here's a program that asks user to enter name. Call it yourName v.2.0
# Unlike yourName v.1.0, v.2.0 uses a break statement to avoid the loop

while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')
