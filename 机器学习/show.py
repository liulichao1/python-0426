import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def show_cost(costs, validation_costs):
    sns.set_style("whitegrid")
    plt.plot(costs)
    plt.plot(validation_costs)
    plt.show()


def read_and_show_aqi():
    aqi_data = pd.read_csv("aqi2.csv")
    sns.set(style='whitegrid', context='notebook')
    cols = ['PM2.5', 'PM10', 'CO', 'No2', 'So2', 'O3']
    sns.pairplot(aqi_data[cols], size=2.5)
    plt.show()

    cm = np.corrcoef(aqi_data[cols].values.T)
    sns.set(font_scale=1.5)
    sns.heatmap(cm, cbar=True, annot=True, square=True,
    fmt='.2f', annot_kws={'size':15}, yticklabels=cols, xticklabels=cols)
    plt.show()
