WITH allids AS (SELECT id FROM Stadium WHERE people >= 100)
SELECT id, visit_date, people
FROM Stadium
WHERE ((id + 0) IN (SELECT id FROM allids)
        AND (id + 1) IN (SELECT id FROM allids)
        AND (id + 2) IN (SELECT id FROM allids))
   OR ((id - 1) IN (SELECT id FROM allids)
        AND (id + 0) IN (SELECT id FROM allids)
        AND (id + 1) IN (SELECT id FROM allids))
   OR ((id - 2) IN (SELECT id FROM allids)
        AND (id - 1) IN (SELECT id FROM allids)
        AND (id + 0) IN (SELECT id FROM allids))
ORDER BY visit_date
;