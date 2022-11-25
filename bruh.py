print("tera baap")

d1={
    1:"A",
    2:"B"
}
d2={
    1:"a",
    2:"b"
}
dic={}

for i,j in d1,d2:
    lst=[]
    lst.append(d1.get(i))
    lst.append(d2.get(j))
    # lst
    dic.update({i:lst})

print(dic)
{1:["a","A"]}