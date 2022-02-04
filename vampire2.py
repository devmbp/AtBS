# This name-checker program checks to see if a user is Alice or an imposter.
# A bug has been introduced in this version to test the importance of order in elif Statements.

name = 'Alice'
age = 11
if name == 'Alice':
    print('Hi Alice.')
elif age < 12:      # Alice is 12 years or older
    print('You are not Alice, kiddo.')
elif age > 100:
    print('You are not Alice, grannie.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
