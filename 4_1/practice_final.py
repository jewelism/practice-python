# a = [ 10, 11, 12, 14, 13 ]
# b = sorted(a)
# print(b)
# print(a)
# 
# 
# del a[0]
# print(a)

# -*- coding: utf-8 -*- #

class Counter:
    def __init__(self):
        self.count = 0

    def Counter(self):
        print(self.count)
        return self

    def reset(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def get(self):
        return self.count


c = Counter()
print(c.Counter())
