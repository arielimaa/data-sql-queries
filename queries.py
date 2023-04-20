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
    pass  # YOUR CODE HERE


def top_five_directors_for(db, genre_name):
    '''return the top 5 of the directors with the most movies for a given genre'''
    pass  # YOUR CODE HERE


def movie_duration_buckets(db):
    '''return the movie counts grouped by bucket of 30 min duration'''
    pass  # YOUR CODE HERE


def top_five_youngest_newly_directors(db):
    '''return the top 5 youngest directors when they direct their first movie'''
    pass  # YOUR CODE HERE
