import sympy

# x = sympy.symbols("x")
# result=sympy.solve([4*(1100-2*x)**2+9*(1100-2*x)**2-144*x**2],[x])
# for item in result:
#     print(item[0])
#     print(float(item[0]))

def f(x):
    ans=-1.0/4-1.0/(4*(4*x+3))+1/(3*4**x)
    return ans

l=[]
sum=0
for n in range(1,100):
    if n%2==1:
        sum+=1.0/((2*n+1)*(2*n+5))
    elif n%2==0:
        sum-=1.0/(2**n)
        l.append(sum)


l2=[]
min=0
index=0
for i in range(100):
    l2.append(f(i))
    if (f(i)<min):
        min=f(i)
        index=i
print(min,index)
print(l)
print(l2[1:])