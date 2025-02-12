from mrjob.job import MRJob

class AverageRating(MRJob):

    def mapper(self, _, line):
        line_split = line.split(',')

        # Emit the movieId as the key and the rating as the value
        (userId,movieId,rating) = line_split

        yield movieId, rating

    # def reducer(self, key, values):
    #     # Calculate the average rating for the movie
    #     ratings = list(values)
    #     # ratingsSum=0
    #     # for line in ratings:
    #     #     ratingsSum+=sum(line)
    #     avg_rating = sum(ratings) / len(ratings)
    #     # Emit the movieId and its average rating
    #     yield key, avg_rating

if __name__ == '__main__':
    AverageRating.run()
