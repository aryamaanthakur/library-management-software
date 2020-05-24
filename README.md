# Library Management Software

This is a small command line based script that I made as my high school project. It is a basic library management software written in python and utilising MySQL for database.

## MySQL database

<pre>
mysql> show tables;
+-------------------+
| Tables_in_library |
+-------------------+
| books             |
| members           |
| transactions      |
+-------------------+

mysql> describe books;
+-------------+----------------------+------+-----+---------+----------------+
| Field       | Type                 | Null | Key | Default | Extra          |
+-------------+----------------------+------+-----+---------+----------------+
| bookID      | smallint(5) unsigned | NO   | PRI | NULL    | auto_increment |
| name        | varchar(100)         | NO   |     | NULL    |                |
| author      | varchar(30)          | NO   |     | NULL    |                |
| publication | varchar(30)          | NO   |     | NULL    |                |
| category    | varchar(30)          | NO   |     | NULL    |                |
| price       | smallint(5) unsigned | NO   |     | NULL    |                |
| isbn        | varchar(20)          | NO   |     | NULL    |                |
| status      | varchar(10)          | NO   |     | ACTIVE  |                |
+-------------+----------------------+------+-----+---------+----------------+

mysql> describe members;
+----------+----------------------+------+-----+---------+----------------+
| Field    | Type                 | Null | Key | Default | Extra          |
+----------+----------------------+------+-----+---------+----------------+
| memberID | smallint(5) unsigned | NO   | PRI | NULL    | auto_increment |
| name     | varchar(30)          | NO   |     | NULL    |                |
| phone    | varchar(10)          | NO   |     | NULL    |                |
| address  | varchar(100)         | NO   |     | NULL    |                |
| email    | varchar(50)          | YES  |     | NULL    |                |
| status   | varchar(10)          | NO   |     | ACTIVE  |                |
+----------+----------------------+------+-----+---------+----------------+

mysql> describe transactions;
+---------------+----------------------+------+-----+---------+----------------+
| Field         | Type                 | Null | Key | Default | Extra          |
+---------------+----------------------+------+-----+---------+----------------+
| transactionID | int(10) unsigned     | NO   | PRI | NULL    | auto_increment |
| bookID        | smallint(5) unsigned | NO   | MUL | NULL    |                |
| memberID      | smallint(5) unsigned | NO   | MUL | NULL    |                |
| issuedate     | datetime             | NO   |     | NULL    |                |
| returndate    | datetime             | YES  |     | NULL    |                |
| status        | varchar(10)          | NO   |     | ISSUED  |                |
+---------------+----------------------+------+-----+---------+----------------+
</pre>
