import random
import string

SECRET_KEY = ''.join(random.choice(string.ascii_letters) for _ in range(32))
