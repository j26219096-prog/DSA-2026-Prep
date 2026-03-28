WITH FilteredStadium AS (
    SELECT 
        id, 
        visit_date, 
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS island_group
    FROM Stadium
    WHERE people >= 100
),
IslandCounts AS (
    SELECT 
        id, 
        visit_date, 
        people,
        COUNT(*) OVER (PARTITION BY island_group) AS consecutive_days
    FROM FilteredStadium
)
SELECT id, visit_date, people
FROM IslandCounts
WHERE consecutive_days >= 3
ORDER BY visit_date;
