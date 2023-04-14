SELECT a.title ,AVG(duration) FROM albums a
    JOIN songs s  ON a.id_albums  = s.id_albums 
    GROUP BY a.title ;