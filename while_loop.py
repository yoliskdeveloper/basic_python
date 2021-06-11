# selama i masih tetap benar maka print nilai i

i = 0
while i < 6:
    print(i)
    i += 1

print()
# degan if statment dan break
i = 0
while i < 10:
    print(i)
    i += 1
    if i == 3:
        break
# selama i kurang dari 10 maka print nilai i, tapi jika nilai i sama dengan 3, maka hentikan pencarian

print()
i = 0
while i < 10:
    print(i)
    i += 1
    if i == 3:
        print('ketemu!!!')
    continue

# selama nilai i kurang dari 10, maka print nilai i, tapi jika nilai i sama dengan 3 maka print 'ketemu', dan lanjutkan
# print sampai akhir
print()

# dengan if... else statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print('nilai i kurang dari nilai 6')
