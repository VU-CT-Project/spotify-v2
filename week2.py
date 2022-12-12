

"""

Steps:

1.Read the data from the spotify-dataset.csv file and store it in a variable called data.
2.Iterate over the rows in data and count the number of times the user has listened to each of the three genres of music (pop, rock, and techno).
3.Calculate the percentage of songs listened to for each music genre by dividing the number of songs listened to for that genre by the total number of songs listened to by the user.
4.If the percentage difference between the user's two favorite genres is less than 10%, consider both genres to be equally important to the user.
5.Use the user's favorite genre(s) to suggest 5 songs from that genre.

"""


# Import necessary libraries
import pandas as pd

# Read in data from spotify-dataset.csv file
data = pd.read_csv("spotify-dataset.csv")

# Set threshold for genre importance
threshold = 50

# Initialize a counter for each genre of music into a dictionary
genre_count = {"pop": 0, "rock": 0, "techno": 0}


# Iterate over rows in data
for index, row in data.iterrows():
    # Check the genre of each song and increment the appropriate counter
    for genre in row["the genre of the track"].split(", "):
      if genre in genre_count:
        genre_count[genre] += 1
    
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

