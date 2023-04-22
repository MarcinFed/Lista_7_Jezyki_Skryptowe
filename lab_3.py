import random
import string
from lab_6 import log
import logging


@log(logging.DEBUG)
class PasswordGenerator:
    def __init__(self, length, charset=None, count=float('inf')):
        self.length = length
        self.charset = charset or string.ascii_letters + string.digits
        self.count = count
        self.generated = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated >= self.count:
            raise StopIteration
        self.generated += 1
        return "".join(random.choice(self.charset) for _ in range(self.length))


if __name__ == "__main__":
    password_generator = PasswordGenerator(10, count=10)
    print(next(password_generator))
    for password in password_generator:
        print(password)