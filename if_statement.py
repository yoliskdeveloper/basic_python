a = 33
b = 209
if b > a:
    print('b lebih besar dari a')


a = 33
b = 33
if b > a:
    print('b lebih besar dari a')
elif a == b:
    print('a dan b nilainya sama')


a = 200
b = 33
if b > a:
    print('b lebih besar dari a')
elif a == b:
    print('a dan b nilainya sama')
else:
    print('a lebih besar dari b')


a = 200
b = 33
if b > a :
    print('b lebih besar dari a')
else:
    print('a lebih besar dari b')


# satu baris statement
# if
if a > b: print('a lebih besar dari b')

# if ... else
print('a lebih besar dari b') if a < b else print('b lebih besar dari a')

# multiple condition di satu baris
a = 230
b = 235
print('A') if a > b else print('==') if a == b else print('b')

# logical operator
# 'and' akan menampilkan nilai true jika kedua kondisi itu benar, jika satu kondisi itu false, maka kondisi tersebut
# itu false
a = 200
b = 33
c = 400
if a > b and c > a:
    print('kedua kondisi itu benar')

# 'or' akan menampilkan nilai true jika hanya satu kondisi yang benar, kondisi akan menjadi false jika kedua kondisi
# adalah salah
if a < b or c > a:
    print('hanya satu kondisi saja yang benar')

# nested if
a = 9
if a > 10:
    print('nilai a diatas 10')
    if a > 20:
        print('nilai a ada diatas 20')
    else:
        print('nilai a bukan diatas 20')
else:
    print('nilai a dibawah 10 dan 20')


# pass statement untuk sebagai pedoman, jika nanti kita akan kembali ke blok code tersebtu
if a > b:
    pass
