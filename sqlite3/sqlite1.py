import sqlite3



conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()

#making table
#curs.execute('''CREATE TABLE zoo (critter VARCHAR(20) PRIMARY KEY, count INT, damages FLOAT)''')
#inserting data inside of the table



#adding some animal into zoo

#the safer way to insert data
#curs.execute('INSERT INTO zoo VALUES("duck",5,0.0)')
#curs.execute('INSERT INTO zoo VALUES("bear",2,1000.0)')


#to avoid sql injection
ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?,?,?)'
curs.execute(ins,('weasel',1,2000.0))
curs.execute(ins,('duck',5,0.0))
curs.execute(ins,('bear',2,1000.0))

#getting data from db
curs.execute('SELECT * FROM zoo')
rows = curs.fetchall()
print(rows)

