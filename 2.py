import re

def cek(text):
    username=re.compile(r'[a-z]')
    coba=len(username.findall(text))
    coba2=len(text)
    if len(text)<=9 and len(text)>=5 and coba==coba2:
        return True
    else:
        return False
    
def ceking(passw):
    hitung=0
    hitung1=0
    hitung2=0
    spasi=0
    for a in passw:
        if (a.isupper()) == True:
            hitung=hitung+1
        elif (a.islower())==True:
            hitung1=hitung1+1
        elif (a.isdigit())==True:
            hitung2=hitung2+1
        elif a==' ':
            spasi=spasi+1
    total=hitung+hitung1+hitung2+spasi
    simbol=len(passw)-total
    if len(passw)==10 and hitung>=1 and hitung1>=1 and hitung2>=1 and spasi==0 and simbol>=1:
        return True
    else:
        return False

#contoh:
#cek('hjasdbajs')
#ceking('145@sAkLmn')=True