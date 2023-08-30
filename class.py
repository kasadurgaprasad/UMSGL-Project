class student:
    
        def insert(self,sid,sname,addr,course):
            f=open('mydb.txt','a')
            f.write('/n')
            f.write(f'{sid},{sname},{addr},{course}')
            f.close()
            print('data inserted successfully')
obj=student()
obj.insert(0,'xyz','pqr','675')
                 
        