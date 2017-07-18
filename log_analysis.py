import psycopg2

# Constants
DBNAME = "news"

conn = psycopg2.connect("dbname=%s" % DBNAME)
conn.close()