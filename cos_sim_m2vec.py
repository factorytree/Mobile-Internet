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

def FindList3MinNum(foo):
    min1, min2, min3 = None, None, None

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
            min3 = num

    return min1, min2, min3

#搜索给定的结点
nodenum=y.index('aLaurenceNigay')
source_x=X[nodenum]  # 应该是特征向量
soure_y=y[nodenum]  # 好像是名字

#min=2
node=[]
#node2=''
distance=0
similarity=[]
for i in range(len(X)):
    if soure_y[0]==y[i][0] and i!=nodenum:#推荐相同类型节点
        distance=cosin_distance(source_x,X[i])
        similarity.append(distance)
        node.append(y[i])
        # if distance<min:
        #     min=distance
        #     node2=y[i]

min1,min2,min3=FindList3MinNum(similarity)
index1=node[similarity.index(min1)]
index2=node[similarity.index(min2)]
index3=node[similarity.index(min3)]
print(index1,min1)
print(index2,min2)
print(index3,min3)
#print('\n')
#print(node2,min)
