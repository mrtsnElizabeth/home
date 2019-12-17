postgres=# CREATE DATABASE school;
postgres=# \c school;
school=# CREATE TABLE teacher (teacher_id int, first_name varchar, last_name varchar, old int, salary int, home_address varchar);
school=# INSERT INTO teacher VALUES (1, 'Peter', 'Karr', 34, 400, 'kharkiv, peremohy street');
school=# INSERT INTO teacher VALUES (2, 'Sarah', 'Li', 56, 800, 'kharkiv, sumska street, 15');
school=# INSERT INTO teacher VALUES (3, 'Richard', 'Torn', 23, 250, 'kharkiv, gimnaziyna naberezhna, 3');
school=# SELECT * FROM teacher;

 teacher_id | first_name | last_name | old | salary |           home_address
------------+------------+-----------+-----+--------+-----------------------------------
          1 | Peter      | Karr      |  34 |    400 | kharkiv, peremohy street
          2 | Sarah      | Li        |  56 |    800 | kharkiv, sumska street, 15
          3 | Richard    | Torn      |  23 |    250 | kharkiv, gimnaziyna naberezhna, 3
(3 rows)

school=# CREATE TABLE lesson (lesson_id int, title varchar, themes varchar, cabinet int, day varchar, class_id int);
school=# INSERT INTO lesson VALUES (1, 'Muzic', '...', 67, 'monday', 4);
school=# INSERT INTO lesson VALUES (2, 'Painting', '...', 25, 'tuesday', 3);
school=# INSERT INTO lesson VALUES (3, 'Math', '...', 84, 'friday', 3);
school=# SELECT * FROM lesson;

lesson_id  |  title   | themes | cabinet |   day   | class_id
-----------+----------+--------+---------+---------+----------
         1 | Muzic    | ...    |      67 | monday  |        4
         2 | Painting | ...    |      25 | tuesday |        3
         3 | Math     | ...    |      84 | friday  |        3
(3 rows)

school=# CREATE TABLE lesson_teacher (teacher_id int, lesson_id int);
school=# INSERT INTO lesson_teacher VALUES (1, 2);
school=# INSERT INTO lesson_teacher VALUES (2, 3);
school=# INSERT INTO lesson_teacher VALUES (3, 1);
school=# SELECT * FROM lesson_teacher;

 teacher_id | lesson_id
------------+-----------
          1 |         2
          2 |         3
          3 |         1
(3 rows)

school=# CREATE TABLE class (class_id int, number int, number_pupils int);
school=# INSERT INTO class VALUES (1, 1, 22);
school=# INSERT INTO class VALUES (2, 2, 27);
school=# INSERT INTO class VALUES (3, 3, 32);
school=# INSERT INTO class VALUES (4, 4, 33);
school=# INSERT INTO class VALUES (5, 2, 25);
school=# SELECT * FROM class;

 class_id | number | number_pupils
----------+--------+---------------
        1 |      1 |            22
        2 |      2 |            27
        3 |      3 |            32
        4 |      4 |            33
        5 |      2 |            25
(5 rows)

school=# \dt

               List of relations
 Schema |      Name      |  Type   | Owner
--------+----------------+---------+----------
 public | class          | table   | postgres
 public | lesson         | table   | postgres
 public | lesson_teacher | table   | postgres
 public | teacher        | table   | postgres
(4 rows)
