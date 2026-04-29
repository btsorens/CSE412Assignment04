import csv
import random
from faker import Faker

fakeDataGenerator = Faker()

NUMBER_OF_TUPLES = 10000

def generateDataForDatabase():
    generatePlayersCSV()
    generateGamestatsCSV()
    return

def generatePlayersCSV():
    #stats only support offensive positions
    availablePositions = ['QB', 'RB', 'WR', 'TE']

    with open('players.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        #match players schema
        writer.writerow(['player_id', 'first_name', 'last_name', 'date_of_birth', 
                         'hometown', 'state', 'position', 'height', 'weight', 'jersey_number'])
        
        for i in range(1, NUMBER_OF_TUPLES + 1):
            writer.writerow([
                i,                                          # player_id
                fakeDataGenerator.first_name(),             # first_name
                fakeDataGenerator.last_name(),              # last_name
                fakeDataGenerator.date_of_birth(minimum_age=18, maximum_age=40), # DOB
                fakeDataGenerator.city(),                   # hometown
                fakeDataGenerator.state_abbr(),             # state (2 chars)
                random.choice(availablePositions),          # position
                random.randint(68, 80),                     # height (inches)
                random.randint(150, 300),                   # weight (lbs)
                random.randint(0, 99)                       # jersey_number
            ])

    print(f"Successful generation of players.csv with {NUMBER_OF_TUPLES} tuples.")

def generateGamestatsCSV():
    with open('gamestats.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        #match gamestats schema
        writer.writerow(['stat_id', 'player_id', 'date_of_game', 'stadium_name', 
                         'rush_yards', 'num_rushes', 'rec_yards', 'num_receptions', 
                         'points', 'snaps_played'])
        
        for i in range(1, NUMBER_OF_TUPLES + 1):
            writer.writerow([
                i,                                                  # stat_id
                random.randint(1, NUMBER_OF_TUPLES),                # player_id (foreign key)
                fakeDataGenerator.date_this_decade(),               # date_of_game
                fakeDataGenerator.company() + " Stadium",           # stadium_name
                random.randint(-5, 150),                            # rush_yards
                random.randint(0, 30),                              # num_rushes
                random.randint(0, 200),                             # rec_yards
                random.randint(0, 15),                              # num_receptions
                random.choice([0, 3, 6, 7, 12, 14, 17, 18, 21, 24, 28]),    # points
                random.randint(1, 80)                               # snaps_played
            ])
    
    print(f"Successful generation of gamestats.csv with {NUMBER_OF_TUPLES} tuples.")




if __name__ == "__main__":
    generateDataForDatabase()