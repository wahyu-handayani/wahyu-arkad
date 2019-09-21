num = int(input("Masukkan tanggal: "))
uang = int(input("Masukkan uang: "))
mie=2500
banyak=uang//mie
if num >= 1 and num <= 30:
    if num%2==1:
        if banyak>=3:
            bonus=banyak//3
            if num%5==0 and bonus%2==0:
                bonus=bonus*10
            elif num%5==0 and bonus%2==1:
                bonus=bonus*5
        else:
            bonus=0
        total=banyak+bonus
    else:
        if banyak>=4:
            bonus=banyak//4
            if num%5==0 and bonus%2==0:
                bonus=bonus*10
            elif num%5==0 and bonus%2==1:
                bonus=bonus*5
        else:
            bonus=0
        total=banyak+bonus
print('Total Mie: ',total)