#!/usr/bin/env python3
import psycopg2

# Constants
DBNAME = "news"

analysis_list = [
    {
        'question': '1. What are the most popular three articles of all time?',
        'query':  '''
SELECT title,
       sum(path_count) AS num_of_view
FROM article_slug_author,
     path_log
WHERE path LIKE ('%'||slug||'%')
GROUP BY title
ORDER BY num_of_view DESC
LIMIT 3;
''',
        'answer_template': '\t"%s" : %d views'
    },
    {
        'question': '2. Who are the most popular article authors of all time?',
        'query':  '''
SELECT name,
       sum(path_count) AS num_of_view
FROM article_slug_author,
     path_log
WHERE path LIKE ('%'||slug||'%')
GROUP BY name
ORDER BY num_of_view DESC;
''',
        'answer_template': '\t%s : %d views'
    },
    {
        'question': '3. On which days did more than 1% of requests lead to errors?',
        'query':  '''
SELECT *
FROM
  (SELECT daily_ok.log_date,
          (daily_error.s_count::numeric / 
            (daily_ok.s_count + daily_error.s_count)::numeric) * 100 
            AS error_percentage
   FROM
     (SELECT log_date,
             s_count
      FROM daily_status_count
      WHERE status LIKE '%200%') AS daily_ok,

     (SELECT log_date,
             s_count
      FROM daily_status_count
      WHERE status NOT LIKE '%200%') AS daily_error
   WHERE daily_ok.log_date = daily_error.log_date) AS daily_error_percentage
WHERE error_percentage > 1;
''',
        'answer_template': '\t%s : %.2f%% errors'
    }

]


def run_analysis(cur, analysis):
    cur.execute(analysis['query'])
    rows = cur.fetchall()

    print(analysis['question'])

    for row in rows:
        print(analysis['answer_template'] % row)

    print()


def log_analysis():
    ''' Start the whole log analysis '''
    conn = psycopg2.connect('dbname=%s' % DBNAME)
    cur = conn.cursor()

    for analysis in analysis_list:
        run_analysis(cur, analysis)

    conn.close()


if __name__ == '__main__':
    log_analysis()
