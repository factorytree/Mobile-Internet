f=open("metapath2vec/out_dbis/out_dbis/m2vpp.dbis.w1000.l100.txt.size128.window7.negative5.txt",encoding='gb18030', errors='ignore')
m=0
X=[]
y=[]
for i in f.readlines():
    data=i.split(" ")
    if m!=0:
        y.append(data[0])
        list=data[1:-1]
        for i in range(len(list)):
            list[i]=float(list[i])
           # print (type(list[i]))
        X.append(list)
    m+=1

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

def FindList3MaxNum(foo):
    max1, max2, max3 = None, None, None

    for num in foo:
        if max1 is None or max1 < num:
            max1, num = num, max1
        if num is None:
            continue
        if max2 is None or num > max2:
            max2, num = num, max2
        if num is None:
            continue
        if max3 is None or num > max3:
            max3 = num

    return max1, max2, max3

source_x=X[20000]
soure_y=y[20000]
min=2
node=""
distance=0

for i in range(len(X)):

    if soure_y[0]==y[i][0] and i!=20000:#推荐相同类型节点
        distance=cosin_distance(source_x,X[i])
        if distance<min:
            node=y[i]
            min=distance
        if y[i]=='aZimingLiu':
            print(distance)

print(soure_y)
print(node,min)







