SELECT year_of_release,COUNT(a.title) FROM albums a
    JOIN songs s  ON a.id_albums  = s.id_albums 
    WHERE a.year_of_release  >= 2019 AND a.year_of_release <= 2020
    GROUP BY year_of_release;