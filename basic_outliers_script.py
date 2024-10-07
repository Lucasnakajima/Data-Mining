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
coaches = pd.read_csv('coaches.csv', delimiter=",")
teams = pd.read_csv('teams.csv', delimiter=",")

# Calculate the mean and standard deviation
mean_won = np.mean(coaches['won'])
std_dev_won = np.std(coaches['won'])
mean_lost = np.mean(coaches['lost'])
std_dev_lost = np.std(coaches['lost'])
mean_post_wins = np.mean(coaches['post_wins'])
std_dev_post_wins = np.std(coaches['post_wins'])
mean_post_losses = np.mean(coaches['post_losses'])
std_dev_post_losses = np.std(coaches['post_losses'])

# Calculate the z-scores for each value
z_scores_won = [(x - mean_won) / std_dev_won for x in coaches['won']]
z_scores_lost = [(x - mean_lost) / std_dev_lost for x in coaches['lost']]
z_scores_post_wins = [(x - mean_post_wins) / std_dev_post_wins for x in coaches['post_wins']]
z_scores_post_losses = [(x - mean_post_losses) / std_dev_post_losses for x in coaches['post_losses']]

# Define a threshold for identifying outliers
threshold = 2  # You can adjust this value based on your needs

# Identify outliers with z-scores exceeding the threshold
outliers_won = [coaches['won'][i] for i, z in enumerate(z_scores_won) if abs(z) > threshold]
outliers_lost = [coaches['lost'][i] for i, z in enumerate(z_scores_lost) if abs(z) > threshold]
outliers_post_wins = [coaches['post_wins'][i] for i, z in enumerate(z_scores_post_wins) if abs(z) > threshold]
outliers_post_losses = [coaches['post_losses'][i] for i, z in enumerate(z_scores_post_losses) if abs(z) > threshold]

print("Coaches Dataset Outliers")
print("Outliers Won:", outliers_won)
print("Outliers Lost:", outliers_lost)
print("Outliers Post Wins:", outliers_post_wins)
print("Outliers Post Losses:", outliers_post_losses)

# Calculate the mean and standard deviation
mean_o_fgm = np.mean(teams['o_fgm'])
std_dev_o_fgm = np.std(teams['o_fgm'])
mean_o_fga = np.mean(teams['o_fga'])
std_dev_o_fga = np.std(teams['o_fga'])
mean_o_ftm = np.mean(teams['o_ftm'])
std_dev_o_ftm = np.std(teams['o_ftm'])
mean_o_fta = np.mean(teams['o_fta'])
std_dev_o_fta = np.std(teams['o_fta'])
mean_o_3pm = np.mean(teams['o_3pm'])
std_dev_o_3pm = np.std(teams['o_3pm'])
mean_o_3pa = np.mean(teams['o_3pa'])
std_dev_o_3pa = np.std(teams['o_3pa'])
mean_o_oreb = np.mean(teams['o_oreb'])
std_dev_o_oreb = np.std(teams['o_oreb'])
mean_o_dreb = np.mean(teams['o_dreb'])
std_dev_o_dreb = np.std(teams['o_dreb'])
mean_o_reb = np.mean(teams['o_reb'])
std_dev_o_reb = np.std(teams['o_reb'])
mean_o_asts = np.mean(teams['o_asts'])
std_dev_o_asts = np.std(teams['o_asts'])
mean_o_pf = np.mean(teams['o_pf'])
std_dev_o_pf = np.std(teams['o_pf'])
mean_o_stl = np.mean(teams['o_stl'])
std_dev_o_stl = np.std(teams['o_stl'])
mean_o_to = np.mean(teams['o_to'])
std_dev_o_to = np.std(teams['o_to'])
mean_o_blk = np.mean(teams['o_blk'])
std_dev_o_blk = np.std(teams['o_blk'])
mean_o_pts = np.mean(teams['o_pts'])
std_dev_o_pts = np.std(teams['o_pts'])
mean_d_fgm = np.mean(teams['d_fgm'])
std_dev_d_fgm = np.std(teams['d_fgm'])
mean_d_fga = np.mean(teams['d_fga'])
std_dev_d_fga = np.std(teams['d_fga'])
mean_d_ftm = np.mean(teams['d_ftm'])
std_dev_d_ftm = np.std(teams['d_ftm'])
mean_d_fta = np.mean(teams['d_fta'])
std_dev_d_fta = np.std(teams['d_fta'])

