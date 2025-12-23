# Movie Clustering & Similarity Project
## Overview:

* This project explores how to group and find similar movies using unsupervised learning, without relying on user ratings.

* Movies are clustered based only on metadata (genres, actors, director) using K-Means.
* The focus is on building a clean end-to-end ML pipeline and understanding how to work with pd and numpy libaries .


## Data Source:
* API: TMDB (The Movie Database)
* Movies: ~150–200 popular movies (prototype scale)
* For each movie, the following metadata is used:
    * Genres
    * Up to 5 main actors
    * Director

## Adjusting the data to vectors that represent similarity:
* The TMDB API provides movie metadata as lists of IDs (for actors, directors, and genres).
* These raw IDs cannot be used directly to measure similarity between movies.

    * For example, consider two movies that share the same actors except one:
        * Movie A: Brad Pitt, Tom Hanks
        * Movie B: Brad Pitt, Leonardo DiCaprio

    * If we treat actor IDs as numeric values, the distance between movies would depend on the arbitrary ID values assigned by  the data source, not on real similarity.
    * Even if two movies share most of their cast, they could appear very far apart numerically just because their IDs are far apart.

* To solve this, the data is transformed into one-hot and multi-hot vectors:
    * the value is binary (0 or 1), indicating presence or absence
    * shared actors or genres reduce distance
    * unrelated movies remain far apart


## Output:
* Clustered movies are exported to a JSON file "movie_clusters_output.json"
* example to the output:
* "9": [
    "Wake Up Dead Man: A Knives Out Mystery",
    "Knives Out",
    "Glass Onion: A Knives Out Mystery"
    ],
* we can see that movies series are clusterd togther which make sence.