# list
kursus = ['masak', 'jahit', 'mengemudi','komputer', 'matematika']
pelajaran = ['matematika', 'bahasa indonesia', 'sejarah','ppkn']

# akses data berdasarkan index pertama
print(kursus[0])

# akses data berdasarkan index terakhir, jika tidak tahu index terakhirnya
print(kursus[-1])

# akses data hanya berdasarkan slicing index
print(kursus[1:4])

# akses data memakai slicing dengan parameter ke 3 yaitu step/skip parameter
print(kursus[::2])

# menampilkan data dari value awal ke akhir
print(kursus[:])

# menampilkan data dari value akhir ke awal dengan slicing dan parameter step
print(kursus[::-1])

# menganti data
kursus[2] = 'komputer'
kursus[3] = 'mengemudi'
print(kursus)

# menambahkan data ke list, masuk di index terakhir
kursus.append('nonton')
print(kursus)

# menambahkan 2 list jadi 1 list
# kursus.append(pelajaran)
# print(kursus[:])

# untuk mengakses data list dalam list
print(kursus[-1])

# menambahkan data ke list, dengan memasukkan di posisi yang kita tentukan. parameter yang dibutuhkan ada 2 yaitu no
# indexnya dan valuenya
kursus.insert(3, 'main bola')
print(kursus)

# menambahkan 2 list ke dalam 1 list tanpa membuat list dalam list. untuk akses nya sama dengan akses list seperti biasa
kursus.extend(pelajaran)
print(kursus)

# menampilkan data dari akhir ke awal dengan cara reverse bukan dengan slicing
kursus.reverse()
print(kursus)

# menghapus list dengan pop, yaitu menghapus dari value akhir
kursus.pop()
print(kursus)

# untuk mengetahui value apa yang diambil dengan pop yaitu dengan menaruh di variable
pop = kursus.pop()
print(pop)
print(kursus)

# menghapus list dengan remove, method ini harus memakai value yang akan dihapus, tidak berdasarkan index
kursus.remove('ppkn')
print(kursus)

# menghapus semua valunya dalam list
# print(kursus.clear())

# menghitung jumlah element di list, jika ada element yang sama, jika tidak ada maka akan menghasilkan not defined
print(kursus.count('matematika'))

# mencari index berdasarkan valuenya yang ada di dalam list, cara ini berguna ketika kita ingin tahu dimana
# sebenarnya posisi index suatu value, setelah ketemu kita lakukan cara-cara yang lain
print(kursus.index('main bola'))

# sorting / mengurutkan element list. jika alphabet maka urutan dari a-z untuk huruf pertama, jika angka maka urutan
# dari 0-9 untuk angka pertama
kursus.sort()
print(kursus)

# WRAPPER DESCRIPTOR

# menambahkan dua list menjadi satu, hampir sama dengan extend
print(kursus.__add__(pelajaran))

# method ini bagus untuk pengecekan apakah elemen value ada dalam list
print(kursus.__contains__('ppkn'))

# method ini belum paham
# print(kursus.__delattr__())

# menhapus item, hampir sama dengan remove
kursus.__delitem__(3)
print(kursus)

# membandingkan value atau element, string juga bisa, jika tidak sesuai dengan typenya akan menghasilkan NotImplemented
print('matematika'.__eq__('matematika'))
print(kursus.__eq__(kursus))
print(kursus.__eq__(pelajaran))
print(kursus.__eq__('matematika'))

# method wrapper ini belum diketahui cara pakainya
# print(kursus.__format__(kursus))
# print(help('FORMATTING'))

# perbandingan 'greater equal' >=
print(kursus.__ge__(kursus))

# method ini belum paham
# print(kursus.__getattribute__('matematika'))
# print(kursus.__setattr__('music', 'pop'))


# akses data hampir sama dengan slicing kursus[5], berdasarkan index tapi agak susah untuk memakai slicing
print(kursus.__getitem__(6))

# comparison 'greater than' >
print(kursus.__gt__(kursus))

# menambahkan item ke list, hampir sama dengan append, insert, tapi jika tidak dimasukkan ke dalam list,
# valuenya akan menjadi pisah-pisah
print(kursus.__iadd__(['olahraga']))

# mengalikan tiap element sesuai dengan parameter yang dispesifikasi, hampir sama dengan  var *= var
print(kursus.__imul__(1))
print(kursus.__mul__(2))
print(kursus.__rmul__(2))

# hampir sama dengan akses variable, __iter__ akan memunculkan nilai valuenya
a = kursus
a.__iter__()
print(a)

# comparison less equal to '<='
print(kursus.__le__(kursus))
print(kursus.__lt__(kursus))

# hampir sama dengan len()
print(kursus.__len__())

# comparison, hampir sama dengan != atau not equal
print(kursus.__ne__(pelajaran))

# helper untuk pickle, belum mengerti cara implementasinya
# print(kursus.__reduce__())
# print(kursus.__reduce_ex__())

# hampir sama dengan str()
print(kursus.__repr__())

# hampir sama dengan reverse atau reversed tapi harus pakai list method atau pakai for loop
print(list(kursus.__reversed__()))
# for i in kursus.__reversed__():
#     print(i)

# __setitem__ hampir sama re assign dict secara standart, a['music'] = 'dangdut'
a = {'music': 'rock'}
print(a)
a.__setitem__('music', 'pop')
print(a)
a['music'] = 'dangdut'
print(a)

# mengecek jumlah ukuran byte variable dalam memory, jika dicek kedua variabel di bawah ini, akan mempunyai jumalh
# byte yang berbeda
print(a.__sizeof__())
print(kursus.__sizeof__())

