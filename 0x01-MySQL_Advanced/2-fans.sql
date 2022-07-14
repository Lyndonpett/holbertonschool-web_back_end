--  ranks country origins of bands, ordered by the number of (non-unique) fans
SELECT origin, SUM(fans) as NB_FANS
FROM metal_bands
GROUP BY origin
ORDER BY NB_FANS DESC;