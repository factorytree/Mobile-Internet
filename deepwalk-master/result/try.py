file=open('../paperdatatotal1/filename.txt','r')
tmp=[]
for line in file.readlines():
    line=line.rstrip('\n')
    tmp.append(line)
file.close()
# file=open('../dataset/filename.txt','w')
# for item in tmp:
#     file.write(item+'\n')
# file.close()
print(tmp)