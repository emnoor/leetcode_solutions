SELECT D.name   AS Department
     , E.name   AS Employee
     , E.salary AS Salary
FROM Employee E
         JOIN Department D ON E.departmentId = D.id
WHERE 3 > (SELECT count(distinct E2.salary)
           FROM Employee E2
           WHERE E2.departmentId = E.departmentId
             AND E2.salary > E.salary)
ORDER BY Department, Salary DESC