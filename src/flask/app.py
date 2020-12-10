from math import sqrt
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('welcome.html')


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
    return [[0,"Titanic"], [1, "Alien"], [2, "Fargo"]] # This is a place holder fake return.

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
