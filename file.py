f=open('new.txt','r')
x=f.readlines()
print(x)
for i in x:
    if'/n' in i:
        x[x.index(i)]=i[0:len(1):-1]
print(x)

defy='C:\Users\DELL\Pictures\Screenshot_2020-03-09-14-26-40-981_com.niksoftware.snapseed.jpg'

f=open('r'C:\Users\DELL\Pictures\Screenshot_2020-03-09-14-26-40-981_com.niksoftware.snapseed.jpg','wb')
f.writelines(y)
f.close()