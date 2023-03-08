create table if not exists music_genre(
	id_misic_genre serial PRIMARY key,
	name VARCHAR(60) not NULL
);

create table if not exists musicians(
	id_musician serial primary key,
	nickname varchar(60) not NULL
);

create table if not exists mixing_genre_and_musiciak(
	id_music_genre integer references music_genre(id_misic_genre),
	id_musician integer references musicians(id_musician)
);

create table if not exists albums(
	id_albums serial primary key,
	title varchar(60) not NULL,
	year_of_release date not NULL
);

create table if not exists mixing_albums_and_musician(
	id serial primary key,
	id_musician integer not NULL references musicians(id_musician),
	id_albums integer not null references albums(id_albums)
);

create table if not exists songs(
	id_songs serial primary key,
	title varchar(60) not NULL,
	duration float8 not NULL,
	id_albums integer not null references albums(id_albums)
);

create table if not exists collection(
	id_collection serial primary key,
	title varchar(60) not null,
	year_of_release date not NULL
);

create table if not exists mixing_collection_and_songs(
	id_songs integer not NULL references songs(id_songs),
	id_collection integer not NULL references collection(id_collection)
);
