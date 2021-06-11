d = {'name': 'liskha', 'age': 38, 'gender': 'female'}

# akses data dict dengan memanggil keynya saja
print(d['name'])

# akses multiple value
print(d['name'], d['gender'])

# menambahkan value dict
d['work'] = 'ibu rumah tangga'
print(d)

# mengganti value dict
d['work'] = 'hotelier'
print(d)

# menghapus semua item yang ada di dict, termasuk key value pair
print(d.clear())
print(d)

d = {'name': 'liskha', 'age': 38, 'gender': 'female'}

# membuat copy key-value pair dari dict
c = d.copy()
print(d)
print(c)

# membuat dictionary baru dengan keys dari key dict lama dan set semua value ke value yang kita tentukan, teknik ini
# bisa dipakai dalam untuk menambah list ke dalam dictionary
tp = ('I', 'Love', 'You')
nd = {}
fk = nd.fromkeys('abcdef', tp, )
print(fk)

# mencari atau mengecek apakah value ada dalam dict dengan memanggil key nya saja, jika tidak ada akan menampilkan
# None, atau bisa dirubah message None nya ke message yang kita mengerti
print(d.get('gender'))
print(d.get('brain'))
print(d.get('brain', 'value tidak ada'))

# menampilkan key-value pair item, output yang keluar akan menjadi tuple, teknik ini berguna untuk mengecek item apa
# saja di dalam sebuah dict
print(d.items())

# menampilkan key saja dalam dict
print(d.keys())

# menampilkan valuenya saja dalam dict
print(d.values())

# mengambil /  menghapus key-value pair dalam dict berdasarkan keynya, jika key dihapus, maka value juga akan mengikuti
print(d)
d.pop('gender')
print(d)

# hamir sams dengan pop, tapi ini akan menghapus item (key-value) dari index paling belakang, LIFO (last in first out),
# output yang diberikan adalah tuple dari key-value. jika item telah habis dalam dict, maka akan tampil error yang
# memberitahu bahwa key-value tidak ada
print(d.popitem())
print(d)
d['age'] = 38
d['gender'] = 'female'

# memasukkan key baru dengan value default jika key yang kita masukkan tidak ada di dalam dict, tapi akan mengembalikan
# value jika key yang kita masukkan ada dalam dict, jika kita spesifikasikan key yang sudah ada value default,
# maka value tersebut tidak akan berubah sama seperti value-value lain
print(d.setdefault('city', 'balikpapan'))
print(d)
print(d.setdefault('age'))
print(d.setdefault('last_name'))
print(d)

# mengupdate key-value di dict, hampir sama dengan traditional update dengan dict[key]= 'value'. jangan lupa untuk
# menaruh braces di dalam parameter update
print(d.update({'last_name': 'pabendan'}))
print(d)
print(d.update({'date_of_birth': {'year' : 1982, 'month': 4, 'date': 9}}))
print(d)
print(help(dict.update))
