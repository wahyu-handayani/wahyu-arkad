from pymongo import MongoClient
democlient=MongoClient()
myclient=MongoClient('localhost',27017)
mydb=myclient["WAHYU_COBA"]
mycoll=mydb["Nama"]
mycoll2=mydb["Work"]
mycoll3=mydb["Kategori"]

mylist=[{"id":1,"name":"Bintang","id_work":1,"id_salary":1},
        {"id":2,"name":"Tasya","id_work":2,"id_salary":2}]
mycoll.insert_many(mylist)

mylist2=[{"id":1,"name":"Fronted Dev","id_salary":1},
         {"id":2,"name":"Backend Dev","id_salary":2}]
mycoll2.insert_many(mylist2)

mylist3=[{"id":1,"salary":10000000},
         {"id":2,"salary":12000000}]
mycoll3.insert_many(mylist3)

def get_multiple_data():
    """
    get document data by document ID
    :return:
    """
    mylist = mycoll.find()
    return list(mylist)
x=get_multiple_data()
print(x)