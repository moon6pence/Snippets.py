import sqlite3

con = sqlite3.connect('test.db')

# cursor = con.cursor()
# cursor.execute("CREATE TABLE kospi(Name text, ClosingPrice int)")
# cursor.execute("INSERT INTO kospi VALUES('LG Eletronics', 74500)")
# cursor.execute("INSERT INTO kospi VALUES('Naver', 774000)")
# cursor.execute("INSERT INTO kospi VALUES('Daum', 169100)")
# con.commit()

cursor = con.cursor()
cursor.execute("SELECT * from kospi")
for row in cursor:
    print(row)

con.close()
