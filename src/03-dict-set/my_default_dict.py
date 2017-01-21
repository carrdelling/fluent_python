from collections import UserDict


class MyDefaultDictFloat(UserDict):

    def __missing__(self, key):
        self[key] = 0.
        return self[key]


a = MyDefaultDictFloat()

a.update({3: 1.5, 2: 1.7})

print(a[3], a[8])



