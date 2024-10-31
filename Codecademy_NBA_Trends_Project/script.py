import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency,pearsonr
import seaborn as sns 
np.set_printoptions(suppress=True, precision = 2)

nba_games = pd.read_csv('c:/Users/Admin/Desktop/Py_project_AI/Codecademy_NBA_Trends_Project/nba_games.csv')
print(nba_games)
knicks_pts_10 = nba_games[nba_games.fran_id=='Knicks'][nba_games.year_id==2010]['pts']
nets_pts_10 = nba_games[nba_games.fran_id=='Nets'][nba_games.year_id==2010]['pts']
knicks_pts_14 = nba_games[nba_games.fran_id=='Knicks'][nba_games.year_id==2014]['pts']
nets_pts_14 = nba_games[nba_games.fran_id=='Nets'][nba_games.year_id==2014]['pts']
diff_means_2010 = knicks_pts_10.mean()-np.mean(nets_pts_10)
diff_means_2014 = knicks_pts_14.mean()-np.mean(nets_pts_14)
plt.hist(knicks_pts_10 , color="blue", label="Knicks",density=True,  alpha=0.5)
plt.hist(nets_pts_10 , color="red", label="Nets",density=True, alpha=0.5)
plt.legend()
plt.show()
plt.close()
plt.hist(knicks_pts_14 , color="blue", label="Knicks",density=True,  alpha=0.5)
plt.hist(nets_pts_14 , color="red", label="Nets",density=True, alpha=0.5)
plt.legend()
plt.show()
plt.close()

sns.boxplot(data=nba_games[nba_games.year_id==2010],x='fran_id',y='pts')
plt.show()
pts_home = nba_games[nba_games.game_location=='H'][nba_games.year_id==2014]['pts']
pts_abroad = nba_games[nba_games.game_location=='A'][nba_games.year_id==2014]['pts']
pts_mean_diff = pts_home.mean() -pts_abroad.mean()
plt.hist(pts_home , color="blue", label="Home",density=True,  alpha=0.5)
plt.hist(pts_abroad , color="red", label="Abroad",density=True, alpha=0.5)
plt.legend()
plt.show()


location_result_freq  = pd.crosstab(nba_games.game_location, nba_games.game_result)
location_result_prop = location_result_freq/len(nba_games)
print(location_result_prop)

chi2,poof,dif,expected = chi2_contingency(location_result_freq)
print(expected)
print(chi2)

point_diff_forecast_corr = pearsonr(nba_games.forecast,nba_games.point_diff)
print(point_diff_forecast_corr)
point_diff_forecast_cov = np.cov(nba_games.forecast,nba_games.point_diff)
print(point_diff_forecast_cov)
plt.scatter(nba_games.forecast,nba_games.point_diff)
plt.xlabel('forecast')
plt.ylabel('point_diff')
plt.show()
fig = plt.figure(figsize=(100,200))
ax=fig.add_subplot(2,1,1)
ax = sns.boxplot(data=nba_games,x='is_playoffs',y='pts')
sx = fig.add_subplot(2,1,2)
ax = plt.hist(pts_home , color="blue", label="Home",density=True,  alpha=0.5)
ax = plt.hist(pts_abroad , color="red", label="Abroad",density=True, alpha=0.5)
ax = fig.add_subplot(2,2,2)
ax = plt.scatter(nba_games.forecast,nba_games.point_diff)
ax = plt.xlabel('forecast')
ax = plt.ylabel('point_diff')
plt.show()