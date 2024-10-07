#For Height
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_players = pd.read_csv('players.csv')

print(df_players.head())

print(df_players.columns)

sns.boxplot(df_players['height'])

plt.show()

#For Weight
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_players = pd.read_csv('players.csv')

print(df_players.head())

print(df_players.columns)

sns.boxplot(df_players['weight'])

plt.show()


###################################

import numpy as np
import pandas as pd

coaches = pd.read_csv('coaches.csv', delimiter=",")
teams = pd.read_csv('teams.csv', delimiter=",")

def identify_outliers(data_column, threshold=2):
    mean_value = np.mean(data_column)
    std_dev = np.std(data_column)
    z_scores = [(x - mean_value) / std_dev for x in data_column]
    outliers = [data_column[i] for i, z in enumerate(z_scores) if abs(z) > threshold]
    return outliers

outliers_won = identify_outliers(coaches['won'])
outliers_lost = identify_outliers(coaches['lost'])
outliers_post_wins = identify_outliers(coaches['post_wins'])
outliers_post_losses = identify_outliers(coaches['post_losses'])

print("\nOutliers for Coaches Dataset:\n")
print("Outliers Won:", outliers_won)
print("Outliers Lost:", outliers_lost)
print("Outliers Post Wins:", outliers_post_wins)
print("Outliers Post Losses:", outliers_post_losses)

outliers_o_fgm = identify_outliers(teams['o_fgm'])
outliers_o_fga = identify_outliers(teams['o_fga'])
outliers_o_ftm = identify_outliers(teams['o_ftm'])
outliers_o_fta = identify_outliers(teams['o_fta'])
outliers_o_3pm = identify_outliers(teams['o_3pm'])
outliers_o_3pa = identify_outliers(teams['o_3pa'])
outliers_o_oreb = identify_outliers(teams['o_oreb'])
outliers_o_dreb = identify_outliers(teams['o_dreb'])
outliers_o_reb = identify_outliers(teams['o_reb'])
outliers_o_asts = identify_outliers(teams['o_asts'])
outliers_o_pf = identify_outliers(teams['o_pf'])
outliers_o_stl = identify_outliers(teams['o_stl'])
outliers_o_to = identify_outliers(teams['o_to'])
outliers_o_blk = identify_outliers(teams['o_blk'])
outliers_o_pts = identify_outliers(teams['o_pts'])
outliers_d_fgm = identify_outliers(teams['d_fgm'])
outliers_d_fga = identify_outliers(teams['d_fga'])
outliers_d_ftm = identify_outliers(teams['d_ftm'])
outliers_d_fta = identify_outliers(teams['d_fta'])

print("\nOutliers for Teams Dataset:\n")
print("Outliers o_fgm:", outliers_o_fgm)
print("Outliers o_fga:", outliers_o_fga)
print("Outliers o_ftm:", outliers_o_ftm)
print("Outliers o_fta:", outliers_o_fta)
print("Outliers o_3pm:", outliers_o_3pm)
print("Outliers o_3pa:", outliers_o_3pa)
print("Outliers o_oreb:", outliers_o_oreb)
print("Outliers o_dreb:", outliers_o_dreb)
print("Outliers o_reb:", outliers_o_reb)
print("Outliers o_asts:", outliers_o_asts)
print("Outliers o_pf:", outliers_o_pf)
print("Outliers o_stl:", outliers_o_stl)
print("Outliers o_to:", outliers_o_to)
print("Outliers o_blk:", outliers_o_blk)
print("Outliers o_pts:", outliers_o_pts)
print("Outliers d_fgm:", outliers_d_fgm)
print("Outliers d_fga:", outliers_d_fga)
print("Outliers d_ftm:", outliers_d_ftm)
print("Outliers d_fta:", outliers_d_fta)
