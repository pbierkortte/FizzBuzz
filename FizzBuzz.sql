;WITH Numbers(i) AS 
(               SELECT   1 
    UNION ALL   SELECT i+1                      FROM Numbers WHERE i < 100
)
, Cte(i, s) AS 
(               SELECT i, 'FizzBuzz'            FROM Numbers WHERE i % 15 = 0
    UNION ALL   SELECT i, 'Fizz'                FROM Numbers WHERE i %  3 = 0
    UNION ALL   SELECT i, 'Buzz'                FROM Numbers WHERE i %  5 = 0
    UNION ALL   SELECT i, CAST(i AS VARCHAR(8)) FROM Numbers 
)
SELECT MAX(s)
FROM Cte
GROUP BY i
