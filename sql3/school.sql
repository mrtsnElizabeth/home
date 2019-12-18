school=# SELECT title, day, last_name
school-# FROM lesson
school-# INNER JOIN teacher
school-# ON lesson.lesson_id = teacher.teacher_id;

  title   |   day   | last_name
----------+---------+-----------
 Muzic    | monday  | Karr
 Painting | tuesday | Li
 Math     | friday  | Torn

school=# SELECT * FROM teacher
school-# LEFT JOIN lesson
school-# ON teacher.teacher_id = lesson.lesson_id;

 teacher_id | first_name | last_name | old | salary |           home_address            | lesson_id |  title   | themes | cabinet |   day   | class_id
------------+------------+-----------+-----+--------+-----------------------------------+-----------+----------+--------+---------+---------+----------
          1 | Peter      | Karr      |  34 |    400 | kharkiv, peremohy street          |         1 | Muzic    | ...    |      67 | monday  |        4
          2 | Sarah      | Li        |  56 |    800 | kharkiv, sumska street, 15        |         2 | Painting | ...    |      25 | tuesday |        3
          3 | Richard    | Torn      |  23 |    250 | kharkiv, gimnaziyna naberezhna, 3 |         3 | Math     | ...    |      84 | friday  |        3

school=# SELECT first_name, last_name, number , title
school-# FROM teacher
school-# RIGHT JOIN class ON teacher.teacher_id = class.class_id
school-# LEFT JOIN lesson ON teacher.teacher_id = lesson.lesson_id;

 first_name | last_name | number |  title
------------+-----------+--------+----------
 Peter      | Karr      |      1 | Muzic
 Sarah      | Li        |      2 | Painting
 Richard    | Torn      |      3 | Math
            |           |      4 |
            |           |      2 |

school=# SELECT * FROM class
school-# LEFT JOIN lesson_teacher
school-# ON class.class_id = lesson_teacher.lesson_id
school-# WHERE lesson_teacher.lesson_id IS NULL;

 class_id | number | number_pupils | teacher_id | lesson_id
----------+--------+---------------+------------+-----------
        4 |      4 |            33 |            |
        5 |      2 |            25 |            |

school=# SELECT number_pupils, title
school-# FROM class
school-# RIGHT JOIN lesson
school-# ON class.class_id = lesson.lesson_id
school-# WHERE lesson.lesson_id IS NULL;
 number_pupils | title
---------------+-------
(0 rows)

school=# SELECT * FROM class
school-# RIGHT JOIN lesson_teacher
school-# ON class.class_id = lesson_teacher.lesson_id
school-# WHERE lesson_teacher.lesson_id IS NULL;

 class_id | number | number_pupils | teacher_id | lesson_id
----------+--------+---------------+------------+-----------
(0 rows)

school=# SELECT number_pupils, number, title
school-# FROM class
school-# FULL JOIN lesson ON class.class_id = lesson.lesson_id;

 number_pupils | number |  title
---------------+--------+----------
            22 |      1 | Muzic
            27 |      2 | Painting
            32 |      3 | Math
            33 |      4 |
            25 |      2 |

school=# SELECT * FROM class
school-# FULL JOIN lesson
school-# ON class.class_id = lesson.lesson_id
school-# WHERE class.class_id IS NULL OR lesson.lesson_id IS NULL;

 class_id | number | number_pupils | lesson_id | title | themes | cabinet | day | class_id
----------+--------+---------------+-----------+-------+--------+---------+-----+----------
        4 |      4 |            33 |           |       |        |         |     |
        5 |      2 |            25 |           |       |        |         |     |