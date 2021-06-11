# 'count', 'index
a = ('math', 'history', 'bahasa indonesia', 'math')

# manampilkan total jumlah value di dalam tuple yang kita spesifikasikan
print(a.count('math'))

# mencari lokasi index dari sebuah value di tupple, parameter start dan stop adalah optional, tugasnya hampir sama
# dengan slicing, jika tidak ada value, maka akan tampil error yang menunjukkan bahwa value tidak ada
print(a.index('bahasa indonesia'))
print(a.index('bahasa indonesia', 2, 5))
print(help(tuple.index))

# tuple tidak menerima item assignment atau pergantian item, karena data structure di tuple adalah immutable,
# beda dengan list, dan dictionary yang data structure adalah mutable. jadi untuk menganti data di tuple adalah
# dengan cara reassign variabel dengan nama yang sama tapi dengan item yang berbeda

print(a)
a = ('math', 'history', 'bahasa indonesia', 'biology')
print(a)
