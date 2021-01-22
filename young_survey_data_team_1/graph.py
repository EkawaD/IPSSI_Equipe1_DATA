import pandas as pd
import matplotlib.pyplot as plt


class Graph:
    '''
        Chaque propriété créé un graph à partir des données de 'data/responses.csv', sauvegarde le graphique en tant qu'image puis renvoi le chemin vers cette image
    '''


    #initialise la DATAFRAME initiale
    def __init__(self):
        self.df = pd.read_csv('data/responses.csv')
        self.comment = ''

    # sauvegarde le dernier plot créé en tant qu'image .jpg
    @classmethod
    def save_plot(cls, name):
        plt.savefig('static/graph/' + name + '.jpg', pad_inches=1, bbox_inches='tight')

    # renvoie la bonne property en fonction du choix de l'utilisateur @return 'str': path to image file
    def select_graph(self, result):
        if 'Music_Happy' in result:
            self.comment = 'Les personnes heureuses écoute majoritairement du Reggae, de la Dance, du Latino. A contrario, le Rock, les musiques Alternatives et le Metal semble plus lié à des personnes qui se disent moins heureuse'
            return self.music_happy
        elif 'Music_Lonely' in result:
            self.comment = 'Certaines musiques comme le Rock, le classique ou l\'alternative sont bien plus représenté pour les personnes se déclarant se sentir seul. A l\'inverse la Country, la Folk, la Latino ou le Reggae sont moins représenté chez cette catégorie de personne'
            return self.music_lonely
        elif 'Happy_Education' in result:
            self.comment='Il vautdrait mieux qu\'on arrête nos études maintenant :)'
            return self.happy_education
        elif 'Happy_Siblings' in result:
            self.comment='Les personnes ayant entre 1 et 2 frère ou soeur semble plus heureuse que la moyenne'
            return self.happy_siblings
        elif 'Music_Speaking' in result:
            self.comment='Les slovaques qui écoutent de la Folk semble moins timide que la moyenne'
            return self.music_fear_speaking
        elif 'Music_Storm' in result:
            self.comment='Les slovaques qui écoutent de la pop semblent avoir plus peur des orages que les autres'
            return self.music_fear_storm
        elif 'Happy_Age' in result:
            self.comment='Les slovaques sont visiblement plus heureux vers 29ans mais c\'est aussi les personnes qui semblement le moins charitable !! A l\'inverse vers 25 ans les slovaques semblent plus empathique et charitable mais bien moins heureux....'
            return self.happy_age
        elif 'Music_Height' in result:
            self.comment='Les slovaques qui écoutent du Musical semble avoir moins peur de la hauteur... Un lien avec l\'opéra ??'
            return self.music_fear_height
        elif 'Happy_Happy' in result:
            self.comment=' Les jeunes slovaques sont en majorité heureux ! Il y a une forte proportion de réponse 4'
            return self.Happiness_in_life
        else:
            return '/static/graph/not_found.png'


    # @return 'str': path to music_lonely.jpg
    @property
    def music_lonely(self):
        lonely5 = self.df[self.df['Loneliness'] == 5]
        lonely1 = self.df[self.df['Loneliness'] == 1]
        ln1_mean = lonely1.iloc[:, 2:19].mean().sort_values(ascending=False)
        average_mean = self.df.iloc[:, 2:19].mean().sort_values(ascending=False)
        ln5_mean = lonely5.iloc[:, 2:19].mean().sort_values(ascending=False)
        all_mean = pd.concat([ln1_mean, average_mean, ln5_mean], axis=1)
        tab = all_mean.rename(columns={0: 'Loneliness1', 1: 'Average', 2: 'Loneliness5'})
        h_var = tab[abs(tab['Loneliness1'] - tab['Loneliness5']) > 0.1]
        h_var.plot.bar()
        self.save_plot('music_lonely')
        return '/static/graph/music_lonely.jpg'

    # @return 'str': path to music_happy.jpg
    @property
    def music_happy(self):
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
        self.save_plot('music_happy')
        return '/static/graph/music_happy.jpg'

    # @return 'str': path to happy_education.jpg
    @property
    def happy_education(self):
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
        self.save_plot('happy_education')
        return '/static/graph/happy_education.jpg'

    # @return 'str': path to happy_siblings.jpg
    @property
    def happy_siblings(self):
        df = self.df
        tab = df.groupby(by='Happiness in life')['Number of siblings'].mean()
        tab.plot.kde()
        self.save_plot('happy_siblings')
        return '/static/graph/happy_siblings.jpg'

    # @return 'str': path to happy_age.jpg
    @property
    def happy_age(self):
        df = self.df
        a = df.groupby(by='Age').mean()
        tab = a.loc[:, ['Charity', 'Happiness in life', 'Empathy']]
        tab.plot()
        self.save_plot('happy_age')
        return '/static/graph/happy_age.jpg'


    # @return 'str': path to music_fear_of_speaking.jpg
    @property
    def music_fear_speaking(self):
        df = self.df
        phobia_public = df[df['Fear of public speaking']>= 4]
        pp_mean = phobia_public.iloc[:,1:18].mean().sort_values(ascending=False)
        phall_mean = df.iloc[:,1:18].mean().sort_values(ascending=False)
        all_pp = pd.concat([pp_mean,phall_mean],axis = 1)
        tab_public = all_pp.rename(columns = {0:'Public speaking fear', 1:'Average'})
        h_var = tab_public[abs(tab_public['Public speaking fear'] - tab_public['Average'])>= 0.1]
        h_var.plot.bar()
        self.save_plot('music_fear_of_speaking')
        return '/static/graph/music_fear_of_speaking.jpg'

    # @return 'str': path to music_fear_of_storm.jpg
    @property
    def music_fear_storm(self):
        df = self.df
        phobia_storm = df[df['Storm']>= 4]
        ps_mean = phobia_storm.iloc[:,1:18].mean().sort_values(ascending=False)
        phall_mean = df.iloc[:,1:18].mean().sort_values(ascending=False)
        all_pst = pd.concat([ps_mean,phall_mean],axis = 1)
        tab_storm = all_pst.rename(columns = {0:'Fear of storm', 1:'Average'})
        h_var_storm = tab_storm[abs(tab_storm['Fear of storm'] - tab_storm['Average'])>= 0.2]
        h_var_storm.plot.bar()
        self.save_plot('music_fear_of_storm')
        return '/static/graph/music_fear_of_storm.jpg'

    # @return 'str': path to music_fear_of_height.jpg
    @property
    def music_fear_height(self):
        df = self.df
        phobia_heights = df[df['Heights']>= 4]
        ph_mean = phobia_heights.iloc[:,1:18].mean().sort_values(ascending=False)
        phall_mean = df.iloc[:,1:18].mean().sort_values(ascending=False)
        all_ph = pd.concat([ph_mean,phall_mean],axis = 1)
        tab_heights = all_ph.rename(columns = {0:'Fear of heights', 1:'Average'})
        h_var_heights = tab_heights[abs(tab_heights['Fear of heights'] - tab_heights['Average'])>= 0.1]
        h_var_heights.plot.bar()
        self.save_plot('music_fear_of_height')
        return '/static/graph/music_fear_of_height.jpg'


    #diagramme à secteurs - comptage du bien-être
    @property
    def Happiness_in_life(self):
        df = self.df
        df['Happiness in life'].value_counts().plot.pie()
        self.save_plot('happiness_in_life')
        return '/static/graph/happiness_in_life.jpg'