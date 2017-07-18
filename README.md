# Log Analysis Application

## What is this?
This is a simple but useful database analysis application for website log database.

## How does it work?
The application takes in a list of analyses. 

In every analysis on the list, there is a question that the analysis need to answer, a pre-defined SQL query that is carefully designed to answer that question, and a template for outputting the result. 

The application then go through every analysis on the list, query the database with SQL statements, and print out the results on the screen.

## What do I need to run it?
Make sure your computer / server have [python3](https://www.python.org/) and [postgreSQL](https://www.postgresql.org/) installed and running. You can follow [this guide](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0) from Udacity to setup. In the database system you should have a database named `news` and its tables should match what this application is designed based on. A sample dataset can be found [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

## Any views I need to create beforehand in my database?
Yes. This application assumes 3 views in your database. Without them it will not work. Please set these 3 views before running the analyses:

The `article_slug_author` view:
```
CREATE VIEW article_slug_author AS
SELECT title,
       slug,
       name
FROM articles,
     authors
WHERE author = authors.id;
```

The `path_log` view:
```
CREATE VIEW path_log AS
SELECT path,
       count(*) AS path_count
FROM log
GROUP BY path
ORDER BY path;
```

The `daily_status_count` view:
```
CREATE VIEW daily_status_count AS
SELECT time::date AS log_date,
       status,
       count(*) AS s_count
FROM log
GROUP BY log_date,
         status;
```
