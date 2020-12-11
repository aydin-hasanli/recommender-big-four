from math import sqrt
from flask import Flask, render_template, request, jsonify
import pandas as pd
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import test
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    user_data = request.json
    user_id, movie_id, number_movies = user_data['user_id'], user_data['movie_id'], user_data['number_movies']
    movie_list = _recommend_movie(user_id, movie_id, number_movies)
    return jsonify({'result': movie_list})

def _recommend_movie(user_id, movie_id, number_movies):
    """Generate recommended movies as a list of list. Each pair follows the pattern [movie_id, movie_name]

    Args:
        user_id (int): user id
        movie_id (int): movie_id that the user watched
        number_movies (int): number of movies to return
    Returns:
        a list of list. Each pair follows the pattern [movie_id, movie_name]
    """
    #get the recommended movie ids from pickled model
    rec_movies = test.get_recommends_from_model(user_id,movie_id,number_movies)
    #get a list of movies ids used in model
    moviesdf = pd.read_csv('../../data/ml-latest-small/movies.csv',index_col='movieId')
    
    #build list of lists with [[imdb ID, movie title, post img link]]
    rec_movies_list = []
    for movie_id in rec_movies:
        temp_list = []
        imdbid_ = get_imdbId(movie_id)
        temp_list.append(imdbid_)
        temp_list.append(moviesdf.loc[movie_id,'title'])
        temp_list.append('http://img.omdbapi.com/?apikey=ae550a04&i=tt'+str(imdbid_))
        rec_movies_list.append(temp_list)
    return rec_movies_list

def get_imdbId(movieIds):
    #if given a list of movie IDs, returns a list of corresponding imdbIDs
    #if given one movie ID, returns the corresponding IMDB ID
    linksdf = pd.read_csv('../../data/ml-latest-small/links.csv',index_col='movieId')
    if type(movieIds)==list:
        imdbIds = []
        for id_ in movieIds:
            imdbIds.append(linksdf.loc[id_,'imdbId'])
    elif type(movieIds)==int:
        imdbIds = linksdf.loc[movieIds,'imdbId']
    else:
        pass
    return imdbIds


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
