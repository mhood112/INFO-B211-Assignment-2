import csv
import numpy as np

# Read the CSV file
file_path = 'players_stats_by_season_full_details.csv' #this is the path to the csv file
#this dictionary will store keys that represent the column names from the csv file and an empty list as the value 
data = {
    'Player': [], #this is the player column
    'Season': [], #this is the season column
    'MIN': [], #this is the minutes column
    'PTS': [], #this is the points column
    'FGM': [], #this is the field goals made column
    'FGA': [], #this is the field goals attempted column
    '3PM': [], #this is the 3-pointers made column
    '3PA': [], #this is the 3-pointers attempted column
    'FTM': [], #this is the free throws made column
    'FTA': [], #this is the free throws attempted column
    'BLK': [], #this is the blocks column
    'STL': [], #this is the steals column
    'GP': [] #this is the games played column
}

try: #try to open the file and read the data
    with open(file_path, 'r') as file: 
        reader = csv.reader(file) #create a csv reader object to iterate through the rows in the csv file
        next(reader)  # Skip the header row
        for row in reader: #this will loop through each row in the csv file starting from the second row
            data['Player'].append(row[3]) #append the player name to the Player list
            data['Season'].append(row[1]) #append the season to the Season list
            data['MIN'].append(float(row[6])) #convert the minutes to a float and append it to the MIN list
            data['PTS'].append(float(row[19])) #convert the points to a float and append it to the PTS list
            data['FGM'].append(float(row[7])) # convert the field goals made to a float and append it to the FGM list
            data['FGA'].append(float(row[8])) #convert the field goals attempted to a float and append it to the FGA list
            data['3PM'].append(float(row[9])) #convert the 3-pointers made to a float and append it to the 3PM list
            data['3PA'].append(float(row[10])) #convert the 3-pointers attempted to a float and append it to the 3PA list
            data['FTM'].append(float(row[11])) #convert the free throws made to a float and append it to the FTM list
            data['FTA'].append(float(row[12])) #convert the free throws attempted to a float and append it to the FTA list
            data['BLK'].append(float(row[18])) #convert the blocks to a float and append it to the BLK list
            data['STL'].append(float(row[17])) #convert the steals to a float and append it to the STL list
            data['GP'].append(float(row[5])) #convert the games played to a float and append it to the GP list
except FileNotFoundError:  #if the file is not found, print an error message and exit the program
    print(f"Error: The file {file_path} was not found.")
    exit(1)
except Exception as e: #if there is an error reading the file, print an error message and exit the program
    print(f"An error occurred while reading the file: {e}")
    exit(1)

try: #try to convert the data to numpy arrays for calculations
    # Convert data to numpy arrays for calculations
    players = np.array(data['Player'])
    seasons = np.array(data['Season'])
    minutes = np.array(data['MIN'], dtype=float)
    points = np.array(data['PTS'], dtype=float)
    fgm = np.array(data['FGM'], dtype=float)
    fga = np.array(data['FGA'], dtype=float)
    tpm = np.array(data['3PM'], dtype=float)
    tpa = np.array(data['3PA'], dtype=float)
    ftm = np.array(data['FTM'], dtype=float)
    fta = np.array(data['FTA'], dtype=float)
    blocks = np.array(data['BLK'], dtype=float)
    steals = np.array(data['STL'], dtype=float)
    games_played = np.array(data['GP'], dtype=float)
except ValueError as e: #if there is a value error, print an error message and exit the program
    print(f"Error: Invalid data format: {e}")
    exit(1)
except Exception as e: #if there is an error, print an error message and exit the program
    print(f"An error occurred while processing the data: {e}")
    exit(1)

# Calculate metrics
try: #try to calculate the metrics
    fg_accuracy = np.divide(fgm, fga, out=np.zeros_like(fgm, dtype=float), where=fga!=0) * 100 #calculate the field goal accuracy in percentage
    tp_accuracy = np.divide(tpm, tpa, out=np.zeros_like(tpm, dtype=float), where=tpa!=0) * 100 #calculate the 3-point accuracy in percentage
    ft_accuracy = np.divide(ftm, fta, out=np.zeros_like(ftm, dtype=float), where=fta!=0) * 100 #calculate the free throw accuracy in percentage
    pts_per_min = np.divide(points, minutes, out=np.zeros_like(points, dtype=float), where=minutes!=0) #calculate the points per minute
    overall_accuracy = np.divide(fgm + tpm + ftm, fga + tpa + fta, out=np.zeros_like(fgm, dtype=float), where=(fga + tpa + fta)!=0) * 100 #calculate the overall accuracy
    blk_per_game = np.divide(blocks, games_played, out=np.zeros_like(blocks, dtype=float), where=games_played!=0) #calculate the blocks per game
    stl_per_game = np.divide(steals, games_played, out=np.zeros_like(steals, dtype=float), where=games_played!=0) #calculate the steals per game
