class Animal :

    def __init__(self, name, nickname, country, birth_year):
        self.name = name
        self.nickname = nickname
        self.country = country
        self.birth_year = birth_year


cat = Animal("mick", "kim", "kenya", 1765)
print(cat.name)
print(cat.country)
print(cat.nickname)

l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
    {'k1': "sudh", 'k2': "ineuron", 'k3': "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]
# extract ineuron
l11 = []
for i in l:
    if type(i)==list or type(i)==tuple or type(i)==set:
        for j in i :
            if j=='ineuron' :
                l11.append(j)
    if type(i)==dict:
        for k in i.items():
            for g in k :
                if g=='ineuron' :
                    l11.append(g)
print(l11)

# flatten the list
l5 = []

for i in l:
    if type(i) == tuple or type(i) == list or type(i) == set:
        for j in i:
            if type(j) == int or type(j) == str:
                l5.append(j)

    if type(i) == dict:
        for k in i.items():
            for g in k:
                if type(g) == int or type(g) == str:
                    l5.append(g)
print(l5)
#number of occurances of all the data .first flatten the list,then convert to set and apply count()

for i in set(l5):
    print(i,":",l5.count(i))

# q11 : Try to find out number of keys in dict element
for i in l:
        if type(i)==dict:
            print(len(list(i.keys())))

# q12 : Try to filter out all the string  in data

for i in l5:
    if type(i)==str:
        print(i)