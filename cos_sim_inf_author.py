def cosin_distance(vector1, vector2):
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return None
    else:
        return 0.5*(1-dot_product / ((normA * normB) ** 0.5))

def FindList3MinNum(foo):
    min1, min2, min3,min4,min5,min6,min7,min8,min9,min10 = None, None, None,None,None,None,None,None,None,None

    for num in foo:
        if min1 is None or min1 > num:
            min1, num = num, min1
        if num is None:
            continue
        if min2 is None or num < min2:
            min2, num = num, min2
        if num is None:
            continue
        if min3 is None or num < min3:
            min3,num = num,min3
        if num is None:
            continue
        if min4 is None or num < min4:
            min4,num = num,min4
        if num is None:
            continue
        if min5 is None or num < min5:
            min5,num = num,min5
        if num is None:
            continue
        if min6 is None or num < min6:
            min6,num = num,min6
        if num is None:
            continue
        if min7 is None or num < min7:
            min7,num = num,min7
        if num is None:
            continue
        if min8 is None or num < min8:
            min8,num = num,min8
        if num is None:
            continue
        if min9 is None or num < min9:
            min9,num = num,min9
        if num is None:
            continue
        if min10 is None or num < min10:
            min10 = num

    return min1, min2, min3,min4,min5,min6,min7,min8,min9,min10

authorID=[]
vec=[]
file=open('deepwalk-master/result/all_author_ratio0.4','r')
for line in file.readlines():
    line=line.split(' ')
    if len(line)==2:
        continue
    authorID.append(line[0])
    line=line[1:]
    for i in range(len(line)):
        line[i]=float(line[i])
    vec.append(line[1:])

#给定结点
nodenum=authorID.index('260837')
id=authorID[nodenum]
v=vec[nodenum]

similarity=[]
node=[]

for i in range(len(authorID)):
    if id==authorID[i]:
        continue
    distance=cosin_distance(v,vec[i])
    similarity.append(distance)
    node.append(authorID[i])

print('给定学者ID',id)
min1,min2,min3,min4,min5,min6,min7,min8,min9,min10=FindList3MinNum(similarity)
index1=node[similarity.index(min1)]
index2=node[similarity.index(min2)]
index3=node[similarity.index(min3)]
index4=node[similarity.index(min4)]
index5=node[similarity.index(min5)]
index6=node[similarity.index(min6)]
index7=node[similarity.index(min7)]
index8=node[similarity.index(min8)]
index9=node[similarity.index(min9)]
index10=node[similarity.index(min10)]
print('推荐学者1',index1,min1)
print('推荐学者2',index2,min2)
print('推荐学者3',index3,min3)
print('推荐学者4',index4,min4)
print('推荐学者5',index5,min5)
print('推荐学者6',index6,min6)
print('推荐学者7',index7,min7)
print('推荐学者8',index8,min8)
print('推荐学者9',index9,min9)
print('推荐学者10',index10,min10)
