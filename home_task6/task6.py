# task-2

# 1-usul
def sun(a, b):
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] + a[j] == b:
                return [i, j]
    return None
arr = [3, 1, 2, 5, 7]
foo = 6

print(sun(arr, foo))


