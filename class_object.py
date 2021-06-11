# create class
import platform
x = dir(platform)
print(x)

class MyClass:
    x = 5

pi = MyClass()
print(pi.x)

# dengan __init__()
class Person_1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # create class method
    def greet(self):
        print('halo nama saya adalah:', self.name)

# create object class
pi = Person_1('John', 38)
pi.greet()
print(pi.age)

class Piring:
    def __init__(ini_adalah, warna, terbuat_dari, bentuk ):
        ini_adalah.warna = warna
        ini_adalah.terbuat_dari = terbuat_dari
        ini_adalah.bentuk = bentuk

    def buat_makan(ini_adalah):
        print('Piring itu berwarna:', ini_adalah.warna)

piring = Piring('Putih', 'kaca', 'bundar')
piring_2 = Piring('Merah', 'Plastik', 'bundar')
piring.buat_makan()
print(piring.warna)
piring_2.buat_makan()


# inheritance atau mewarisi dari parent ke child
# base class
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print('halo nama lengkap saya adalah', self.fname, self.lname)

# buat object
x = Person('Yosua', 'Audi')
x.printname()

# buat child class, agar semua property yang ada di parent bisa kita ambil dan kita pakai di child class
# bila ada property / method yang ingin definiisikan sendiri, tinggal di overwrite method yang ada di parent class
class Student(Person):
    def __init__(self, fname, lname, year):
        # dengan cara ini kita tidak perlu lagi memanggil parent class dan membuaat methodnya lagi di child class,
        # dengan super, secara otomatis method dan property dari parent class akan sama di class object
        super().__init__(fname, lname)

        # property
        self.graduation_year = year

        # cara lain untuk inherit
        # Person.__init__(self, fname, lname)

    def welcome(self):
        print('Selama datang', self.fname, self.lname, 'di angkatan tahun', self.graduation_year)


s = Student('Jake', 'Daniel', 2019)
s.printname()
s.welcome()

