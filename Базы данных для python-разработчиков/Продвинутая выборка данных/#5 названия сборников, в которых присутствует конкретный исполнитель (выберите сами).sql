SELECT c.title  FROM collection c
        JOIN mixing_collection_and_songs mcas  ON c.id_collection  = mcas.id_collection 
        JOIN songs s  ON mcas.id_songs  = s.id_songs 
        JOIN albums a  ON s.id_songs  = a.id_albums 
        JOIN mixing_albums_and_musician maam  ON a.id_albums  = maam.id_albums 
        JOIN musicians m  ON maam.id_albums = m.id_musician 
        WHERE m.nickname  LIKE 'Lumen';