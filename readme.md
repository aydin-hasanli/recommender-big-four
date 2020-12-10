# Movie Recommender Case Study

Today you are going to have a little friendly competition with your classmates.

You are going to building a recommendation system based off data from the
[MovieLens dataset](http://grouplens.org/datasets/movielens/). It includes movie
information, user information, and the users' ratings. Your goal is to build a
recommendation system and to suggest movies to users!

The **movies data** and **user data** are in `data/movies.dat` and `data/users.dat`.

The **ratings data** can be found in `data/training.csv`. The users' ratings have been broken into a training and test set for you (to obtain the testing set, we have split the 20% of **the most recent** ratings).

You can get **additional metadata** by downloading [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset/version/7). This may be useful for creating NLP (content-based) features, which could be part of your team's solution to the "cold start" problem. (Remember to start with a simple model first!)

## Your mission [read carefully]

You are provided a **request** file in `data/requests.csv`. It contains a list of `user,movie` pairs.

**Your mission** is to provide a rating for each of those `user,movie` pairs. You will submit a csv file with three columns `user,movie,rating` as created by the script `src/run.py` (see below).

We ask you to **provide this submission file via a link to your github repository** (the master of your group).

Your **score** will be measured based on how well you predict the ratings for the users' ratings compared to our test set. At the end of the day, we will collect your predicted ratings and provide a score (see below).


## How to implement your recommender

The file `src/recommender.py` is your main template for creating your recommender. You can work from this file and implement whatever strategy you think is best. You need to implement both the `.fit()` and the `.transform()` methods.

**Tips**: You might want to consider working in a notebook first, in order to establish a proper training strategy (proof of concept). In practice, it is not necessary to implement the file `src/recommender.py` to provide a submission file (a notebook can perfectly do that without running through `src/run.py`). If you don't do that during the case study, eventually we recommend you to try to integrate your implementation into the `src/recommender.py` file.


## How to run your recommender

`src/run.py` has been prepared for your convenience (doesn't need modification). By executing it you create an instance of a `MovieRecommender` class (see file `src/recommender.py`), feeds it with the training data and outputs the results in a file.

It outputs a _properly formatted_ file of recommendations for you!

  Here's how to use this script:
  ```bash
  usage: run.py [-h] [--train TRAIN] [--requests REQUESTS] [--silent] outputfile

  positional arguments:
    outputfile           output file (where predictions are stored)

  optional arguments:
    -h, --help           show this help message and exit
    --train TRAIN        path to training ratings file (to fit)
    --requests REQUESTS  path to the input requests (to predict)
    --silent             deactivate debug output
  ```

When running this script, **you need to** specify your prediction output file as an argument (the one you will submit).

**Try now** to create a random prediction file by typing:

```bash
python src/run.py data/sample_submission.csv
```

## How we will submit your prediction for scoring

`src/submit.py` is the script **we** will use to submit your results for scoring. It reads your submission from a csv as produced by `src/run.py` compares it to our **secret testing set**.

Here's how we use this script:
  ```bash
  usage: submit.py [-h] [--silent] [--testing TESTING] predfile

  positional arguments:
    predfile           prediction file to submit

  optional arguments:
    -h, --help         show this help message and exit
    --silent           deactivate debug output
    --testing TESTING  testing set
  ```

**You need to** specify your prediction file (the one produced by `src/run.py`) as an argument.

If you want to try this script, try running :

```bash
python src/submit.py --testing data/fake_testing.csv data/sample_submission.csv
```

It should return a score around 2.50. **WARNING: this fake_testing.csv is just a random testing test, DO NOT USE IT to validate your model**.


## Evaluation: how the score is computed

We provide this submit script so that you can understand the scoring methodology. Look at the function `compute_score()` to get the idea:
- we will use your prediction file to extract, for each user, the 5% most highly predicted movies
- we will look at the actual rating of those movies in our hidden testing set.
- we will compute the mean of those ratings.

Thus, for an algorithm to score well, it only needs to identify which movies a user is likely to rate most highly (so the absolute accuracy of your ratings is less important than the rank ordering).

As mentioned above, your submission should be in the same format as the sample
submission file, and the only thing that will be changed is the ratings column.


## Note on running your script with Spark

If your `recommender.py` script relies on spark, you may want to use the script `run_on_spark.sh` to execute your code.

In a terminal, use: `run_on_spark.sh src/run.py` with arguments to run your recommender.

The `src/submit.py` doesn't need to run on spark, as it simply reads the result file produced by `run.py`.
