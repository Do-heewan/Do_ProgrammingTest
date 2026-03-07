WITH RECURSIVE generations AS (
    -- 부모가 없으면 1세대
    SELECT ID, PARENT_ID, 1 AS GENERATION
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    
    UNION ALL
    
    -- 재귀적으로 각 개체의 자식을 찾아 세대를 계산
    SELECT e.ID, e.PARENT_ID, g.GENERATION + 1
    FROM ECOLI_DATA e
    INNER JOIN generations g 
    ON e.PARENT_ID = g.ID
)
-- 자식이 없는 개체들을 찾고 세대별로 카운트
SELECT 
    COUNT(*) AS COUNT, 
    g.GENERATION
FROM generations g
WHERE NOT EXISTS (
    SELECT 1 
    FROM ECOLI_DATA child 
    WHERE child.PARENT_ID = g.ID
)
GROUP BY g.GENERATION
ORDER BY g.GENERATION;