-- an SQL script that ranks country origins of bands
-- import metal bands
SELECT origin as country, SUM(fans) as nb_fans
FROM metal_bands GROUP BY origin
ORDER BY nb_fans DESC;
