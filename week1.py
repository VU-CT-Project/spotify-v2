# Week 1 of the Spotify Playlist Generator project

import pandas as pd
import random

# Load the Spotify dataset into a Pandas DataFrame
df = pd.read_csv("spotify-dataset.csv")

# Create a random list of 3 listened and 3 unlistened songs
listened_songs = random.sample(list(df["title"]), 3)
unlistened_songs = random.sample(list(set(df["title"]).difference(set(listened_songs))), 3)

print("Listened songs: ", listened_songs)
print("Unlistened songs: ", unlistened_songs)

# Create a list of 100 playlists with each 50 random songs
playlists = [random.sample(list(df["title"]), 50) for _ in range(100)]

# Find the playlist that contains 3 listened and 3 unlistened songs
for playlist in playlists:
    if set(listened_songs).issubset(set(playlist)) and set(unlistened_songs).issubset(set(playlist)):
        print("Found a playlist that contains 3 listened and 3 unlistened songs!")
        print("Playlist: ", playlist)
        break
 
# Select 5 songs from the playlist that are not in the listened songs
suggested_songs = [song for song in playlist if song not in listened_songs][:5]

print("Suggested songs: ", suggested_songs)
