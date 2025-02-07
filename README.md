# INFO-B211-Assignment-2

This project is designed to analyze player statistics from a CSV file containing data on various basketball players across different seasons. The analysis includes calculating various metrics such as field goal accuracy, three-point accuracy, free throw accuracy, points per minute, overall shooting accuracy, blocks per game, and steals per game. Additionally, the project identifies the top 100 players for each of these metrics and writes the results to new CSV files for easy reference.

## File Structure

  - import - csv
  - import - numpy as np
  - input - CSV file players_stats_by_season_full_details.csv
  - outputted - player_accuracy_metrics.csv - for calculated metrics for each player
  - outputted - top_100_players_metrics.csv - contains top 100 players for each metric

## Class Design and Implementation

There are no classes within this project. Instead, there are functions and other programming techniques used.

### Program Explanation

#### Importing necessary libraires.
  - CSV - Allows the programs to read from and write to CSV files.
  - NumPy - This library allows for numerical computations needed in this program.

#### Defining the File Path, Data Structure
  - file_path - this is the path for the CSV that has all the data on the players
  - data - this is a dictionary where each key represents a column in the CSV defined in the file_path. The values start off as an empty list and will store data later. 

#### Reading the CSV File
  - This block of code will read the CSV, and append the relevent data to the corresponding lists in the data dictionary made previously 

#### Converting Data to NumPy Arrays
  - This block of code will convert our lists in the data dictionary to NumPy arrays for numerical computations used later

#### Calculating Metrics
  - This block of code calcuates our metrics, below,  that we will need using the NumPy operations.
      - field goal accuracy
      - three - point accuracy
      - free throw accuracy
      - points per minute
      - overall shooting accuracy
      - blocks per game
      - steals per game

#### Combining Results into a List of Dictionaries
  - This combines the calculated metrics from earlier into a list of dictionaries. These dictionaries represent the player statistics for a particular season

#### Writing the Results to a New CSV File
  - This block writes the results from the last block into a new CSV file

#### Creating a List of the Top 100 players for Each Metric
  - This block of code creates a list of the top 100 players for each metric by sorting the values in descending order.

#### Writing the Top 100 Players for Each Metric to a New CSV
  - This block writes the top 100 players for each metric into a new CSV named, top_100_players_metrics.csv. It will add an empty row between each metric as well as the headers too

## Limitations
  - This program does no handle any missing data, so it may result in an error; however, the provided CSV does not have any empty fields as they have a default of zero.
  - This program also assumes that this CSV is in the correct order and is formed well.

## Conclusion
This project provides a comprehensive analysis of player statistics from a CSV file, including calculating various metrics and identifying the top 100 players for each metric. The results are written to new CSV files for easy reference. 
