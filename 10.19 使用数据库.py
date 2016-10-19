import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='passwd',
                       db='mysql',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

cur.execute('USE patscraper')

cur.close()
conn.close()
