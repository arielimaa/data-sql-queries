# pylint: disable=C0103, missing-docstring

def detailed_movies(db):
    '''return the list of movies with their genres and director name'''
    query= """
    SELECT movies.title, movies.genres, directors.name
FROM movies
JOIN directors ON movies.director_id = directors.id
"""
    db.execute(query)
    results = db.fetchall()
    return results


def late_released_movies(db):
    '''return the list of all movies released after their director death'''
    query= """
     SELECT movies.title
        FROM directors
        JOIN movies ON directors.id = movies.director_id
        WHERE (movies.start_year - directors.death_year) > 0
        ORDER BY movies.title
        """
    db.execute(query)
    results = db.fetchall()
    return [r[0] for r in results]


def stats_on(db, genre_name):
    '''return a dict of stats for a given genre'''
    query= """
    SELECT COUNT(m.title), AVG(m.minutes) 
    FROM movies m 
    WHERE m.genres = ?
    """
    db.execute(query, (genre_name,))
    results = db.fetchall()
    return({'genre': genre_name,'number_of_movies': results[0][0],
            'avg_length': round(results[0][1],2)})


def top_five_directors_for(db, genre_name):
    '''return the top 5 of the directors with the most movies for a given genre'''
    query= """
    SELECT d.name ,COUNT(*) movie_count
    FROM movies m
    JOIN directors d ON m.director_id = d.id
    WHERE m.genres = ?
    GROUP BY d.name
    ORDER BY movie_count DESC , d.name
    LIMIT 5
    """
    db.execute(query, (genre_name,))
    results = db.fetchall()
    return results


def movie_duration_buckets(db):
    '''return the movie counts grouped by bucket of 30 min duration'''
    query= """SELECT (minutes / 30 + 1)*30 time_range,
    COUNT(*)
    FROM movies
    WHERE minutes IS NOT NULL
    GROUP BY time_range
    """
    db.execute(query)
    results = db.fetchall()
    return results


def top_five_youngest_newly_directors(db):
    '''return the top 5 youngest directors when they direct their first movie'''
    query= """SELECT directors.name, movies.start_year - directors.birth_year age
    FROM directors
    JOIN movies ON directors.id = movies.director_id
    GROUP BY directors.name
    HAVING age IS NOT NULL
    ORDER BY age
    LIMIT 5
    """
    db.execute(query)
    results = db.fetchall()
    return results
