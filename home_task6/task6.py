# task-1

class Animals:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'name: {self.name}'

    def __repr__(self):
        main_name = type(self).__name__
        return f'{main_name}'

    def __del__(self):
        return 'del method is working'

    def __eq__(self, other):
        self.other = other
        return f'eq method is working, {self.other == self.name}'

c1 = Animals('tiger')
c2 = Animals('panda')
c3 = Animals('bear')
c4 = Animals('kitty')
c5 = Animals('kitty')
print(c1)
print(c2.__repr__())

del c3
# print(c3)

print(c4 == c5)


# task-2

# 1-usul
# def sun(a, b):
#     for i in range(len(a) - 1):
#         for j in range(i + 1, len(a)):
#             if a[i] + a[j] == b:
#                 return [i, j]
#     return None
# arr = [3, 1, 2, 5, 7]
# foo = 6
#
# print(sun(arr, foo))