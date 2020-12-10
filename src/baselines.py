#!/usr/bin/env python

"""
http://surprise.readthedocs.io/en/stable/building_custom_algo.html
"""

import sys
import numpy as np
from surprise import AlgoBase, Dataset
from surprise.model_selection.validation import cross_validate

class GlobalMean(AlgoBase):
    def __init__(self):

        # Always call base method before doing anything.
        AlgoBase.__init__(self)

    def fit(self, trainset):

        # Here again: call base method before doing anything.
        AlgoBase.fit(self, trainset)

        # Compute the average rating. We might as well use the
        # trainset.global_mean attribute ;)
        self.the_mean = np.mean([r for (_, _, r) in
                                 self.trainset.all_ratings()])

        return self

    def estimate(self, u, i):

        return self.the_mean


class MeanofMeans(AlgoBase):
    def __init__(self):

    # Always call base method before doing anything.
        AlgoBase.__init__(self)


    def fit(self, trainset):

        # Here again: call base method before doing anything.
        AlgoBase.fit(self, trainset)

        users = np.array([u for (u, _, _) in self.trainset.all_ratings()])
        items = np.array([i for (_, i, _) in self.trainset.all_ratings()])
        ratings = np.array([r for (_, _, r) in self.trainset.all_ratings()])

        user_means,item_means = {},{}
        for user in np.unique(users):
            user_means[user] = ratings[users==user].mean()
        for item in np.unique(items):
            item_means[item] = ratings[items==item].mean()

        self.global_mean = ratings.mean()
        self.user_means = user_means
        self.item_means = item_means

    def estimate(self, u, i):
        """
        return the mean of means estimate
        """

        if u not in self.user_means:
            return(np.mean([self.global_mean,
                            self.item_means[i]]))

        if i not in self.item_means:
            return(np.mean([self.global_mean,
                            self.user_means[u]]))

        return(np.mean([self.global_mean,
                        self.user_means[u],
                        self.item_means[i]]))


if __name__ == "__main__":

    data = Dataset.load_builtin('ml-100k')
    print("\nGlobal Mean...")
    algo = GlobalMean()
    cross_validate(algo, data)

    print("\nMeanOfMeans...")
    algo = MeanofMeans()
    cross_validate(algo, data)