# Calculate the z-scores for each value
z_scores_o_fgm = [(x - mean_o_fgm) / std_dev_o_fgm for x in teams['o_fgm']]
z_scores_o_fga = [(x - mean_o_fga) / std_dev_o_fga for x in teams['o_fga']]
z_scores_o_ftm = [(x - mean_o_ftm) / std_dev_o_ftm for x in teams['o_ftm']]
z_scores_o_fta = [(x - mean_o_fta) / std_dev_o_fta for x in teams['o_fta']]
z_scores_o_3pm = [(x - mean_o_3pm) / std_dev_o_3pm for x in teams['o_3pm']]
z_scores_o_3pa = [(x - mean_o_3pa) / std_dev_o_3pa for x in teams['o_3pa']]
z_scores_o_oreb = [(x - mean_o_oreb) / std_dev_o_oreb for x in teams['o_oreb']]
z_scores_o_dreb = [(x - mean_o_dreb) / std_dev_o_dreb for x in teams['o_dreb']]
z_scores_o_reb = [(x - mean_o_reb) / std_dev_o_reb for x in teams['o_reb']]
z_scores_o_asts = [(x - mean_o_asts) / std_dev_o_asts for x in teams['o_asts']]
z_scores_o_pf = [(x - mean_o_pf) / std_dev_o_pf for x in teams['o_pf']]
z_scores_o_stl = [(x - mean_o_stl) / std_dev_o_stl for x in teams['o_stl']]
z_scores_o_to = [(x - mean_o_to) / std_dev_o_to for x in teams['o_to']]
z_scores_o_blk = [(x - mean_o_blk) / std_dev_o_blk for x in teams['o_blk']]
z_scores_o_pts = [(x - mean_o_pts) / std_dev_o_pts for x in teams['o_pts']]
z_scores_d_fgm = [(x - mean_d_fgm) / std_dev_d_fgm for x in teams['d_fgm']]
z_scores_d_fga = [(x - mean_d_fga) / std_dev_d_fga for x in teams['d_fga']]
z_scores_d_ftm = [(x - mean_d_ftm) / std_dev_d_ftm for x in teams['d_ftm']]
z_scores_d_fta = [(x - mean_d_fta) / std_dev_d_fta for x in teams['d_fta']]

# Define a threshold for identifying outliers
threshold = 2  # You can adjust this value based on your needs

# Identify outliers with z-scores exceeding the threshold
outliers_o_fgm = [teams['o_fgm'][i] for i, z in enumerate(z_scores_o_fgm) if abs(z) > threshold]
outliers_o_fga = [teams['o_fga'][i] for i, z in enumerate(z_scores_o_fga) if abs(z) > threshold]
outliers_o_ftm = [teams['o_ftm'][i] for i, z in enumerate(z_scores_o_ftm) if abs(z) > threshold]
outliers_o_fta = [teams['o_fta'][i] for i, z in enumerate(z_scores_o_fta) if abs(z) > threshold]
outliers_o_3pm = [teams['o_3pm'][i] for i, z in enumerate(z_scores_o_3pm) if abs(z) > threshold]
outliers_o_3pa = [teams['o_3pa'][i] for i, z in enumerate(z_scores_o_3pa) if abs(z) > threshold]
outliers_o_oreb = [teams['o_oreb'][i] for i, z in enumerate(z_scores_o_oreb) if abs(z) > threshold]
outliers_o_dreb = [teams['o_dreb'][i] for i, z in enumerate(z_scores_o_dreb) if abs(z) > threshold]
outliers_o_reb = [teams['o_reb'][i] for i, z in enumerate(z_scores_o_reb) if abs(z) > threshold]
outliers_o_asts = [teams['o_asts'][i] for i, z in enumerate(z_scores_o_asts) if abs(z) > threshold]
outliers_o_pf = [teams['o_pf'][i] for i, z in enumerate(z_scores_o_pf) if abs(z) > threshold]
outliers_o_stl = [teams['o_stl'][i] for i, z in enumerate(z_scores_o_stl) if abs(z) > threshold]
outliers_o_to = [teams['o_to'][i] for i, z in enumerate(z_scores_o_to) if abs(z) > threshold]
outliers_o_blk = [teams['o_blk'][i] for i, z in enumerate(z_scores_o_blk) if abs(z) > threshold]
outliers_o_pts = [teams['o_pts'][i] for i, z in enumerate(z_scores_o_pts) if abs(z) > threshold]
outliers_d_fgm = [teams['d_fgm'][i] for i, z in enumerate(z_scores_d_fgm) if abs(z) > threshold]
outliers_d_fga = [teams['d_fga'][i] for i, z in enumerate(z_scores_d_fga) if abs(z) > threshold]
outliers_d_ftm = [teams['d_ftm'][i] for i, z in enumerate(z_scores_d_ftm) if abs(z) > threshold]
outliers_d_fta = [teams['d_fta'][i] for i, z in enumerate(z_scores_d_fta) if abs(z) > threshold]

print("Teams Dataset Outliers")
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
