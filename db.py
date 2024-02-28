import psycopg2
conn = psycopg2.connect(dbname='botdb', user='admin',
                        password='12345678', host='194.87.103.98')
cursor = conn.cursor()
cursor.execute('SELECT * FROM Olimpiads')
records = cursor.fetchall()
print(records)
cursor.close()
conn.close()