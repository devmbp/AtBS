# This ID verification program utilizes all Flow Control Statements together.
# Again, the order of precedence is critical here (if > elif > else)

if name == 'Alice':
    print('Hi Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')
