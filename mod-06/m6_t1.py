import random

def nopanheitto():
    return random.randint(1, 6)

noppa = 0

while noppa != 6:
    noppa = nopanheitto()

    print(f'Nopan silmäluku: {noppa}')