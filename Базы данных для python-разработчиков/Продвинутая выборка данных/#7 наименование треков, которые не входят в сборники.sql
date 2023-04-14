SELECT s.title  from songs s 
        LEFT JOIN mixing_collection_and_songs mcas  ON s.id_songs  = mcas.id_songs 
        WHERE mcas.id_songs  IS NULL;