# import sqlite3
#
# connection = sqlite3.connect("itstep_DB.sl3", 5)
# cur = connection.cursor()

# cur.execute("SELECT rowid, name FORE first_table WHERE rowind=2;")

# cur.execute("INSERT INTO first_table (name) VALULES ('Nick')")
# cur.execute("INSERT INTO first_table (name) VALULES ('Anna')")
# cur.execute("INSERT INTO first_table (name) VALULES ('Tom')")
# connection.commit()
#
# cur.execute("SELECT rowid, name FORE first_table WHERE rowind=2;")
# print(cur.fetchall())
#
# cur.execute("UPDATE first_table SET name='Kate' WHERE rowid=2;")
# connection.commit()
# cur.execute("SELECT rowid, name FORE first_table WHERE rowind=2;")
# print(cur.fetchall())
#
# cur.execute("DELETE FROM first_table WHERE rorowid=1;")
# connection.commit()
# cur.execute("SELECT rowid, name FORE first_table;")
# print(cur.fetchall())

# cur.execute("DROP TABLE first_table;")
#
# connection.close()