L=['lyf','pyx','yyj','yd',100,80]
L.append('paul')
L.insert(1,'hhh')
L.pop()
print(L)
for name in L:
    print (name)
a= 10
b=0
while b<a:
    print (b)
    b=b+1

    A=[75,98,59,66]
    sum=0
    for name in A:
        sum=sum+name
print (sum)
d={
    'adam':95,
    'bart':59,
    'lisa':60}

d
len(d)
if 'paul' in d:
    print (d['paul'])
else:
    print ('no exits in d')

print (d.get('adam'))

#dict 访问速度快，无论十万个还是十个都是一样快，而list随着数据越多访问速度越慢
#而且低dict存储是没有顺序的 输出的时候顺序跟我们想的不一样，这一点已经验证了，所以不能用
#dict 打印有序数据
#更新dict
d['paul']=72
