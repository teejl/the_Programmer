/*  Query Outline for Efficiency     
    BY THOMAS LOCKWOOD      
    CREATED ON 11/2/2017
*/

SELECT
    Column1
    ,Column2
    
FROM 
    (SELECT Table1.Column1, Table1.Column2 FROM Table1 --BRING IN DETAILS AND TRIM FOR SPEED
        -- WHERE BOOLEAN CONDITION 
        ) Table1
    ,(SELECT Table2.Column1, Table2.Column2 FROM Table2
        -- WHERE BOOLEAN CONDITION
        ) Table2
WHERE
    Table1.Column1 = Table2.Column1 (+) -- LEFT JOIN ON PO LINE ID
    
-- GROUP BY
    -- COLUMNS(include all non-aggregate functions)