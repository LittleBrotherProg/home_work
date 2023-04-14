SELECT distinct(m.nickname) ,year_of_release FROM albums a
    JOIN mixing_albums_and_musician maam ON a.id_albums  = maam.id_albums 
    JOIN musicians m  ON maam.id_musician  = m.id_musician 
    WHERE a.year_of_release != 2020;