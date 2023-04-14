SELECT distinct(m.nickname) , s.duration FROM musicians m
        JOIN mixing_albums_and_musician maam ON m.id_musician  = maam.id_musician 
        JOIN albums a ON maam.id_albums  = a.id_albums 
        JOIN songs s  ON a.id_albums  = s.id_albums 
        WHERE s.duration IN (SELECT MIN(duration) FROM songs)