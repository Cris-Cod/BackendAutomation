import mysql.connector

from utilities.configurations import *

#host, database, user, password
#conn = mysql.connector.connect(host='localhost', database='APIDevelop', user='root', password='root')

conn = getConection()
print(conn.is_connected())
cursor = conn.cursor()
cursor.execute('select * from CustomerInfo')

"""row = cursor.fetchone()
print(row)
print(row[3])
rowAll = cursor.fetchall()
print(rowAll)"""

rows = cursor.fetchall()
print(type(rows))
print(rows)
sum = 0
for row in rows:
    sum += row[2]
print(sum)
assert sum == 1083

#update
query = "update CustomerInfo set Location = %s where CourseName = %s"
data = ("UK", "Jmeter")
cursor.execute(query, data)
conn.commit()

#Delete
query = "delete from customerInfo where courseName = 'WebServices'"


conn.close()

