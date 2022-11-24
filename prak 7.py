v = int(input('masukan angka: '))
def prima():
 b = 'bilangan prima'
 if v <= 1:
    b = 'bukan bilangan prima'
 for i in range (2,b):
    if v % i == 0:
        b ='bukan bilangan'
    print(v, 'adalah' ,b)
 print()