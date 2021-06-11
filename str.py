# STR
s = 'saya ibu budi'
s1 = 'SAYA IBU BUDI'

# SLICING
print(s)

# melihat jumlah karakter string
print(len(s))

# akses string perindex
print(s[0])

# akses string dari index awal sampai index yang kita tentukan
print(s[2:5])
print(s[5:])

# tampilkan string berdasarkan index dengan step/skip method
print(s[3:9:2])

# tampilkan string dari akhir ke awal dengan teknik slicing
print(s[::-1])

# tampilkan string jika digabung dengan proses perkalian, untuk proses aritmetik seperti + perlu
# mengguanakan satu type yaitu string agar tidak raise error
print(s*5)
print(s + str(5))

# METHOD
# membuat karakter pertama upper case dan karakter selanjutnya lower case
print(s.capitalize())

# menampilkan string dengan lower case semua, walaupun string huruf besar semua akan menjadi huruf kecil semua
print(s1.casefold())

# menampilkan string ke tengah, mempunyai 2 parameter width dan fillchar, untuk width akan menjumlahkan jumlah
# karakter di string, jika melebihi maka fill char akan ditampilkan, jika angka width kurang dari jumlah karakter,
# maka fill char tidak akan ditampilkan, jika parameter width sudah diberikan tetapi tidak ada fill char,
# maka default parameter yaitu 'space' akan ditampilkan. dan fill char hanya boleh satu karakter saja
print(s.center(20, '^'))
print(s.center(14, '-'))
print(s.center(20))

# menghitung jumlah karakter yang kita spesifikasikan, jika kita spesifikasikan empty string maka, count akan
# mengembalikna jumlah total keseluruhan string, parameter start dan end adalah optional, cara kerjanya sama dengan
# slicing, mencari karakter di index awal dan index akhir.
print(s.count('a'))
print(s.count('ibu'))
print(s.count('ibu', 3, 7))

# mengencode string menggunakan codec yang teregister untuk encoding, teknik biasa digunakan saat mengambil data
# structure dari internet atau external source. data bisa berupa csv dan json file format
print(s.encode(encoding='utf-8'))
# print(s.encode(encoding='utf-8', errors='strict'))

# mengembalikan nilai boolean true atau false, method ini biasa digunakan untuk pengecekan karakter yang berakhiran
# dengan kita spesifikasikan, ada optional parameter yaitu start dan end, kerjanya hampir sama dengan slicing
print(s.endswith('i'))
print(s.endswith('u', 4, 8))

# menampilkan string yang mempunyai tab,jika tidak spesifikasikna tabsize, maka tab tidak akan muncul,
# tapi jika dispesifikasikan tabsize maka string akan berpengaruh sesuai jumlah tabnya, tabsize default adalah 8 space
print(s.expandtabs(tabsize=12))

# menemukan karakter per karakter dari string, jika ada karakter dalam string , maka dia akan menampilkan posisi
# index karakter itu berada, jika mencari satu kata dalam kalimat maka akan ditampilkan nilai index / posisi kata itu
# berada jika tidak ada maka akan diberikan nilai -1, optional parameter adalah start dan end , tekniknya hampir
# sama dengan slicing
print(s.find('y'))
print(s.find('ibu', 3, 8))

# teknik formating karakter, hampir sama dengan teknik f-string, bisa dengan positional paramter, atau placeholder
# parameter menerima *args => banyak argument,  **kwargs => keyword argument
a = '{} {} mengasihi saya'
print(a.format('Tuhan', 'Yesus'))
a = '{0} {1} {2} {3}'
print(a.format('I', 'love', 'you', 'baby'))
b = 'nilai c:{c} dan f:{f}'
print(b.format(c=234, f=345))

# hampir sama dengan format, tapi method ini hanya bisa menampung 1 parameter saja, dan mapping ke variable lainnya,
# biasa yang dipakai mapping adalah sebuah variabel dictionary
a = '{nama_awal} {nama_akhir} adalah anak pelaut'
b = {'nama_awal':'Yosua', 'nama_akhir':'Audi'}
print(a.format_map(b))

# method ini hampir sama dengan find, mencari substring dalam sebuah string, optional parameter adalah start dan end
# hampis sama dengan slicing
print(s.index('ibu'))
print(s.index('ibu', 3, 8 ))

# mengecek apakah sebuah string adalah alpha-numberik atau string berbentuk angka/ numerik, akan menampilkan nilai
# boolean True or False
a = 'kabil industri 234'
b = 'kabil industri'
c = '123'
print(a.isalnum())
print(b.isalnum())
print(c.isalnum())

# mengecek apakah string adalah alphabetic, maksudnya adalah ada huruf a - z di dalam sebuah string,
# walaupun substingnya mempunyai karakter yang sama. method ini akan mengembalikan nilai boolean
a = 'abcdefghijklmnopqrstuvwxyz'
print(a.isalpha())

# mengecek nilai ascii dalam suatu string, dan akan menampilkan boolean
print(s.isascii())

# mengecek string apakah ada nilai decimal di dalamnya, dan akan menampilkan boolean
a = "19"
print(s.isdecimal())
print(a.isdecimal())

# mengecek string apakah ada nilai digit / numerik di dalamnya
print(a.isdigit())
print(s.isdigit())

# mengecek apakah string adalah reserved python identifier
a = 'def'
print(a.isidentifier())
print(s.isidentifier())

