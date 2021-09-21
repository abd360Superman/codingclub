player_runs = {'Rohit Sharma': 264,
               'AB de Villiers': 149,
               'MS Dhoni': 183,
               'Chris Gayle': 175,
               'Virat Kohli': 113}

#Adding to dict
player_runs['Donald Bradman'] = 334
print(player_runs)

#Removing from dict
del player_runs['Virat Kohli']
print(player_runs)

#Replacing values from dict
player_runs['AB de Villiers'] = 176
print(player_runs)

#Length of Dict
print(len(player_runs))

#Get all keys
player_names = player_runs.keys()
print(player_names)

#Get all values
player_runs_arr = player_runs.values()
print(player_runs_arr)
