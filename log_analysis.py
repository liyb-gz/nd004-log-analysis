import psycopg2

# Constants
DBNAME = "news"

QUERY = '''
select title, sum(path_count) as num_of_view 
from articles, path_log 
where path like ('%'||slug||'%')
group by title
order by num_of_view desc
limit 3;
'''

def log_analysis():
	''' Run log analysis '''
	conn = psycopg2.connect("dbname=%s" % DBNAME)
	cur = conn.cursor()
	cur.execute(QUERY)
	rows = cur.fetchall()
	for row in rows:
		print("%s : %d" % row)

	conn.close()


if __name__ == '__main__':
	log_analysis()