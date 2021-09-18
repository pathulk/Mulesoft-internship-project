import sqlite3

conn=sqlite3.connect('Movies.db')
c= conn.cursor()

#CREATING A TABLE Movies TO STORE FAVOURITE MOVIES
c.execute("""CREATE TABLE Movies
       (Movie_Name TEXT NOT NULL,Actor TEXT NOT NULL,Actress TEXT NOT NULL,Director TEXT NOT NULL,Year_of_release INT NOT NULL);""")

#INSERTING ELEMENTS INTO TABLE
c.execute("INSERT INTO Movies VALUES('DRISHYAM','MOHANLAL','MEENA','JEETHU JOSEPH',2013)")
c.execute("INSERT INTO Movies VALUES('LUCIFER','MOHANLAL','MANJU WARRIOR','PRITHVIRAJ SUKUMARAN',2019)")
c.execute("INSERT INTO Movies VALUES('MY BOSS','DILEEP','MAMTA MOHANDAS','JEETHU JOSEPH',2012)")
c.execute("INSERT INTO Movies VALUES('MEMORIES','PRITHVIRAJ SUKUMARAN','MIA','JEETHU JOSEPH',2013)")

#SELECTING ALL ELEMENTS FROM THE TABLE
x=c.execute("select * from Movies")
for i in x:
   print(i)

#SELECTING ELEMENT WITH A PARTICULAR CHARACTERISTICS
m=c.execute("select * from Movies WHERE Director='PRITHVIRAJ SUKUMARAN'")
for row in m:
   print(row)


conn.commit()
conn.close()
