import json
def tes():
    lis = {"name" 	 : "Wahyu Handayani",
           "age"  	 : 22,
           "address"	 : "Jl. Danau Laut Tawar",
           "hobbies"	 : ["bersepeda", "mendengarkan musik"],
           "is_married" : False,
           "list_school": {"name" : "Universitas Brawijaya",
                           "year_in" : 2015,
                           "year_out": 2018,
                           "major" : "Mathematics"},
           "skills": [{"skill_name" : "python programming",
                       "level"  : "advanced"},{"skill_name" : "matlab programming","level"  : "advanced"}],
           "interest_in_coding" :True
    }
    baru = json.dumps(lis) #mengkonversi dictionary pada python ke json
    return baru;

bar=json.loads(tes())
print(bar)
#buat manggil data2 tertentu:
#bar["name"]