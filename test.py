

import psycopg2

DB = psycopg2.connect("dbname=tournament")
cursor = DB.cursor()
cursor.execute("SELECT count(player_id) from players;")
numAr = cursor.fetchone() 
print numAr[0]
DB.close()