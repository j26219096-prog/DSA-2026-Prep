WITH DailySales AS (
    SELECT visited_on, SUM(amount) AS daily_total
    FROM Customer
    GROUP BY visited_on
)
SELECT 
    visited_on,
    SUM(daily_total) OVER (
        ORDER BY visited_on 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS amount,
    ROUND(AVG(daily_total) OVER (
        ORDER BY visited_on 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ), 2) AS average_amount
FROM DailySales
LIMIT 1000 OFFSET 6; -- Skips the first 6 incomplete days
