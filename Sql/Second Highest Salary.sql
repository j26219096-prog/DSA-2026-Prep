SELECT (
  
    SELECT DISTINCT Salary 
    FROM (
        SELECT Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) as rank_num
        FROM Employee
    ) as RankedSalaries
    WHERE rank_num = 2
) AS SecondHighestSalary;
