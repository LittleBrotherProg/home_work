SELECT a.title  FROM albums a
        JOIN mixing_albums_and_musician maam  ON a.id_albums  = maam.id_albums 
        JOIN musicians m  ON maam.id_musician  = m.id_musician 
        JOIN mixing_genre_and_musiciak mgam  ON m.id_musician  = mgam.id_musician 
        GROUP BY m.nickname, a.title 
        HAVING count(mgam.id_music_genre) > 1;