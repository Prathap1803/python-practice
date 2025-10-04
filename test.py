name = "this is test to test the test"
dict = {}
dict2 = {}
for s in name:
    dict[s] = dict.get(s, 0) + 1
for key, value in dict.items():
    dict2.setdefault(value, []).append(key)

print(dict)
print((dict2))    