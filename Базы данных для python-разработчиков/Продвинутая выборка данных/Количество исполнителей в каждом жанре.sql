 SELECT title,COUNT(title) FROM musicians
    JOIN mixing_genre_and_musiciak ON musicians.id_musician  = mixing_genre_and_musiciak.id_musician 
    JOIN collection ON mixing_genre_and_musiciak.id_music_genre  = collection.id_collection 
    GROUP BY title;

