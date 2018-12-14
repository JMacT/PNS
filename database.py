import sqlite3

conn = sqlite3.connect('data.db')

c = conn.cursor()

#Create the subcatagory database
# c.execute('''CREATE TABLE subcatagory
#              (name text, subtable text)''')
#
# # Insert orings into database
# c.execute("INSERT INTO subcatagory VALUES ('orings', 'as568')")
# c.execute("INSERT INTO subcatagory VALUES ('mfs', 'dwgnum')")
# c.execute("INSERT INTO subcatagory VALUES ('oilseals', 'profiles')")


#Fetch and print -001 data
# c.execute("SELECT * FROM subcatagory")
# #
# print(c.fetchall())


#Create the as568 database
# c.execute('''CREATE TABLE as568
#              (dash text, id float, od float, cs float)''')

#Insert -001 into database
# c.execute("INSERT INTO as568 VALUES ('-001', 0.029, 0.069, 0.040)")


#Fetch and print -001 data
# c.execute("SELECT * FROM as568 WHERE dash='-001'")
#
# print(c.fetchone())

conn.commit()

conn.close()