except ZeroDivisionError as e: #if there is a zero division error, print an error message and exit the program
    print(f"Error: Division by zero encountered in calculations: {e}")
    exit(1)
except Exception as e: #if there is an error, print an error message and exit the program
    print(f"An error occurred during calculations: {e}")
    exit(1)

# Combine results into a list of dictionaries
results = [] #this list will store the results of the calculations
for player, season, fg_acc, tp_acc, ft_acc, ppm, oa, bpg, spg in zip(players, seasons, fg_accuracy, tp_accuracy, ft_accuracy, pts_per_min, overall_accuracy, blk_per_game, stl_per_game):
    #this will loop through each player and season and append the results to the results list
    results.append({
        'Player': player,
        'Season': season,
        'FG_accuracy': f"{round(fg_acc, 2)}%",  # Round to 2 decimal places and add percent sign
        '3P_accuracy': f"{round(tp_acc, 2)}%",  # Round to 2 decimal places and add percent sign
        'FT_accuracy': f"{round(ft_acc, 2)}%",  # Round to 2 decimal places and add percent sign
        'PTS_per_MIN': round(ppm, 2),           # Round to 2 decimal places
        'Overall_accuracy': f"{round(oa, 2)}%", # Round to 2 decimal places and add percent sign
        'BLK_per_game': round(bpg, 2),          # Round to 2 decimal places
        'STL_per_game': round(spg, 2)           # Round to 2 decimal places
    })

# Write the results to a new CSV file
output_file_path = 'player_accuracy_metrics.csv'

try: #try to write the results to a csv file
    with open(output_file_path, 'w', newline='') as file:
        #write the results to a csv file
        writer = csv.DictWriter(file, fieldnames=['Player', 'Season', 'FG_accuracy', '3P_accuracy', 'FT_accuracy', 'PTS_per_MIN', 'Overall_accuracy', 'BLK_per_game', 'STL_per_game'])
        writer.writeheader()
        writer.writerows(results)
    print(f"Results written to {output_file_path}")
except Exception as e: #if there is an error, print an error message and exit the program
    print(f"An error occurred while writing the results to the file: {e}")
    exit(1)

# Create a list of the top 100 players for each metric
metrics = {
    'FG_accuracy': fg_accuracy,
    '3P_accuracy': tp_accuracy,
    'FT_accuracy': ft_accuracy,
    'PTS_per_MIN': pts_per_min,
    'Overall_accuracy': overall_accuracy,
    'BLK_per_game': blk_per_game,
    'STL_per_game': stl_per_game
}

top_100_players = {} #this dictionary will store the top 100 players for each metric

for metric, values in metrics.items():
    #sort the values in descending order and get the top 100 players for each metric
    sorted_indices = np.argsort(values)[::-1][:100] 
    top_100_players[metric] = [(players[i], seasons[i], values[i]) for i in sorted_indices] #store the top 100 players in the dictionary

# Write the top 100 players for each metric to a new CSV file
top_100_output_file_path = 'top_100_players_metrics.csv'

try: #try to write the top 100 players to a csv file
    with open(top_100_output_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Metric', 'Player', 'Season', 'Value'])
        
        for metric, top_players in top_100_players.items():
            #write the top 100 players for each metric to the csv file
            writer.writerow([])  # Add an empty row for separation
            writer.writerow([metric])  # Add the metric as a header
            for player in top_players:
                #write the player name, season, and value to the csv file
                value = f"{round(player[2], 2)}%" if 'accuracy' in metric or 'per_game' in metric else round(player[2], 2)
                writer.writerow([metric, player[0], player[1], value])
    print(f"Top 100 players for each metric written to {top_100_output_file_path}")
except Exception as e: #if there is an error, print an error message and exit the program
    print(f"An error occurred while writing the top 100 players to the file: {e}")
    exit(1)
