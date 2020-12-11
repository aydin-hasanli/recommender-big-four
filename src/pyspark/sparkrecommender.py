import sys
import numpy as np
import pandas as pd
import pyspark
from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.mllib.evaluation import RegressionMetrics

movies = pd.read_csv('../../data/ml-latest-small/movies.csv')
ratings = pd.read_csv('../../data/ml-latest-small/ratings.csv')
spark = SparkSession.builder.getOrCreate()
spark_ratings = spark.createDataFrame(ratings)
train, test = spark_ratings.randomSplit([0.8, 0.2], seed=427471138)
only_in_test_movies_id = set(test.toPandas().movieId) - set(train.toPandas().movieId)
movie_only_in_test = test.filter(test.movieId.isin(only_in_test_movies_id))
train = train.union(movie_only_in_test)
test = test.filter(~test.movieId.isin(only_in_test_movies_id))

als_model_final = ALS(userCol='userId',
                itemCol='movieId',
                ratingCol='rating',
                nonnegative=True,
                regParam=0.1,
                rank=30
               )

recommender = als_model_final.fit(train)
predictions_train = recommender.transform(train)
rmse_train = evaluator.evaluate(predictions_train)
print("Root-mean-square error for train = " + str(rmse_train))

predictions = recommender.transform(test)
rmse_test = evaluator.evaluate(predictions)
print("Root-mean-square error = " + str(rmse_test))

def movie_recomendation(user=1, movie=500, number=10):
    data = [(user, movie)]
    columns = ('userId', 'movieId')
    one_row_spark_df = spark.createDataFrame(data, columns)
    userSubsetRecs = recommender.recommendForUserSubset(one_row_spark_df, number)
    pd_format=userSubsetRecs.toPandas()
    list_recommend=[]
    for n in pd_format.recommendations[0]:
        list_recommend.append(n[0])
    return list_recommend

if __name__ == "__main__":

    print(movie_recomendation(user=1, movie=500, number=15))