# mengecek apakah string adalah lowercase semuanya
print(s.islower())
print(s1.islower())

# mengecek apakah string adalah numerik value
a = '23'
print(a.isnumeric())

# mengecek apakah satu string adalah string yang dapat di print
print(s.isprintable())

# mangecek apakah di dalam string ada di whitespace atau empty string
a = ' '
print(a.isspace())

# mengecek apakah ada teknik title-case atau uppercase diikuti lowercase dalam sebuah string
a = 'Saya Ibu Budi'
print(a.istitle())

# cek apakah di string semua karakternya adalah uppercase
print(s1.isupper())

# mengabungkan beberapa string dengan karakter yang dispesifikasikan. method ini hanya menerima satu parameter saja,
# jadi jika ada banyak string yang ingin di masukkan , harus dijadikan sebuah list
print('-'.join(s))
print(' | '.join(['juan', 'huan', 'kuan', 'luan']))

# method ini hampir sama dengan center, tapi dia left justified, jika ada fillchar di parameter kedua, maka fillchar
# akan menambah ke bagian kanan sesuai jumlah width / karakter yang dispesifikasikan
print(s.ljust(30, '=' ))

# konversi string ke lower case
a = 'SAYA ADALAH ANAK PELAUT'
print(a.lower())

# menghapus extra whitespace di sebuah string jika ada
a = '    saya adalah ibu budi      '
print(a.lstrip())

# manemapilkan konversi dari karakter biasa ke unicode ordinals, jika 1 parameter maka mappingnya adalah dictionary,
# jika diberi 2 parameter, maka parameter pertama dan parameter kedua harus mempunyai ukuran dimensi yang sama atau
# key-value pair. method ini bisa digunakan untuk membuat cipher key, dan biasa digabung dengan method translate
d = {'a':23, 'b':34, 'c':45}
b = 'abc'
c = ''.maketrans(d)
print(b.translate(c))
a = 'jones'
b = 'jonis'
print(''.maketrans(a, b))
a = 'ultra milk'
b = '0987654321'
print(''.maketrans(a, b, ' '))
c = ''.maketrans(a, b)
d = 'hari ini makan nasi padang, enak sekali'
print(d.translate(c))

# hampir sama dengan method search, tapi disini partition akan menampilkan parameter string yang dicari. dan
# ditampilkan dalam 3 output tuple. strukturnya adalah  (string sebelum separator, separator itu sendiri,
# dan karakter setelah separator)
print('jekokjek'.partition('jek'))

# mengganti string dari string lama ke baru sesuai dengan string yang ditentukan, jika diberikan parameter ke tiga
# yaitu count yang berupa integer,maka pergantian string akan mengikuti nilai integer di parameter ke tiga,
# jika count = 2, maka pergantian string yang lama ke baru hanya terjadi di 2 string yang pertama. setelah itu tidak
# ada pergantian walaupun ada string yang lama setelahnya. jika tanpa parameter ke tiga, maka semua string yang lama
# yang ada dan sesuai akan terganti, uppercase dan lowercase juga berpengaruh
a = 'makan nasi padang di warung padang dengan orang padang'
print(a.replace('padang', 'jawa'))
a = 'minum air putih di awan putih dengan gelas yang berwarna putih'
print(a.replace('putih', 'coklat', 2))

# mencari sebuah substring dalam string, dan jika ditemukan akan menampilkan angka indexnya yang pertama, jika tidak
# ditemukan maka akan diberikan nilai -1, parameter kedua dan ketiga adalah parameter optional, tugasnya sama dengan
# teknik slicing
print(a.rfind('air', 7))

# hampir sama dengan yang diatas, parameter kedua dan ketiga adalah optional dan tugasnya sama dengan slicing
print(a.rindex('air'))

# kebalikannya ljust / left-justified, kalo ini rjust / right-justified
print(s.rjust(23, '='))

# hampir sama dengan partition method, tatapi parameter sebelum separator dan setelah separator akan dimunculkan
print('okjekok'.rpartition('jek'))

# membuat string menjadi urutan list jika tidak ada parameter. jika ada parameter string yang sebagai separatornya,
# maka string tersebut akan menjadi pemisah antara string sebelum dan setelah dan string tersebut akan dihliangkan
print(s.rsplit())
a = 'saya ada belajar bahasa pemrograman python'
print(a.rsplit('ada'))

# sama dengan lstrip
a = 'saya ada belajar bahasa pemrograman python       '
print(a.rstrip())

# sama dengan rspit
print(a.split())

# menampilkan list dari baris di dalam string, break pembatasan baris
print(a.splitlines(keepends=True))

# hampir sama dengan endswith, tapi ini mengecek karakter awalan dulu, manghasilkan nilai boolean, uppercase dan
# lowercase juga berpengaruh untuk pengecekan
print(a.startswith('saya'))

# sama dengan rstrip dan lstrip
print(a.strip(' '))

# konversi uppercase ke lowercase atau vice versa
a = 'SAYA ADALAH ORANG AMBON'
print(a.swapcase())
b = 'saya adalah orang ambon'
print(b.swapcase())

# menampilkan setiap string di setiap kata adalah huruf besar di huruf pertamanya
print(b.title())

# menjadikan semua karakter di string uppercase
print(s.upper())

# membuat traling zero di depan string, sesuai dengan jumlah parameter width yang dispesifikasikan
print(s.zfill(23))

