# empty_set = set()
myset = {"apple", "banana", "cherry"}
myset1 = {"apple", "manggo", "cherry",'avocado'}


# akses set tidak bisa memakai indexing atau key call, harus memakai for loop, value yang ada di set tidak bisa
# direplace dan setiap pemanggilan pasti akan berubah posisi, walaupun anda mengkonversi ke list, tapi nilai set
# sebelum dikonversi pasti akan berubah dan ini juga akan berpengaruh akan hasil konversi
for s in myset:
    print(s)

print(myset)
l = list(myset)
print(type(l))
l[1] = 'pisang'
print(l)
myset = set(l)
print(myset)

# check value
print('banana' in myset)

myset = {"apple", "banana", "cherry"}
myset1 = {"apple", "manggo", "cherry",'avocado'}

# built in method

# menambahkan element dalam set
myset.add('manggo')
print(myset)

# copy value dari set
c = myset.copy()
print(c)

# menampilkan perbedaaan value dari 2 atau lebih set sebagai set yang baru
ns = myset.difference(myset1)
print(ns)

# hapus semua element dari set yang lain dari element set yang dijadikan referensi
du = myset1.difference_update(myset)
print(du)

myset = {"apple", "banana", "cherry"}
myset1 = {"apple", "manggo", "cherry",'avocado'}

# hapus element berdasarkan value dari set jika element tersebut adalah anggota dari set, jika tidak ada maka jangan
# lakukan apa-apa
print(myset1.discard('apple'))
print(myset1)

# menampilkan pertemuan element yang sama dari 2 buah set dan outputnya menjadi 1 set
newset = myset.intersection(myset1)
print(newset)
print(myset1)
print(myset)

myset = {"apple", "banana", "cherry",}
myset1 = {"apple", "manggo", "cherry",'avocado',}

# update element set dengan nilai intersection set itu sendiri dan set yang lain
newset = myset.intersection_update(myset1)
print(newset)

myset = {"apple", "banana", "cherry",}
myset1 = {"apple", "manggo", "cherry",'avocado',}

# tampilkan nilai True jika 2 set mempunyai null intersection
print(myset.isdisjoint(myset1))

# memberitahu apakah set yang satu mempunyai element yang sama dengan set yang lain
print(myset1.issubset(myset))

# hampir sama dengan yang diatas
print(myset.issuperset(myset1))

# hapus dan tampilkan element set yang dihapus
myset1.pop()
print(myset1)

# hapus set element, jika element set adalah member dari set, jika tidak ada maka akan tampil error
myset.remove('cherry')
print(myset)

myset = {"apple", "banana", "cherry",}
myset1 = {"apple", "manggo", "cherry",'avocado',}

# tampilkan element yang tidak ada dari 2 set dan jadikan 1 set
newset = myset.symmetric_difference(myset1)
print(newset)

# update sebuah set dengan element yang mempunyai perbedaan simetric akan set itu sendiri dan set yang lain
newset = myset.symmetric_difference_update(myset1)
print(newset)

# tampilkan gabungan 2 buah set sebagai 1 set, jika kedua set mempunyai element yang sama, maka akan dihitung satu
print(myset.union(myset1))

# update nilai set, bisa dengan gabungan dari set itu sendiri atau dengan set yang lain
setupdate = {'jambu', 'manggis'}
myset.update(setupdate)
print(myset)

print(help(set.update))
# menghapus tiap element dalam set
myset.clear()
print(myset)
