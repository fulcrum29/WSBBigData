-- Load the ratings data
ratings = LOAD 'ratings.csv' USING PigStorage(',') AS (userId:int, movieId:int, rating:double, timestamp:long);

-- Group the ratings by movieId
grouped_ratings = GROUP ratings BY movieId;

-- Calculate the average rating for each movie
average_ratings = FOREACH grouped_ratings GENERATE group AS movieId, AVG(ratings.rating) AS average_rating;

-- Display the results
DUMP average_ratings;-- Load the ratings data
ratings = LOAD 'ratings.csv' USING PigStorage(',') AS (userId:int, movieId:int, rating:double, timestamp:long);

-- Group the ratings by movieId
grouped_ratings = GROUP ratings BY movieId;

-- Calculate the average rating for each movie
average_ratings = FOREACH grouped_ratings GENERATE group AS movieId, AVG(ratings.rating) AS average_rating;

-- Display the results
DUMP average_ratings;
