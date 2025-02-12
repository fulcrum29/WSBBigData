-- Load the ratings data
ratings = LOAD 'ratings.csv' USING PigStorage(',') AS (userId:int, movieId:int, rating:double, timestamp:long);

-- Load the movies data
movies = LOAD 'movies.csv' USING PigStorage(',') AS (movieId:int, title:chararray, genres:chararray);

-- Group the ratings by movieId
grouped_ratings = GROUP ratings BY movieId;

-- Calculate the average rating for each movie
average_ratings = FOREACH grouped_ratings GENERATE group AS movieId, AVG(ratings.rating) AS average_rating;

-- Join the average ratings with the movies data
joined_data = JOIN average_ratings BY movieId, movies BY movieId;

-- Generate the final output with title and average rating
final_output = FOREACH joined_data GENERATE movies::title AS title, average_ratings::average_rating AS average_rating;

-- Display the results
DUMP final_output;
