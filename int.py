# INT
a = 123

# menampilkan sepasang angka integer, yang dimana rasio nya itu sama dengan nilai integer asli dan dengan denominator
# positif
print(a.as_integer_ratio())

# menampilkan jumlah bit dalam suatu angka
print(a.bit_length())
print((123).bit_length())
print(bin(a.bit_length()))

# menampilkan konjugate complex untuk semua integer
print(a.conjugate())

# tampilkan denominator dari bilangan rational dalam terms yang terkecil
print((234).denominator)

# menampilkan nilai integer yang direpresentasikan oleh byte array
print((23).from_bytes([2,2],'little'))

# menmapilkan bilangan imaginary
print(a.imag)

# menampilkan numerator dari bilangan rational dalam term yang terkecil
print(a.numerator)

# menampilkan bilangan real dari complex number
print(a.real)

# menampilkan array byte yang merepresentasikan sebuah integer
print(a.to_bytes(2,'little'))

