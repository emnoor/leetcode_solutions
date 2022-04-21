SELECT coalesce(max(T.salary), NULL) AS SecondHighestSalary
FROM (
    SELECT salary
    FROM Employee
    GROUP BY salary
    ORDER BY salary DESC
    LIMIT 1
    OFFSET 1
) T