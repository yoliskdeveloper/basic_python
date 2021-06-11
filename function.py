# definisikan function di memory
def my_function():
    print('Halo semua')

# manggil atau function call
my_function()

print()
# function dengan parameter dan argument
# parameter => variable yang di pass kan ke dalam function define
def greet(fname):
    print('halo', fname)

# argument -> value yang diberikan di function call
greet('Yosua')
greet('Liskha')
greet('Anjel')

print()
def greet_2(fname, lname):
    print('halo', fname, lname)
greet_2('Yosua', 'audi')

print()
# arbitray argument atau *args atau argument yang kita tidak tahu pasti mau seberapa banyak yang akan di passkan
def family(*kids):
    print('anggota keluarga:',kids)
family('Yosua', 'Liskha', 'Rosalia', 'Anjel', 'KSan')

print()
# keyword argument **kwargs, hampir sama dengan *args tapi ini butuh key-value pair
def car(merk, tahun, harga):
    print(f'mobil {merk} itu dibuat tahun: {tahun} dan di jual dengan harga {harga}')
car('bmw', 2017, '300 Juta')


print()
def family_1(**kwargs):
    print('anggota keluarga:',kwargs)
family_1(ayah='Yosua', ibu='Liskha', anak='yolis')

print()
# default parameter, yaitu parameter yang kita spesifikasikan, jika  ada paramter ini tidak dipanggil dalam function
# call argument, maka default parameter ini akan mengisinya
def nation(nation='Indonesia'):
    print('Saya adalah warga negara', nation)
nation('Belanda')
nation('Belgia')
nation('Singapore')
nation()

print()
# passing list sebagai argument
def food(food):
    for x in food:
        print(x)
fruits = ['appel', 'guava','manggo', 'cherry' ]
food(fruits)

print()
# return value
def luas_persegi_panjagn(panjang, lebar):
    return panjang * lebar

luas_pp = luas_persegi_panjagn(12, 6)
print(luas_pp)

print()
# rekursive function -> masih belum paham
def tri_recursive(k):
    if k > 0:
        hasil = k + tri_recursive(k - 1)
        print(hasil)
    else:
        hasil = 0
    return hasil
tri_recursive(5)
