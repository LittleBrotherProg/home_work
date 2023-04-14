SELECT a.title , COUNT(s.id_songs) FROM albums a
    JOIN songs s  ON a.id_albums  = s.id_albums 
    GROUP BY a.title  
    HAVING count(s.id_songs) in (
        SELECT COUNT (s.id_songs)
        FROM albums a
        JOIN songs s2  ON a.id_albums  = s2.id_albums 
        GROUP BY a.title 
        ORDER BY count(s.id_songs)
        LIMIT 1)