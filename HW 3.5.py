import random

class Shyfrator:
    def __init__(self, num):
        self.num = num

        r = random.randint(1, 5)

        if random.randint(0, 1) == 0:
            self.result = self.num + r
        else:
            self.result = self.num * r

a = Shyfrator(5)
print(a.result)