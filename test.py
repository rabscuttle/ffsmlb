# Import
import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser

# Variables
file_name = "FFS MLB Sheet.xlsx"
ffs_teams_list = ['ARI','ATL','BAL','BOS','CHC','CWS','CIN','CLE','COL','DET','HOU','KC','LAA','LAD','MIA','MIL','MIN','NYM','NYY','OAK','PHI','PIT','SD','SF','SEA','STL','TB','TEX','TOR','WAS']

# Splinter
executable_path = {'executable_path': 'c:/bin/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=True)

# FFS Player List
# Import FFS MLB Sheet
# Read Player Names
name_cols = "G"
current_year = "2020"
player_list = []

# Loop through each tab to pull list of player names
for team in ffs_teams_list:

	# Variables
	sheet = pd.read_excel(file_name, sheet_name=team, usecols=name_cols, skiprows=2)
	names = sheet['Player']

	# Remove empty rows
	nan_value = float("NaN")
	names.replace("", nan_value, inplace=True)
	names.dropna(inplace=True)

	# Write progress to console
	print(f"Processing data for {team}")

	# loop through each name in the sheet
	for name in names:

	        # Remove FFS lingo from name (formatting)
		name = name.replace('RV', '')
		name = name.replace('R1', '')
		name = name.replace(team, '')
		name = name.strip()
		entry = {
			"name": name,
			"owner": team
		}
		player_list.append(entry)


# Get Prospects List
url = "https://www.prospects1500.com/top-50-lists-2020/"
browser.visit(url)
html = browser.html
soup = bs(html, 'html.parser')

td = soup.findAll('td')
links = td.findAll('a')
print(links)
