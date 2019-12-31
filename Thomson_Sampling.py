#Thompson Sampling

#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

#importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

#implementing Thompson Sampling
total_users = 10000
total_ads = 10
ads_selected = []
numbers_of_rewards_1 = [0] * total_ads
numbers_of_rewards_0 = [0] * total_ads
total_reward = 0
for n in range(0, total_users):
    max_random = 0
    ad = 0
    for i in range(0, total_ads):
        random_beta = random.betavariate(numbers_of_rewards_1[i]+1, numbers_of_rewards_0[i]+1)
        if random_beta > max_random:
            max_random = random_beta
            ad = i
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    if reward == 1:
        numbers_of_rewards_1[ad] = numbers_of_rewards_1[ad] + 1
    else:
        numbers_of_rewards_0[ad] = numbers_of_rewards_0[ad] + 1
    total_reward = total_reward + reward
    
#visualising
plt.hist(ads_selected)
plt.title('Histogram of Ad selection')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()