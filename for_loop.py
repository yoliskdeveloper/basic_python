fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

print()
# loop dengan string
for i in 'banana':
    print(i)

print()
# loop dengan break statement
for x in fruits:
    print(x)
    if x == 'banana':
        break
# untuk item x di list fruits print nilai elementnya, tapi jika nilai x sama dengan 'banana' maka hentikan pencarian

print()
for x in fruits:
    if x == 'banana':
        break
    print(x)

# loop dengan continue
for x in fruits:
    if x == 'banana':
        print('ketemu!!')
        continue
    print(x)

print()
# dengan range()
for x in range(6):
    print(x)

# print nilai x dari range nilai 0 = 5

print()
for x in range(3, 10):
    print(x)
# print nilai x dari range mulai dari nilai 3 - 9, 10 tidak termasuk

print()
for x in range(3, 10, 3):
    print(x)
# print nilai x dari range 3 - 9 tapi hanya kelipatan 3 saja

print()
# dengan else
for x in range(1, 9):
    print(x)
else:
    print('akhirnya selesai juga')

print()
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

# nested loop
for x in adj:
    for y in fruits:
        print(x, y)
