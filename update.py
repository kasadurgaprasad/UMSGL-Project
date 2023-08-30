import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    database='UMS',
    user='root',
    password='raje4357'
)

cur = conn.cursor()


class updated:
    
    def dptupdate(x,colname,newval,oldval):
        cur.execute(f"update department set {colname}='{newval}' where {colname} = '{oldval}'")
        conn.commit()

