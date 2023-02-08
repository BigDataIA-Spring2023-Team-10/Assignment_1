import sqlite3
conn = sqlite3.connect('src/data/GEOSPATIAL_DATA.db')
c = conn.cursor()
#c.execute("INSERT INTO goes18meta (year, month, hour) VALUES (?,?,?)", (2022, 209, 1))
conn.commit()
def geos_get_hour(year, month):
    c.execute("SELECT DISTINCT hour FROM goes18meta WHERE year = ? and month = ?", (year,month))
    rows = c.fetchall()
    count=0
    for row in rows:
        print(row)
        count+=1
    return count
print(geos_get_hour(2022,209))