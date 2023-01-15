a = list(input())
b = {}
for i in a:
    try: 
        b[i] += 1
    except: 
        b[i] = 1

for key, values in b.items():
    print(key, ",", values, sep = "")