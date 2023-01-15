a = [3, 1, 2]

indices = sorted(
    range(len(a)),
    key=lambda index: a[index]
)

print(indices)