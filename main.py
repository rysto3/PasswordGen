# basically just a demo of how it works

import PasswordOps

# Generate one password that is 4 words long and uses - as the separator
print(PasswordOps.generate_password(4,'-'))

# Generate one password that is 6 words long and uses a space as the separator
print(PasswordOps.generate_password(6,' '))

# Generate 100 passwords that are 12 words long and uses _ as the separator
for i in range(100):
    print(PasswordOps.generate_password(12,'_'))