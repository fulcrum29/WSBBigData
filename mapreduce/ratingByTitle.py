from mrjob.job import MRJob
from mrjob.step import MRStep

class MovieRatingsAverage(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_ratings,
                   reducer=self.reducer_average_rating),
            MRStep(mapper_init=self.mapper_init_movies,
                   mapper=self.mapper_join_movies)
        ]

    def mapper_ratings(self, _, line):
        # Read ratings.csv
        # Format: userId,movieId,rating,timestamp
        parts = line.split(',')
        if parts[0] != "userId":  # Skip header
            yield int(parts[1]), float(parts[2])  # (movieId, rating)

    def reducer_average_rating(self, movieId, ratings):
        ratings_list = list(ratings)
        avg_rating = sum(ratings_list) / len(ratings_list)
        yield movieId, avg_rating

    def mapper_init_movies(self):
        # Read movies.csv and store movieId -> title mapping
        self.movie_titles = {}
        with open("/home/fulcrum/projects/studia/wsbbigdata/mapreduce/movies.csv", encoding='utf-8') as f:
            for line in f:
                parts = line.strip().split(',')  # Handle movieId, title
                if parts[0] != "movieId":  # Skip header
                    self.movie_titles[int(parts[0])] = parts[1]

    def mapper_join_movies(self, movieId, avg_rating):
        title = self.movie_titles.get(movieId)
        yield title, avg_rating

if __name__ == '__main__':
    MovieRatingsAverage.run()
