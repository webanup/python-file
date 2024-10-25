#1 get function
#2 keys function
#3 values function
#4 items function
d={
    'name':'anup',
    'roll no':'229016',
    'branch':'bca',
}
for a in d.keys():
    print(a)

for a in d.values():
    print(a)
    
for a,b in d.items():
    print(a,b)
    
n=d.get('name')
print(n)          