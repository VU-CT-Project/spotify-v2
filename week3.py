""" Week 3
Steps:
    1.Collect data on the user's listening history, including the energy, danceability, bpm, valence, and acousticness of the songs they have listened to.
    2.Initialize variables to store the average energy, danceability, bpm, valence, and acousticness of the songs the user has listened to. These values will be used to determine the user's preferences.
    3.Iterate through the data on the user's listening history and calculate the average energy, danceability, bpm, valence, and acousticness of the songs they have listened to.
    4.Classify the songs in happy, lounge, calming and party by their valence.
    5.Iterate through the types of songs and find the songs that are similar to the user's preferences.
    6.Print the suggested songs.
"""

import pandas as pd

# Read dataset
data = pd.read_csv("spotify-dataset.csv")

# Initialise the threshold for similarity search
threshold = 10

# Initialise the type of songs
happy = []
party = []
calming = []
lounge = []
types = [happy, party, calming, lounge]

# Initialise variables to store the average energy, danceability, bpm, valence, and acousticness of the songs the user has listened to.
energy = 0
danceability = 0
bpm = 0
valence = 0
acousticness = 0

# Initialise row names for readability
_energy: str = 'Energy- The energy of a song - the higher the value, the more energtic'
_danceability: str = 'Danceability - The higher the value, the easier it is to dance to this song'
_bpm: str = 'Beats.Per.Minute -The tempo of the song'
_valence: str = 'Valence - The higher the value, the more positive mood for the song'
_acousticness: str = 'Acousticness - The higher the value the more acoustic the song is'

_popularity: str = 'Popularity- The higher the value the more popular the song is'

# Iterate through the data on the user's listening history and calculate the average energy, danceability, bpm, valence, and acousticness of the songs they have listened to.
for index, row in data.iterrows():
    energy += row[_energy]
    danceability += row[_danceability]
    bpm += row[_bpm]
    valence += row[_valence]
    acousticness += row[_acousticness]


# Normalize the values
energy //= len(data)
danceability //= len(data)
bpm //= len(data)
valence //= len(data)
acousticness //= len(data)


# Initialise the suggested songs list
suggested_songs = []

# Classify the songs in happy, lounge, calming and party by their valence
for index, row in data.iterrows():
    if row[_valence] > 70:
        party.append(row)
    elif row[_valence] > 50:
        happy.append(row)
    elif row[_valence] > 20:
        lounge.append(row)
    else:
        calming.append(row)
    

# Iterate through the types of songs and find the songs that are similar to the user's preferences
for type in types:
    for song in type:
        if song[_valence] in range(valence - threshold, valence + threshold) \
        and song[_danceability] in range(danceability - threshold, danceability + threshold) \
        and song[_energy] in range(energy - threshold, energy + threshold) \
        and song[_bpm] in range(bpm - threshold, bpm + threshold) \
        and song[_acousticness] in range(acousticness - threshold, acousticness + threshold):
            suggested_songs.append(song)

# Sort the suggested songs by popularity
suggested_songs.sort(key=lambda x: x[_popularity], reverse=True)

# Print the suggested songs
for song in suggested_songs[:5]:
    print(song['title'])