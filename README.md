# Panduan
## Soal 1
Function untuk menampilkan biodata dengan return value berformat json. Pada pembahasan ini, digunakan perintah:
```
json.dumps(lis)
```
dengan tujuan untuk mengkonversi dictionary yang disimpan dalam "lis" ke bentuk json.
Output program berformat json dipanggil dengan mendeklarasikan:
```
bar=json.loads(tes())
```
Dan ketika ``` bar ``` ditampilkan, akan diperoleh output sebagai berikut:
```
{'name': 'Wahyu Handayani', 'age': 22, 'address': 'Jl. Danau Laut Tawar', 'hobbies': ['bersepeda', 'mendengarkan musik'], 'is_married': False, 'list_school': {'name': 'Universitas Brawijaya', 'year_in': 2015, 'year_out': 2018, 'major': 'Mathematics'}, 'skills': [{'skill_name': 'python programming', 'level': 'advanced'}, {'skill_name': 'matlab programming', 'level': 'advanced'}], 'interest_in_coding': True}
```
Kegunaan JSON pada REST API:
Sebagai format untuk bertukar data client dan server atau antar aplikasi. 
Sumber: https://www.petanikode.com/json-pemula/
## Soal 2
Digunakan modul Regex pada python untuk melakukan pengecekan terhadap username dan password, Username dan password memiliki ketentuan-ketentuan tertentu (sesuai pada soal). Program dapat dijalankan dengan memberikan perintah pada command window seperti contoh berikut
```
cek('hjasdbajs')
```
Note: ``` cek ``` merupakan fungsi untuk mengecek username
Diperoleh output:``` True```. Sedangkan untuk melakukan pengecekan pada password digunakan fungsi ```ceking```, dapat dilakukan seperti contoh berikut:
```
ceking('145sAkLmn')
```
Output: ```False``` karena tidak mengandung minimal 1 simbol. Sehingga dengan menambahkan simbol unik sebagai berikut:
```
ceking('145@sAkLmn')
```
Diperoleh output: ``` True ```
## Soal 3
Menghitung banyaknya jabat tangan menggunakan perulangan.
Dengan menggunakan fungsi ``` jabat ``` dan ```n``` merupakan banyaknya tamu, maka banyaknya jabat tangan dapat dihitung menggunakan perintah berikut
```
jabat(6)
```
Output:
```
15
```
## Soal 4
Function menampilkan barisan Fibonacci dengan memetakan menjadi x baris dan y kolom.
Contoh perintah:
```
text(3,4)
```
Menampilkan barisan fibonacci dalam 4 baris 3 kolom, output:
```
0   1   1   
2   3   5   
8   13   21   
34   55   89 
```
## Soal 5
Menampilkan total mie yang akan diterima ketika seseorang membeli pada tanggal "x". Dengan total mie telah ditambahkan dengan bonus mie yang didapat. Parameter yang digunakan adalah Tanggal dan Uang yang akan digunakan untuk belanja.
Contoh perintah:
```
Masukkan tanggal: 13

Masukkan uang: 60000
```
Output:
```
Total Mie:  32
```
## Soal 6
Menampilkan database pada MongoDB
