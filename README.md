
# Recommendation System Case Study

- [Recommendation System Case Study](#recommendation-system-case-study)
  - [Objectives](#objectives)
  - [Tech Stacks and Team Organization](#tech-stacks-and-team-organization)
    - [Tech Stacks](#tech-stacks)
    - [Team Organization](#team-organization)
  - [The Case Study Description](#the-case-study-description)
    - [Data Description](#data-description)
    - [References and Hints](#references-and-hints)
Students will use collaborative filtering and matrix factorization in `Spark` or `Surprise` in this case study. Students are also encouraged to build a simple `flask` application.


## Objectives

There are three aims of the following case study:

  1. **Improve your big data skills** by including as part of your solution a working recommender written in Spark.
  2. **Demonstrate your knowledge of recommendation systems** by using the library **Surprise** to tweak and customize different algorithms
  3. **Practice you communication** by presenting to a non-technical audience

## Tech Stacks and Team Organization

### Tech Stacks

You can choose either to use `Spark` or `Surprise` for the recommendation system building. You can use both by properly allocating workload if time permits. If you choose to use `Spark`, the earlier assignments and lecture notes will be useful. However, `Surprise` is also a good choice and its API is very similar to `scikit-learn`.

1. Spark and the big data solution

    These are two useful links for the Spark approach.

  * [The official documentation](https://spark.apache.org/docs/latest/ml-collaborative-filtering.html)
  * [A solution blog](https://www.codementor.io/jadianes/building-a-recommender-with-apache-spark-python-example-app-part1-du1083qbw)

    The second blog post uses MLlib instead of ML it
    is still a useful resource.  `ML` is the more stable library and it is preferred to MLLib (if possible).

2. [`Surprise`](http://surpriselib.com/)

    [Suprise](http://surpriselib.com/) is a Python library that is designed for the recommendation system building. Surprise has a version of the data built in to it.

    Here is a [blog post](https://medium.com/hacktive-devs/recommender-system-made-easy-with-scikit-surprise-569cbb689824) that uses `Surprise` to predict movie ratings.

    And the documentation is pretty good.

3. Flask

    A sample Flask template `app.py` file is included in the [src](src) directory.


### Team Organization

The dataset is pretty clean so **parallelization** can be utilized to improve the efficiency. For example. If you have a team of 3 Alice, Bob and Carl, you can allocate tasks as following.

1. Alice: Test baseline models in `Spark` or `Surprise` and learn the workflow, not necessarily using this dataset.
2. Bob: Prepare and do EDA analysis of the dataset, communicate with Alice to prepare the dataset to feed into models.
3. Carl: Write the skeleton of the `Flask` application. Define the `API` to connect your teammates' model to the web interface. Test it with fake data for example.

Later the tasks can be reassigned to create readmes/slides, etc.

## The Case Study Description


You and a team of talented data scientists are working for the
company, **Movies-Legit**, who has used a production recommenders for
many years now.  The recommender provides a significant revenue stream
so your managers are heisitent to touch it.  The issue is that these
systems have been around a long time and your head of data science has
asked you and your team members to explore new solutions.

The solution that has been around for so long is called the **Mean of
Means**.  We see that some users like to rate things highly---others
simply do not.  Some items are just better or worse.  We can capture
these general trends through per-user and per-item rating means. We
also incorporate the global mean to smooth things out a bit. So if we
see a missing value in cell $R_{ij}$, we'll average the global
mean with the mean of $U_i$ and the mean of $V_j$ and use
that value to fill it in.

We would like you to use this as a baseline when making your
comparisons.  The basic code showing you how this is done is provided
for you in `src/baselines.py`.
   
At the end of the day you are to present your solution to the bosses
and the entire product team.  You can assume that they have little to no
depth of knowledge in statistics and big data technologies.

The main goal here is to improve the RMSE, however, another equally
important goal is to present your model and the details of your
explorations in a clear, but technically sound manner.  *You need to
convince us that you understand the tools you are using AND that it is
a better way forward.* After all we are making a lot of money with
*mean of means* and it is a major risk to swap it out with anything else.

We would also like you to include some discussion about how you would
move from prototype to production.

### Data Description


`MovieLens` is a classical recommender dataset and you can assume your audience is already familiar with it.

There is a larger version of the dataset available from this (link](https://grouplens.org/datasets/movielens), but we do not expect a production ready recommender in only a
day's time so do not worry too much about scale for now.  You will find
the smaller version of the data as part of this repo. Read the [`README.txt`](data/ml-latest-small/README.txt) to understand the data description.

    
### References and Hints


  * A challenge with the Spark solution can be to implement a *mean of means* baseline
  * `Surprise` can be challenging to shape into what you might want, but it has a lot builtin
  * Make sure you show an example of a prediction
  * **The numeric results are not as important here as how well you communicate what you have done**  
  * Finally, the 'bosses' are not real keen thinking too hard about
    RMSE or MAE.  You might be able to explain it to them, but if you
    report it as percent improvement over mean-of means they are more
    likely to listen.
    
Good luck!
