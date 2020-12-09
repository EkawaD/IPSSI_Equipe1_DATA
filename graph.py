import pandas as pd
import matplotlib.pyplot as plt


class Graph:

    def __init__(self):
        self.df = pd.read_csv('data/responses.csv')

    @classmethod
    def save_plot(cls, name):
        plt.savefig('static/graph/' + name + '.jpg', pad_inches=1, bbox_inches='tight')

    @property
    def music_lonely(self):
        self.create_plot_music_lonely()
        self.save_plot('music_lonely')
        return '/static/graph/music_lonely.jpg'

    @property
    def music_happy(self):
        self.create_plot_music_happy()
        self.save_plot('music_happy')
        return '/static/graph/music_happy.jpg'

    def create_plot_music_lonely(self):
        lonely5 = self.df[self.df['Loneliness'] == 5]
        lonely1 = self.df[self.df['Loneliness'] == 1]
        ln1_mean = lonely1.iloc[:, 2:19].mean().sort_values(ascending=False)
        average_mean = self.df.iloc[:, 2:19].mean().sort_values(ascending=False)
        ln5_mean = lonely5.iloc[:, 2:19].mean().sort_values(ascending=False)
        all_mean = pd.concat([ln1_mean, average_mean, ln5_mean], axis=1)
        tab = all_mean.rename(columns={0: 'Loneliness1', 1: 'Average', 2: 'Loneliness5'})
        h_var = tab[abs(tab['Loneliness1'] - tab['Loneliness5']) > 0.1]
        h_var.plot.bar()

    def create_plot_music_happy(self):
        df = self.df
        not_happy = df[df['Happiness in life'] <= 2]
        happy = df[df['Happiness in life'] >= 4]
        not_hp_mean = not_happy.iloc[:, 2:19].mean().sort_values(ascending=False)
        hp_mean = happy.iloc[:, 2:19].mean().sort_values(ascending=False)
        all_mean = df.iloc[:, 2:19].mean().sort_values(ascending=False)
        all_mean = pd.concat([not_hp_mean, all_mean, hp_mean], axis=1)
        tab = all_mean.rename(columns={0: 'Not Happy', 1: 'Average', 2: 'Happy'})
        h_var = tab[abs(tab['Not Happy'] - tab['Happy']) >= 0.3]
        h_var.sort_values('Average', ascending=False).plot.bar()