def text(kolom,baris):
    a, b , c= 0,1,0
    for baris in range (4):
        for kolom in range (4):
            print(a,' ',end=' ')
            c=a+b
            a=b
            b=c
        print()
    