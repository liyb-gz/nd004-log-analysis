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

analysis_list = [
	{
		'question': '1. What are the most popular three articles of all time?',
		'query':  '''
select title, sum(path_count) as num_of_view 
from articles, path_log 
where path like ('%'||slug||'%')
group by title
order by num_of_view desc
limit 3;
''',
		'answer_template': '\t"%s" : %d views'
	}
]

def run_analysis(cur, analysis):
	cur.execute(analysis['query'])
	rows = cur.fetchall()

	print(analysis['question'])

	for row in rows:
		print(analysis['answer_template'] % row)

def log_analysis():
	''' Run log analysis '''
	conn = psycopg2.connect('dbname=%s' % DBNAME)
	cur = conn.cursor()

	for analysis in analysis_list:
		run_analysis(cur, analysis)

	conn.close()


if __name__ == '__main__':
	log_analysis()