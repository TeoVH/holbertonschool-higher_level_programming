-- Script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title

SELECT title FROM tv_shows WHERE title NOT IN (
SELECT s.title FROM tv_genres g, tv_show_genres t, tv_shows s
WHERE g.id = t.genre_id
    AND t.show_id = s.id
    AND g.name = "Comedy"
) ORDER BY title ASC;