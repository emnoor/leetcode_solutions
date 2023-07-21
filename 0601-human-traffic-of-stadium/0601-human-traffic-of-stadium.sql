WITH validids AS (SELECT id
                  FROM Stadium
                  WHERE people >= 100)
SELECT id
     , visit_date
     , people
FROM Stadium
WHERE (id IN (SELECT id FROM validids)
        AND (id + 1) IN (SELECT id FROM validids)
        AND (id + 2) IN (SELECT id FROM validids))
   OR ((id - 1) IN (SELECT id FROM validids)
        AND id IN (SELECT id FROM validids)
        AND (id + 1) IN (SELECT id FROM validids))
   OR ((id - 2) IN (SELECT id FROM validids)
        AND (id - 1) IN (SELECT id FROM validids)
        AND id IN (SELECT id FROM validids))
ORDER BY visit_date
;
