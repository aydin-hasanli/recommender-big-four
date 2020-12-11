#flask testing python script to return a list of movie Ids 
import random
import pandas as pd

def get_recommends_from_model(user_id, movie_id, number_movies):
    #get a list of movies ids used in model
    movies = pd.read_csv('../../data/ml-latest-small/movies.csv',usecols=['movieId','title'])
    movieIds = list(movies.movieId)
    #builds the movie names df
    # movies.set_index('movieId',inplace=True)
    #edit this part to call the pickled models to get a list of recommended movie IDs
    random.seed(1)
    recIds = random.sample(movieIds,number_movies)
    return recIds
    #builds the return list of [[movieID, movie title]]
    # return_list = []
    # for id_ in recIds:
    #     return_list.append([id_,movies.loc[id_,'title']])
    # return return_list

if __name__ == '__main__':
    pass