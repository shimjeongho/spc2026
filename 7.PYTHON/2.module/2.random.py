import random
import string

def generate_random_password(lenght=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for i in range(lenght))

print(generate_random_password())
print(generate_random_password(16))
print(generate_random_password(32))

"""
zEs2AAvb
u30OStrnXpDTO57Z
6s2xA6jJipQv961BT3xmksaHVU3cA8Yy
"""