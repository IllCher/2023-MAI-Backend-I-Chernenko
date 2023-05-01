CREATE SCHEMA IF NOT EXISTS public;

CREATE TABLE
  public.film (
    title text NOT NULL CHECK (length (title) < 64),
    year integer CHECK (year > 0),
    uuid uuid NOT NULL DEFAULT gen_random_uuid (),
    CONSTRAINT film_pkey PRIMARY KEY (uuid)
  )
WITH(oids = false);

CREATE TABLE
  public.director (
    name text NOT NULL CHECK (length (name) < 64),
    uuid uuid NOT NULL DEFAULT gen_random_uuid (),
    CONSTRAINT director_pkey PRIMARY KEY (uuid)
  )
WITH (oids = false);

CREATE TABLE
  film_director (
    film_uuid uuid NOT NULL,
    director_uuid uuid NOT NULL,
    CONSTRAINT film_director_pkey PRIMARY KEY (film_uuid, director_uuid),
    CONSTRAINT film_director_film_uuid_fkey FOREIGN KEY (film_uuid) REFERENCES film (uuid) ON DELETE CASCADE,
    CONSTRAINT film_director_director_uuid_fkey FOREIGN KEY (director_uuid) REFERENCES director (uuid) ON DELETE CASCADE
  );
