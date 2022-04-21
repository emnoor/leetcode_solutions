CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    DECLARE ofst INT;
    SET ofst = N - 1;
    RETURN (
        SELECT max(T.salary)
        FROM (
            SELECT salary
            FROM Employee
            GROUP BY salary
            ORDER BY salary DESC
            LIMIT 1
            OFFSET ofst
        ) T
    );
END