import pandas as pd
import matplotlib.pyplot as plt


class Graph:

    def __init__(self):
        self.df = pd.read_csv('data/responses.csv')

    @property
    def music_on_loneliness(self):
        lonely5 = self.df[self.df['Loneliness'] == 5]
        lonely1 = self.df[self.df['Loneliness'] == 1]
        ln1_mean = lonely1.iloc[:, 2:19].mean().sort_values(ascending=False)
        average_mean = self.df.iloc[:, 2:19].mean().sort_values(ascending=False)
        ln5_mean = lonely5.iloc[:, 2:19].mean().sort_values(ascending=False)
        all_mean = pd.concat([ln1_mean, average_mean, ln5_mean], axis=1)
        tab = all_mean.rename(columns={0: 'Loneliness1', 1: 'Average', 2: 'Loneliness5'})
        h_var = tab[abs(tab['Loneliness1'] - tab['Loneliness5']) > 0.1]
        h_var.plot.bar()
        plt.savefig('static/graph/tab_lonely.jpg', pad_inches=1, bbox_inches='tight')

        return '/static/graph/tab_lonely.jpg'


