h,m=map(int,input().split())
m-=45
if m<0:
    m+=60
    h-=1
if h<0:
    h+=24
elif h==24:
    h=0
print(h,m)