import pandas as pd
import matplotlib.pyplot as plt


class Graph:

    def __init__(self):
        self.df = pd.read_csv('data/responses.csv')

    @classmethod
    def save_plot(cls, name):
        plt.savefig('static/graph/' + name + '.jpg', pad_inches=1, bbox_inches='tight')

    def select_graph(self, result):
        if 'Music_Happy' in result:
            return self.music_happy
        elif 'Music_Lonely' in result:
            return self.music_lonely
        elif 'Happy_Education' in result:
            return self.happy_education
        elif 'Happy_Siblings' in result:
            return self.happy_siblings
        elif 'Music_Speaking' in result:
            return self.music_fear_speaking
        elif 'Music_Storm' in result:
            return self.music_fear_storm
        elif 'Happy_Age' in result:
            return self.happy_age
        elif 'Music_Height' in result:
            return self.music_fear_height
        else:
            return '/static/graph/not_found.png'


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

    @property
    def happy_education(self):
        self.create_plot_happy_education()
        self.save_plot('happy_education')
        return '/static/graph/happy_education.jpg'

    @property
    def happy_siblings(self):
        self.create_plot_happy_siblings()
        self.save_plot('happy_siblings')
        return '/static/graph/happy_siblings.jpg'

    @property
    def happy_age(self):
        self.create_plot_happy_age()
        self.save_plot('happy_age')
        return '/static/graph/happy_age.jpg'

    @property
    def music_fear_speaking(self):
        self.create_plot_fear_of_speaking_music()
        self.save_plot('music_fear_of_speaking')
        return '/static/graph/music_fear_of_speaking.jpg'

    @property
    def music_fear_storm(self):
        self.create_plot_fear_of_storm()
        self.save_plot('music_fear_of_storm')
        return '/static/graph/music_fear_of_storm.jpg'

    @property
    def music_fear_height(self):
        self.create_plot_fear_of_heights()
        self.save_plot('music_fear_of_height')
        return '/static/graph/music_fear_of_height.jpg'

    def create_plot_happy_siblings(self):
        df = self.df
        tab = df.groupby(by='Happiness in life')['Number of siblings'].mean()
        tab.plot.kde()

    def create_plot_happy_age(self):
        df = self.df
        a = df.groupby(by='Age').mean()
        tab = a.loc[:, ['Charity', 'Happiness in life', 'Empathy']]
        tab.plot()

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

    def create_plot_happy_education(self):
        df = self.df
        secondary = df[df['Education'] == 'secondary school']
        primary = df[df['Education'] == 'primary school']
        college = df[df['Education'] == 'college/bachelor degree']
        masters = df[df['Education'] == 'masters degree']
        doctorate = df[df['Education'] == 'doctorate degree']
        a = secondary[['Happiness in life', 'Education']].mean() - 3
        b = primary[['Happiness in life', 'Education']].mean() - 3
        c = college[['Happiness in life', 'Education']].mean() - 3
        d = masters[['Happiness in life', 'Education']].mean() - 3
        e = doctorate[['Happiness in life', 'Education']].mean() - 3
        all_mean = pd.concat([a, b, c, d, e], axis=1)
        tab = all_mean.rename(columns={0: 'Secondary', 1: 'Primary', 2: 'College', 3: 'Masters', 4: 'Doctorate'})
        tab.plot.bar()

    def create_plot_fear_of_speaking_music(self):
        df = self.df
        phobia_public = df[df['Fear of public speaking']>= 4]
        pp_mean = phobia_public.iloc[:,1:18].mean().sort_values(ascending=False)
        phall_mean = df.iloc[:,1:18].mean().sort_values(ascending=False)
        all_pp = pd.concat([pp_mean,phall_mean],axis = 1)
        tab_public = all_pp.rename(columns = {0:'Public speaking fear', 1:'Average'})
        h_var = tab_public[abs(tab_public['Public speaking fear'] - tab_public['Average'])>= 0.1]
        h_var.plot.bar()

    def create_plot_fear_of_storm(self):
        df = self.df
        phobia_storm = df[df['Storm']>= 4]
        ps_mean = phobia_storm.iloc[:,1:18].mean().sort_values(ascending=False)
        phall_mean = df.iloc[:,1:18].mean().sort_values(ascending=False)
        all_pst = pd.concat([ps_mean,phall_mean],axis = 1)
        tab_storm = all_pst.rename(columns = {0:'Fear of storm', 1:'Average'})
        h_var_storm = tab_storm[abs(tab_storm['Fear of storm'] - tab_storm['Average'])>= 0.2]
        h_var_storm.plot.bar()
    
    def create_plot_fear_of_heights(self):
        pass

   