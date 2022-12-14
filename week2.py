""" Week 2
Steps:
    1.Read the data from the spotify-dataset.csv file and store it in a variable called data.
    2.Iterate over the rows in data and count the number of times the user has listened to each of the three genres of music (pop, rock, and techno).
    3.Calculate the percentage of songs listened to for each music genre by dividing the number of songs listened to for that genre by the total number of songs listened to by the user.
    4.If the percentage difference between the user's two favorite genres is less than 10%, consider both genres to be equally important to the user.
    5.Use the user's favorite genre(s) to suggest 5 songs from that genre.
"""

import pandas as pd

# read dataset
data = pd.read_csv("spotify-dataset.csv")

# Set threshold for genre importance
threshold = 50

# counter for each genre of music
genre_count = {"pop": 0, "rock": 0, "techno": 0}

# subgenres of pop, rock, and techno
pop_subgenres = [
    'electro',
    'danish pop',
    'moroccan pop',
    'colombian pop',
    'candy pop',
    'canadian pop',
    'australian pop',
    'chicago rap',
    'acoustic pop',
    'baroque pop',
    'atl hip hop',
    'hip hop',
    'folk-pop',
    'french indie pop',
    'detroit hip hop',
    'dance pop',
    'canadian hip hop',
    'art pop',
    'pop',
    'barbadian pop',
    'hip pop',
    'metropopolis',
    'hollywood',
    'tropical house',
    'escape room',
    'indie pop',
    'latin',
    'british soul',
    'electropop',
    'irish singer-songwriter',
    'canadian latin',
    'boy band',
    'australian hip hop',
    'australian dance',
    'house',
]

rock_subgenres = [
    'alaska indie',
    'permanent wave',
    'canadian contemporary r&b',
    'contemporary country',
    'celtic rock',
    'alternative r&b',
]

techno_subgenres = [
    'complextro',
    'electronic trap',
    'electro house',
    'belgian edm',
    'big room',
    'neo mellow',
    'brostep',
    'edm',
    'downtempo',
]

# Take into account the subgenres of pop, rock, and techno
for index, row in data.iterrows():
    # Check the genre of each song and increment the appropriate counter
    for genre in row["the genre of the track"].split(", "):
      if genre in pop_subgenres:
        genre_count["pop"] += 1
      if genre in rock_subgenres:
        genre_count["rock"] += 1
      if genre in techno_subgenres:
        genre_count["techno"] += 1

# Initialize variable to store total number of songs listened to by user
total_songs = 0

# Calculate total number of songs listened to by user 
for genre, count in genre_count.items():
    total_songs += count

# Calculate percentage of songs listened to for each genre 
for genre, count in genre_count.items():
    genre_count[genre] = count / total_songs * 100

# Determine user's favorite genre(s)
favorite_genres = []

for genre, percent in genre_count.items():
    # Check if genre is user's favorite genre
    if percent >= threshold:
        favorite_genres.append(genre)
    # Check if genre is tied for user's favorite genre
    elif percent >= threshold - 10:
        favorite_genres.append(genre)

# Initialize list to store suggested songs
suggested_songs = []

# Iterate over rows in data
for index, row in data.iterrows():
    # Check if song's genre matches user's favorite genre(s)
    if row["the genre of the track"] in favorite_genres:
        # Add song to suggested_songs list if the song hasn't already been suggested
        if row["title"] not in suggested_songs:
            suggested_songs.append(row["title"])
        # Stop suggesting songs once 5 songs have been suggested
        if len(suggested_songs) == 5:
            break

# Print suggested songs
print(suggested_songs)
